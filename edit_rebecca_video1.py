import numpy as np, wave, subprocess, re
S = "/tmp/claude-0/-home-user-AlikaChunguana123/454ae166-c611-562b-9501-8da9887ce379/scratchpad"
U = "/root/.claude/uploads/454ae166-c611-562b-9501-8da9887ce379"
OUT = "/home/user/AlikaChunguana123/rebecca_video1_edit.mp4"
SR = 44100
def run(c): subprocess.run(c, shell=True, check=True)
XF = 0.3
# clip: (file, start, length, crop-x expression as fraction of width)
CL = [
 ("28add947-video_11", 0.0, 10.0, "0.34"),
 ("4e0ac643-video_5", 0.0, 14.8, "if(lt(t,4.0),0.10,0.33)"),
 ("0f3f0c80-video_7", 0.0, 5.5, "0.34"),
 ("30d7eb7d-video_8", 0.8, 7.4, "0.34"),
]
starts = []; t = 0
for i, c in enumerate(CL):
    starts.append(t); t += c[2] - XF
TOTAL = starts[-1] + CL[-1][2]
V = "-c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 30"
for i, (f, ss, ln, cx) in enumerate(CL):
    grade = "eq=saturation=1.12:contrast=1.03"
    if i == 1: grade = "eq=saturation=1.12:contrast=1.03,eq=saturation=0.45:brightness=-0.07:enable='lt(t,4.0)'"
    fade = ",fade=t=in:st=0:d=0.25:color=white" if i == 0 else ""
    run(f"ffmpeg -v error -y -ss {ss} -i {U}/{f}.mp4 -t {ln} -vf \"fps=30,setpts=PTS-STARTPTS,crop=w=ih*9/16:h=ih:x='iw*({cx})':y=0,"
        f"scale=1620:2880,zoompan=z='1+0.00025*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,{grade}{fade}\" "
        f"{V} -c:a aac -ar {SR} -ac 2 {S}/R{i}.mp4")
fc = []; v = "[0:v]"; a = "[0:a]"
trans = ["slideleft", "slideup", "fadewhite"]
for i in range(1, len(CL)):
    fc.append(f"{v}[{i}:v]xfade=transition={trans[i-1]}:duration={XF}:offset={starts[i]}[v{i}]")
    fc.append(f"{a}[{i}:a]acrossfade=d={XF}[a{i}]")
    v, a = f"[v{i}]", f"[a{i}]"
ins = " ".join(f"-i {S}/R{i}.mp4" for i in range(len(CL)))
run(f"ffmpeg -v error -y {ins} -filter_complex \"{';'.join(fc)}\" -map {v} -map {a} {V} -c:a pcm_s16le {S}/Rjoined.mov")

# ---------- music: bossa-style guitar (Karplus-Strong) + bass + shaker ----------
n = int((TOTAL + 2) * SR); mus = np.zeros(n); sfx = np.zeros(n)
def f(m): return 440 * 2 ** ((m - 69) / 12)
def pluck(buf, t, m, dur=1.6, vol=0.12):
    i = int(t * SR); L = int(dur * SR); p = int(SR / f(m))
    x = np.zeros(L); x[:p] = np.random.uniform(-1, 1, p)
    for k in range(p, L): x[k] = 0.996 * 0.5 * (x[k-p] + x[k-p-1])
    e = min(n, i + L); buf[i:e] += vol * x[:e-i]
def soft(buf, t, m, dur=3.0, vol=0.1):
    i = int(t*SR); L = int(dur*SR); tt = np.arange(L)/SR
    w = (np.sin(2*np.pi*f(m)*tt) + .35*np.sin(4*np.pi*f(m)*tt)) * np.minimum(1, tt/0.01) * np.exp(-tt*1.5)
    e = min(n, i+L); buf[i:e] += vol*w[:e-i]
