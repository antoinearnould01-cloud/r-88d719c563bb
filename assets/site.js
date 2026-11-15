/* Research portfolio - shared script. Plain JavaScript, no dependencies.
   - builds the project cards on the home page from window.PROJECTS
   - renders LaTeX with the local copy of KaTeX when it is loaded
   - writes the current year in the footer */
(function () {
  "use strict";

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function projectCard(p) {
    var card = el("li", "card");

    if (p.image) {
      var img = el("img", "card-image");
      img.src = p.image;
      img.alt = "";
      img.loading = "lazy";
      card.appendChild(img);
    }

    var body = el("div", "card-body");
    if (p.kind) body.appendChild(el("p", "card-kind", p.kind));

    var title = el("h3");
    var link = el("a", null, p.title);
    link.href = "projects/" + p.slug + "/index.html";
    title.appendChild(link);
    body.appendChild(title);

    if (p.summary) body.appendChild(el("p", "card-summary", p.summary));

    var meta = [p.where, p.when].filter(Boolean).join(" · ");
    if (meta) body.appendChild(el("p", "card-meta", meta));

    if (Array.isArray(p.tags) && p.tags.length) {
      var tags = el("ul", "tags");
      p.tags.forEach(function (t) {
        tags.appendChild(el("li", null, t));
      });
      body.appendChild(tags);
    }

    card.appendChild(body);
    return card;
  }

  function renderProjects() {
    var grid = document.getElementById("project-grid");
    if (!grid || !Array.isArray(window.PROJECTS)) return;
    var visible = window.PROJECTS.filter(function (p) {
      return p && p.slug && !p.hidden;
    });
    // Highest "order" first: give the most recent project the largest number.
    visible.sort(function (a, b) {
      return (b.order || 0) - (a.order || 0);
    });
    grid.textContent = "";
    visible.forEach(function (p) {
      grid.appendChild(projectCard(p));
    });
  }

  function renderMath() {
    if (typeof window.renderMathInElement !== "function") return;
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "\\[", right: "\\]", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false }
      ],
      throwOnError: false
    });
  }

  function setYear() {
    var nodes = document.querySelectorAll("[data-year]");
    var year = String(new Date().getFullYear());
    for (var i = 0; i < nodes.length; i++) nodes[i].textContent = year;
  }

  function init() {
    renderProjects();
    renderMath();
    setYear();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
