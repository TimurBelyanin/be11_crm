// Смена фона а также значка солнышко
const lightMode = document.querySelector(".theme");
const body = document.body;
const links = document.querySelectorAll(".sidebar a");

function start() {
    updatePaddingSidebar();
    checkScrollbar();
    updateSvg();

    if (localStorage.getItem("theme")) {
        body.classList.toggle("light-mode-variables");
    }

    const storedItemId = localStorage.getItem("selectedMenuItem");
    if (storedItemId) {
        const selectedItem = document.getElementById(storedItemId);
        if (selectedItem) {
            links.forEach((l) => l.classList.remove("active"));
            selectedItem.classList.add("active");
        }
    } else {
        links[0].classList.add("active");
    }

    updateProfileLogo();
}

lightMode.addEventListener("click", () => {
    body.classList.toggle("light-mode-variables");
    if (body.classList.contains("light-mode-variables")) {
        localStorage.setItem("theme", "light");
    } else {
        delete localStorage.theme;
    }
    updateProfileLogo();
});

// добавление (и удаление) класса active при нажатии на элемент сайдбара
links.forEach((link) => {
    link.addEventListener("click", (event) => {
        event.preventDefault();
        links.forEach((l) => l.classList.remove("active"));
        link.classList.add("active");
        localStorage.setItem("selectedMenuItem", link.id);
    });
});

// Реализация выпадающего меню
//const arrow = document.querySelector(".arrow.bebra");
//const dropdown = document.querySelectorAll(".dropdown-content");
//
//arrow.addEventListener("click", () => {
//    // dropdown.forEach((down) => down.classList.toggle("open"));
//    dropdown[1].classList.toggle("open");
//    if (
//        Array.from(dropdown).some((element) =>
//            element.classList.contains("open"),
//        )
//    ) {
//        arrow.style.transform =
//            window.innerWidth <= 768
//                ? "rotate(-180deg) scale(0.84)"
//                : "rotate(-180deg)";
//    } else {
//        arrow.style.transform =
//            window.innerWidth <= 768
//                ? "rotate(0deg) scale(0.84)"
//                : "rotate(0deg)";
//    }
//});

// Добавление стилей к сайдбару (укзазание паддинга при сжимании)
const sidebar = document.querySelector("aside");

function updatePaddingSidebar() {
    // console.log("Padding in sidebar has changed!");
    const screenWidth = window.innerWidth;
    const hoverWindow = Math.round((9 / 842) * screenWidth + 2541 / 421) + "px";
    const scaleLogo = parseFloat(
        (((21 / 401) * screenWidth + 29547 / 421) / 147).toFixed(2),
    );
    const moveLogoLeft = Math.round((-1 / 86) * screenWidth + 600 / 43);
    const sunMarginRight = Math.max(
        1.8,
        Math.min(
            parseFloat(((71 / 2120) * screenWidth - 2576 / 265).toFixed(1)),
            16,
        ),
    );
    // const widthPalka = Math.max(
    //     3.8,
    //     Math.min(
    //         parseFloat(((297 / 4240) * screenWidth - 10757 / 530).toFixed(1)),
    //         33.5,
    //     ),
    // );
    const widthPalka = Math.max(
        3.6,
        Math.min(
            parseFloat(((69 / 1060) * screenWidth - 9801 / 530).toFixed(1)),
            31.5,
        ),
    ) + 2;
    const bellMarginRight = Math.max(
        2.3,
        Math.min(
            parseFloat(((177 / 4240) * screenWidth - 3196 / 265).toFixed(1)),
            20,
        ),
    );
    // console.log("Sun ", sunMarginRight);
    // console.log("Palka ", widthPalka);
    // console.log("Bell ", bellMarginRight);


    let paddingSidebar;
    // console.log(hoverWindow);
    if (screenWidth < 598) {
        paddingSidebar = "12px";
    } else if (screenWidth > 1400) {
        paddingSidebar = "64px";
    } else {
        paddingSidebar =
            Math.round((26 / 401) * screenWidth - 10736 / 401) + "px";
    }

    // Зная, каким стал паддинг, мы должны правильно настроить вылезающее окно
    // При 64px -

    document.documentElement.style.setProperty(
        "--padding-sidebar",
        paddingSidebar,
    );
    document.documentElement.style.setProperty("--hover-window", hoverWindow);
    document.documentElement.style.setProperty("--scale-logo", scaleLogo);
    document.documentElement.style.setProperty(
        "--move-logo-left",
        moveLogoLeft >= 0 ? moveLogoLeft + "px" : 0 + "px",
    );
    document.documentElement.style.setProperty("--sun-margin-right", sunMarginRight + "px");
    document.documentElement.style.setProperty("--width-palka", widthPalka + "px");
    document.documentElement.style.setProperty("--bell-margin-right", bellMarginRight + "px");
}

