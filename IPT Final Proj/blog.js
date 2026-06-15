/* CLICK SOUND */
const _clickSoundBase = new Audio('assets/sounds/click.wav');
_clickSoundBase.volume = 1;

let _audioUnlocked = false;

function _unlockAudio() {
    if (_audioUnlocked) return;
    _audioUnlocked = true;

    const silent = _clickSoundBase.cloneNode();
    silent.volume = 0;
    silent.play().catch(() => {});

    ['click', 'touchstart', 'keydown'].forEach(evt =>
        document.removeEventListener(evt, _unlockAudio)
    );
}

['click', 'touchstart', 'keydown'].forEach(evt =>
    document.addEventListener(evt, _unlockAudio, { once: false, capture: true, passive: true })
);

function playClick() {
    const sfx = _clickSoundBase.cloneNode();
    sfx.volume = 1;
    sfx.play().catch(() => {});
}

/* THEME MODE */
const _toggle = document.getElementById('theme-toggle');

if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark');
    if (_toggle) _toggle.checked = true;
}

if (_toggle) {
    _toggle.addEventListener('change', () => {
        playClick();
        const isDark = _toggle.checked;
        document.body.classList.toggle('dark', isDark);
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
}

const _navLinks = document.querySelectorAll('nav a');

_navLinks.forEach(el => {
    el.addEventListener('click', (e) => {
        const href = el.getAttribute('href');

        if (href === '#' || el.id === 'contact-nav-link' || el.id === 'contact-nav-btn') {
            playClick();
            return;
        }

        e.preventDefault();
        playClick();

        _navLinks.forEach(l => l.classList.remove('active'));
        el.classList.add('active');

        setTimeout(() => {
            window.location.href = href;
        }, 180);
    });
});

/* LOGO SOUND */
const _logoLink = document.querySelector('.logo a');
if (_logoLink) {
    _logoLink.addEventListener('click', (e) => {
        e.preventDefault();
        playClick();
        setTimeout(() => { window.location.href = _logoLink.getAttribute('href'); }, 400);
    });
}

const _sections = document.querySelectorAll('main section');
_sections.forEach(s =>
    new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                _navLinks.forEach(l => l.classList.remove('active'));
                const match = document.querySelector(`nav a[href="#${entry.target.id}"]`);
                if (match) match.classList.add('active');
            }
        });
    }, { threshold: 0.35 }).observe(s)
);

/* CONTACT MODAL */
function openContact(e) {
    if (e) e.preventDefault();
    playClick();
    const modal   = document.getElementById('contactModal');
    const overlay = document.getElementById('overlay');
    if (modal)   modal.classList.add('active');
    if (overlay) overlay.classList.add('active');
}

function closeContact() {
    playClick();
    const modal   = document.getElementById('contactModal');
    const overlay = document.getElementById('overlay');
    if (modal)   modal.classList.remove('active');
    if (overlay) overlay.classList.remove('active');
}

document.addEventListener('click', (e) => {
    const target = e.target.closest(
        'button, .card, .gallery-card, .music-card, ' +
        '.zoom-close, .player-close, .contact-close-btn, ' +
        '.ctrl-btn, .btn-primary, .btn-secondary, ' +
        '.tag-pill, .lyric-line, .marquee-btn, ' +
        '#overlay, [data-click-sound]'
    );
    if (!target) return;
    if (target.dataset.noClick === 'true') return;
    if (target.closest('nav')) return; 
    playClick();
}, true); 