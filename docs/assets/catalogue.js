/* Candidats 2027 — filtres du catalogue des productions. */
(function () {
  "use strict";

  var rows = Array.prototype.slice.call(
    document.querySelectorAll("[data-catalog-row]")
  );
  if (!rows.length) return;

  var search = document.querySelector("[data-catalog-search]");
  var album = document.querySelector("[data-catalog-album]");
  var docsOnly = document.querySelector("[data-catalog-docs]");
  var buttons = Array.prototype.slice.call(
    document.querySelectorAll("[data-catalog-status]")
  );
  var count = document.querySelector("[data-catalog-count]");
  var empty = document.querySelector("[data-catalog-empty]");
  var status = "all";

  function normalize(value) {
    return (value || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9]+/g, " ")
      .trim();
  }

  function apply() {
    var query = normalize(search ? search.value : "");
    var selectedAlbum = album ? album.value : "";
    var onlyDocs = docsOnly ? docsOnly.checked : false;
    var shown = 0;

    rows.forEach(function (row) {
      var visible = true;
      if (query && (row.dataset.search || "").indexOf(query) === -1) visible = false;
      if (selectedAlbum && row.dataset.album !== selectedAlbum) visible = false;
      if (status !== "all" && row.dataset.status !== status) visible = false;
      if (onlyDocs && row.dataset.docs !== "1") visible = false;
      row.hidden = !visible;
      if (visible) shown += 1;
    });

    if (count) count.textContent = String(shown);
    if (empty) empty.hidden = shown !== 0;
  }

  if (search) search.addEventListener("input", apply);
  if (album) album.addEventListener("change", apply);
  if (docsOnly) docsOnly.addEventListener("change", apply);

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      status = button.dataset.catalogStatus || "all";
      buttons.forEach(function (other) {
        var active = other === button;
        other.classList.toggle("is-active", active);
        other.setAttribute("aria-pressed", active ? "true" : "false");
      });
      apply();
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key !== "/" || event.metaKey || event.ctrlKey || event.altKey) return;
    var tag = (document.activeElement && document.activeElement.tagName) || "";
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(tag)) return;
    if (!search) return;
    event.preventDefault();
    search.focus();
    search.select();
  });

  apply();
})();
