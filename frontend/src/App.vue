<template>
  <div class="app-shell">
    <AppHeader />

    <main class="hero">
      <section class="hero__intro">
        <p class="eyebrow">Цифровая библиотека</p>
        <h1>Library Juls</h1>
        <a class="hero__link" href="#catalog">Электронный каталог</a>
      </section>

      <BookList
        id="catalog"
        :books="books"
        :loading="loading"
        :error-message="errorMessage"
        @add-book="addBook"
        @delete-book="deleteBook"
      />
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import AppFooter from '@/components/AppFooter.vue';
import AppHeader from '@/components/AppHeader.vue';
import BookList from '@/components/BookList.vue';

const books = ref([]);
const loading = ref(false);
const errorMessage = ref('');

async function requestJson(url, options = {}) {
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`Ошибка API: ${response.status}`);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

async function loadBooks() {
  loading.value = true;
  errorMessage.value = '';

  try {
    books.value = await requestJson('/api/books');
  } catch (error) {
    errorMessage.value = 'Не удалось загрузить каталог книг.';
  } finally {
    loading.value = false;
  }
}

async function addBook(bookPayload) {
  errorMessage.value = '';

  try {
    const createdBook = await requestJson('/api/books', {
      method: 'POST',
      body: JSON.stringify(bookPayload),
    });

    books.value = [...books.value, createdBook];
  } catch (error) {
    errorMessage.value = 'Не удалось добавить книгу.';
  }
}

async function deleteBook(bookId) {
  errorMessage.value = '';

  try {
    await requestJson(`/api/books/${bookId}`, {
      method: 'DELETE',
    });

    books.value = books.value.filter((book) => book.id !== bookId);
  } catch (error) {
    errorMessage.value = 'Не удалось удалить книгу.';
  }
}

onMounted(loadBooks);
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
