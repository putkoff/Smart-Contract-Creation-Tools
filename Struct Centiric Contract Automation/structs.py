import functions as f
import json
def contName():
    ask = input('what is the contarct name?: ')
    cont = 'contract '+str(ask)+'{'
    prev = 'abstract prev'+str(ask)+' is Context{'
    return cont,prev
def createStructVars(x):
    structs = f.reader_B(x).replace(' {','{')
    structs = '{"'+structs.replace('\n','').replace('\t','').replace(' ','*').replace('**','').replace('{',',"{"').replace('}','"},"').replace(';','","').replace(',""','').replace(',"{','":{').replace('struct','').replace(',"*',',"').replace('"*','"')
    while structs[-1] != '}':
        structs = structs[:-1].replace('"*','"')
    structNames = []
    returnList = []
    structsSpl = structs.split(':')
    for i in range(0,len(structsSpl)-1):
        n = structsSpl[i].replace('{','')
        if '},' in n:
            n = n.replace('{','').split('},')[1].replace('*','') 
        structNames.append(n.replace('"',''))
    structJS = json.loads('{'+structs.replace('{','[').replace('}',']').replace("*':","':")[1:]+'}')
    return structNames,structJS
def structFormat():
    lists = []
    for i in range(0,len(structNames)):
        ls = input('is '+structNames[i]+' a structured list or stationary? (n,l,s')
        if ls != 'n' and ls != 'N':
            lists.append('y')
        else:
            lists.append('n')
    top = ''
    for i in range(0,len(structNames)):
        top =top + '\tstruct '+structNames[i]+'{\n\t\t'
        n = structJS[structNames[i]]
        for j in range(0,len(n)):
                       top = top + n[j].replace('*',' ')+';\n\t\t'
        top = top + '}\n'
    return lists,top
def mapping():
    maps = ''
    for i in range(0,len(structNames)):
        kk = ''
        if lists[i] == 'n':
            kk = '[]'
        maps = maps + '\tmapping(address => '+structNames[i]+kk+') public '+structNames[i].lower()+';\n'
    return maps
def structInputsSmall():
    littleStructs = ''
    smallStructs = ''
    for i in range(0,len(structNames)):
        n,nL,nLF,st = getStructInitials(i)
        topPuts,puts = getPuts(i)
        func = '\tfunction update'+nLF+'(address _account,'+topPuts
        for k in range(0,len(st)):
            stL = st[k].replace('*',' _')
            func = func + stL+','
        returnList.append(func+') external onlyGuard()')
        smallStructs = smallStructs + func+') external {\n'
        
        for j in range(0,len(st)):
            stL = st[j].split('*')[1]
            smallStructs = smallStructs +'\t\t'+nLF+'[_account]'+puts+'.'+stL+' = '+'_'+stL+';\n'
        smallStructs = smallStructs + '\t}\n'
    return smallStructs
def getStructName(i):
    return structNames[i]
def getStructVarList(x):
    return structJS[x]
def getLower(x):
    return x.lower()
def getUpper(x):
    return x[0].upper()+x[1:]
def getStructVar(x):
    return x.split('*')[1]
def getStructType(x):
    return x.split('*')[0]
def getPuts(i):
    topPuts = ''
    puts =  ''
    if lists[i] == 'n':
        topPuts = ',uint256 _x,'
        puts = '[_x]'
    return topPuts,puts
def getStructInitials(i):
    n = getStructName(i)
    a = getLower(n)
    b = getUpper(a)
    c = getStructVarList(n)
    return n,a,b,c
def structInputsLittle():
    littleStructs = ''
    smallStructs = ''
    for i in range(0,len(structNames)):
        n,nL,nLF,st = getStructInitials(i)
        topPuts,puts = getPuts(i)
        for j in range(0,len(st)):
            print(st[j])
            stL = getStructVar(st[j])
            stLF = getUpper(stL)
            funUp = '\tfunction update'+stLF+'(address _account'+topPuts+','+st[j].split('*')[0]+' _'+stL+') external '
            returnList.append(funUp)
            littleStructs = littleStructs+'\t'+funUp+' onlyGuard() {\n\t\t'+nL+'[_account]'+puts+'.'+stL+' = _'+stL+';\n\t}\n'
            intfunUp = '\tfunction INTupdate'+stLF+'(address _account'+topPuts+','+st[j].split('*')[0]+' _'+stL+') internal {\n\t\t'+nL+'[_account]'+puts+'.'+stL+' = _'+stL+';\n\t}\n'
            littleStructs = littleStructs + intfunUp
            intfunGet = '\tfunction INTget'+stLF+'(address _account'+topPuts+') internal pure returns('+st[j].split('*')[0]+'){'
            littleStructs = littleStructs+'\t'+intfunGet+'\n\t\treturn '+nL+'[_account]'+puts+'.'+stL+';\n\t}\n'
            funGet = '\tfunction get'+stLF+'(address _account'+topPuts+') external returns('+st[j].split('*')[0]+'){'
            returnList.append(funGet)
            littleStructs = littleStructs+'\t'+funGet+'\n\t\treturn '+nL+'[_account]'+puts+'.'+stL+';\n\t}\n'
    return littleStructs

def getLength(x):
    'function get'+getUpper(x)+'Length(address _account,uint256 _x) external returns(uint256){\n\t\t'+lsName+'[] storage _'+x+' = '+x+'[_account];\n\t\t return _'+x+'[_x].length;\n\t}\n'
