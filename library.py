#creat a superclass 'Media'
class Media:
    def __init__(self,title,author,topic,language):
        self.__title      = title
        self.__author     = author
        self.__topic      = topic
        self.__language   = language


#new class 'Book' add 'location' as parameter
class Book(Media):
    __total = 0
    __inside = 0
    def __init__(self,title,author,topic,language,location):
        super(Book,self).__init__(title,author,topic,language)
        self.__location    = location

  #add books
    def Book_add(self,add_number):
        print(self._Media__title,'\nyou added %d books successfully!\n'%(add_number))
        with open('book_file0.txt','a') as book_file:
            book_file.write('\n\n''title:{},author:{},topic:{},language:{},location:{}   *add_number:{}'
                            .format(self._Media__title,self._Media__author,self._Media__topic,
                                    self._Media__language,self.__location,add_number))

  #check quantity of books
    def Book_check(self):
        global __total
        global __inside
        def search_total(search_type):
            sum = 0
            with open ('book_file0.txt','r') as find_number:
                for i in find_number:
                    line = find_number.readline()
                    if line.find(search_type)>0 and line.find(self._Media__title)>0:
                        str1,str2=line.split(search_type)
                        sum += int(str2)
            return(sum)
        self.__inside = search_total('add_number:') - search_total('borrow_number:') + search_total('return_number:')
        self.__total = search_total('add_number:')
        print(self._Media__title,'\ntotal of books is: ',self.__total,'\ninside of books is: ',self.__inside,'\n')

  #borrow books
    def Book_borrow(self):
        if self.__inside > 0:
            print(self._Media__title,'\nyou borrowed the book successfully!\n')
            self.__inside-=1
            with open('book_file0.txt','a') as book_file:
                book_file.write('\n\n''title:{},author:{},topic:{},language:{},location:{}   *borrow_number:{}'
                                .format(self._Media__title,self._Media__author,self._Media__topic,
                                        self._Media__language,self.__location,1))
        else:
            print(self._Media__title,'\nsorry, the book has been borrowed!\n')

  #return books
    def Book_return(self):
        print(self._Media__title,'\nyou returned the book successfully!\n')
        self.__inside+=1
        with open('book_file0.txt','a') as book_file:
            book_file.write('\n\n''title:{},author:{},topic:{},language:{},location:{}   *return_number:{}'
                            .format(self._Media__title,self._Media__author,self._Media__topic,
                                    self._Media__language,self.__location,1))

  #calculate cost
    def Book_cost(self,dags):
        if self._Media__topic is 'novel' or 'short story':
            if dags <= 30:
                cost = 0
            elif 30 < dags <= 60:
                cost = (dags - 30)*5
            else:
                cost = 30*5 + (dags-60)*20
        else:
            if dags <= 60:
                cost = 0
            else:
                cost = (dags-60)*5
        print('your cost is : ',cost,'\n')


#new class 'Ebook' add 'limited' as parameter
class Ebook(Media):
    def __init__(self,title,author,topic,language,age_limited):
        super(Ebook,self).__init__(title,author,topic,language)
        self.__age_limited     = age_limited

  #borrow e-books
    def Ebook_borrow(self):
        age=int(input('please enter your age: '))
        print('\n')
        if age >= self.__age_limited:
            print(self._Media__title,'\nyes,you can borrow this e-book\n')
        else:
            print(self._Media__title,'\nsorry,you have\'nt reached the age\n')


#set items
book1  = Book('Forgiven','Agnes Lidbeck','novel','swedish','Shelf 4')
book2  = Book('The war that ended peace','Margaret MacMillan','history','english','Shelf 8')
ebook1 = Ebook('A guided tour of London','John Præstegaard','geography','english',12)
ebook2 = Ebook('Rich boy','Caroline Ringskog','novel','swedish',18)

#add books
def add_book():
    book= (eval(input('Which book do you want to add?')))
    quantity = int(input('How many books do you want to add? '))
    print('\n')
    book.Book_add(quantity)

#check books
def check_book():
    book= (eval(input('Which book do you want to check?')))
    print('\n')
    book.Book_check()

#seach the record of a book
def search_book():
    search_str = (input('Which book do you want to search? (title/author)'))
    with open ('book_file0.txt','r') as find_line:
        with open ('book_record0.txt','w') as write_line:
            for i in find_line:
                line=find_line.readline()
                if line.find(search_str)>0:
                    write_line.write(line)

#borrow books
def borrow_book():
    book= (eval(input('Which book do you want to borrow?')))
    print('\n')
    book.Book_borrow()

#return books
def return_book():
    book= (eval(input('Which book do you want to return?')))
    print('\n')
    book.Book_return()

#calculate cost
def calculate_cost():
    book= (eval(input('Which book have you borrowed?')))
    dags = int(input('How many dags have you borrowed? '))
    print('\n')
    book.Book_cost(dags)

#borrow e-books
def borrow_ebook():
    ebook= (eval(input('Which ebook do you want to borrow?')))
    ebook.Ebook_borrow()


# Media management
def management():
    while True:
        print("----HELP:----")
        print("1: set items")
        print("2: add books")
        print("3: check books")
        print("4: search books record")
        print("5: exit")
        print("-------------\n")
        choice=input("Please enter a option ：")
        if choice is '2':
            add_book()
        elif choice is '3':
            check_book()
        elif choice is '4':
            search_book()
        elif choice is '5':
            break
        else:
             print("Please enter a valid action option！")

#Customer using
def using():
    while True:
        print("----HELP:----")
        print("1: check inside")
        print("2: borrow books")
        print("3: return books")
        print("4: calculate cost")
        print("5: borrow e-books")
        print("6: exit")
        print("-------------\n")
        choice=input("Please enter a option ：")
        if choice is '2':
            borrow_book()
        elif choice is '3':
            return_book()
        elif choice is '4':
            calculate_cost()
        elif choice is '5':
            borrow_ebook()
        elif choice is '6':
            break
        else:
             print("Please enter a valid action option！")

'''running'''
#management()
using()

