import csv

def get_species_from_molis(filename):
    corres = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for row in [[s.strip() for s in inner] for inner in reader]:
            cells = list(filter(None, row))
            if cells:
                corres[cells[0]]={}
                corres[cells[0]]["genus"]=cells[1].replace(" ", "")
                corres[cells[0]]["species"]=cells[2].replace(" ", "")
    return(corres)
