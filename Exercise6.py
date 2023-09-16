#Coder: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Phone: 0987773061
#Blog for self-study: https://tranduythanh.com

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
while True:#Book Search Keywords
    choice=input('''Book Search Keywords
     1. Book name
     2. Author name
     3. Publisher name
     select(1,2,3):''')
    if choice=='1' :
        kwd="Title"
        break
    elif choice=='2':
        kwd="Author"
        break
    elif choice=='3':
        kwd="Publisher"
        break
    else:
        print("Invalid input.")
userin=input(kwd+">>>")
find=False
for onebook in mybooks:
    if userin==onebook[kwd]:
        print("Title:", onebook["Title"])
        print("Author:", onebook["Author"])
        print("Publisher:", onebook["Publisher"])
        print("Price", onebook["Price"])
        find=True
if find==False:
    print("There are no books found..")
