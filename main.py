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
            if work.authors==new_authors:
                print(f"Skip {work.olid}")
            else:
                work.authors=new_authors
                print(f"Deduplicated {work.olid}")
                work.save("Removed duplicate olid of author")
           
