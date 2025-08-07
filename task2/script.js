document.addEventListener("DOMContentLoaded", function () {
  const exploreBtn = document.querySelector(".btn");
  exploreBtn.addEventListener("click", function () {
    const portfolioSection = document.getElementById("portfolio");
    if (portfolioSection) {
      portfolioSection.scrollIntoView({ behavior: "smooth" });
    }
  });
});