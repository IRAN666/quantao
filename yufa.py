cihui={'qt':100,'lj':200,
    'slt':-11,'xlt':-21,
    'st':-11,'xt':-21,
    'kj':-31,'yl':-32,
    'da':101,'zql':102,'qthf':103,
    'pen':201,'tlj':202,
    'blcz':300,'bl':300,
    'ca':301,'ba':302,'xing':303,
    'tk':400,'duang':401,
    'dbj':500,'kan':501}
ren={}
def plus(a,b):
    ren[a]=b
def yufa(a):
    b=a.split(" ")
    try:
        y=cihui[b[0]]
        try:
            name=ren[b[1]]
            return (y,name)
        except:
            return (y,0)
    except KeyError:
        return (0,0)
