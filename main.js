const menuBtn = document.querySelector(".menu__btn");
const menuList = document.querySelector(".menu__list");

function toggleMenuVisibility() {
    menuList.classList.toggle("hide");
}

menuBtn.addEventListener("click", toggleMenuVisibility);

const portfolioToggleBtn = document.getElementById("portfolioToggleBtn");
const portfolioContent = document.getElementById("portfolioContent");

function togglePortfolioVisibility() {
    portfolioContent.classList.toggle("hide");
    if (portfolioContent.classList.contains("hide")) {
        portfolioToggleBtn.querySelector("span").textContent = "Открыть портфолио";
    } else {
        portfolioToggleBtn.querySelector("span").textContent = "Закрыть портфолио";
    }
}

portfolioToggleBtn.addEventListener("click", togglePortfolioVisibility);
