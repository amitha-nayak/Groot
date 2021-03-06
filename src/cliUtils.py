import os
import shutil

def clear(*vargs):
    os.system("clear")


def nano(filename):
    os.system(f"nano {filename}")


def cat(filename):
    os.system(f"cat {filename}")
    print()


def ls(path="."):
    print("\n".join(os.listdir(path)))


def mkdir(dirname):
    cur_path = os.getcwd()
    path = os.path.join(cur_path, dirname)
    try:
        os.mkdir(path)
    except:
        print("Error while creating directory.")


def rmdir(dirname):
    cur_path = os.getcwd()
    path = os.path.join(cur_path, dirname)
    try:
        shutil.rmtree(path)
    except:
        print("Error while deleting directory.")


def cd(path):
    try:
        os.chdir(path)
    except OSError:
        print("Error while changing path.")


def help(*vargs):
    content = '''TOGEPI

Togepi is a command line based version control system built using Python3 and Google Drive API

1. User Commands

tgp create user -- Create an account
tgp user login username password -- Login to existing account

2. Repository Commands

tgp init repository_name -- Create a new repository

3. CLI tools

You can invoke other CLI commands such as -- 

cd
ls
cat
nano
rmdir
mkdir'''
    print(content)


def togepi(*vargs):
    content = '''     
     .^. .  _    
    /: ||`\/ \~  ,       
  , [   &    / \ y'   
 {v':   `\   / `&~-,  
'y. '    |`   .  ' /   
 \   '  .       , y   
 v .        '     v   
 V  .~.      .~.  V   
 : (  0)    (  0) :   
  i `'`      `'` j     
   i     __    ,j     
    `%`~....~'&         
 <~o' /  \/` \-s,        
  o.~'.  )(  r  .o ,.  
 o',  %``\/``& : 'bF  
d', ,ri.~~-~.ri , +h  
`oso' d`~..~`b 'sos`  
     d`+ II +`b              
     i_:_yi_;_y  '''
     
    print(content)