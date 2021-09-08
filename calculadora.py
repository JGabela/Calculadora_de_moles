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

#def space_count(ele):
    #count = 0
    #for sp in ele:
        #if sp == " ":
            #count += 1
    #space_count.spc = count
#if tea == 2:
#    van = trrr.split('#')
#    vam = float(trt[1])
#    print(va, "u")
#
#if tea == 4:
#    van = va.split('#')
#    vbn = vb.split('#')
#    vam = van[1]
#    vbm = vbn[1]
#    tear = (va * vam) + (vb * vcm)
#    print(tear, "u")
#
#if tea == 6:
#    va = va.split('#')
#    vb = vb.split('#')
#    vc = vc.split('#')
#    vam = va[1]
#    vbm = vb[1]
#    vcm = vc[1]
#    tear = (va * vam) + (vb * vbm) + (vc * vcm)
#    print(tear, "u")
#
#if tea == 8:
#    va = va.split('#')
#    vb = vb.split('#')
#    vc = vc.split('#')
#    vd = vd.split('#')
#    ve = ve.split('#')
#    vam = va[1]
#    vbm = vb[1]
#    vcm = vc[1]
#    vdm = vd[1]
#    tear = (va * vam) + (vb * vbm) + (vc * vcm) + (vd * vdm)
#    print(tear, "u")
#
#if tea == 10:
#    va = va.split('#')
#    vb = vb.split('#')
#    vc = vc.split('#')
#    vd = vd.split('#')
#    ve = ve.split('#')
#    vam = va[1]
#    vbm = vb[1]
#    vcm = vc[1]
#    vdm = vd[1]
#    vem = ve[1]
#    tear = (va * vam) + (vb * vbm) + (vc * vcm) + (vd * vdm) + (ve * vem)
#    print(tear, "u")
#