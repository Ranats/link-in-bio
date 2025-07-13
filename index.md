---
layout: default
title: Glasse-age
permallink: /
---

<div class="profile">
  <img src="https://avatars.githubusercontent.com/u/9674834?v=4" alt="Ranats">
  <h1>Satoshi Coda. / Ranats のリンク集</h1>
</div>

<div class="links">
  <div class="link-card">
    <a href="https://ranats.github.io/kurohon-roulette" target="_blank">🎷 黒本ルーレット</a>
    <p>ジャズスタンダード曲をランダム抽選<br>
      キー・スタイルで絞り込み可能！</p>
  </div>
  <div class="link-card">
    <a href="https://note.com/ranats" target="_blank">📝 note連載</a>
    <p>ジャズや教育、AI活用について発信予定です！</p>
  </div>
  <div class="link-card">
    <a href="https://github.com/ranats" target="_blank">💻 GitHub プロジェクト一覧</a>
    <p>教育×AI×自動化のコードやツール公開中！</p>
  </div>
</div>

<!-- Carousel Section -->
<section id="portfolio-carousel" class="container py-8 bg-gray-900">
  <div class="max-w-6xl mx-auto px-4">
    <h2 class="text-3xl font-bold text-white mb-6">Illustration</h2>
    
<!-- Swiper CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

{% assign folders = "" | split: "" %}
{% for file in site.static_files %}
  {% if file.path contains 'assets/thumbnails/' and file.extname == '.webp' %}
    {% assign parts = file.path | split: '/' %}
    {% assign folder = parts[2] %}
    {% unless folders contains folder %}
      {% assign folders = folders | push: folder %}
    {% endunless %}
  {% endif %}
{% endfor %}

{% assign sorted_folders = folders | sort %}
{% for folder in sorted_folders %}

<div class="swiper mySwiper mb-8">
  <div class="swiper-wrapper">
    {% assign thumbs = site.static_files | where: "extname", ".webp" %}
    {% assign sorted_thumbs = thumbs | sort: "name" %}
    {% for image in sorted_thumbs %}
      {% if image.path contains folder and image.path contains 'assets/thumbnails/' %}
        {% assign base = image.name | split: '.' | first %}
        <div class="swiper-slide thumb">
          <a href="/images/#{{ base }} | relative_url }}">
            <img src="{{ image.path | relative_url }}"
                 alt="{{ image.name }}"
                 >
          </a>
        </div>
      {% endif %}
    {% endfor %}
  </div>
  <div class="swiper-button-next"></div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-pagination"></div>
</div>
{% endfor %}

  </div>
</section>

<div class="support-section">
  <h2>🎁 応援はこちらから / Support & Donations</h2>
  <div class="support-buttons">
    <a href="https://coff.ee/sopurani88f" target="_blank">Buy Me a Coffee</a>
    <a href="https://github.com/sponsors/Ranats" target="_blank">GitHub Sponsors</a>
    <a href="https://ofuse.me/d2c3aa65" target="_blank">OFUSE</a>
    <a href="https://ko-fi.com/ranats" target="_blank">Ko-fi</a>
  </div>
</div>

<!-- Swiper JS -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".mySwiper").forEach((el) => {
      new Swiper(el, {
        slidesPerView: "auto",
        spaceBetween: 20,
        navigation: {
          nextEl: el.querySelector(".swiper-button-next"),
          prevEl: el.querySelector(".swiper-button-prev")
        },
        pagination: {
          el: el.querySelector(".swiper-pagination"),
          clickable: true
        },
        keyboard: { enabled: true }
      });
    });
  });
</script>

<style>
.swiper-slide.thumb {
  width: 180px;
  flex-shrink: 0;
}
.swiper-slide.thumb img {
  width: 100%;
  height: auto;
  object-fit: cover;
}
.container {
  max-width: 500px;
  margin: 0 auto;
  padding: 0 1rem;
}

</style>
