document.documentElement.classList.add("js");

const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#primary-navigation");

if (menuButton && navigation) {
  const closeMenu = () => {
    menuButton.setAttribute("aria-expanded", "false");
    navigation.classList.remove("is-open");
    menuButton.setAttribute("aria-label", "Open navigation");
    menuButton.querySelector(".sr-only").textContent = "Open navigation";
  };

  menuButton.addEventListener("click", () => {
    const opening = menuButton.getAttribute("aria-expanded") !== "true";
    menuButton.setAttribute("aria-expanded", String(opening));
    navigation.classList.toggle("is-open", opening);
    menuButton.setAttribute("aria-label", opening ? "Close navigation" : "Open navigation");
    menuButton.querySelector(".sr-only").textContent = opening ? "Close navigation" : "Open navigation";
  });

  navigation.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement && window.matchMedia("(max-width: 900px)").matches) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      closeMenu();
      menuButton.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (!window.matchMedia("(max-width: 900px)").matches) closeMenu();
  });
}

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});

const revealElements = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        currentObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -35px 0px" });
  revealElements.forEach((element) => observer.observe(element));
} else {
  revealElements.forEach((element) => element.classList.add("is-visible"));
}

const enquiryForm = document.querySelector("#enquiry-form");
if (enquiryForm) {
  const serviceSelect = enquiryForm.elements.namedItem("service");
  const requestedService = new URLSearchParams(window.location.search).get("service");
  if (serviceSelect && requestedService && [...serviceSelect.options].some((option) => option.value === requestedService)) {
    serviceSelect.value = requestedService;
  }

  const status = document.querySelector("#form-status");
  const submitButton = enquiryForm.querySelector('button[type="submit"]');

  enquiryForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    status.textContent = "";
    status.removeAttribute("data-state");

    if (!enquiryForm.reportValidity()) return;

    const formData = new FormData(enquiryForm);
    const payload = {
      name: String(formData.get("name") || "").trim(),
      email: String(formData.get("email") || "").trim(),
      company: String(formData.get("company") || "").trim(),
      service: String(formData.get("service") || ""),
      message: String(formData.get("message") || "").trim(),
      consent: formData.get("consent") === "on",
      website: String(formData.get("website") || ""),
    };

    submitButton.disabled = true;
    submitButton.setAttribute("aria-busy", "true");
    status.textContent = "Sending your enquiry…";

    try {
      const response = await fetch("/api/enquiry", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) {
        throw new Error(result.error || "We could not send your enquiry. Please email hello@arixova.tech instead.");
      }
      enquiryForm.reset();
      status.dataset.state = "success";
      status.textContent = "Your enquiry has been sent. Thank you — we’ll be in touch.";
    } catch (error) {
      status.dataset.state = "error";
      status.textContent = error instanceof Error
        ? error.message
        : "We could not send your enquiry. Please email hello@arixova.tech instead.";
    } finally {
      submitButton.disabled = false;
      submitButton.removeAttribute("aria-busy");
    }
  });
}
