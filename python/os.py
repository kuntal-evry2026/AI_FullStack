import os
import sys
import shutil
shutil.rmtree('new_test_Dir')


print(os.getcwd())
print(os.listdir())
os.mkdir('test_dir')
os.rename('test_dir','new_test_Dir')
os.remove('t.txt')
os.remove('new_test_Dir')

print(sys.platform)
print(sys.version)
print(sys.argv)