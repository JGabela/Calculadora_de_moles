
import masa_mol_dict

def n(a):
    if a in masa_mol_dict.alkali:
        n.tr = masa_mol_dict.alkali[a]
    elif a in masa_mol_dict.alkalinos:
        n.tr = masa_mol_dict.alkalinos[a]
    elif a in masa_mol_dict.transicion:
        n.tr = masa_mol_dict.transicion[a]
    elif a in masa_mol_dict.halogenos:
        n.tr = masa_mol_dict.halogenos[a]
    elif a in masa_mol_dict.gases_nobles:
        n.tr = masa_mol_dict.gases_nobles[a]
    elif a in masa_mol_dict.no_metales:
        n.tr = masa_mol_dict.no_metales[a]
    elif a in masa_mol_dict.otros_metales:
        n.tr = masa_mol_dict.otros_metales[a]
    elif a in masa_mol_dict.metaloides:
        n.tr = masa_mol_dict.metaloides[a]
    elif a in masa_mol_dict.latanidos:
        n.tr = masa_mol_dict.latanidos[a]
    elif a in masa_mol_dict.alkali:
        n.tr = masa_mol_dict.actinidos[a]
    else:
        n.tr = ""
