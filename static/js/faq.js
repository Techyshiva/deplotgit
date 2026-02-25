const faqs = document.querySelectorAll(".faq");

faqs.forEach((faq) => {
  faq.querySelector(".question").addEventListener("click", () => {
    // Close all other FAQs
    faqs.forEach((item) => {
      if (item !== faq) {
        item.classList.remove("active");
      }
    });

    // Toggle current FAQ
    faq.classList.toggle("active");
  });
});