BPM = 112; b = 60 / BPM
prog = [[48,52,55,59],[45,48,52,55],[50,53,57,60],[43,47,50,53]]  # Cmaj7 Am7 Dm7 G7
SOFA0, SOFA1 = starts[1], starts[1] + 4.0
def bossa(t0, t1):
    bar = 0; t = t0
    while t < t1 - 0.1:
        ch = prog[bar % 4]
        pluck(mus, t, ch[0] - 12, 1.2, 0.22); pluck(mus, t + 1.5*b, ch[0] - 5, 1.0, 0.16)   # bass
        pluck(mus, t + 2*b, ch[0] - 12, 1.2, 0.2); pluck(mus, t + 3.5*b, ch[0] - 5, 1.0, 0.14)
        for off in [0, 0.75, 1.5, 2.5, 3.25]:          # syncopated chord stabs
            if t + off*b < t1:
                for m in ch[1:]: pluck(mus, t + off*b + 0.004*(m % 3), m + 12, 0.9, 0.06)
        for k in range(8):                              # shaker
            tt = t + k*b/2
            if tt < t1:
                i = int(tt*SR); L = int(0.05*SR); sfx_vol = 0.05 if k % 2 else 0.08
                mus[i:i+L] += sfx_vol*np.random.randn(L)*np.exp(-np.arange(L)/300)
        t += 4*b; bar += 1
bossa(0, SOFA0 + 0.2)
for k, m in enumerate([57, 60, 64, 62]):                 # soft emotional piano on the sofa
    soft(mus, SOFA0 + 0.2 + k*0.95, m, 2.5, 0.12)
soft(mus, SOFA0 + 0.2, 45, 4.0, 0.12)
bossa(SOFA1, TOTAL - 1.0)
for m in [48, 60, 64, 67, 71]: pluck(mus, TOTAL - 1.0, m, 2.0, 0.12)
# birds
for tb in []:
    for j in range(3):
        i = int((tb + j*0.13)*SR); L = int(0.09*SR); tt = np.arange(L)/SR
        sfx[i:i+L] += 0.05*np.sin(2*np.pi*(3200 + 2500*tt/0.09)*tt)*np.sin(np.pi*tt/0.09)
# sfx
def whoosh(t, d=0.45, vol=0.3):
    i = int(t*SR); L = int(d*SR); x = np.convolve(np.random.randn(L), np.ones(8)/8, 'same')
    sfx[i:i+L] += vol*x*np.sin(np.pi*np.arange(L)/L)**2
def boom(t, vol=0.6):
    i = int(t*SR); L = int(1.4*SR); tt = np.arange(L)/SR
    sfx[i:i+L] += vol*np.sin(2*np.pi*(55-20*tt)*tt)*np.exp(-tt*2.8)
def thump(t, vol=0.5):
    for d in [0, 0.22]:
        i = int((t+d)*SR); L = int(0.25*SR); tt = np.arange(L)/SR
        sfx[i:i+L] += vol*np.sin(2*np.pi*48*tt)*np.exp(-tt*14)
def pop(t, vol=0.25):
    i = int(t*SR); L = int(0.08*SR); tt = np.arange(L)/SR
    sfx[i:i+L] += vol*np.sin(2*np.pi*(900-600*tt/0.08)*tt)*np.exp(-tt*50)
def ding(t, vol=0.2):
    i = int(t*SR); L = int(1.0*SR); tt = np.arange(L)/SR
    sfx[i:i+L] += vol*(np.sin(2*np.pi*1760*tt)+.5*np.sin(2*np.pi*2637*tt))*np.exp(-tt*4)
boom(0.0); [whoosh(s - 0.25) for s in starts[1:]]
thump(SOFA0 + 0.6); thump(SOFA0 + 2.0, 0.4); thump(SOFA0 + 3.2, 0.35)
CARD_SQ = starts[1] + 4.6; CARD_CR = starts[2] + 0.4; END = TOTAL - 3.0
ding(CARD_SQ); pop(SOFA0 + 0.3); pop(CARD_CR); pop(END)
def save(buf, p):
    x = np.clip(buf, -1, 1); st = np.stack([x, x], 1)
    with wave.open(p, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype('<i2').tobytes())
save(mus, f"{S}/Rmusic.wav"); save(sfx, f"{S}/Rsfx.wav")

