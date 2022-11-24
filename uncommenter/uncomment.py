import functions as f

def find_beg(x):
    if '/**' in x:
        z = x.split('/**')[0]
        return z
    return False
def find_end(x):
    if '*/' in x:
        z = x.split('*/')[1]
        return z
    return False
lines = f.read_lines('nft_stake.sol')
m = ''
going = 0
for i in range(0,len(lines)):
    n = lines[i]
    
    skip = False
    if str(n) == '\n' or'//' in n:
        skip = True
    if skip != True:
        if going == 0:
            beg = find_beg(n)
            if beg != False:
                m = m + beg
                going = 1
            else:
                m = m + n
        if going == 1:
            end = find_end(n)
            if end != False:
                m = m + end
                going = 0
f.pen(m,'nft_stake.sol')
