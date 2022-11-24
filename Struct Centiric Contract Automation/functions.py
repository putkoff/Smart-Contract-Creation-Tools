import json
from dotenv import load_dotenv
import os
from web3 import Web3
import pyperclip
import subprocess
import sys
def change_gears(x): #(dir) changes directory and spits back the previous one
    y = os.getcwd()
    os.chdir(x)
    return y
def create_path(x,y):
    home = os.getcwd()
    n = '/'
    if '\\' in home:
        n = '\\'
    ###print(x[-2:])
    while x[-2:] == n:
        x = x[:-2]
    z = x + n + y
    return z
def choose_wall():
	dyn_walls()
	q = input('which wallet would you like to use?')
	if nos(q) == False:
		return int(-1)
	return int(q) - int(1)

def send_all(x,n,k):
    
    a,p = get_walls(choose_wall())
    for i in range(n,k):
        if str(x) != str(a[i]):
            var = [a[i],x,p[i]]
            strs = ['account_1','account_2','private_key1']
            for i in range(0,len(strs)):
                change_glob(strs[i],var[i])
            sv_env(p)
            #print(p)
            change_glob('maxxi',1)
            send()
def back_pro(x):
    p = subprocess.Popen([sys.executable, str(x)],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return
def blanks():
    js = exists_js('adds.txt')
    a,n = js['adds'],js['names']
    js['names'] = []
    for i in range(0,len(a)):
        js['names'].append(str(''))
    pen(js,'adds.txt')
def create_em():
    from eth_account import Account
    import secrets
    from hexbytes import HexBytes
    import json
    js = exists_js('adds.txt')
    priv = secrets.token_hex(32)
    private_key = priv
    acct = Account.from_key(private_key)
    ls = private_key,acct.address
    js['adds'].append(ls[1])
    js['priv'].append(ls[0])
    js['names'].append('')
    pen(js,'adds.txt')
    back_pro(js)
def clip_it(x):
    text = str(x)
    os.system("echo '{}' | xclip -selection clipboard".format(text))
def change_glob(x,v):
    globals()[x] = v
def globulars():
    global wall_file,w3,main,mains,ch_id,net,account_1,private_key1,account_2,a,p,maxxi
    wall_file = ''
    w3 = ''
    maxxi = 0
    main = ''
    mains = ''
    net = ''
    ch_id = ''
    account_1 = ''
    account_2 = ''
    private_key1 = ''
    a = ''
    p = ''
def expos():
    return float(1e-18)
def wall_check():
    if exists('adds.txt') == False:
        pen('{"adds":[],"priv":[],"names":[]}','adds.txt')
    return js_read('adds.txt')  
def is_ls(ls):
    if type(ls) is list:
        return True
    return False
def exists_js(file):
    if exists(file) == False:
        x = js_it('{}')
        if is_ls(file) is True:
            x = (file[1])
        pen(x,file)
        return x
    else:
        x = js_it(str(reader_B(file)))
    return x
def exists(file):
    try:
        x = reader_B(file)
        return True
    except IOError:
        return False
def timer(i):
    return int(i) + int(1)
def hx(x):
    a = json.loads(exists('adds.txt').replace("'",'"'))
    k = 'adds','priv'
    
    for i in range(0,2):
        x = "".join(["{:02X}".format(b) for b in HexBytes("0x"+str(x))])
        a[k[i]].append(str(x))
    
def pen(x,p):
    with open(p, 'w',encoding='UTF-8') as f:
        
        return f.write(str(x))
def reader_B(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()
        return text
def get_walls():
    js = exists_js('adds.txt')
    a = js['adds']
    p = js['priv']
    return a,p
def js_it(x):

    return json.loads(str(x).replace("'",'"'))
def js_read(x):
    return js_it(reader_B(x))
def sv_env(x):
    if is_num(x) == True:
        ls = exists_js('adds.txt')
        x = ls['priv'][x]
    pen('MNEMONIC=\nPRIVATE_KEY='+str(x),'.env')
def get_env(x):
    load_dotenv()
    load_dotenv('.env')
    p = os.environ.get("privateKey")
def find_it(ls,k):
    for i in range(0,len(ls)):
        if str(k) == ls[i]:
            return int(int(i) - int(1))
        i = timer(i)
    return None
def set_net(x):
    return Web3(Web3.HTTPProvider(x))
def get_bal(x):
    return w3.eth.getBalance(x)
def send():
    maxx = get_bal(account_1)
    gas = float(100000)
    maxx = float(float(maxx)-float(float(maxx)*float(0.05)))*float(1e-18)
    if maxxi == 0:
        amt = input_it('how much would you like to send?\n you can send a max of '+str(maxx))
    else:
        amt = maxx
        #print('sending a max: '+str(maxx)+' to '+str(account_2))
    nonce = w3.eth.getTransactionCount(account_1)
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': w3.toWei(float(amt), 'ether'),
        'gas':100000,
        'gasPrice': 15000000000000,
        'chainId': 338
    }
    #build a transaction in a dictionary
    bal = w3.eth.getBalance(account_1)
    #print(bal)
    #sign the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key1)
    #send transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    #get transaction hash
    #print(w3.toHex(tx_hash))
    change_glob('maxxi',0)
def zeros():
    a,p = get_walls()
    n = 0
    for i in range(n,len(a)):
        w = a[i]
        if float(get_bal(w))*expos() == float(0.0):
            clip_it(w)
            import webbrowser
            webbrowser.open("https://cronos.org/faucet")
            q = input_it("enter")
        n = timer(n)
        ##print(i+1,' - ',a[i],' has a balance of ',str(round(float(get_bal(a[i]))*expos(),4)),main)
def is_num(x):
    try:
        i = float(x)
        i = int(x)
        return True
    except:
        return False
def re_wa():
    return 
def disp_dyn():
    exists_js(str(wall_file))
def dyn_walls():
    a,p = get_walls()
    #print(re_wa())
    if re_wa() == None:
        new = '"0 - create new wallet"'
        for i in range(0,len(a)):
            new = new +',\n"'+ str(str(i+1)+' - '+str(a[i])+' has a balance of '+str(round(float(get_bal(a[i]))*expos(),4))+' '+str(main))+'"'
            #print(new)
            nn = i
        pen(new.replace('"','').replace(',',''),str(wall_file))
        pen(nn,'num_'+str(wall_file))
    
def name_it(x):
    txt = exists_js('adds.txt')
    i = x
    a = txt['adds']
    n = txt['names']
    if is_num(x) == False:
        i = find_it(a,x)
    
    new = input_it("name_wall")
    if str(new) != '' and str(new) != ' ' and str(new) != 'n':
        if len(a) > len(n):
             txt['names'][i].append(str(new))
        else:
             txt['names'][i] = str(new)
        pen(txt,'adds.txt')
        return new
    return n
def nos(x):
    x.append(['N']).append('NO')
    if str(x) not in str(x[1:]):
        if  x[0] not in str(x[1:]):
            return True
    return False
def input_it(x):
    y = js_it({"which":"which account would you like to use?","zeros":"wanna start with the zero wallets first?(enter/n)","test":"getting test coins?(enter/n)","new_wall":"did you want to grab some new wallets?(how many?/n)","enter":"press enter when ready","name_wall":"what would you like to name the wallet?(name/(enter,n)"})
    if str(x) in y:
        x = y[x]
    return input(str(x)+':\n')
    
def pic_walls():
    dyn_walls()
    #print(disp_dyn())
    a_num = input_it("which")
    
    if a_num == int(0):
        from create import ls
        account_1 = ls[1]
        private_key1 = ls[0]
        sv_env(-1)
    else:
        a,p = get_walls()
        a_num = int(a_num)-int(1)
        account_1 = a[a_num]
        private_key1 = p[a_num]
        sv_env(a_num)
        a,p = get_walls()
    #print(account_1,'chosen')
    return account_1,private_key1
def ch_main(x):
    y = js_read('adds.txt')
    y['main'] = x
    pen(y,'adds.txt')
def change_main():
    q = input_it('did you want to keep '+str(get_main())+' as your main acct?(enter/n)')
    if str(q) == '':
        return get_main()
    else:
        dyn_walls()
        #print(re_wa())
        a_num = int(input_it("which")) - int(1)
        y = js_read('adds.txt')
        y['main'] = a[a_num]
        pen(y,'adds.txt')
        return get_main()
def get_main():
    return js_read('adds.txt')['main']
def get_new_gas():
    q_3 = 'n'
    #name_it("name_wall")
    q = input_it("new_wall")
    q_2 = input_it("test")
    if q_2 != 'n':
        q_3 = input_it('zeros')
        if q_3 != 'n':
            zeros()
    if str(q) != 'n':
        if is_num(q) == False:
            q = 1
        for i in range(0,int(q)):
            create_em()
            a = js_read('adds.txt')['adds'][-1]
            clip_it(a)
            if str(q_2) != 'n':
                import webbrowser
                webbrowser.open("https://cronos.org/faucet")
                input_it("enter")
            i = timer(i)

