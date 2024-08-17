# feel free to skid but don't forget the original creator ;)

import os
import time
import random

import base64,py_compile,marshal,lzma,zlib

import ast, re, io, tokenize, sys, platform, math


def lemon(text):
    os.system(""); faded = ""
    red = 0; green = 50; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 15; green += 15; blue += 0
            if red > 255 and green > 255 and blue != 255:
                red = 255; green = 255; blue = 0
    return faded

def lemons(text):
    os.system(""); faded = ""
    red = 190; green = 200; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 15; green += 15; blue += 0
            if red > 255 and green > 255 and blue != 255:
                red = 255; green = 255; blue = 0
    return faded

def reds(text):
    os.system(""); faded = ""
    red = 200; green = 0; blue = 5
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 15; green += 0; blue += 5
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 0; blue = 20
    return faded

banner = f'''            _   _
          .-_; ;_-.
         / /     \ \\
        | |       | |
         \ \.---./ /
     .-"~   .---.   ~"-.
   ,`.-~/ .'`---`'. \~-.`,
   '`   | | \(_)/ | |   `'
   ,    \  \ | | /  /    ,
   ;`'.,_\  `-'-'  /_,.'`;
    '-._  _.-'^'-._  _.-'       
        ``         ``
______________________________________________________
                                                      |
[*] Plague Obfuscator                                 |
[*] By : Edu2rdo                                      |
______________________________________________________|

'''

plague = 'PLAGUE__PLAGUE__PLAGUE'
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
junk = plague * random.randint(5,15)

def vars():
    rndint = random.randint(10,50)
    random_vars = ''.join(random.choice(chars) for i in range(rndint))
    return random_vars

print(lemon(banner))

def zip(code):
    deziem = lzma.compress(code.encode())
    return deziem

#Encrypt 3:



#RENAM VAR
def remove_docs(source):
    io_obj = io.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    out = '\n'.join(l for l in out.splitlines() if l.strip())
    return out

def do_rename(pairs, code):
    for key in pairs:
        code = re.sub(fr"\b({key})\b", pairs[key], code, re.MULTILINE)
    return code

