books={
    "physics":180,
    "Chemistry":220,
    "math":250
}
books["physics"]=200
print(books)
books["SS"]=190
books["French"]=200
print(books)
print(books.keys())
del books["French"]
print(books)