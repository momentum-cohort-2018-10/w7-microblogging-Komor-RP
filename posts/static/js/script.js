

let mobileMenu = document.querySelector('.navbar-menu');
document.querySelector('.navbar-burger').addEventListener('click', function() {
    this.classList.toggle('is-active');
    mobileMenu.classList.toggle('is-active');
});


let newPost = document.querySelector('#new-post.navbar-item');
document.querySelector('#new-post.navbar-item').addEventListener('click', toggleModal );

document.querySelector('.modal-close').addEventListener('click', toggleModal );
document.querySelector('.modal-background').addEventListener('click', toggleModal);
function toggleModal() {
    let modal = document.querySelector('.modal');
    modal.classList.toggle('is-active');
}