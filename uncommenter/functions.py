import json
from dotenv import load_dotenv
import os
from web3 import Web3
import pyperclip
import subprocess
import sys
import requests
from hexbytes import HexBytes
import os
def if_in_ls(x,y):
	for i in range(0,len(y)):
		if str(x) in y[i]:
			return i
	return False
def str_in_var(x,y):
	if is_ls(y) == False:
		y = [y]
	for i in range(0,len(y)):
		if y[i] in str(x):
			return True
	return False
def isFile(x):
	ext = ['.sol','txt','.json','.js']
	print(x,ext,str_in_var(x,ext))
	if str_in_var(x,ext) != False:
		return True
	return False
def make_all_dirs(x):
	x_n = ''
	ls = []
	x_og = []
	if  is_ls(x) == False:
		x = [x]
	for i in range(0,len(x)):
		if isFile(x[i]) == False:
			if i ==0:
				x_n = x[i]
			else:
				x_n = create_path(x_n,x[i])
			if is_dir(create_path(home,x_n)) == False:
				make_dir(create_path(home,x_n))
		else:
			x_n = create_path(x_n,x[i])
			if is_dir(create_path(home,x_n)) == False:
				if exists(x_n) == False:
					pen_C('',x_n)
	return x_n

def is_num(x):
	try:
		x = int(x) - int(x)
		return True
	except:
		return False
def is_dir(x):
	return os.path.isdir(x)
def is_file(x):
	return os.path.isfile(x)
def is_ls(x):
	if type(x) is list:
		return True
	return False
def fold_rename(x,y):
    os.rename(x,y)
def create_new_dirs(x,y):
    new_dirs = exists_make('',create_path(all_dirs['variables'],'new_dirs.py'))
    pen(new_dirs+"all_dirs = change_places(all_dirs,'"+str(x)+"',create_path(all_dirs["+y+"],'"+str(x)+"'))\n",create_path(all_dirs['variables'],'new_dirs.py'))
def get_name():
    return os.path.basename(__file__)
def change_path(x):
    os.path.abspath(x)
def get_curr_path():
    return os.getcwd()
def get_parent_dir():
    return str(get_curr_path()).replace('/'+str(get_curr_path()).split('/')[-1],'')
def change_parent_dir():
    return change_gears(get_parent_dir())
def change_gears(x):
    curr = get_curr_path()
    change_path(x)
    return curr
def home_it():
    curr = get_curr_path()
    slash = '\\'
    if slash not in str(curr):
        slash = '/'
    change_glob('slash',slash)
    change_glob('home',curr)
    return curr,slash
def check_str(x,y):
    c = ''
    if str(x) != str(y):
        c = y
    return c
def del_file(x):
    os.remove(x)
def clean_list(x,y):
    new_ls = []
    for i in range(0,len(x)):
        if x[i] not in y:
            new_ls.append(x[i])
    return new_ls
def clean_folder(x):
    ls = list_files(x)
    for i in range(0,len(ls)):
        if ls[i] != 'flattened':
            del_file(create_path(x,ls[i]))
def create_path(x,y):
    if x == '':
        return str(y) + str(check_str(str(y),slash))
    return str(x) + str(check_str(x[-1],slash))+str(y)
def check_dir(x):
    return os.path.isdir(x)
def do_all_dir(x):
    m = ''
    for i in range(0,len(x)):
        n = x[i]
        m = create_path(m,n)
        m = m.replace('//','/')
        if isFile(x[i]) == False:
        	do_the_dir(m)
    return m
def do_the_dir(x):
    if type(x) is not list:
        x = [x]
    old = x[0]
    for i in range(1,len(x)):
        old = create_path(old,x[i])
    x = old
    if check_dir(x) == False:
        make_dir(x)
    return x
def check_file(x):
    return os.path.isfile(x)
def do_the_file(x,y,z):
    if check_file(x) == False:
        pen(y,z)
        return y
    return reader(z)
def make_dir(x):
    if check_dir(x) == False:
        os.makedirs(x)
def delete_it(x):
    os.remove(x)
def find_it(x,y):
    i = 0
    for i in range(0,len(x)):
        if str(x[i]) == str(y):
            return i
    return False
def reader_C(file):
    with open(file, 'r',encoding='utf-8-sig') as f:
        text = f.read()

        return text