function hideScrollbar() {
    sidebar.classList.add("no-scrollbar");
}

function showScrollbar() {
    sidebar.classList.remove("no-scrollbar");
}

function checkScrollbar() {
    if (sidebar.scrollHeight > sidebar.clientHeight) {
        hideScrollbar(); // Скрываем полосу прокрутки, если контент больше высоты
    } else {
        showScrollbar(); // Показываем полосу прокрутки, если контент помещается
    }
}

// Icons
const svgElement = document.querySelector(".logo");
const deskIcon = `<svg
                        width="147"
                        height="23"
                        viewBox="0 0 147 23"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <g clip-path="url(#clip0_2_29)">
                            <path
                                id="NaOH"
                                d="M0.343994 22V1.7H10.262C12.814 1.7 14.728 2.18333 16.004 3.15C17.2993 4.11667 17.947 5.39267 17.947 6.978C17.947 8.04133 17.686 8.96933 17.164 9.762C16.642 10.5353 15.9267 11.1347 15.018 11.56C14.1093 11.9853 13.0653 12.198 11.886 12.198L12.437 11.009C13.713 11.009 14.844 11.2217 15.83 11.647C16.816 12.053 17.5797 12.662 18.121 13.474C18.6817 14.286 18.962 15.2817 18.962 16.461C18.962 18.201 18.2757 19.564 16.903 20.55C15.5303 21.5167 13.51 22 10.842 22H0.343994ZM5.01299 18.462H10.494C11.712 18.462 12.6303 18.2687 13.249 17.882C13.887 17.476 14.206 16.838 14.206 15.968C14.206 15.1173 13.887 14.489 13.249 14.083C12.6303 13.6577 11.712 13.445 10.494 13.445H4.66499V10.023H9.68199C10.8227 10.023 11.6927 9.82967 12.292 9.443C12.9107 9.037 13.22 8.428 13.22 7.616C13.22 6.82333 12.9107 6.23367 12.292 5.847C11.6927 5.441 10.8227 5.238 9.68199 5.238H5.01299V18.462ZM29.9428 22.232C28.1642 22.232 26.5981 21.884 25.2448 21.188C23.9108 20.492 22.8765 19.5447 22.1418 18.346C21.4071 17.128 21.0398 15.7457 21.0398 14.199C21.0398 12.633 21.3975 11.2507 22.1128 10.052C22.8475 8.834 23.8431 7.88667 25.0998 7.21C26.3565 6.514 27.7775 6.166 29.3628 6.166C30.8902 6.166 32.2628 6.49467 33.4808 7.152C34.7182 7.79 35.6945 8.718 36.4098 9.936C37.1252 11.1347 37.4828 12.575 37.4828 14.257C37.4828 14.431 37.4732 14.634 37.4538 14.866C37.4345 15.0787 37.4151 15.2817 37.3958 15.475H24.7228V12.836H35.0178L33.2778 13.619C33.2778 12.807 33.1135 12.1013 32.7848 11.502C32.4562 10.9027 32.0018 10.4387 31.4218 10.11C30.8418 9.762 30.1652 9.588 29.3918 9.588C28.6185 9.588 27.9321 9.762 27.3328 10.11C26.7528 10.4387 26.2985 10.9123 25.9698 11.531C25.6411 12.1303 25.4768 12.8457 25.4768 13.677V14.373C25.4768 15.2237 25.6605 15.9777 26.0278 16.635C26.4145 17.273 26.9461 17.766 27.6228 18.114C28.3188 18.4427 29.1308 18.607 30.0588 18.607C30.8902 18.607 31.6152 18.4813 32.2338 18.23C32.8718 17.9787 33.4518 17.6017 33.9738 17.099L36.3808 19.709C35.6655 20.521 34.7665 21.1493 33.6838 21.594C32.6012 22.0193 31.3542 22.232 29.9428 22.232Z"
                                fill="white"
                            />
                            <path
                                d="M53.3476 9.878H63.1206V13.532H53.3476V9.878ZM53.6956 18.23H64.7446V22H49.0266V1.7H64.3676V5.47H53.6956V18.23ZM68.1637 22V0.481995H72.6877V22H68.1637ZM84.6293 22.232C82.8507 22.232 81.2847 21.884 79.9313 21.188C78.5973 20.492 77.563 19.5447 76.8283 18.346C76.0937 17.128 75.7263 15.7457 75.7263 14.199C75.7263 12.633 76.084 11.2507 76.7993 10.052C77.534 8.83399 78.5297 7.88667 79.7863 7.21C81.043 6.514 82.464 6.166 84.0493 6.166C85.5767 6.166 86.9493 6.49467 88.1673 7.152C89.4047 7.79 90.381 8.71799 91.0963 9.936C91.8117 11.1347 92.1693 12.575 92.1693 14.257C92.1693 14.431 92.1597 14.634 92.1403 14.866C92.121 15.0787 92.1017 15.2817 92.0823 15.475H79.4093V12.836H89.7043L87.9643 13.619C87.9643 12.807 87.8 12.1013 87.4713 11.502C87.1427 10.9027 86.6883 10.4387 86.1083 10.11C85.5283 9.762 84.8517 9.588 84.0783 9.588C83.305 9.588 82.6187 9.762 82.0193 10.11C81.4393 10.4387 80.985 10.9123 80.6563 11.531C80.3277 12.1303 80.1633 12.8457 80.1633 13.677V14.373C80.1633 15.2237 80.347 15.9777 80.7143 16.635C81.101 17.273 81.6327 17.766 82.3093 18.114C83.0053 18.4427 83.8173 18.607 84.7453 18.607C85.5767 18.607 86.3017 18.4813 86.9203 18.23C87.5583 17.9787 88.1383 17.6017 88.6603 17.099L91.0673 19.709C90.352 20.521 89.453 21.1493 88.3703 21.594C87.2877 22.0193 86.0407 22.232 84.6293 22.232ZM99.1321 22L92.5781 6.398H97.2471L102.699 19.825H100.379L106.034 6.398H110.384L103.801 22H99.1321ZM119.548 22.232C117.77 22.232 116.204 21.884 114.85 21.188C113.516 20.492 112.482 19.5447 111.747 18.346C111.013 17.128 110.645 15.7457 110.645 14.199C110.645 12.633 111.003 11.2507 111.718 10.052C112.453 8.83399 113.449 7.88667 114.705 7.21C115.962 6.514 117.383 6.166 118.968 6.166C120.496 6.166 121.868 6.49467 123.086 7.152C124.324 7.79 125.3 8.71799 126.015 9.936C126.731 11.1347 127.088 12.575 127.088 14.257C127.088 14.431 127.079 14.634 127.059 14.866C127.04 15.0787 127.021 15.2817 127.001 15.475H114.328V12.836H124.623L122.883 13.619C122.883 12.807 122.719 12.1013 122.39 11.502C122.062 10.9027 121.607 10.4387 121.027 10.11C120.447 9.762 119.771 9.588 118.997 9.588C118.224 9.588 117.538 9.762 116.938 10.11C116.358 10.4387 115.904 10.9123 115.575 11.531C115.247 12.1303 115.082 12.8457 115.082 13.677V14.373C115.082 15.2237 115.266 15.9777 115.633 16.635C116.02 17.273 116.552 17.766 117.228 18.114C117.924 18.4427 118.736 18.607 119.664 18.607C120.496 18.607 121.221 18.4813 121.839 18.23C122.477 17.9787 123.057 17.6017 123.579 17.099L125.986 19.709C125.271 20.521 124.372 21.1493 123.289 21.594C122.207 22.0193 120.96 22.232 119.548 22.232ZM139.583 6.166C140.821 6.166 141.923 6.41733 142.889 6.92C143.875 7.40333 144.649 8.15733 145.209 9.182C145.77 10.1873 146.05 11.4827 146.05 13.068V22H141.526V13.764C141.526 12.5073 141.246 11.5793 140.685 10.98C140.144 10.3807 139.371 10.081 138.365 10.081C137.65 10.081 137.002 10.2357 136.422 10.545C135.862 10.835 135.417 11.2893 135.088 11.908C134.779 12.5267 134.624 13.3193 134.624 14.286V22H130.1V6.398H134.421V10.719L133.609 9.41399C134.17 8.36999 134.972 7.56767 136.016 7.007C137.06 6.44633 138.249 6.166 139.583 6.166Z"
                                fill="#FF0000"
                            />
                        </g>
                        <defs>
                            <clipPath id="clip0_2_29">
                                <rect width="147" height="23" fill="white" />
                            </clipPath>
                        </defs>
                    </svg>`;

