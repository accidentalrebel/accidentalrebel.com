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
