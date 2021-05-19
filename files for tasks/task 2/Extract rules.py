def extract_rules(old_file, new_file, rule):
    with open(old_file, "r") as file:
        data = file.readlines()

    for line in data:
        new_line = line.split("==>")
        right = new_line[1]
        if rule in right:
            newfile = open(new_file, "a")
            newfile.write(line)
            
    newfile.close()

#eg extract_rules("assoc rules.txt", "assoc rules (yes).txt", "price_category=Yes")