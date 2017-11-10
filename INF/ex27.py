import copy
def InsererDans(el,liste_triee):
    i=0;imax=len(liste_triee)
    ls = copy.copy(liste_triee)
    while i<imax:
        if(ls[i]>el):
            ls.insert(i,el)
        i+=1
    if imax == 0:
        ls.insert(0,el)
    return ls
def FusionListesT(ls1, ls2):
    i=0;imax=len(ls1)
    jmax=len(ls2)
    lsc1 = copy.copy(ls1)
    lsc2 = copy.copy(ls2)
    while i<imax:
        ls2 = InsererDans(ls1[i],ls2)
        i+=1
    return lsc2
def SupprimDoublons(list1):
    i=0;imax=len(list1)
    ls1 = copy.copy(list1)
    while i<imax:
        j=1;jmax=len(ls1)
        while j<jmax:
            if(ls1[j]==ls1[i]):
                ls1.pop(j)
        j+=1
    i+=1
    imax=len(list)
    return list1
print(InsererDans(1,[2,4,3,5]))
print(FusionListesT([],[]))
print(FusionListesT([1,3,4],[2,2,7,9]))
print(SupprimDoublons([1,2,3]))
print(SupprimDoublons([1,1,1,1,1]))
