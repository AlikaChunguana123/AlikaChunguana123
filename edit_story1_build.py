import numpy as np, wave, subprocess, os, re
S = "/tmp/claude-0/-home-user-AlikaChunguana123/454ae166-c611-562b-9501-8da9887ce379/scratchpad"
U = "/root/.claude/uploads/454ae166-c611-562b-9501-8da9887ce379"
IMG = "/tmp/claude-0/-home-user-AlikaChunguana123/454ae166-c611-562b-9501-8da9887ce379/images/1.webp"
OUT = "/home/user/AlikaChunguana123/whitmore_story1_edit.mp4"
SR = 44100
def run(c): subprocess.run(c, shell=True, check=True)

# ---------- timeline ----------
A_LEN, B_LEN, C_IN, C_LEN, XF = 13.0, 7.0, 0.5, 14.54, 0.3
B0 = A_LEN - XF            # 12.7
C0 = B0 + B_LEN - XF       # 19.4
TOTAL = C0 + C_LEN         # 33.94

# ---------- video segments (1080x1920, 30fps) ----------
V = "-c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 30"
zoom = "scale=1620:2880,zoompan=z='1+0.0002*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30"
run(f"ffmpeg -v error -y -i {U}/6167b839-video_scene_1_and_2.mp4 -t {A_LEN} -vf \"fps=30,crop=ih*9/16:ih,{zoom},fade=t=in:st=0:d=0.25:color=white\" {V} -c:a aac -ar {SR} -ac 2 {S}/A.mp4")
run(f"ffmpeg -v error -y -ss {C_IN} -i {U}/323cea20-video_3.mp4 -t {C_LEN} -vf \"fps=30,setpts=PTS-STARTPTS,crop=w=ih*9/16:h=ih:x='iw*(0.30+0.04*t/15)':y=0,{zoom}\" {V} -c:a aac -ar {SR} -ac 2 {S}/C.mp4")
run(f"ffmpeg -v error -y -loop 1 -framerate 30 -i {IMG} -f lavfi -i anullsrc=r={SR}:cl=stereo -t {B_LEN} -vf \"crop=ih*9/16:ih,scale=1620:2880,zoompan=z='1+0.0009*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,eq=brightness=-0.12:saturation=0.45:enable='gte(t,4.6)'\" {V} -c:a aac -shortest {S}/B.mp4")

run(f"ffmpeg -v error -y -i {S}/A.mp4 -i {S}/B.mp4 -i {S}/C.mp4 -filter_complex "
    f"\"[0:v][1:v]xfade=transition=slideup:duration={XF}:offset={B0}[v1];[v1][2:v]xfade=transition=fadewhite:duration={XF}:offset={C0}[v];"
    f"[0:a][1:a]acrossfade=d={XF}[a1];[a1][2:a]acrossfade=d={XF}[a]\" -map [v] -map [a] {V} -c:a pcm_s16le {S}/joined.mov")

# ---------- music + sfx (synthesised) ----------
n = int(TOTAL * SR) + SR
mus = np.zeros(n); sfx = np.zeros(n)
def f(note): return 440 * 2 ** ((note - 69) / 12)
def piano(buf, t, note, dur=2.5, vol=0.18):
    i = int(t * SR); L = int(dur * SR); tt = np.arange(L) / SR
    fr = f(note)
    w = sum(a * np.sin(2*np.pi*fr*k*tt) for k, a in [(1,1),(2,.45),(3,.2),(4,.1)])
    env = np.minimum(1, tt/0.008) * np.exp(-tt*2.2)
    seg = vol * w * env
    e = min(n, i+L); buf[i:e] += seg[:e-i]
def pad(buf, t0, t1, notes, vol=0.035):
    i, e = int(t0*SR), int(t1*SR); tt = np.arange(e-i)/SR
    w = sum(np.sin(2*np.pi*f(x)*tt) + .3*np.sin(2*np.pi*f(x)*2.003*tt) for x in notes)
    env = np.minimum(1, tt/1.0) * np.minimum(1, (tt[-1]-tt)/1.0)
    buf[i:e] += vol * w * env