# ---------- subtitles ----------
RED = r"{\c&H2B20E5&}"; WHITE = r"{\c&HFFFFFF&}"
def ts(x): return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
ev = []
def add(t0, t1, text, style="Sub"): ev.append(f"Dialogue: 0,{ts(t0)},{ts(t1)},{style},,0,0,0,,{text}")
KEY = {"64","anos","ninguém","independência","idade","força","levantar","cadeira","escadas","todos","dias","dez","vezes","ginásio","vaidade","liberdade","hábito"}
def lines(text, intervals, offset):
    words = text.split(); tot = sum(b-a for a, b in intervals); per = tot / sum(len(w)+2 for w in words)
    times = []; ci = 0; cur = intervals[0][0]
    for w in words:
        d = (len(w)+2)*per; st = cur
        while d > 1e-6:
            a, b2 = intervals[ci]; room = b2 - cur
            if d <= room: cur += d; d = 0
            else: d -= room; ci = min(ci+1, len(intervals)-1); cur = intervals[ci][0]
        times.append((st, cur))
    chunk = []
    for i, w in enumerate(words):
        chunk.append(i)
        if len(chunk) == 3 or w[-1] in ".…,?:" or i == len(words)-1:
            t0 = times[chunk[0]][0] + offset; t1 = times[chunk[-1]][1] + offset + 0.12
            txt = " ".join((RED if re.sub(r"[^\w]", "", words[j]).lower() in KEY else WHITE) + words[j].upper() for j in chunk)
            add(t0, t1, r"{\fscx70\fscy70\t(0,90,\fscx105\fscy105)\t(90,160,\fscx100\fscy100)}" + txt)
            chunk = []
lines("Tenho 64 anos… e ninguém carrega isto por mim.", [(0.0, 2.02), (2.39, 4.40)], starts[0])
lines("Sabes o que mais tira a independência a uma mulher depois dos 60? Não é a idade.", [(5.79, 9.95)], starts[0])
lines("É perder força. Levantar de uma cadeira fica difícil. Subir escadas também.", [(4.87, 7.05), (7.47, 8.04)], starts[1])
lines("Por isso, todos os dias: sento e levanto da cadeira. Dez vezes.", [(10.63, 11.12), (11.53, 14.6)], starts[1])
lines("Levanto caixas da minha colheita, trato da horta, subo a colina. O meu ginásio é a quinta.", [(0.33, 1.51), (2.25, 5.4)], starts[2])
lines("Força não é vaidade, minha querida. É liberdade. Segue para o hábito número dois.", [(1.16-0.8, 3.54-0.8), (4.15-0.8, 5.14-0.8), (5.46-0.8, 7.16-0.8)], starts[3])
pp = r"{\an5\pos(540,1080)\fscx60\fscy60\t(0,120,\fscx110\fscy110)\t(120,200,\fscx100\fscy100)}"
add(0.0, 4.4, pp + RED + "64 ANOS. " + WHITE + r"NINGUÉM\NCARREGA ISTO POR MIM", "Title")
add(SOFA0 + 0.3, SOFA1, pp + "O " + RED + "MÚSCULO" + WHITE + r" VAI-SE\NSE NÃO O USARES", "Card")
add(CARD_SQ, CARD_SQ + 3.2, pp + RED + "10x" + WHITE + " POR DIA", "Card")
add(CARD_CR, starts[3] - 0.1, pp + r"O MEU GINÁSIO\N= A QUINTA", "Card")
add(END, TOTAL, pp + r"HÁBITO Nº1 · " + RED + r"FORÇA" + WHITE + r"\N{\fs54}SEGUE PARA O Nº2", "Title")
ass = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,DejaVu Sans,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,1,0,1,7,3,2,70,70,560,1
Style: Title,DejaVu Sans,70,&H00FFFFFF,&H00FFFFFF,&H00000000,&HB4000000,1,0,0,0,100,100,1,0,3,18,0,8,60,60,230,1
Style: Card,DejaVu Sans,92,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,1,0,1,8,4,8,60,60,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n"
open(f"{S}/Rsubs.ass", "w").write(ass)

run(f"ffmpeg -v error -y -i {S}/Rjoined.mov -i {S}/Rmusic.wav -i {S}/Rsfx.wav -filter_complex "
    f"\"[0:a]volume=1.6,asplit=2[vo][key];[1:a]volume=0[m];[m][key]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
    f"[vo][md][2:a]amix=inputs=3:normalize=0,alimiter=limit=0.95,afade=t=out:st={TOTAL-0.6}:d=0.6[a];"
    f"[0:v]ass={S}/Rsubs.ass,fade=t=out:st={TOTAL-0.4}:d=0.4[v]\" -map [v] -map [a] -t {TOTAL} "
    f"-c:v libx264 -crf 19 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart {OUT}")
print("done", round(TOTAL, 2), [round(s, 2) for s in starts])
