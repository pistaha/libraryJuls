<template>
  <article class="book-card">
    <div class="book-card__top">
      <span class="book-card__category">{{ book.category }}</span>
      <span :class="['book-card__badge', book.available ? 'is-available' : 'is-busy']">
        {{ book.available ? 'Доступна' : 'Выдана' }}
      </span>
    </div>

    <h3>{{ book.title }}</h3>
    <p class="book-card__author">{{ book.author }}</p>
    <p class="book-card__description">{{ book.description }}</p>

    <dl class="book-card__meta">
      <div>
        <dt>Издательство</dt>
        <dd>{{ book.publisher }}</dd>
      </div>
      <div>
        <dt>Год</dt>
        <dd>{{ book.year }}</dd>
      </div>
    </dl>

    <button class="book-card__delete" type="button" @click="$emit('delete-book')">
      Удалить
    </button>
  </article>
</template>

<script setup>
defineProps({
  book: {
    type: Object,
    required: true,
  },
});

defineEmits(['delete-book']);
</script>

<style scoped>
.book-card {
  padding: 20px;
  border-radius: 20px;
  background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
  border: 1px solid rgba(148, 163, 184, 0.22);
}

.book-card__top {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
}

.book-card__category {
  font-size: 0.82rem;
  color: #486581;
}

.book-card__badge {
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 700;
}

.book-card__badge.is-available {
  background: #d1fae5;
  color: #065f46;
}

.book-card__badge.is-busy {
  background: #fee2e2;
  color: #991b1b;
}

.book-card h3 {
  margin: 16px 0 8px;
  color: #102a43;
}

.book-card__author {
  margin: 0 0 12px;
  color: #0f766e;
  font-weight: 600;
}

.book-card__description {
  margin: 0 0 18px;
  color: #52606d;
}

.book-card__meta {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin: 0;
}

.book-card__meta div {
  padding-top: 12px;
  border-top: 1px solid rgba(148, 163, 184, 0.2);
}

.book-card__meta dt {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #829ab1;
}

.book-card__meta dd {
  margin: 6px 0 0;
  color: #334e68;
  font-weight: 600;
}

.book-card__delete {
  width: 100%;
  margin-top: 18px;
  border: 1px solid rgba(153, 27, 27, 0.18);
  border-radius: 8px;
  padding: 10px 12px;
  background: #fff5f5;
  color: #991b1b;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}

.book-card__delete:hover {
  background: #fee2e2;
}
</style>
