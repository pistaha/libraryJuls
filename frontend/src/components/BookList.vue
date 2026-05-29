<template>
  <section class="catalog">
    <div class="catalog__heading">
      <div>
        <p class="catalog__eyebrow">Каталог</p>
        <h2>Книги библиотеки</h2>
      </div>
      <span class="catalog__count">Найдено: {{ filteredBooks.length }} из {{ books.length }}</span>
    </div>

    <form class="book-form" @submit.prevent="submitBook">
      <label>
        Название
        <input v-model.trim="form.title" required type="text" placeholder="Название книги">
      </label>
      <label>
        Автор
        <input v-model.trim="form.author" required type="text" placeholder="Автор">
      </label>
      <label>
        Описание
        <textarea v-model.trim="form.description" required rows="3" placeholder="Краткое описание"></textarea>
      </label>
      <label>
        Издательство
        <input v-model.trim="form.publisher" required type="text" placeholder="Издательство">
      </label>
      <label>
        Год
        <input v-model.number="form.year" required min="1" type="number">
      </label>
      <label>
        Категория
        <input v-model.trim="form.category" required type="text" placeholder="Категория">
      </label>
      <label class="book-form__checkbox">
        <input v-model="form.available" type="checkbox">
        Доступна для выдачи
      </label>
      <button type="submit">Добавить книгу</button>
    </form>

    <div class="filters">
      <label>
        Поиск
        <input v-model.trim="searchQuery" type="search" placeholder="Название, автор, описание">
      </label>
      <label>
        Категория
        <select v-model="categoryFilter">
          <option value="">Все категории</option>
          <option v-for="category in categories" :key="category" :value="category">
            {{ category }}
          </option>
        </select>
      </label>
      <label>
        Статус
        <select v-model="availabilityFilter">
          <option value="all">Все книги</option>
          <option value="available">Доступные</option>
          <option value="busy">Выданные</option>
        </select>
      </label>
    </div>

    <p v-if="errorMessage" class="catalog__message catalog__message--error">
      {{ errorMessage }}
    </p>
    <p v-else-if="loading" class="catalog__message">
      Загрузка каталога...
    </p>
    <p v-else-if="!filteredBooks.length" class="catalog__message">
      По выбранным условиям книг нет.
    </p>

    <div v-else class="catalog__grid">
      <BookItem
        v-for="book in filteredBooks"
        :key="book.id"
        :book="book"
        @delete-book="$emit('delete-book', book.id)"
      />
    </div>
  </section>
</template>

<script setup>
import { computed, reactive, ref } from 'vue';
import BookItem from '@/components/BookItem.vue';

const props = defineProps({
  books: {
    type: Array,
    required: true,
  },
  loading: {
    type: Boolean,
    default: false,
  },
  errorMessage: {
    type: String,
    default: '',
  },
});

const emit = defineEmits(['add-book', 'delete-book']);

const currentYear = new Date().getFullYear();
const searchQuery = ref('');
const categoryFilter = ref('');
const availabilityFilter = ref('all');

const form = reactive(createEmptyForm());

const categories = computed(() => {
  return [...new Set(props.books.map((book) => book.category).filter(Boolean))].sort((a, b) => {
    return a.localeCompare(b, 'ru');
  });
});

const filteredBooks = computed(() => {
  const query = searchQuery.value.toLowerCase();

  return props.books.filter((book) => {
    const matchesSearch = !query || [
      book.title,
      book.author,
      book.description,
      book.publisher,
    ].some((value) => value.toLowerCase().includes(query));

    const matchesCategory = !categoryFilter.value || book.category === categoryFilter.value;
    const matchesAvailability =
      availabilityFilter.value === 'all' ||
      (availabilityFilter.value === 'available' && book.available) ||
      (availabilityFilter.value === 'busy' && !book.available);

    return matchesSearch && matchesCategory && matchesAvailability;
  });
});

function createEmptyForm() {
  return {
    title: '',
    author: '',
    description: '',
    publisher: '',
    year: currentYear,
    category: '',
    available: true,
  };
}

function resetForm() {
  Object.assign(form, createEmptyForm());
}

function submitBook() {
  emit('add-book', {
    title: form.title,
    author: form.author,
    description: form.description,
    publisher: form.publisher,
    year: Number(form.year),
    category: form.category,
    available: form.available,
  });

  resetForm();
}
</script>

<style scoped>
.catalog {
  padding: 28px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.92);
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
}

.catalog__heading {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 16px;
  margin-bottom: 24px;
}

.catalog__eyebrow {
  margin: 0 0 8px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.8rem;
  color: #486581;
}

.catalog h2 {
  margin: 0;
  color: #102a43;
}

.catalog__count {
  color: #627d98;
  font-weight: 600;
}

.book-form,
.filters {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  margin-bottom: 22px;
}

.book-form {
  padding: 18px;
  border: 1px solid rgba(148, 163, 184, 0.26);
  border-radius: 12px;
  background: #f8fbff;
}

.filters {
  margin-top: 12px;
}

.book-form label,
.filters label {
  display: grid;
  gap: 7px;
  color: #486581;
  font-size: 0.86rem;
  font-weight: 700;
}

.book-form input,
.book-form textarea,
.filters input,
.filters select {
  width: 100%;
  border: 1px solid rgba(98, 125, 152, 0.34);
  border-radius: 8px;
  padding: 10px 12px;
  color: #102a43;
  font: inherit;
  background: #ffffff;
}

.book-form textarea {
  resize: vertical;
}

.book-form__checkbox {
  align-self: end;
  display: flex !important;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 9px !important;
  min-height: 42px;
}

.book-form__checkbox input {
  width: 18px;
  height: 18px;
}

.book-form button {
  align-self: end;
  min-height: 42px;
  border: 0;
  border-radius: 8px;
  padding: 10px 14px;
  background: #0f766e;
  color: #ffffff;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}

.book-form button:hover {
  background: #0b5f59;
}

.catalog__message {
  margin: 0;
  padding: 18px;
  border-radius: 12px;
  background: #eef6ff;
  color: #334e68;
  font-weight: 600;
}

.catalog__message--error {
  background: #fee2e2;
  color: #991b1b;
}

.catalog__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
  margin-top: 12px;
}

@media (max-width: 900px) {
  .book-form,
  .filters {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 768px) {
  .catalog {
    padding: 22px 18px;
  }

  .catalog__heading {
    flex-direction: column;
    align-items: start;
  }

  .book-form,
  .filters {
    grid-template-columns: 1fr;
  }
}
</style>
