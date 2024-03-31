import grp
import pwd
import os
import sys
import hashlib
import tempfile
from contextlib import contextmanager
from pathlib import Path, PurePath
from shutil import copyfile, move, rmtree

def file_hash(file):
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    with open(file, "rb") as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    return file_hash.hexdigest()

def is_writable(path):
    try:
        testfile = tempfile.TemporaryFile(dir = path)
        testfile.close()
    except OSError as e:
        if e.errno == errno.EACCES:  # 13
            return False
        e.filename = path
        raise
    return True

def dir_exists(path):
    return os.path.isdir(path)

def dir_create(path):
    if not os.path.exists(path):
        os.makedirs(path)

def dir_delete(path):
    try:
        rmtree(path)
    except FileNotFoundError:
        pass

def file_delete(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass

def file_copy(src, dst):
    copyfile(src, dst)

def file_rename(src, dst):
    os.rename(src, dst)

def file_move(src, dst):
    move(src, dst)
    
def _get_pathfrom(fullpath, dirfrom):
    dirfrom = dirfrom + "/"
    return str(fullpath.replace(dirfrom,""))

@contextmanager
def contextmanager_cwd(path):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)

class FileObject:
    def __init__(self, path , dirfrom):
        self.fullpath = str(Path(path).absolute())       
        self.dirfrom = str(Path(dirfrom).absolute())
        self.pathfrom = _get_pathfrom(self.fullpath, self.dirfrom)
        self.parent = str(PurePath(self.fullpath).parent)
        self.suffix = str(PurePath(self.fullpath).suffix)
        self.name = str(PurePath(self.fullpath).name)
        self.stem  = str(PurePath(self.fullpath).stem)
        self.size  = str(os.path.getsize(self.fullpath))
        self.md5  = str(hashlib.md5(open(self.fullpath,'rb').read()).hexdigest())
        self.statinfo  = str(os.stat(self.fullpath))
        self.permissionmask  = str(oct(os.stat(self.fullpath).st_mode)[-3:])
        self.owner  = str(Path(self.fullpath).owner())
        self.group  = str(Path(self.fullpath).group())

class FilesystemSingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FilesystemSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass
 
    def getdirs(self, path):
        complete_files = []
        for root, dir_names, file_names in os.walk(path):
            for f in file_names:
                complete_files.append(os.path.join(root, f))
        complete_files = sorted(complete_files)
        return complete_files

fs = FilesystemSingleton()
