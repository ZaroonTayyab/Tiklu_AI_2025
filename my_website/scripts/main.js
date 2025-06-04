const form = document.querySelector("form");
const feedback = document.getElementById("form-feedback");
// Mobile Navigation Toggle
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const navLinksItems = document.querySelectorAll(".nav-links a");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
  hamburger.classList.toggle("active");
});

navLinksItems.forEach((item) => {
  item.addEventListener("click", () => {
    navLinks.classList.remove("active");
    hamburger.classList.remove("active");
  });
});

// Header Scroll Effect
const header = document.getElementById("header");
window.addEventListener("scroll", () => {
  if (window.scrollY > 50) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});

// FAQ Accordion
const faqQuestions = document.querySelectorAll(".faq-question");
if (faqQuestions) {
  faqQuestions.forEach((question) => {
    question.addEventListener("click", () => {
      const faqItem = question.parentElement;
      faqItem.classList.toggle("active");

      // Close other open items
      faqQuestions.forEach((q) => {
        if (q !== question) {
          q.parentElement.classList.remove("active");
        }
      });
    });
  });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    if (targetId === "#") return;

    const targetElement = document.querySelector(targetId);
    if (targetElement) {
      window.scrollTo({
        top: targetElement.offsetTop - 70,
        behavior: "smooth",
      });
    }
  });
});

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const submitButton = form.querySelector("[type='submit']");
  submitButton.disabled = true;
  submitButton.value = "Sending...";

  try {
    const response = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    });

    if (response.ok) {
      form.reset();
      document.getElementById("popupOverlay").classList.add("active");
    } else {
      throw new Error("Form submission failed");
    }
  } catch (error) {
    feedback.innerHTML =
      "<p style='color: red;'>Error sending message. Please try again.</p>";
  } finally {
    submitButton.disabled = false;
    submitButton.value = "Send Message";
  }
});
// Popup close
const popupOverlay = document.getElementById("popupOverlay");
const popupClose = document.getElementById("popupClose");

popupClose.addEventListener("click", () => {
  popupOverlay.classList.remove("active");
});

popupOverlay.addEventListener("click", (e) => {
  if (e.target === popupOverlay) {
    popupOverlay.classList.remove("active");
  }
});
