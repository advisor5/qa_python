from main import BooksCollector
import pytest

class TestBooksCollector:
    
    # Проверка добавления двух книг
    def test_add_new_book_add_two_books(self):
        
        collector = BooksCollector()
        # добавляем две книги     
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        
        assert len(collector.get_books_genre()) == 2
    
    # Проверка невозможности добавить одну и ту же книгу несколько раз
    def test_add_new_book_same_book_no_added(self):
        collector = BooksCollector()
        # добавляем одну книгу    
        collector.add_new_book('Гордость и предубеждение и зомби')
        # добавляем ту же книгу повторно 
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    # Проверка добавления книги, содержащей допустимое количество символов (1, 32, 40)
    @pytest.mark.parametrize('name', ['А','Гордость и предубеждение и зомби', 'Гордость и предубеждение и зомби, и коты']) 
    def test_add_new_book_1_32_40_simbol_in_name_books_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1
    
    # Проверка невозможности добавления книги, содержащий недопустимое количество символов (0, 41, 42)
    @pytest.mark.parametrize('name', ['', 'Гордость и предубеждение и зомби, и коты!', 'Гордость и предубеждение и зомби, и коты!!' ]) 
    def test_add_new_book_0_41_42_simbol_in_name_books_no_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # Проверка отсутствия у добавленной книги жанра
    def test_set_book_genre_without_genre(self):

        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу без жанра
        collector.add_new_book(name)
        
        assert collector.get_book_genre(name) == ''  

    # Проверка добавления жарна книге
    def test_set_book_genre_comedy_added(self):
        
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Комедии'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жарн книге
        collector.set_book_genre(name, genre)
        
        assert collector.get_book_genre(name) == genre

    # Проверка недобавления отсутствующего в списке жанра книге
    def test_set_book_genre_not_in_list_genre_not_added(self):

        collector = BooksCollector()
        name = 'Гордость'
        genre = 'Аниме'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жарн книге
        collector.set_book_genre(name, genre)
        
        assert collector.get_book_genre(name) == ''

    # Проверка получения  жанра книги по её имени
    def test_get_book_genre_name_book_pride_is_detective(self):

        collector = BooksCollector()
        name_1 = 'Гордость и предубеждение и зомби'
        genre_1 = 'Комедии'
        name_2 = 'Гордость'
        genre_2 = 'Детективы'
        # добавляем книгу
        collector.add_new_book(name_1)
        # добавляем жарн книге
        collector.set_book_genre(name_1, genre_1)
        collector.add_new_book(name_2)
        # добавляем жарн книге
        collector.set_book_genre(name_2, genre_2)
        
        assert collector.get_book_genre(name_2) == genre_2

    # Проверка вывода списка книг с жанром - Комедии
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Гордость'])
    def test_get_books_with_specific_genre_comedy_done(self, name):
        
        collector = BooksCollector()
        genre = 'Комедии'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жарн книге
        collector.set_book_genre(name, genre)
        
        assert name in collector.get_books_with_specific_genre(genre)

    # Проверка вывода текущего словаря с книгами
    def test_get_books_genre_done(self):
        
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Комедии'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жарн книге
        collector.set_book_genre(name, genre)
        
        assert collector.get_books_genre() == {name: genre} 

    # Проверка книги по наименованию в списке книг, которые подходят детям
    def test_get_books_for_children_name_book_in_list_for_children(self):
        
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        genre = 'Комедии'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жарн книге
        collector.set_book_genre(name, genre)

        assert  name in collector.get_books_for_children()

    # Проверкка недобавления книги с возрастным рейтингом, в список книг для детей
    def test_get_books_for_children_book_in_genre_age_rating_not_added(self):
        
        collector = BooksCollector()
        name = 'Что делать, если ваш кот хочет вас убить'
        genre = 'Ужасы'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем жанр книге
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_for_children()) == 0

    # Проверкка добавления книги в избранное из словаря books_genre
    def test_add_book_in_favorites_by_name_done(self):
       
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в Избранное 
        collector.add_book_in_favorites(name)

        assert  name in collector.get_list_of_favorites_books()
     
    # Проверка недобавления книги в избранное, если ее нет в словаре - books_genre
    def test_add_book_in_favorites_book_which_does_not_in_dict_books_genre_not_added(self):
       
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в Избранное 
        collector.add_book_in_favorites('Гордость')

        assert collector.get_list_of_favorites_books() == []

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_by_name_done(self):
        
        collector = BooksCollector()
        
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в Избранное 
        collector.add_book_in_favorites(name)
        # удаляем книгу из Избранного
        collector.delete_book_from_favorites(name)
        
        assert collector.get_list_of_favorites_books() == []

    # Проверка по наименованию книги, ее наличие в избранном
    def test_get_list_of_favorites_books_by_name_in_favorites(self):
        
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        # добавляем книгу
        collector.add_new_book(name)
        # добавляем книгу в Избранное 
        collector.add_book_in_favorites(name)
       
        assert name in collector.get_list_of_favorites_books()      