def returnFuncs():
    returns = ''
    for i in range(0,len(structNames)):
        n,nL,nLF,st = getStructInitials(i)
        func = '\tfunction get'+nLF+'(address _account,uint256 _x) external returns('
        for k in range(0,len(st)):
            stL = getStructType(st[k])
            func = func + stL+','
        func = func+'){\n\t'
        n = structNames[i]
        nL = structNames[i].lower()
        gets = func
        if lists[i] == 'n':
            gets = gets +'\t'+n+'[] storage _'+nL+' = '+nL+'[_account];\n\t'+n+' storage _'+nL+'_ = _'+nL+'[_x];\n'
            keyvar = '_'+nL+'_'
        else:
            gets = gets + '\t\t'+n+' storage _'+nL+' = '+nL+'[_account];\n'
            keyvar = '_'+nL
        gets = gets + '\t\treturns ('
        func = gets
        for k in range(0,len(st)):
            stL = keyvar+'.'+st[k].split('*')[1]
            func = func + stL+','
        func = func + ');\n\t}\n'
        returns =returns+ func.replace(',)',')')
        if lists[i] == 'n':
            returns =returns+'\tfunction get'+nLF+'Length(address _account,uint256 _x) external returns(uint256){\n\t\t'+n+'[] storage _'+nL+' = '+nL+'[_account];\n\t\t return _'+nL+'[_x].length;\n\t}\n'
            n = structNames[i]
            nL = structNames[i].lower()
            st = structJS[n]
            func = '\tfunction add'+nLF+'(address _account,'
            for k in range(0,len(st)):
                stL = st[k].replace('*',' _')
                func = func + stL+','
            returns = returns + func+') external {\n\t\t'+n+'[] storage _'+nL+' = '+nL+'[_account];\n\t'
            returns =returns + '\t'+nL+'.push('+structNames[i]+'({\n\t\t'
            n = structJS[structNames[i]]
            for j in range(0,len(n)):
                ll = ''
                if j != len(n):
                    ll = ','
                returns = returns +'\t' +n[j].split('*')[1]+':_'+n[j].split('*')[1]+ll+'\n\t\t' 
            returns = returns + '\n\t\t}));\n\t}\n'
        print(returns)
    return returns,returnList
def createAbstract():
    abstract = prev+'\n'
    for i in range(0,len(returnList)):
        abstract = abstract+'\t'+returnList[i].replace('\t','').replace('{','').replace('external','external virtual').replace(',)',')').replace('\n','').replace(',,',',')+';'+'\n'
    abstract = abstract+'}\n'
    return abstract
def createContract():
    contract = abstract+cont+'\n'+top+'\n'+maps+constructor()+'\n'+smallStructs+'\n'+littleStructs+'\n'+retrunsStructs+'\n\t'+addTXNsafe()
    return contract.replace(',)',')').replace(',,',',')
def addTXNsafe():
        transferOut ='function transferOut(address payable _to,uint256 _amount) payable external onlyOwner(){\n\t\t_to.transfer(_amount);\n\t}\n\t'
        sendOut = 'function sendTokenOut(address _to,address _token, uint256 _amount) external onlyOwner(){\n\t\tIERC20 newtok = IERC20(_token);\n\t\tfeeTok.transferFrom(address(this), _to, _amount);\n\t}\n\t'
        transferAll = 'function transferAllOut(address payable _to,uint256 _amount) payable external onlyOwner(){\n\t\t_to.transfer(address(this).balance);\n\t}\n'
        sendAll = 'function sendAllTokenOut(address payable _to,address _token) external onlyOwner(){\n\t\tIERC20 newtok = IERC20(_token);\n\t\tfeeTok.transferFrom(address(this), _to, feeTok.balanceOf(address(this)));\n\t}\n'
        return transferOut+sendOut+transferAll+sendAll+'\n}'
def constructor():
    return '\n\tuint256 public Zero = 0;\nuint256 public One = 1;\naddress[] public Managers;\n\taddress[] public protoOwners;\n\taddress[] public transfered;\n\taddress payable treasury;\n\tuint256 public Zero = 0;\n\tuint256 public One = 1;\n\tuint256 public protoLife = protoLife;\n\taddress public _boostMGR;\n\taddress public _feeMGR;\n\taddress public _dropMGR;\n\taddress public _overseer; \n\tboostManager public boostMGR;\n\tfeeManager public feeMGR;\n\tdropManager public dropMGR;\n\toverseer public over;\n\tIERC20 feeTok;\n\tmodifier managerOnly() {require(nebuLib.addressInList(Managers,msg.sender)== true); _;}\n\tconstructor(address[] memory _addresses,address payable _treasury){\n\t\t_boostMGR = _addresses[0]\n\t\tboostMGR = boostManager(_boostMGR);\n\t\t_feeMGR = _addresses[1];\n\t\tfeeManager = feeMGR(_feeMGR);\n\t\t_dropMGR = _addresses[2]\n\t\tdropManager = dropMGR(_dropMGR);\n\t\t_overseer = _addresses[3]\n\t\tover = overseer(_overseer);\n\t\tfeeToken = _addresses[4];\n\t\tfeeTok = IERC20(feeToken);\n\t\ttreasury = payable(_treasury);\n\t\tManagers.push(owner());\n\t}'
global contract,prev,cont,abstract,returns,structNames,returnList,intReturnList,structJS,retrunsStructs,returns,maps,top
cont = ''
prev = ''
abstract = ''
contract = ''
returns = ''
returnList = []
structNames = []
returnList = []
intReturnList = []
structJS = []
cont,prev = contName()
structNames,structJS= createStructVars('structs.txt')
lists,top = structFormat()
maps = mapping()
smallStructs = structInputsSmall()
littleStructs = structInputsLittle()
retrunsStructs,returnList = returnFuncs()
abstract = createAbstract()
contract = createContract()

print(contract.replace('string','string memory'))