const mobIcon = `
<svg width="41" height="16" viewBox="0 0 41 16" fill="none" xmlns="http://www.w3.org/2000/svg">
<path id="NaOH" d="M0.699543 15V0.299999H7.88154C9.72954 0.299999 11.1155 0.649999 12.0395 1.35C12.9775 2.05 13.4465 2.974 13.4465 4.122C13.4465 4.892 13.2575 5.564 12.8795 6.138C12.5015 6.698 11.9835 7.132 11.3255 7.44C10.6675 7.748 9.91154 7.902 9.05754 7.902L9.45654 7.041C10.3805 7.041 11.1995 7.195 11.9135 7.503C12.6275 7.797 13.1805 8.238 13.5725 8.826C13.9785 9.414 14.1815 10.135 14.1815 10.989C14.1815 12.249 13.6845 13.236 12.6905 13.95C11.6965 14.65 10.2335 15 8.30154 15H0.699543ZM4.08054 12.438H8.04954C8.93154 12.438 9.59654 12.298 10.0445 12.018C10.5065 11.724 10.7375 11.262 10.7375 10.632C10.7375 10.016 10.5065 9.561 10.0445 9.267C9.59654 8.959 8.93154 8.805 8.04954 8.805H3.82854V6.327H7.46154C8.28754 6.327 8.91754 6.187 9.35154 5.907C9.79954 5.613 10.0235 5.172 10.0235 4.584C10.0235 4.01 9.79954 3.583 9.35154 3.303C8.91754 3.009 8.28754 2.862 7.46154 2.862H4.08054V12.438ZM22.1332 15.168C20.8452 15.168 19.7112 14.916 18.7312 14.412C17.7652 13.908 17.0162 13.222 16.4842 12.354C15.9522 11.472 15.6862 10.471 15.6862 9.351C15.6862 8.217 15.9452 7.216 16.4632 6.348C16.9952 5.466 17.7162 4.78 18.6262 4.29C19.5362 3.786 20.5652 3.534 21.7132 3.534C22.8192 3.534 23.8132 3.772 24.6952 4.248C25.5912 4.71 26.2982 5.382 26.8162 6.264C27.3342 7.132 27.5932 8.175 27.5932 9.393C27.5932 9.519 27.5862 9.666 27.5722 9.834C27.5582 9.988 27.5442 10.135 27.5302 10.275H18.3532V8.364H25.8082L24.5482 8.931C24.5482 8.343 24.4292 7.832 24.1912 7.398C23.9532 6.964 23.6242 6.628 23.2042 6.39C22.7842 6.138 22.2942 6.012 21.7342 6.012C21.1742 6.012 20.6772 6.138 20.2432 6.39C19.8232 6.628 19.4942 6.971 19.2562 7.419C19.0182 7.853 18.8992 8.371 18.8992 8.973V9.477C18.8992 10.093 19.0322 10.639 19.2982 11.115C19.5782 11.577 19.9632 11.934 20.4532 12.186C20.9572 12.424 21.5452 12.543 22.2172 12.543C22.8192 12.543 23.3442 12.452 23.7922 12.27C24.2542 12.088 24.6742 11.815 25.0522 11.451L26.7952 13.341C26.2772 13.929 25.6262 14.384 24.8422 14.706C24.0582 15.014 23.1552 15.168 22.1332 15.168Z" fill="white"/>
<path d="M30.0052 15V0.299999H33.4072V15H30.0052ZM36.8958 15V0.299999H40.2978V15H36.8958Z" fill="#FF0000"/>
</svg>
`;

