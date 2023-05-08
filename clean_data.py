import csv

# keyword_dict ={ "for":"until" , "while":"until",'[':"array of",']':" ",'_':"suffix of",'^':"to the power"}
replace_dict = { "for":"until" , "while":"until",'[':"array of",']':" ",'_':"suffix of",'^':"to the power",
               '=':"assign to",'==':"equal to",'⊕' : "XOR",'∀' : "For All",'∃' : "There Exists",'∈' : "Belongs to",'∉' : "Does not Belong to",'f̂' : "f_^",'⊆' : "is subset of",
'⊂' : "is subset of",'ø' : "Phi",'∅' : "Phi",'α' : "alpha",'β' : "beta",'γ' : "Gamma",'δ' : "Delta",'ε' : "Epsilon",'η' : "Eta",'θ' : "Theta",'κ' : "Kappa",'λ' : "Lambda",
'μ' : "mu",'π' : "pi",'ρ' : "rho",'υ' : "nu",'φ' : "si",'∞' : "Infinity",'σ' : "sigma",'∏' : "product",'∑' : "sum",'Π' : "product",'Σ' : "sum",
'Δ' : "Delta",'∪' : "Union",'∩' : "Intersection",'≠' : "is Not Equal to",'←' : "is assigned",'⇒' : "Implies",'→' : "is assigned to",'⇔' : "Implies and Implied by"}

with open('pseudo_desc.csv', 'r+') as input_file, open('cleaned_pseudo_desc.csv', 'w+') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    for row in reader:
        for i, cell in enumerate(row):
            print(cell)
            for key in replace_dict:
                if key in cell:
                    row[i] = cell.replace(key, replace_dict[key])
        writer.writerow(row)
