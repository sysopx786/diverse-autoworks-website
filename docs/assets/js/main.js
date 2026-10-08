/* Diverse Autoworks — site scripts. No dependencies, no trackers. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* footer year */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* header: shrink on scroll, open/closed strip, menu + search panels */
  var hdr = $("#hdr");
  var HD = {};
  try { HD = JSON.parse($("#shop-data").textContent); } catch (e) {}

  /* Open / closed status. Pure function; uses the shop's time zone, never the visitor's clock. */
  /* STATUS-LOGIC-START */
  function computeStatus(now, cfg, L) {
    var DAY = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
    function toMin(s) { var p = String(s).split(":"); return (+p[0]) * 60 + (+p[1]); }
    function pad(n) { return n < 10 ? "0" + n : "" + n; }
    function fmt(min) {
      var h = Math.floor(min / 60), m = min % 60, ap = h >= 12 ? (L.pm || "PM") : (L.am || "AM");
      return (h % 12 === 0 ? 12 : h % 12) + ":" + pad(m) + " " + ap;
    }
    function ranges(dayKey) {
      var out = [], src = (cfg.hours && cfg.hours[dayKey]) || [];
      for (var i = 0; i < src.length; i++) {
        var a = toMin(src[i][0]), b = toMin(src[i][1]);
        if (!(a >= 0 && b > a && b <= 1440)) continue;
        out.push([a, b]);
      }
      out.sort(function (x, y) { return x[0] - y[0]; });
      var merged = [];
      for (var j = 0; j < out.length; j++) {
        var last = merged[merged.length - 1];
        if (last && out[j][0] <= last[1]) last[1] = Math.max(last[1], out[j][1]);
        else merged.push(out[j]);
      }
      return merged;
    }
    var f = new Intl.DateTimeFormat("en-US", { timeZone: cfg.timeZone, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", weekday: "short", hour: "2-digit", minute: "2-digit" });
    var P = {}; f.formatToParts(now).forEach(function (p) { P[p.type] = p.value; });
    var y = +P.year, mo = +P.month, d = +P.day, nowMin = (+P.hour) * 60 + (+P.minute);
    function dayInfo(offset) {
      var dt = new Date(Date.UTC(y, mo - 1, d + offset));
      var key = dt.getUTCFullYear() + "-" + pad(dt.getUTCMonth() + 1) + "-" + pad(dt.getUTCDate());
      var closed = (cfg.closedDates || []).indexOf(key) > -1;
      return { dow: dt.getUTCDay(), ranges: closed ? [] : ranges(DAY[dt.getUTCDay()]) };
    }
    var today = dayInfo(0);
    for (var i = 0; i < today.ranges.length; i++) {
      var r = today.ranges[i];
      if (nowMin >= r[0] && nowMin < r[1]) {
        var soon = (r[1] - nowMin) <= (cfg.closingSoonMinutes || 60);
        return { state: soon ? "soon" : "open", text: (soon ? L.soon : L.open).replace("{time}", fmt(r[1])) };
      }
    }
    for (var off = 0; off <= 8; off++) {
      var info = dayInfo(off);
      for (var k = 0; k < info.ranges.length; k++) {
        var start = info.ranges[k][0];
        if (off === 0 && start <= nowMin) continue;
        var when = off === 0 ? L.today : off === 1 ? L.tomorrow : L.days[info.dow];
        return { state: "closed", text: L.closed.replace("{when}", when).replace("{time}", fmt(start)) };
      }
    }
    return { state: "closed", text: L.never };
  }
  /* STATUS-LOGIC-END */

  if (hdr) {
    /* shrink on scroll (hysteresis: shrink past 40px, grow back under 8px) */
    var shrunk = false, ticking = false;
    var onScroll = function () {
      var y = window.pageYOffset || document.documentElement.scrollTop || 0;
      if (!shrunk && y > 40) { shrunk = true; hdr.classList.add("is-shrunk"); }
      else if (shrunk && y < 8) { shrunk = false; hdr.classList.remove("is-shrunk"); }
      ticking = false;
    };
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; window.requestAnimationFrame(onScroll); } }, { passive: true });
    onScroll();
    window.requestAnimationFrame(function () { window.requestAnimationFrame(function () { hdr.classList.remove("no-tr"); }); });

    /* open/closed strip; the static hours line stays if anything fails */
    var box = $("#shop-status"), txt = box && $(".status-text", box), lastKey = "";
    if (box && HD.shop && HD.ui) {
      if (HD.shop.sample) {
        var tag = document.createElement("span");
        tag.className = "status-sample"; tag.textContent = HD.ui.sample || "Sample";
        box.appendChild(tag);
        if (window.console) console.warn("Header hours are SAMPLE values. Edit SHOP in tools/build.py, set sample False, rebuild.");
      }
      var paint = function () {
        var s;
        try { s = computeStatus(new Date(), HD.shop, HD.ui); } catch (e) { return; }
        var key = s.state + "|" + s.text;
        if (key === lastKey) return;
        lastKey = key; box.setAttribute("data-state", s.state); txt.textContent = s.text;
      };
      paint();
      setInterval(paint, 30000);
      document.addEventListener("visibilitychange", function () { if (!document.hidden) paint(); });
      window.addEventListener("focus", paint);
    }

    /* menu + search panels (one open at a time) */
    var mb = $(".menu-btn"), nav = $("#site-nav");
    var sb = $(".search-btn"), sp = $("#site-search"), si = $("#site-search-input");
    var sres = $("#site-search-res"), sempty = $("#site-search-empty");
    var closeMenu = function () { if (nav) nav.classList.remove("open"); if (mb) mb.setAttribute("aria-expanded", "false"); };
    var closeSearch = function () { if (sp) sp.classList.remove("open"); if (sb) sb.setAttribute("aria-expanded", "false"); };
    if (mb && nav) {
      mb.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        mb.setAttribute("aria-expanded", open ? "true" : "false");
        if (open) closeSearch();
      });
      $$("a", nav).forEach(function (a) { a.addEventListener("click", closeMenu); });
    }
    if (sb && sp && si) {
      sb.addEventListener("click", function () {
        if (sp.classList.contains("open")) { closeSearch(); return; }
        closeMenu(); sp.classList.add("open"); sb.setAttribute("aria-expanded", "true"); si.focus();
      });
      $(".srch-close", sp).addEventListener("click", function () { closeSearch(); sb.focus(); });
    }
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      if (sp && sp.classList.contains("open")) { closeSearch(); sb.focus(); }
      else if (nav && nav.classList.contains("open")) { closeMenu(); mb.focus(); }
    });
    document.addEventListener("click", function (e) { if (!hdr.contains(e.target)) { closeMenu(); closeSearch(); } });

    /* site search: local index, accent-insensitive */
    if (si && sres && HD.search) {
      var norm = function (t) { return String(t).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
      var run = function () {
        var q = norm(si.value.trim());
        sres.textContent = ""; sempty.hidden = true;
        if (!q) return;
        var tokens = q.split(/\s+/), hits = [];
        HD.search.forEach(function (row) {
          var title = norm(row[0]), hay = title + " " + norm(row[2]);
          if (!tokens.every(function (t) { return hay.indexOf(t) > -1; })) return;
          hits.push({ row: row, score: tokens.reduce(function (n, t) { return n + (title.indexOf(t) > -1 ? 2 : 1); }, 0) });
        });
        hits.sort(function (a, b) { return b.score - a.score; });
        hits.slice(0, 6).forEach(function (h) {
          var li = document.createElement("li"), a = document.createElement("a");
          a.href = h.row[1]; a.textContent = h.row[0];
          if (/^https?:/.test(h.row[1])) { a.target = "_blank"; a.rel = "noopener"; }
          li.appendChild(a); sres.appendChild(li);
        });
        sempty.hidden = hits.length > 0;
      };
      si.addEventListener("input", run);
      si.addEventListener("keydown", function (e) {
        var first = $("a", sres);
        if (e.key === "Enter" && first) { e.preventDefault(); first.click(); }
        if (e.key === "ArrowDown" && first) { e.preventDefault(); first.focus(); }
      });
      sres.addEventListener("keydown", function (e) {
        var links = $$("a", sres), i = links.indexOf(document.activeElement);
        if (e.key === "ArrowDown" && i < links.length - 1) { e.preventDefault(); links[i + 1].focus(); }
        if (e.key === "ArrowUp") { e.preventDefault(); (i > 0 ? links[i - 1] : si).focus(); }
      });
    }
  }

  /* hero gauge: one sweep on load, press-and-hold to rev */
  var needle = $("#needle"), gbtn = $("#gauge-btn");
  if (needle) {
    var REST = -34, REV = 118;
    if (!reduce) {
      needle.classList.add("sweep");
      needle.addEventListener("animationend", function () {
        needle.classList.remove("sweep");
        needle.style.transform = "rotate(" + REST + "deg)";
        needle.classList.add("live");
      });
    }
    var set = function (deg) {
      if (reduce) return;
      needle.classList.remove("sweep");
      needle.classList.add("live");
      needle.style.transform = "rotate(" + deg + "deg)";
    };
    if (gbtn) {
      var down = function (e) { if (e.type === "keydown" && e.key !== " " && e.key !== "Enter") return; if (e.type === "keydown" && e.repeat) return; set(REV); if (e.type === "keydown") e.preventDefault(); };
      var up = function (e) { if (e.type === "keyup" && e.key !== " " && e.key !== "Enter") return; set(REST); };
      gbtn.addEventListener("pointerdown", down);
      ["pointerup", "pointerleave", "pointercancel", "blur"].forEach(function (n) { gbtn.addEventListener(n, up); });
      gbtn.addEventListener("keydown", down);
      gbtn.addEventListener("keyup", up);
    }
  }

  /* service picker */
  var pdata = $("#picker-data");
  if (pdata) {
    var P = JSON.parse(pdata.textContent);
    var chips = $$(".chip[data-svc]");
    var res = $("#picker-result");
    var show = function (chip) {
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
      var d = P.items[chip.getAttribute("data-svc")];
      if (!d) return;
      var html = '<div class="res-ic">' + d.icon + '</div><h3>' + d.title + '</h3><p>' + d.desc + '</p>';
      if (d.note) html += '<p class="note">' + d.note + '</p>';
      html += '<div class="acts"><a class="btn btn-sign" href="' + d.request + '">' + P.ui.request + '</a>' +
        '<a class="btn btn-line" href="' + d.learn + '">' + P.ui.learn + '</a>' +
        '<a class="btn btn-line" href="' + P.tel + '">' + P.ui.call + '</a></div>';
      res.innerHTML = html;
      var ic = res.querySelector(".res-ic svg"); if (ic) { ic.classList.add("res-ic"); ic.removeAttribute("width"); ic.removeAttribute("height"); }
    };
    chips.forEach(function (c) { c.addEventListener("click", function () { show(c); }); });
  }

  /* motorcycle inspection diagram */
  var moto = $("#moto");
  if (moto) {
    var names = JSON.parse($("#moto-data").textContent);
    var note = $("#moto-note");
    var pick = function (id) {
      $$(".part,.hot", moto).forEach(function (el) { el.classList.toggle("on", el.getAttribute("data-part") === id); });
      $$(".parts button").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-part") === id ? "true" : "false"); });
      if (note) note.innerHTML = '<strong>' + names.sel + ' ' + names.parts[id] + '</strong> — ' + names.listed;
    };
    $$(".hot", moto).forEach(function (h) {
      h.addEventListener("click", function () { pick(h.getAttribute("data-part")); });
      h.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pick(h.getAttribute("data-part")); } });
    });
    $$(".parts button").forEach(function (b) { b.addEventListener("click", function () { pick(b.getAttribute("data-part")); }); });
  }

  /* FAQ filter + search */
  var fq = $("#faq-root");
  if (fq) {
    var cats = $$(".faq-cat", fq), items = $$("details.q", fq);
    var search = $("#faq-search"), chipsF = $$(".faq-chips button"), empty = $("#faq-empty"), count = $("#faq-count");
    var active = "all";
    var apply = function () {
      var q = (search && search.value || "").trim().toLowerCase(), shown = 0;
      items.forEach(function (d) {
        var cat = d.closest(".faq-cat").getAttribute("data-cat");
        var ok = (active === "all" || cat === active) && (!q || d.textContent.toLowerCase().indexOf(q) > -1);
        d.hidden = !ok; if (ok) shown++;
      });
      cats.forEach(function (c) { c.hidden = !$$("details.q", c).some(function (d) { return !d.hidden; }); });
      if (empty) empty.classList.toggle("show", shown === 0);
      if (count) count.textContent = count.getAttribute("data-tpl").replace("{n}", shown);
    };
    chipsF.forEach(function (b) { b.addEventListener("click", function () {
      active = b.getAttribute("data-cat");
      chipsF.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      apply();
    }); });
    if (search) search.addEventListener("input", apply);
    if (location.hash) {
      var t = document.getElementById(location.hash.slice(1));
      if (t && t.matches(".faq-cat")) { /* anchor to category: nothing to filter, just scroll */ }
    }
    apply();
  }

  /* map: load Google Maps only after the visitor asks */
  var mapBtn = $("#map-load");
  if (mapBtn) {
    mapBtn.addEventListener("click", function () {
      var box = $("#mapbox"), src = mapBtn.getAttribute("data-src");
      var f = document.createElement("iframe");
      f.src = src; f.title = mapBtn.getAttribute("data-title"); f.loading = "lazy"; f.referrerPolicy = "no-referrer-when-downgrade";
      f.setAttribute("allowfullscreen", "");
      box.appendChild(f);
      var face = $(".map-face", box); if (face) face.remove();
    });
  }

  /* request forms */
  $$("form[data-request]").forEach(function (form) {
    var i18n = JSON.parse($("#form-i18n").textContent);
    var endpoint = form.getAttribute("data-endpoint") || "";
    var to = form.getAttribute("data-email");
    var status = $(".form-status", form);
    var say = function (msg, bad) { status.innerHTML = msg; status.classList.add("show"); status.classList.toggle("bad", !!bad); status.setAttribute("tabindex", "-1"); status.focus(); };
    var val = function (n) { var el = form.elements[n]; return el ? (el.value || "").trim() : ""; };
    var clear = function () { $$(".err", form).forEach(function (e) { e.textContent = ""; }); $$("[aria-invalid]", form).forEach(function (e) { e.removeAttribute("aria-invalid"); }); };
    var bad = function (name, msg) {
      var el = form.elements[name]; var err = $("#err-" + name + "-" + form.id, form) || $("[data-err='" + name + "']", form);
      if (el) { el.setAttribute("aria-invalid", "true"); }
      if (err) err.textContent = msg;
    };

    /* pre-fill from ?service= */
    var qs = new URLSearchParams(location.search), svc = qs.get("service");
    if (svc && form.elements.service) {
      var opt = $("option[value='" + svc.replace(/[^a-z-]/g, "") + "']", form.elements.service);
      if (opt) form.elements.service.value = opt.value;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault(); clear(); status.classList.remove("show");
      if (val("company_site")) return; /* honeypot */
      var ok = true, first = null;
      var flag = function (n, m) { bad(n, m); ok = false; if (!first) first = form.elements[n]; };
      if (!val("name")) flag("name", i18n.name);
      var ph = val("phone"), em = val("email"), pref = (form.querySelector("input[name='contact']:checked") || {}).value || "phone";
      if (!ph && !em) { flag("phone", i18n.either); }
      if (pref === "phone" && !ph && em) { /* allow: they gave email only */ }
      if (em && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)) flag("email", i18n.email);
      if (ph && ph.replace(/\D/g, "").length < 10) flag("phone", i18n.phone);
      if (!ok) { if (first) first.focus(); return; }

      var svcSel = form.elements.service, svcLabel = svcSel && svcSel.selectedIndex > -1 ? svcSel.options[svcSel.selectedIndex].text : "";
      var fields = [
        [i18n.l_name, val("name")], [i18n.l_phone, ph], [i18n.l_email, em], [i18n.l_pref, pref === "email" ? i18n.p_email : i18n.p_phone],
        [i18n.l_vehicle, val("vehicle")], [i18n.l_service, svcLabel], [i18n.l_date, val("date")], [i18n.l_fleet, val("fleet")], [i18n.l_desc, val("message")]
      ].filter(function (f) { return f[1]; });

      if (endpoint) {
        var btn = $("button[type=submit]", form); btn.disabled = true;
        var body = new FormData(form); body.delete("company_site");
        fetch(endpoint, { method: "POST", body: body, headers: { Accept: "application/json" } })
          .then(function (r) { if (!r.ok) throw new Error("bad"); form.reset(); say("<strong>" + i18n.sent + "</strong> " + i18n.notconf); })
          .catch(function () { say(i18n.fail, true); })
          .then(function () { btn.disabled = false; });
      } else {
        var lines = fields.map(function (f) { return f[0] + ": " + f[1]; }).join("\n");
        var subject = i18n.subject + (form.getAttribute("data-fleet") ? " (" + i18n.fleet + ")" : "");
        var href = "mailto:" + to + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines + "\n\n" + i18n.notconf);
        say("<strong>" + i18n.opened + "</strong> " + i18n.notconf + ' <a href="' + href + '">' + i18n.again + "</a>");
        window.location.href = href;
      }
    });
  });
})();
