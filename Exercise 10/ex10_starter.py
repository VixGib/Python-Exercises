import sys, glob, os

# Get the directory name, hdir is home directory, sys.platform is the system being used
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# # Construct a portable wildcard pattern (pattern is the home directory)
pattern = os.path.join(hdir,'*')
#
# # TODO: Use the glob.glob() function to obtain the list of filenames we want a file list from pattern(which is the directory) using glob.glb
file_list = glob.glob(pattern)
print(file_list)
# # TODO: use os.path.getsize to find each file's size,
#  file in file list is each element with in the file list, so we are asking for each element in the file list
#  to print with ts size via the os.path.getsize of file
for file in file_list:
     print(os.path.getsize(file))

#

# TODO: Add a test to only display files that are not zero length
#so for each element (file) within the file_list, if the os.path.getsize of each element (file)=
#is less than or equal to (!=) 0 the print the (file)via the os.path.getsize
#
for file in file_list:
    if (os.path.getsize(file)) != 0:
        print(file)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename() for every element (file) within file_list,
# if the (file) is less than or equal to zero using the os.path.basename path
#print "Basename" + os.path.basename of every (file)
# print(os.environ)

for file in file_list:

    if (os.path.basename(file)) != 0:
        print("Basename: " + os.path.basename(file))







