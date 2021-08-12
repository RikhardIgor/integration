

let navItems = document.getElementsByClassName('nav-link');
console.log(navItems);

let activeItem = null;

for (let item of navItems) {
    item.addEventListener('click', evt => {
        if (activeItem) {
            activeItem.classList.remove('active');
        }
        item.classList.add('active');
        activeItem = item;
    })
}