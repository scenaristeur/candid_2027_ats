/* Candidats 2027 — interactions minimales, sans dépendance. */
(function () {
  "use strict";

  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");

  function currentTheme() {
    return root.dataset.theme === "dark" ? "dark" : "light";
  }

  function updateToggle() {
    if (!toggle) return;
    var dark = currentTheme() === "dark";
    toggle.setAttribute(
      "aria-label",
      dark ? "Passer au thème clair" : "Passer au thème sombre"
    );
    toggle.setAttribute("title", dark ? "Thème clair" : "Thème sombre");
  }

  if (toggle) {
    updateToggle();
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.dataset.theme = next;
      try {
        localStorage.setItem("theme", next);
      } catch (error) {
        /* stockage indisponible : le choix ne sera pas mémorisé */
      }
      updateToggle();
    });
  }

  var cards = Array.prototype.slice.call(
    document.querySelectorAll("[data-track]")
  );
  if (!cards.length) return;

  var input = document.querySelector("[data-search-input]");
  var buttons = Array.prototype.slice.call(
    document.querySelectorAll("[data-filter]")
  );
  var count = document.querySelector("[data-count]");
  var empty = document.querySelector("[data-empty]");
  var activeFilter = "all";

  function normalize(value) {
    return (value || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9]+/g, " ")
      .trim();
  }

  function matchesFilter(card) {
    if (activeFilter === "all") return true;
    if (activeFilter === "als") return card.dataset.als === "1";
    if (activeFilter === "audio") return card.dataset.audio === "1";
    if (activeFilter === "midi") return card.dataset.midi === "1";
    return card.dataset.lyrics === activeFilter;
  }

  function apply() {
    var query = normalize(input ? input.value : "");
    var shown = 0;

    cards.forEach(function (card) {
      var haystack = card.dataset.search || "";
      var visible = matchesFilter(card) && (!query || haystack.indexOf(query) !== -1);
      card.hidden = !visible;
      if (visible) shown += 1;
    });

    if (count) count.textContent = String(shown);
    if (empty) empty.hidden = shown !== 0;
  }

  if (input) {
    input.addEventListener("input", apply);
    input.addEventListener("search", apply);
  }

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      activeFilter = button.dataset.filter || "all";
      buttons.forEach(function (other) {
        var isActive = other === button;
        other.classList.toggle("is-active", isActive);
        other.setAttribute("aria-pressed", isActive ? "true" : "false");
      });
      apply();
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key !== "/" || event.metaKey || event.ctrlKey || event.altKey) return;
    var tag = (document.activeElement && document.activeElement.tagName) || "";
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(tag)) return;
    if (!input) return;
    event.preventDefault();
    input.focus();
    input.select();
  });

  apply();
})();
