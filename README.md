# Sprint_4

Тесты:

1 - test_add_new_book_add_two_books - Проверка добавления двух книг 
2 - test_add_new_book_same_book_no_added - Проверка невозможности добавить одну и ту же книгу несколько раз
3 - test_add_new_book_1_32_40_simbol_in_name_books_added - Проверка добавления книги, содержащей допустимое количество символов (1, 32, 40)
4 - test_add_new_book_0_41_42_simbol_in_name_books_no_added - Проверка невозможности добавления книги, содержащий недопустимое количество символов (0, 41, 42)
5 - test_set_book_genre_without_genre - Проверка отсутствия у добавленной книги жанра
6 - test_set_book_genre_comedy_added - Проверка добавления жарна книге
7 - test_set_book_genre_not_in_list_genre_not_added - Проверка недобавления отсутствующего в списке жанра книге
8 - test_get_book_genre_name_book_pride_is_detective - Проверка получения  жанра книги по её имени
9 - test_get_books_with_specific_genre_comedy_done -     # Проверка вывода списка книг с жанром - Комедии
10 - test_get_books_genre_done - Проверка вывода текущего словаря с книгами
11 - test_get_books_for_children_name_book_in_list_for_children - Проверка книги по наименованию в списке книг, которые подходят детям
12 - test_get_books_for_children_book_in_genre_age_rating_not_added - Проверкка недобавления книги с возрастным рейтингом, в список книг для детей
13 - test_add_book_in_favorites_by_name_done - Проверкка добавления книги в избранное из словаря books_genre
14 - test_add_book_in_favorites_book_which_does_not_in_dict_books_genre_not_added - Проверка недобавления книги в избранное, если ее нет в словаре - books_genre
15 - test_delete_book_from_favorites_by_name_done - Проверка удаления книги из избранного
16 - test_get_list_of_favorites_books_by_name_in_favorites - Проверка по наименованию книги, ее наличие в избранном