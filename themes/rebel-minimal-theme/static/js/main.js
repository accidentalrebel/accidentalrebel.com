function toggleMenu() {
    var navLinks = document.getElementById('navLinks');
    navLinks.classList.toggle('active');
}

window.addEventListener('scroll', function() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    document.getElementById('progress').style.width = scrolled + '%';
});

// Click an article image to view it enlarged
(function () {
    var content = document.querySelector('.article-content');
    if (!content) return;

    var images = Array.from(content.querySelectorAll('img'));
    if (!images.length) return;

    var overlay = document.createElement('dialog');
    overlay.className = 'lightbox';
    overlay.setAttribute('aria-label', 'Enlarged image. Click image or press Escape to close.');
    var full = document.createElement('img');
    overlay.appendChild(full);
    var dismiss = document.createElement('button');
    dismiss.type = 'button';
    dismiss.className = 'lightbox-close';
    dismiss.textContent = '\u00d7';
    dismiss.setAttribute('aria-label', 'Close enlarged image');
    overlay.appendChild(dismiss);
    document.body.appendChild(overlay);

    var previousOverflow = '';

    function close() {
        if (!overlay.open) return;
        document.body.style.overflow = previousOverflow;
        overlay.close();
    }

    function open(img) {
        if (overlay.open) return;
        full.src = img.currentSrc || img.src;
        full.alt = img.alt;
        previousOverflow = document.body.style.overflow;
        img.focus({ preventScroll: true });
        overlay.showModal();
        document.body.style.overflow = 'hidden';
    }

    images.forEach(function (img) {
        img.classList.add('is-zoomable');
        img.setAttribute('tabindex', '0');
        img.setAttribute('role', 'button');
        img.setAttribute('aria-label', 'View image' + (img.alt ? ': ' + img.alt : ''));
        img.setAttribute('aria-haspopup', 'dialog');
        img.addEventListener('click', function (e) {
            e.preventDefault();
            open(img);
        });
        img.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                open(img);
            }
        });
    });

    overlay.addEventListener('click', close);
    overlay.addEventListener('keydown', function (e) {
        if (e.key === 'Tab') {
            e.preventDefault();
            dismiss.focus();
        }
    });
    overlay.addEventListener('cancel', function (e) {
        e.preventDefault();
        close();
    });
})();
