import masa_mol_dict

def n(a):
    if a in masa_mol_dict.alkali:
        n.rr = masa_mol_dict.alkali[a]
    if a in masa_mol_dict.alkalinos:
        n.rr = masa_mol_dict.alkalinos[a]
    if a in masa_mol_dict.transicion:
        n.rr = masa_mol_dict.transicion[a]
    if a in masa_mol_dict.halogenos:
        n.rr = masa_mol_dict.halogenos[a]
    if a in masa_mol_dict.gases_nobles:
        n.rr = masa_mol_dict.gases_nobles[a]
    if a in masa_mol_dict.no_metales:
        n.rr = masa_mol_dict.no_metales[a]
    if a in masa_mol_dict.otros_metales:
        n.rr = masa_mol_dict.otros_metales[a]
    if a in masa_mol_dict.metaloides:
        n.rr = masa_mol_dict.metaloides[a]
    if a in masa_mol_dict.latanidos:
        n.rr = masa_mol_dict.latanidos[a]
    if a in masa_mol_dict.alkali:
        n.rr = masa_mol_dict.actinidos[a]

def n1(a, b):
    if a in masa_mol_dict.alkali:
        n.rr = masa_mol_dict.alkali[a]
    if b in masa_mol_dict.alkali:
        n1.rt = masa_mol_dict.alkali[b]
