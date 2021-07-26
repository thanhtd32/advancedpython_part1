#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://duythanhcse.wordpress.com
#Facebook for solving coding problem: https://www.facebook.com/groups/communityuni

#Description:
# These codes I improved from exercise 6o:
    # 1. Book input
    # 2. Search by book name
    # 3. Search by author name
    # 4. Search by publisher name
    # 5. End
# with input a new book:
    #title>>
    #Author's name>>
    #Publisher>>
    #price>>
    #Publication year>>
mybooks=[
    {"Title": "Android App Development", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
    {"Title": "Python", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
    {"Title": "JavaScript", "Author": "Pham Dieu",
     "Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
    {"Title": "HTML5", "Author": "Man Nhi",
     "Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
    {"Title": "Compiler", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
    {"Title": "C language", "Author": "Man Nhi",
     "Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
    {"Title": "Programming Linguistics", "Author": "Pham Dieu",
     "Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
    {"Title": "C# language", "Author": "Thanh Tran",
     "Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
    {"Title": "App Inventor", "Author": "Man Nhi",
     "Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]
while True:#Book input/search
    choice=input('''Enter/Search for Books
     1. Book input
     2. Search by book name
     3. Search by author name
     4. Search by publisher name
     5. End
     select(1,2,3,4,5):''')
    if choice=='1':#book input
        while True:#repeatly enter new books
            book=dict()
            title=input("title>>")
            author=input("Author's name>>")
            publisher = input("Publisher>>")
            price = input("price>>")
            year = input("Publication year>>")
            book["Title"]=title
            book["Author"] = author
            book["Publisher"] = publisher
            book["Price"] = price
            book["Published_Year"] = year
            mybooks.append(book)
            print("Enter a new book successfully!")
            continueEnterBook=input("Do you want to continue enter new book or not(Y/N)?>>")
            if continueEnterBook=='N' or continueEnterBook=='n':
                break
    elif choice=='2' :
        kwd="Title"
    elif choice=='3':
        kwd="Author"
    elif choice=='4':
        kwd="Publisher"
    elif choice=='5':
        break;
    else:
        print("input is invalid.")
    # finding the book with keyword:
    if choice=='2' or choice=='3' or choice=='4':
        userin=input(kwd+">>>")
        find=False
        print("Title\t\tAuthor\t\tPublisher\t\tPrice\t\tPublished Year")
        print("-"*40)
        for onebook in mybooks:
            if userin==onebook[kwd]:
                print(onebook["Title"], "\t", onebook["Author"], "\t",
                      onebook["Publisher"], "\t",onebook["Price"], "\t",
                      onebook["Published_Year"])
                find=True
        print("-" * 40)
        if find==False:
            print("No books were found.")
print("Thanks so much for your using the program!")