beat = 60/76/2   # eighth notes at 76 bpm
# Part 1: elegant arpeggios 0 -> B0 (Am F C G)
chords1 = [[57,60,64,69],[53,57,60,65],[48,55,60,64],[55,59,62,67]]
t = 0.0; k = 0
while t < B0 - 0.2:
    ch = chords1[(k // 8) % 4]
    piano(mus, t, ch[[0,1,2,3,2,1,2,3][k % 8]] + 12, vol=0.13)
    if k % 8 == 0: piano(mus, t, ch[0]-12, 3.5, 0.16); pad(mus, t, t+8*beat+0.5, ch, 0.02)
    t += beat; k += 1
# Part 2: tension (staccato low pulse + clock tick) B0 -> B0+4.6
t = B0
while t < B0 + 4.5:
    piano(mus, t, 45, 0.5, 0.2); piano(mus, t+beat, 45, 0.4, 0.12)
    t += 2*beat
for tt in np.arange(B0, B0+4.6, 0.5):
    i = int(tt*SR); L = int(0.03*SR); sfx[i:i+L] += 0.15*np.random.randn(L)*np.exp(-np.arange(L)/150)
# Part 3: sad sparse piano from crash to end (Am Dm E Am)
chords3 = [[57,60,64],[50,53,57],[52,56,59],[57,60,64]]
t = B0 + 5.0; k = 0
while t < TOTAL - 2.5:
    ch = chords3[(k // 4) % 4]
    piano(mus, t, ch[k % 3] + 12, 3.0, 0.12)
    if k % 4 == 0: piano(mus, t, ch[0]-12, 4.0, 0.15); pad(mus, t, t+4*2*beat+0.5, ch, 0.025)
    t += 2*beat; k += 1
for x in [45, 57, 60, 64, 69]: piano(mus, TOTAL-2.4, x, 3.0, 0.12)   # final chord
# SFX
def whoosh(t, d=0.45, vol=0.35):
    i = int(t*SR); L = int(d*SR); x = np.random.randn(L)
    x = np.convolve(x, np.ones(8)/8, 'same'); env = np.sin(np.pi*np.arange(L)/L)**2
    sfx[i:i+L] += vol*x*env
def boom(t, vol=0.9):
    i = int(t*SR); L = int(1.6*SR); tt = np.arange(L)/SR
    sfx[i:i+L] += vol*np.sin(2*np.pi*(55-20*tt)*tt)*np.exp(-tt*2.5)
def ding(t, vol=0.22):
    i = int(t*SR); L = int(1.2*SR); tt = np.arange(L)/SR
    sfx[i:i+L] += vol*(np.sin(2*np.pi*1760*tt)+.5*np.sin(2*np.pi*2637*tt))*np.exp(-tt*4)
whoosh(B0-0.25); whoosh(C0-0.25); boom(0.0, 0.6)
ding(B0+0.35); boom(B0+2.65, 0.5); boom(B0+5.5, 0.9)
def save(buf, p):
    x = np.clip(buf, -1, 1); st = np.stack([x, x], 1)
    with wave.open(p, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype('<i2').tobytes())
save(mus, f"{S}/music.wav"); save(sfx, f"{S}/sfx.wav")

# ---------- subtitles (ASS) ----------
RED = r"{\c&H2B20E5&}"; WHITE = r"{\c&HFFFFFF&}"; GREEN = r"{\c&H4FC24A&}"
def ts(x):
    h = int(x//3600); m = int(x%3600//60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"
ev = []
def add(t0, t1, text, style="Sub"):
    ev.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},{style},,0,0,0,,{text}")
KEY = {"whitmores","forty","million","dollars","broke","old","money","mansion","bleed","lifestyle","mistake","earns","never","rarely"}
def lines(text, intervals, offset):
    words = text.split()
    tot = sum(b-a for a, b in intervals); per = tot / sum(len(w)+2 for w in words)
    # map words onto voiced time
    times = []; cur_i = 0; cur = intervals[0][0]
    for w in words:
        d = (len(w)+2) * per; st = cur
        while d > 1e-6:
            a, b = intervals[cur_i]; room = b - cur
            if d <= room: cur += d; d = 0
            else:
                d -= room; cur_i = min(cur_i+1, len(intervals)-1); cur = intervals[cur_i][0]
        times.append((st, cur))
    chunk = []
    for i, w in enumerate(words):
        chunk.append(i)
        if len(chunk) == 3 or w[-1] in ".…," or i == len(words)-1:
            t0 = times[chunk[0]][0] + offset; t1 = times[chunk[-1]][1] + offset + 0.12
            txt = " ".join((RED if re.sub(r"\W", "", words[j]).lower() in KEY else WHITE) + words[j].upper() for j in chunk)
            add(t0, t1, r"{\fscx70\fscy70\t(0,90,\fscx105\fscy105)\t(90,160,\fscx100\fscy100)}" + txt)
            chunk = []
lines("The Whitmores inherited forty million dollars… and still went broke.", [(0.32, 5.98)], 0)
lines("Old family. Old money. A mansion on the hill.", [(7.36, 12.36)], 0)
lines("Fortunes rarely die from one big mistake. They bleed… from a lifestyle.", [(1.96, 4.92), (5.2, 7.55)], C0 - C_IN)
lines("Old money lives on what the money earns. Never on the money itself.", [(10.06, 12.33), (12.78, 14.03)], C0 - C_IN)
# title + number cards
pop = r"{\fscx60\fscy60\t(0,120,\fscx110\fscy110)\t(120,200,\fscx100\fscy100)}"
add(0.0, 6.4, pop + r"MISTAKE " + RED + r"#1" + WHITE + r"\NTHAT KILLS FORTUNES", "Title")
add(6.9, B0, pop + r"$40,000,000", "Card")
add(B0+0.3, B0+2.6, pop + r"IT EARNED\N" + GREEN + r"+$2M" + WHITE + r" A YEAR", "Card")
add(B0+2.6, B0+4.6, pop + r"HE SPENT\N" + RED + r"−$5M" + WHITE + r" A YEAR", "Card")
add(B0+4.6, B0+5.5, r"{\fad(150,0)}12 YEARS LATER…", "Card")
add(B0+5.5, C0, pop + r"{\s1}$40,000,000{\s0}\N" + RED + r"{\fs200}$0", "Card")
add(TOTAL-3.0, TOTAL, pop + r"MISTAKE " + RED + r"#1" + WHITE + r" OF 5\N{\fs56}FOLLOW FOR #2", "Title")
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,DejaVu Sans,88,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,1,0,1,7,3,2,70,70,560,1
Style: Title,DejaVu Sans,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&HB4000000,1,0,0,0,100,100,1,0,3,18,0,8,60,60,230,1
Style: Card,DejaVu Sans,104,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,1,0,1,9,4,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open(f"{S}/subs.ass", "w").write(ass)

# ---------- final mix + burn ----------
run(f"ffmpeg -v error -y -i {S}/joined.mov -i {S}/music.wav -i {S}/sfx.wav -filter_complex "
    f"\"[0:a]volume=1.6,asplit=2[vo][key];[1:a]volume=0.9[m];[m][key]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
    f"[vo][md][2:a]amix=inputs=3:normalize=0,alimiter=limit=0.95,afade=t=out:st={TOTAL-0.6}:d=0.6[a];"
    f"[0:v]ass={S}/subs.ass,fade=t=out:st={TOTAL-0.4}:d=0.4[v]\" -map [v] -map [a] -t {TOTAL} "
    f"-c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart {OUT}")
print("done", TOTAL)
