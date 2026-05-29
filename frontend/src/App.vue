<template>
  <div class="app-shell">
    <AppHeader />

    <main class="hero">
      <section class="hero__intro">
        <p class="eyebrow">Цифровая библиотека</p>
        <h1>ElectoLibrary</h1>
        <p class="hero__description">
          Прототип SPA-приложения для поиска, просмотра и дальнейшего управления
          электронным книжным каталогом.
        </p>
        <a class="hero__link" href="#catalog">Электронный каталог</a>
      </section>

      <BookList id="catalog" :books="books" />
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import AppFooter from '@/components/AppFooter.vue';
import AppHeader from '@/components/AppHeader.vue';
import BookList from '@/components/BookList.vue';

const books = [
  {
    id: 1,
    title: 'Чистый код',
    author: 'Роберт Мартин',
    description: 'Практики написания поддерживаемого и читаемого кода.',
    publisher: 'Питер',
    year: 2020,
    category: 'Программирование',
    available: true,
  },
  {
    id: 2,
    title: 'Алгоритмы. Построение и анализ',
    author: 'Томас Кормен',
    description: 'Базовый академический справочник по алгоритмам и структурам данных.',
    publisher: 'Вильямс',
    year: 2019,
    category: 'Информатика',
    available: false,
  },
  {
    id: 3,
    title: 'Паттерны проектирования',
    author: 'Эрих Гамма и др.',
    description: 'Классическое руководство по объектно-ориентированным паттернам.',
    publisher: 'Диалектика',
    year: 2021,
    category: 'Архитектура ПО',
    available: true,
  },
];
</script>

<style>
:root {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  color: #1f2933;
  background:
    radial-gradient(circle at top, rgba(121, 178, 255, 0.25), transparent 35%),
    linear-gradient(180deg, #f7fafc 0%, #edf2f7 100%);
  line-height: 1.5;
  font-weight: 400;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-width: 320px;
}

a {
  color: inherit;
  text-decoration: none;
}

#app {
  min-height: 100vh;
}
</style>

<style scoped>
.app-shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.hero {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
  padding: 32px 0 48px;
  display: grid;
  gap: 32px;
}

.hero__intro {
  padding: 32px;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.86);
  box-shadow: 0 20px 60px rgba(15, 23, 42, 0.08);
}

.eyebrow {
  margin: 0 0 12px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.8rem;
  color: #486581;
}

h1 {
  margin: 0;
  font-size: clamp(2.2rem, 4vw, 3.8rem);
  line-height: 1.05;
  color: #102a43;
}

.hero__description {
  max-width: 720px;
  margin: 16px 0 24px;
  font-size: 1.05rem;
  color: #334e68;
}

.hero__link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 18px;
  border-radius: 999px;
  background: #0f766e;
  color: #fff;
  font-weight: 600;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.hero__link:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 24px rgba(15, 118, 110, 0.28);
}

@media (max-width: 768px) {
  .hero {
    width: min(100% - 20px, 1120px);
    padding-top: 20px;
  }

  .hero__intro {
    padding: 24px 20px;
  }
}
</style>
