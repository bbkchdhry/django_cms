const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const cardbody = document.querySelectorAll('.card-body');
const currentTheme = localStorage.getItem('theme');
const ibox = document.querySelectorAll('.ibox');
const sideNavbar = document.querySelector(".page-sidebar");
const pills = document.querySelectorAll('.nav-pills.nav-pills-air .nav-link.active');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
        cardbody.forEach(cbody => {
            cbody.style.backgroundColor = "#1c1e21";
        })
        ibox.forEach(ibox => {
            ibox.style.backgroundColor = "#1c1e21";
        })
        sideNavbar.style.backgroundColor = "#1c1e21";
        sideNavbar.style.boxShadow = "0 5px 20px #1c1e21";
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        cardbody.forEach(cbody => {
            cbody.style.backgroundColor = "#1c1e21";
        })
        ibox.forEach(ibox => {
            ibox.style.backgroundColor = "#1c1e21";
        })
        sideNavbar.style.backgroundColor = "#1c1e21";
        sideNavbar.style.boxShadow = "0 5px 20px #1c1e21";
        localStorage.setItem('theme', 'dark');
    }
    else {
        document.documentElement.setAttribute('data-theme', 'light');
        cardbody.forEach(cbody => {
            cbody.style.backgroundColor = "#fff";
        })
        ibox.forEach(ibox => {
            ibox.style.backgroundColor = "#fff";
        })
        sideNavbar.style.backgroundColor = "#fff";
        sideNavbar.style.boxShadow = "0 5px 20px #d6dee4";
        localStorage.setItem('theme', 'light');
    }
}

toggleSwitch.addEventListener('change', switchTheme, false);