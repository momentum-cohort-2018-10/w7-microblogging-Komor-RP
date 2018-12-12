

let mobileMenu = document.querySelector('.navbar-menu');
document.querySelector('.navbar-burger').addEventListener('click', function() {
    this.classList.toggle('is-active');
    mobileMenu.classList.toggle('is-active');
});
