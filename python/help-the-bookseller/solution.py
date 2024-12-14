def stock_list(list_of_art, list_of_cat):
    dictionary = {}
    for book in list_of_art:
        category_label = book[0]
        if category_label in list_of_cat:
            separator = book.find(" ")
            book_code = int(book[separator+1:])

            if category_label not in dictionary:
                dictionary[category_label] = book_code
            else:
                dictionary[category_label] += book_code 

    zero_books = []
    result = ""
    for cat in list_of_cat:
        if cat in dictionary:
            book_code = dictionary[cat]
            if result != "":
                result += ' - ({} : {})'.format(cat, book_code)
            else:
                result = '({} : {})'.format(cat, book_code)
        else:
            zero_books.append(cat)
            if result != "":
                result += ' - ({} : {})'.format(cat, 0)
            else:
                result = '({} : {})'.format(cat, 0)
    if zero_books == list_of_cat:
        return ''
    return result