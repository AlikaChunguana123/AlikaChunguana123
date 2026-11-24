// Dunamis advisor client: profile, topics, streaming chat, offline fallback.
const $ = (id) => document.getElementById(id);
const S = window.SECTORS;
const TOPICS = { ideas: '💡 Ideas', marketing: '📣 Marketing', money: '💰 Money & pricing', growth: '🚀 Growth', risks: '⚠️ Risks' };
const QUICK = {
  ideas: ['Give me 5 new income ideas for my business', 'How can I make money on slow days?'],
  marketing: ['Make me a 30-day social media plan', 'How do I get my first 100 customers?'],
  money: ['How should I price my products?', 'How do I improve my cash flow?'],
  growth: ['Should I hire my first employee?', 'How do I open a second location?'],
  risks: ['What are the biggest risks for my business?', 'How do I prepare for a slow season?']
};
const FIELDS = ['bizName', 'sector', 'location', 'stage', 'size', 'challenge'];
let topic = 'ideas';
let history = []; // [{role, content}] text only

function safeGet(k) { try { return localStorage.getItem(k); } catch { return null; } }
function safeSet(k, v) { try { localStorage.setItem(k, v); } catch { /* private mode */ } }

// --- setup UI
$('sector').innerHTML = Object.entries(S).map(([k, s]) => `<option value="${k}">${s.icon} ${s.name}</option>`).join('');
const saved = JSON.parse(safeGet('dunamis_profile') || '{}');
FIELDS.forEach(f => { if (saved[f]) $(f).value = saved[f]; $(f).addEventListener('change', saveProfile); });
function profile() { return Object.fromEntries(FIELDS.map(f => [f, $(f).value.trim()])); }
function saveProfile() { safeSet('dunamis_profile', JSON.stringify(profile())); renderQuick(); }

function renderTopics() {
  $('topics').innerHTML = Object.entries(TOPICS).map(([k, v]) =>
    `<button type="button" data-t="${k}" class="${k === topic ? 'on' : ''}">${v}</button>`).join('');
  $('topics').querySelectorAll('button').forEach(b => b.onclick = () => { topic = b.dataset.t; renderTopics(); renderQuick(); });
}
function renderQuick() {
  $('quick').innerHTML = QUICK[topic].map(q => `<button type="button">${q}</button>`).join('');
  $('quick').querySelectorAll('button').forEach(b => b.onclick = () => { $('q').value = b.textContent; ask(); });
}

function bubble(role, text) {
  const div = document.createElement('div');
  div.className = `bubble ${role === 'user' ? 'user' : 'ai'}`;
  div.textContent = text;
  $('messages').appendChild(div);
  $('messages').scrollTop = $('messages').scrollHeight;
  return div;
}

function welcome() {
  const s = S[$('sector').value];
  bubble('ai', `Hi! I'm your Dunamis advisor ${s.icon}\nFill in your business details on the left, pick a topic, and ask me anything. I'll give you practical steps that fit your sector and budget.`);
}

// Offline / no-server fallback: sector library
function offlineAdvice() {
  const s = S[$('sector').value];
  const key = topic === 'growth' ? 'ideas' : topic;
  const list = s[key] || s.ideas;
  return `(Offline tips: connect to the internet for personalised AI advice)\n\n${s.icon} ${TOPICS[topic]} for ${s.name}:\n` +
    list.map((t, i) => `${i + 1}. ${t}`).join('\n') +
    `\n\nThis week: pick ONE tip above, try it for 7 days, and measure the result.`;
}

async function ask(e) {
  if (e) e.preventDefault();
  const q = $('q').value.trim();
  if (!q) return;
  $('q').value = '';
  bubble('user', q);
  history.push({ role: 'user', content: q });
  const out = bubble('ai', '…');
  $('send').disabled = true; $('status').textContent = 'Thinking…';
  try {
    const res = await fetch('/api/advice', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ profile: profile(), topic, sectorTips: S[$('sector').value], messages: history.slice(-12) })
    });
    if (!res.ok || !res.body) throw new Error((await res.text().catch(() => '')) || res.statusText);
    const reader = res.body.getReader(); const dec = new TextDecoder();
    let text = '';
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      text += dec.decode(value, { stream: true });
      out.textContent = text;
      $('messages').scrollTop = $('messages').scrollHeight;
    }
    history.push({ role: 'assistant', content: text });
    $('status').textContent = '';
  } catch (err) {
    const fallback = offlineAdvice();
    out.textContent = fallback;
    history.pop(); // don't keep an unanswered turn in AI history
    $('status').textContent = 'AI advisor unavailable right now; showing offline sector tips.';
    console.warn(err);
  } finally { $('send').disabled = false; }
}

$('form').addEventListener('submit', ask);
$('q').addEventListener('keydown', (e) => { if (e.key === 'Enter' && !e.shiftKey) ask(e); });
renderTopics(); renderQuick(); welcome();

// --- install as app (PWA)
let deferred;
window.addEventListener('beforeinstallprompt', (e) => { e.preventDefault(); deferred = e; $('install').hidden = false; });
$('install').onclick = async () => { if (deferred) { deferred.prompt(); deferred = null; $('install').hidden = true; } };
if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js');
