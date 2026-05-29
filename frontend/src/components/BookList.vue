<template>
  <section class="catalog">
    <div class="catalog__heading">
      <div>
        <p class="catalog__eyebrow">Каталог</p>
        <h2>Доступные книги</h2>
      </div>
      <span class="catalog__count">Всего: {{ books.length }}</span>
    </div>

    <div class="catalog__grid">
      <BookItem
        v-for="book in books"
        :key="book.id"
        :book="book"
      />
    </div>
  </section>
</template>

<script setup>
import BookItem from '@/components/BookItem.vue';

defineProps({
  books: {
    type: Array,
    required: true,
  },
});
</script>

<style scoped>
.catalog {
  padding: 28px;
  border-radius: 24px;
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

.catalog__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
}

@media (max-width: 768px) {
  .catalog {
    padding: 22px 18px;
  }

  .catalog__heading {
    flex-direction: column;
    align-items: start;
  }
}
</style>