function updateSvg() {
    const isMobile = window.innerWidth <= 768;

    // console.log(window.innerWidth);
    if (isMobile) {
        svgElement.innerHTML = mobIcon; // Замена на мобильный контент
        // console.log("MOBILE");
    } else {
        svgElement.innerHTML = deskIcon; // Замена на десктопный контент
        // console.log("DESKTOP");
    }
}

const logo = document.querySelector("aside .logo");
const deepSidebar = document.querySelector("aside .sidebar")
function squeezeAside() {
    sidebar.classList.toggle("squeeze-aside");
    logo.classList.toggle("squeeze-logo");
    deepSidebar.classList.toggle("hide-sidebar");
}

function updateProfileLogo() {
    const logo = document.getElementById('profile-logo');
    if (!logo) {
      console.error("Элемент с id 'profile-logo' не найден!");
      return; // Прерываем выполнение, если элемент не найден
    }

    const isLightMode = document.body.classList.contains('light-mode-variables');
    logo.src = isLightMode ? '/images/light-userr.svg' : '/images/userr.svg';
  }

document.addEventListener('alpine:init', () => {
    Alpine.data('myForm', () => ({
        errors: {},

        updateErrors(event) {
            const responseText = JSON.parse(event.detail.xhr.response);

            if (event.detail.xhr.response && responseText.errors) {
                this.errors = responseText.errors;
                console.log(responseText);
            } else {
                console.log('Ошибки не найдены в ответе');
            }
        }
    }))
})


window.addEventListener("resize", updatePaddingSidebar);
window.addEventListener("resize", checkScrollbar);
window.addEventListener("resize", updateSvg);
