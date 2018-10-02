#create parent class Media(attribute:title,author,topic,language)
class Media:
    def __init__(self,title,author,topic,language):
        self.__title      = title
        self.__author     = author
        self.__topic      = topic
        self.__language   = language


#create child class Book, add own attribute location and inherit all patent class's attribute
class Book(Media):
    __location = None
    def __init__(self,title,author,topic,language,location):
        super(Book,self).__init__(title,author,topic,language)
        self.__location = location

  #add books, save records in book_file0.txt
    def Book_add(self,add_number):
        print(self._Media__title,'\nYou added %d books successfully!\n'%(add_number))
        with open('book_file0.txt','a') as book_file:
            book_file.write('\n\n''title:{},author:{},topic:{},language:{},location:{}   *add_number:{}'
                            .format(self._Media__title,self._Media__author,self._Media__topic,
                                    self._Media__language,self.__location,add_number))

  #search books' adding/borrowing/returning record from book_file0.txt
    def search_total(self,search_type):
        number = 0
        with open ('book_file0.txt','r') as find_number:
            for i in find_number:
                line = find_number.readline()
                if line.find(search_type) > 0  and  line.find(self._Media__title) > 0:
                    str1,str2 = line.split(search_type)
                    number += int(str2)
            return(number)

  #calculate books' total and stock
    def Book_check(self):
        self.__total  = self.search_total('add_number:')
        self.__inside = self.search_total('add_number:') - self.search_total('borrow_number:') \
                         + self.search_total('return_number:')
        print(self._Media__title,'\nTotal of books is: ',self.__total,'\nBooks inside is: ',self.__inside,'\n')

  #borrow books, if inside>0, say it can be borrowed, save record in book_file0.txt
    def Book_borrow(self):
        if self.__inside > 0:
            print(self._Media__title,'\nYou borrowed the book successfully!\n')
            self.__inside -= 1
            with open('book_file0.txt','a') as book_file:
                book_file.write('\n\n''title:{},author:{},topic:{},language:{},location:{}   *borrow_number:{}'
                                .format(self._Media__title,self._Media__author,self._Media__topic,
                                        self._Media__language,self.__location,1))
        else:
            print(self._Media__title,'\nSorry, the book has been borrowed!\n')

  #return books, save record in book_file0.txt
    def Book_return(self):
        print(self._Media__title,'\nYou returned the book successfully!\n')
        with open('book_file0.txt','a') as book_file:
            book_file.write('\n\n''title:{},author:{},topic:{},language:{},location:{}   *return_number:{}'
                            .format(self._Media__title,self._Media__author,self._Media__topic,
                                    self._Media__language,self.__location,1))

  #calculate fines, use Nested if statement
    def Book_cost(self,dags):
        if self._Media__topic is 'novel' or 'short story':
            if dags <= 30:
                cost = 0
            elif 30 < dags <= 60:
                cost = (dags - 30)*5
            else:
                cost = (30*5) + (dags - 60)*20
        else:
            if dags <= 60:
                cost = 0
            else:
                cost = (dags - 60)*5
        print('Your fines is : ',cost,' kr','\n')


#create child class Ebook, inherit all patent class's attribute
class Ebook(Media):
    def __init__(self,title,author,topic,language):
        super(Ebook,self).__init__(title,author,topic,language)

  #set dictionary(age_limit), according to class attribute to check is it allowed to borrow the ebook
    def Ebook_borrow(self):
        age = int(input('Please enter your age: '))
        age_limit = {'novel':18,'short story':18,'history':16,'geography':15,'kids book':0}
        limit = age_limit[self._Media__topic]
        print('\n')
        if age >= limit:
            print(self._Media__title,'\nYes,you can borrow this e-book\n')
        else:
            print(self._Media__title,'\nSorry,you have\'nt reached the age\n')


#set items
book1  = Book('Forgiven','Agnes Lidbeck','novel','swedish','Shelf 4')
book2  = Book('The war that ended peace','Margaret MacMillan','history','english','Shelf 8')
ebook1 = Ebook('A guided tour of London','John Præstegaard','geography','english')
ebook2 = Ebook('Rich boy','Caroline Ringskog','novel','swedish')


#define functions add_book(),check_book(),Etc., to call class's method, asking for input
def add_book():
    book     = (eval(input('Which book do you want to add?')))
    quantity = int(input('How many books do you want to add? '))
    print('\n')
    book.Book_add(quantity)

def check_book():
    book = (eval(input('Which book do you want to check?')))
    print('\n')
    book.Book_check()

def borrow_book():
    book = (eval(input('Which book do you want to borrow?')))
    print('\n')
    book.Book_check()
    book.Book_borrow()

def return_book():
    book = (eval(input('Which book do you want to return?')))
    print('\n')
    book.Book_return()

def calculate_cost():
    book = (eval(input('Which book have you borrowed?')))
    dags = int(input('How many dags have you borrowed? '))
    print('\n')
    book.Book_cost(dags)

def borrow_ebook():
    ebook = (eval(input('Which ebook do you want to borrow?')))
    ebook.Ebook_borrow()

#search en book's all records from book_file0.txt and output to book_record0.txt for checking
def search_book():
    search_str = (input('Which book do you want to search? (title/author)'))
    with open ('book_file0.txt','r') as find_line:
        with open ('book_record0.txt','w') as write_line:
            for i in find_line:
                line = find_line.readline()
                if line.find(search_str) > 0:
                    write_line.write(line)
            print('\nNow, you kan find records in book_record0.txt\n')


#build a menu for administrator, choose how to manage books, then call functions above
def management():
    while True:
        print("**---Welcome to Li's library---**")
        print("1 add books")
        print("2 check books")
        print("3 search books record")
        print("4 exit")
        print("**-----------------------------**\n")
        choice=input("Please enter a option ： ")
        if choice is '1':
            add_book()
        elif choice is '2':
            check_book()
        elif choice is '3':
            search_book()
        elif choice is '4':
            print('\nThank you for your using!\n')
            break
        else:
             print("Please enter a valid action option！\n\n")

#build a menu for customer, choose how to borrow/return books,Etc., then call functions above
def using():
    while True:
        print("**---Welcome to Li's library---**")
        print("1: borrow books")
        print("2: return books")
        print("3: calculate cost")
        print("4: borrow e-books")
        print("5: exit")
        print("**-----------------------------**\n")
        choice=input("Please enter a option ：")
        if choice is '1':
            borrow_book()
        elif choice is '2':
            return_book()
        elif choice is '3':
            calculate_cost()
        elif choice is '4':
            borrow_ebook()
        elif choice is '5':
            print('\nThank you for your using!\n')
            break
        else:
             print("Please enter a valid action option！\n\n")