def reader_B(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()

        return text
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def pen_B(paper, place):
    
    with open(place, 'w',encoding='UTF-8') as f:
        f.write(str(paper))
        f.close()
        return
def pen_C(paper,place):
	with open(os.path.join(home, place), "w") as f:
        	f.write(str(paper))
        	f.close()
        	return
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
        return
def list_files(x):
    return os.listdir(x)
def get_c(i):
    c = ''
    if c != 0:
        c = ',\n'
    return c
def add_many_str(x,k,z):
    y = ''
    for i in range(0,k):
        y = y + x
    return y+z
def get_words(x,y):
    if type(y) is not list:
        y = [y]
    z = ''
    while x[0] not in list_var_in_str(x[0],y):
        z = z + str(x[0])
        x = x[1:]
    return z
def del_space_in(x,y):
    if type(y) is not list:
        y = [y]
    
    for i in range(0,len(y)):
        res = list_var_in_str(x,['[','{','('])
        if y[i] in res:
            x = x.replace(y[i] + ' ',y[i])
        res = list_var_in_str(x,[']','}',')'])
        if y[i] in res:
            x = x.replace(' '+y[i],y[i])
    return x
def del_space_front(x,y):
    if type(y) is not list:
        y = [y]
    for i in range(0,len(x)):
        
        if list_var_in_str(x[0],y) in y:
            x = x[1:]
        else:
            return x
def get_words_and_junk(x,y):
    if type(y) is not list:
        y = [y]
    z = ''
    
    for i in range(0,len(y)):
        if list_var_in_str(x,z) not in y:
            z = z + str(x[0])
            x = x[1:]
    return z,x
def get_blank_bracs(x):
    n = []
    m = list()
    for i in range(0,len(x)):
        m.append(n)
    
    return m
def js_it(x):
    return json.loads(str(x).replace('{,','{').replace(',}','}').replace('[,','[').replace(',]',']').replace("'",'"'))

def line_num(x,filename):
    m = []
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if x in line:
                m.append(num-1)
    return m
def js_wrap(x):
    return js_it('{'+str(x)+'}')
def js_qu(x):
    return '"'+str(x)+'"'
def make_js(x,y):
    return js_qu(x)+':'+js_qu(y)
def add_js(x,y):
    return js_it(str(x)[:-1]+get_c(len(x))+str(y)+'}')
def do_js(x,z):
    for i in range(0,len(x)):
        y = make_js(x[i],z)
        if i == 0:
            w = js_wrap(y)
        else:
            w = add_js(w,y)
    return js_it(str(w).replace("'[]'","[]"))
def get_c_tf(i):
    if i == 0:
        return True
    return False
def new_line_it(x):
    y = ''
    for i in range(0,len(x)):
        c = ''
        if get_c_tf(i) == False:
            c = '\n'
        y =y+c+ str(x[i])
    return y
def try_it(x,y):
    try:
        n = x[y]
        return True
    except:
        return False
def find_lowest(x):
    x.sort()
    if try_it(x,0) == True:
        return x[0]
    else:
        return False
def find_highest(x):
    x.sort()
    if try_it(x,-1) == True:
        return x[-1]
    else:
        return False
def range_list(x):
    return [find_lowest(x),find_highest(x)]
def exists_make(x,y):
    if exists(y) == False:
        pen(x,y)
        return x
    else:
        return reader_C(y)
def exists(x):
    try:
        x = reader(x)
        return True
    except:
        return False
def count_lines(x):
    if exists(x) == False:
        pen('',x)
    count = 1
    with open(r''+str(x)+'', 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return count
def fake_line(x,l,k):
    y = ''
    for i in range(l,k):
        y = y + '\n'
    return y
def read_lines(x):
    a = open(x, "r")
    rd = a.readlines()
    a.close()
    return rd
def write_lines(x,y):
    a = open(x, "w")
    a.writelines(y)
    a.close()
def add_lines(x,line):
    n = count_lines(x)
    fake = ''
    if line > n:
        fake = fake_line(x,n+1,line+1)
    pen(reader(x)+fake,x)
    add_lines(x,y+1)
    list_of_lines = read_lines(x)
    list_of_lines[y] = z
    write_lines(x,list_of_lines)
    
def split_lines(file):
    mylines = []                                # Declare an empty list.
    with open (file, 'rt') as myfile:    # Open lorem.txt for reading text.
        for myline in myfile:                   # For each line in the file,
            mylines.append(myline.rstrip('\n')) # strip newline and add to list.
    return mylines
def list_var_in_str(x,y):
    res = [ele for ele in y if(ele in x)]
    return res
def comb_ls(x,y):
    for i in range(0,len(y)):
        x.append(y[i])
    return x

def if_not_in(x,y):
    if x not in y:
        return True
    return False
def int_chk(x):
    try:
        n =int(x)
        return False
    except:
        return True
def list_check(x):
    if type(x) is str:
        return js_it(l),len_x
    if type(x) is list:
        return x,len(x)
    else:
         return x,
def ls_to_str(x):
    new = ''
    for i in range(0,len(x)):
        new = new + str(x[i])
    return new
def chop_lines(x,y):
    w = []
    for i in range(0,len(x)):
        a = x[i]
        if i+1 < len(x):
            z = x[i+1]
            n = ls_to_str(y[int(a):int(z)])
            w.append(n)
        else:
            n = ls_to_str(y[int(a):])
            w.append(n)
    return w

def list_it(x):
    x,k = list_check(x)
    n = ''
    
    for i in range(0,k):
        n = n + x[i]
    return n
def change_glob(x,v):
    globals()[x] = v
def add_it(x,y):
    return int(x) + int(y)
def add_str(x,y):
    return str(x)+str(y)
def str_kill(x,y):
    y = ''
    x,i = list_check(x)
    st = []
    for l in range(0,len(y)):
        if type(y[l]) is list:
            yy = [],[]
            for ll in range(0,len(y_a)):
                st.append(y[l][ll])
                yy[ll].append(y[l][ll])
                y = go
        else:
            st.append(y[l])
        if list_var_in_str(x,z):
            print('bo')
    z = list_var_in_str(x,y)  
    z = add_str(yy,x[i])
    i = add_it(i,1)
    return z,i
def str_go(x,y,z):
    for i in range(y):
        x.append(y[i])
    x,y = list_check(x)
    res = list_var_in_str(x,z)
    if res in y:
        return res,1
    elif res in x:
        return res,-1
    else:
        return False
def check_it(x,y):
    if type(y) is not list:
        y = [y]
    for i in range(0,len(y)):
        res=list_var_in_str(x,y)
        if len(res) != 0:
            return res
    return False

def create_ls_bracs(x,k):
    w = []
    y = '[]'
    for ii in range(0,k):
        z = []
        for i in range(0,x):
            z.append(y)
        w.append(js_it(z))
    return str(w).replace('"','').replace("'",'')
def var_str(x):
    if type(x) is not list:
        x = [x]
    for i in range(0,len(x)):
        #var = 710
        #variable_name = [k for k, v in locals().items() if v == 710][0] 
        #print("Your variable name is " + variable_name)
        
        exec("%s = %s" % (x[i],'z'))
        z = x[i]
        exec("%s = %s" % (z,x[i]))
def create_blanks(x):
    y = ''
    for i in range(0,x):
        y = y + ' '
    return y
def timer(x):
    return int(x) + 1
def remove_end(x):
    return str(x).replace(str(y)+str(slash).split(str(y))[-1],'')
def get_end(x):
    return str(x).split(str(slash))[-1]
def copy_it(x,y):
    pen(reader(x),y)
def get_prag(lines,pr):
    ls_pr = '{}'
    for i in range(0,len(pr)):
        n = lines[pr[i]]
        n = n.split('pragma solidity ')[1]
        print(n)
        n = n.split(';')[0]
        print(n)
        if str(pr[i]) not in ls_pr:
            print(str(str(ls_pr)[:-1] + ','+str(make_js(pr[i],n)+'}').replace('{,','{')))
            ls_pr = js_it(str(str(ls_pr)[:-1] + ','+str(make_js(pr[i],n)+'}')).replace('{,','{'))
        return ls_pr
def get_lins_is(file):
    lines = read_lines(file)
    var = ['pragma solidity','}','contract','library','function','constructor','abstract','interface']
    z = 'is'
    ls_a,ls_b = do_js(var,[]),json.loads('{"is":[]}')
    line = read_lines(file)
    for i in range(0,len(var)):
        n = var[i]
        ls_a[n] = line_num(n,file)
        for k in range(0,len(ls_a[n])):
            x = lines[ls_a[n][k]]
            while str(x)[:len(n)] in list_var_in_str(str(x)[:len(n)],['\t',' ','\n']):
                x = x[1:]
            if x[:len(n)] == n:
                m = ls_a[n]
                if z in str(x):
                    print(x)
                    ne = x.split(z)[1].replace(', ',',').replace(' ,',',').split(',')
                    for k_1 in range(0,len(ne)):
                        while ne[k_1][0] == ' ':
                            ne[k_1] = ne[k_1][1:]
                        while ne[k_1][-1] == ' ':
                            ne[k_1] = ne[k_1][:-1]
                        ne[k_1] = ne[k_1].split(' ')[0]
                        if str(ne[k_1]) not in ls_b['is']:
                            ls_b = str(str(ls_b)[:-1] + ','+str(make_js(ne[k_1],ls_a[n][k]))+'}').replace('{,','{')
                            ls_b = js_it(ls_b)
                            ls_b['is'].append(ne[k_1])
                        if int(ls_b[ne[k_1]]) < int(ls_a[n][k]):
                            ls_b[ne[k_1]] = int(ls_a[n][k])
    return ls_b,ls_a,lines
def find_it_alph(x,k):
    i = 0
    while str(x[i]) != str(k):
        i = i + 1
    return i
def get_c(x):
        c = ','
        if int(x) == int(0):
                c = ''
        return c
def wrap_up(x,y,z):
        w = str(z)[:-1]+get_c(len(z))+'"'+str(x)+'":"'+str(y)+'"'+str(z)[-1]
        return js_it(w)
def create_wrap_ls(x,y):
        z = json.loads('{}')
        for i in range(0,len(x)):
                z = wrap_up(x[i],y[i],z)
        return z
def check_sum(x):
    return Web3.toChecksumAddress(str(x))
def get_alph():
    alph = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz,aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj,kkk,lll,mmm,nnn,ooo,ppp,qqq,rrr,sss,ttt,uuu,vvv,www,xxx,yyy,zzz'
    sp = alph.split(',')
    return sp
def create_ask(x,y):
        alph = get_alph()
        n = 'which '+str(y)+' would you like to use?\n'
        for i in range(0,len(x)):
                n = n + str(alph[i]) + ') '+str(x[i])+'\n'
        ask = input(n)
        i = find_it_alph(alph,str(ask))
        return x[i]
def rem_file(x):
        os.remove(x) 
def rem_var():
        if exists('variables/vars.txt') == True:
                rem_file('variables/vars.txt')
def mains():
        global scanners,net,ch_id,main,file,w3,last_api,c_k,hashs_js,expo,dec,network,scan_num
        hashs_js = ""
        last_api = [0,0]
        main = {
        	"avax_test":{"net":"https://api.avax-test.network/ext/bc/C/rpc","chain":"43113","main_tok":"AVAX","scanners":"api-testnet.snowtrace.io"},
        	"polygon":{"net":"https://polygon-rpc.com/","chain":"137","main_tok":"MATIC","scanners":"api.polygonscan.com"},
        	"ethereum":{"net":"https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161","chain":"1","main_tok":"ETH","scanners":"api.etherscan.io"},
        	"cronos_test":{"net":"https://cronos-testnet-3.crypto.org:8545/","chain":"338","main_tok":"TCRO","scanners":"api.cronoscan.com"},
        	"optimism":{"net":"https://kovan.optimism.io","chain":"69","main_tok":"OPT","scanners":"api-kovan.etherscan.io"},
        	"binance":{"net":"https://bsc-dataseed.binance.org/","chain":"56","main_tok":"bsc","scanners":"api.bscscan.com"}
                }
        scan = ["avax_test","polygon","ethereum","cronos_test","optimism","binance"]
        var_names = ['scanners','net','ch_id','main_tok','file','w3','network']
        file = 'variables/vars.txt'
        if exists('variables/vars.txt') == False:
                network = create_ask(scan,'network')
                all = main[network]
                scanners,net,ch_id,main_tok,w3 = all["scanners"],all["net"],all["chain"],all["main_tok"],Web3(Web3.HTTPProvider(all["net"]))
                vars = [scanners,net,ch_id,main_tok,file,w3,network]
                pen(create_wrap_ls(var_names,vars),'variables/vars.txt')
        fi = js_it(reader('variables/vars.txt'))
        return fi['scanners'],fi['net'],fi['ch_id'],fi['main_tok'],fi['file'],Web3(Web3.HTTPProvider(fi["net"])),fi['network']

global home,slash
home, slash = home_it()

