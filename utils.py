import numpy as np
import os
import zipfile
import shutil, os


def mv_files(source, dest):
	#  functions used to mv files to other folder. 
	for f in source:
		files = os.listdir(f)
		for item in files:
			shutil.move(f+"/"+item, dest+f+"/"+item)

def zipdir(path, ziph):
    # ziph is zipfile handle
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file), file)

def unzip_files(a):
	rand = np.random.randint(0,900,100)
	for i in rand:
		zipf = zipfile.ZipFile('./middleImagenet/' + a[i] +'.zip', 'w', zipfile.ZIP_DEFLATED)
		zipdir('./imagenet_object_localization/ILSVRC/train/'+a[i], zipf)
		zipf.close()
		print ("zip " + str(i) + " folder")

def mv_files():
	"""
    mv files to zip. 
    """
	filename = glob.glob('*.zip')
	for file in filename:
		os.mkdir(file[0:-4])
		zip_ref = zipfile.ZipFile(file, 'r')
		zip_ref.extractall(file[0:-4])
		zip_ref.close()
		os.remove(file)