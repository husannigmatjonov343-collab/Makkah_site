document.addEventListener('DOMContentLoaded', () => {

  // ---------- Mobil navigatsiya (hamburger) ----------
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('open');
      toggle.classList.toggle('open', isOpen);
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
    // Havolaga bosilganda menyuni yopish
    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ---------- Yuqoriga qaytish tugmasi ----------
  const backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      backToTop.classList.toggle('visible', window.scrollY > 480);
    }, { passive: true });
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ---------- O'qish progress paneli (maqola sahifasi) ----------
  const readBar = document.querySelector('.reading-progress-bar');
  if (readBar) {
    window.addEventListener('scroll', () => {
      const h = document.documentElement;
      const total = h.scrollHeight - h.clientHeight;
      const scrolled = total > 0 ? (h.scrollTop / total) * 100 : 0;
      readBar.style.width = scrolled + '%';
    }, { passive: true });
  }
});
