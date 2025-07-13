---
layout: default
title: Illustration
permalink: /images/
---

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>

<section class="portfolio-gallery max-w-5xl mx-auto px-4 py-8">
  <h1 class="text-3xl font-bold text-center mb-12">Illustration</h1>

  {% assign folders = "" | split: "" %}
  {% for file in site.static_files %}
    {% if file.path contains 'assets/full_webp/' and file.extname == '.webp' %}
      {% assign parts = file.path | split: '/' %}
      {% assign folder = parts[3] %}
      {% unless folders contains folder %}
        {% assign folders = folders | push: folder %}
      {% endunless %}
    {% endif %}
  {% endfor %}

  {% assign sorted_folders = folders | sort %}
  {% for folder in sorted_folders %}
      {% assign genre_display = site.data.genres[folder] | default: folder %}
      <h2 class="text-2xl font-semibold mt-12 mb-4">{{ genre_display }}</h2>

    <div class="swiper mySwiper mb-8">
      <div class="swiper-wrapper">
        {% assign images = site.static_files | where: "extname", ".webp" %}
        {% assign sorted_images = images | sort: "name" %}
        {% assign folder_path = 'assets/full_webp/' | append: folder | append: '/' %}
        {% for image in sorted_images %}
          {% if image.path contains folder_path %}
            <div class="swiper-slide ">
              <img src="{{ image.path | relative_url }}" alt="{{ image.name }} "
                   class="swiper-thumb rounded shadow-md cursor-pointer w-full h-auto"
                   data-src="{{ image.path | relative_url }}"
                   data-folder="{{ folder }}"
                   id = "{{base}}">
            </div>
          {% endif %}
        {% endfor %}
      </div>
      <!-- Navigation -->
      <div class="swiper-button-next"></div>
      <div class="swiper-button-prev"></div>
      <!-- Pagination (optional) -->
      <div class="swiper-pagination"></div>
    </div>
  {% endfor %}
</section>

<!-- Modal -->
<div id="modal" class="modal hidden">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modal-img">
  <div class="modal-caption" id="modal-caption"></div>
    <div class="modal-nav">
    <button onclick="prevImage()">←</button>
    <button onclick="nextImage()">→</button>
  </div>
</div>

<style>
.modal-nav {
  margin-top: 1rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
}
.modal-nav button {
  background: white;
  border: none;
  padding: 0.5rem 1rem;
  font-size: 1.5rem;
  cursor: pointer;
  border-radius: 0.25rem;
}
</style>

<style>
.swiper {
  width: 100%;
  padding-bottom: 40px;
  max-width: 1200px;
}
.swiper-slide {
  width: auto;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: visible;
  margin: 12px 12px;
}
.swiper-slide img {
  height: clamp(200px, 30vw, 300px); /* 画面サイズに応じて */
  width: auto;             /* 縦横比を維持 */
  object-fit: contain;     /* 画像全体が収まるように */
    border-radius: 12px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1); /* 通常の影 */
}
.swiper-slide img:hover,
.swiper-slide img:active {
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(0,0,0,0.25); /* ホバー時の影 */
}
.modal {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  z-index: 9999;
}
.modal.hidden {
  display: none;
}
.modal-content {
  max-width: 90%;
  max-height: 80vh;
  object-fit: contain;
}
.modal-caption {
  color: white;
  margin-top: 1rem;
}
.close {
  position: absolute;
  top: 1rem;
  right: 2rem;
  color: white;
  font-size: 2rem;
  cursor: pointer;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<script>
  const modal = document.getElementById("modal");
  const modalImg = document.getElementById("modal-img");
  const modalCaption = document.getElementById("modal-caption");
  let currentImages = []; // ← ジャンルごとに差し替える
  let currentIndex = 0;

  // 各画像にイベントを追加
  document.querySelectorAll('.swiper-thumb').forEach((img) => {
    img.addEventListener('click', () => {
      const folder = img.dataset.folder;
      const allImages = Array.from(document.querySelectorAll(`.swiper-thumb[data-folder='${folder}']`));
      currentImages = allImages;
      currentIndex = allImages.indexOf(img); // ← 配列内でのインデックス
      openModal();
    });
  });

  function openModal() {
    modal.classList.remove("hidden");
    updateModal();
  }

  function closeModal() {
    modal.classList.add("hidden");
  }

  function updateModal() {
    const img = currentImages[currentIndex];
    modalImg.src = img.getAttribute("data-src") || img.src;
    modalCaption.textContent = img.alt || "";
  }

  function prevImage() {
    currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
    updateModal();
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % currentImages.length;
    updateModal();
  }

  // キーボード操作対応
  document.addEventListener('keydown', (e) => {
    if (modal.classList.contains("hidden")) return;
    if (e.key === "ArrowLeft") prevImage();
    if (e.key === "ArrowRight") nextImage();
    if (e.key === "Escape") closeModal();
  });
</script>


<script>
  document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".mySwiper").forEach((swiperEl) => {
    new Swiper(swiperEl, {
      slidesPerView: "auto",
      spaceBetween: 20,
      pagination: { el: swiperEl.querySelector(".swiper-pagination"), clickable: true },
      navigation: {
        nextEl: swiperEl.querySelector(".swiper-button-next"),
        prevEl: swiperEl.querySelector(".swiper-button-prev")
      }
    });
  });
});


  function closeModal() {
    document.getElementById("modal").classList.add("hidden");
  }
</script>