def rename(filename):
    code = filename
    code = remove_docs(code)
    parsed = ast.parse(code)

    funcs = {
        node for node in ast.walk(parsed) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    classes = {
        node for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)
    }
    args = {
        node.id for node in ast.walk(parsed) if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)
    }
    attrs = {
        node.attr for node in ast.walk(parsed) if isinstance(node, ast.Attribute) and not isinstance(node.ctx, ast.Load)
    }
    for func in funcs:
        if func.args.args:
            for arg in func.args.args:
                args.add(arg.arg)
        if func.args.kwonlyargs:
            for arg in func.args.kwonlyargs:
                args.add(arg.arg)
        if func.args.vararg:
            args.add(func.args.vararg.arg)
        if func.args.kwarg:
            args.add(func.args.kwarg.arg)

    pairs = {}
    used = set()
    for func in funcs:
        if func.name == "__init__":
            continue
        newname = "O0".join("O0" for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "O0".join("O0" for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[func.name] = newname

    for _class in classes:
        newname = "O0".join("O0" for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "O0".join("O0" for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[_class.name] = newname

    for arg in args:
        newname = "O0".join("O0" for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "O0".join("O" for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[arg] = newname

    for attr in attrs:
        newname = "O0".join("O" for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "O0".join("O0" for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[attr] = newname

    string_regex = r"('|\")[\x1f-\x7e]{1,}?('|\")"

    original_strings = re.finditer(string_regex, code, re.MULTILINE)
    originals = []

    for matchNum, match in enumerate(original_strings, start=1):
        originals.append(match.group().replace("\\", "\\\\"))

    placeholder = os.urandom(16).hex()
    code = re.sub(string_regex, f"'{placeholder}'", code, 0, re.MULTILINE)

    for i in range(len(originals)):
        for key in pairs:
            originals[i] = re.sub(r"({.*)(" + key + r")(.*})", "\\1" + pairs[key] + "\\3", originals[i], re.MULTILINE)

    while True:
        found = False
        code = do_rename(pairs, code)
        for key in pairs:
            if re.findall(fr"\b({key})\b", code):
                found = True
        if found == False:
            break


    replace_placeholder = r"('|\")" + placeholder + r"('|\")"
    for original in originals:
        code = re.sub(replace_placeholder, original, code, 1, re.MULTILINE)

    return code

def encrypt4(file):
    count = 50
    for i in range(count):
        out = file.replace('.py', '') + '-plague.py'
        oa = open(file).read()
        ni = compile(oa, 'PLAGUE__PLAGUE__PLAGUE', 'exec')
        bo = marshal.dumps(ni)
        ab = repr(bo)
        s = open(out, 'w')
        s.write('# Compiled bY Plague.#9115\nimport marshal, zlib\nexec(marshal.loads('+str(ab)+'))')
        s.close()
        while True:
            for i in range(12):
                nz = open(out).read()
                dn = compile(nz, 'PLAGUE__PLAGUE__PLAGUE', 'exec')
                bx = marshal.dumps(dn)
                nl = repr(bx)
                ns = open(out, 'w')
                ns.write('# Compiled bY Plague.#9155\nimport marshal\nexec(marshal.loads('+str(nl)+'))')
                ns.close()
                continue
            break
        mx = open(out).read()
        nl = base64.b32encode(mx.encode('utf-8'))
        xn = open(out, 'w')
        xn.write("# Compiled bY Plague.#9115\nimport base64,marshal,zlib,lzma\nexec(base64.b32decode(%s))" % nl)
        xn.close()
def encrypt3(file):
    count = input('[>] insert Encryption Layers [1-200] :').replace('[', lemons('[')).replace(']', lemons(']'))
    for i in range(int(count)):
        out = file.replace('.py', '') + '_encoded.py'
        oa = open(file).read()
        ni = compile(oa, 'PLAGUE__PLAGUE__PLAGUE', 'exec')
        bo = marshal.dumps(ni)
        ab = repr(bo)
        s = open(out, 'w')
        s.write('# Compiled bY Plague.#9115\nimport marshal, zlib\nexec(marshal.loads('+str(ab)+'))')
        s.close()
        while True:
            for i in range(12):
                nz = open(out).read()
                dn = compile(nz, 'PLAGUE__PLAGUE__PLAGUE', 'exec')
                bx = marshal.dumps(dn)
                nl = repr(bx)
                ns = open(out, 'w')
                ns.write('# Compiled bY Plague.#9155\nimport marshal\nexec(marshal.loads('+str(nl)+'))')
                ns.close()
                continue
            break
        mx = open(out).read()
        nl = base64.b32encode(mx.encode('utf-8'))
        xn = open(out, 'w')
        xn.write("# Compiled bY Plague.#9115\nimport base64,marshal,zlib,lzma\nexec(base64.b32decode(%s))" % nl)
        xn.close()
        
def encrypt2(file):
    ok = zip(file)
    oke = f'exec(lzma.decompress({ok}))'
    okk = zip(oke)
    okke = f'exec(lzma.decompress({okk}))'
    return okke

def encrypt1(file):
    global junk
    code=file
    encrypted = ""
    encrypted2 = ""
    for c in range(len(code)//95):
        junky = f'{vars()*random.randint(1,10)}="{vars()*random.randint(1,20)}";'
        zero = 'lol="invalid code lol xD"'
        cc = compile(zero, "PLAGUE_PLAGUE_PLAGUE", "exec")
        cc = marshal.dumps(cc)
        cc = repr(cc)
        cc = f'exec(marshal.loads({cc}))'
        cc = base64.b64encode(cc.encode())
        junks = f'{junk}=exec(base64.b64decode({cc}));'
        cc1 = zip(junks)
        cc2 = f'exec(lzma.decompress({cc1}));'
        maxjunk = f'{junky}{cc2}'
        encrypted += maxjunk
    abc = compile(code, "PLAGUE__PLAGUE__PLAGUE", "exec")
    abcd = marshal.dumps(abc)
    abcde = repr(abcd)
    run = f'exec(marshal.loads({abcde}));'
    runq = base64.b64encode(run.encode())
    runa = f'{junk}=exec(base64.b64decode({runq}));'
    cc3 = zip(runa)
    cc4 = f'exec(lzma.decompress({cc3}));'
    rrna = f'{vars()*random.randint(1,10)}="{vars()*random.randint(1,20)}";{cc4}'
    encrypted2 += encrypted
    encrypted2 += rrna
    encrypted2 += encrypted
    #Return to final result:
    return encrypted2

file = input('['+lemons('>')+'] '+lemons('drag or drop file [.py] here : '))
if not os.path.isfile(file):
    print('['+reds('!')+'] '+reds('File not found'))
    time.sleep(1.5)
    exit()

code = open(file,'r').read()
first = rename(code)
second = encrypt1(first)
third = encrypt2(second)
with open(file.replace('.py', '')+'-backup.py', 'w') as backup:
    backup.write(code)
with open(file, 'w') as end:
    end.write(f'# -- Plague Obfucator -- :\n\nimport base64,marshal,lzma\n{third}')
filee = file
fourth = encrypt3(filee)
fileee = file.replace('.py', '')+'_encoded.py'
five = encrypt4(fileee)

if '\\' in file:
    os.remove(f'{file.replace(".py", "")}.py')
    os.remove(f'{file.replace(".py", "")}_encoded.py')
else:
    os.remove(f'.\\{file.replace(".py", "")}.py')
    os.remove(f'.\\{file.replace(".py", "")}_encoded.py')
