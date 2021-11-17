from olclient.openlibrary import OpenLibrary
ol = OpenLibrary()
with open("dup.txt") as f:
    for line in f:
        olids = line.split(",")
        for olid in olids:
            work=ol.Work.get(olid)
            new_authors=[]
            for author in work.authors:
                if author not in new_authors:
                    new_authors.append(author)
            work.authors=new_authors
            #work.save("removed duplicate olid of author")
           
