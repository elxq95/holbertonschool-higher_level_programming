document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("toggle_header").addEventListener("click", () => {
      const header = document.querySelector("header");
      if (header.classList.contains("red")) {
        header.classList.replace("red", "green");
      } else if (header.classList.contains("green")) {
        header.classList.replace("green", "red");
      }
    });
  });