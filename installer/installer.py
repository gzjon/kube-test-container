import yaml, os, shutil
import wget
import tarfile


destination='/usr/local/bin/'
packagelist='packages.yaml'

# Extract foo from foo.tar
def decompress(file):
    os.rename(file, 'compressed')
    print('Extracting tarfile ' + package)
    tar = tarfile.open('compressed', "r")
    untar = tar.extract(package)
    tar.close()
    os.remove('compressed')


with open(packagelist, 'r') as file:
    try:
        packages = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

# Download package from URl, check if tar.gz and move  it
for package in packages:
    wget.download(packages[package]['url'], out=package)
    if tarfile.is_tarfile(package):
        decompress(package)

    os.chmod(package, 777)
    shutil.move('./' + package, destination + package)
    print('\nBinary available in ' + destination +  package)


