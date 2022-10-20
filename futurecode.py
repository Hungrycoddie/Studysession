
import sys
import os
import re
import subprocess

def main():
    if len(sys.argv) != 2:
        print "Usage: %s <file>" % sys.argv[0]
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.isfile(file):
        print "File %s does not exist" % file
        sys.exit(1)

    # Get the file type
    file_type = subprocess.check_output(["file", file])
    file_type = file_type.split(":")[1].strip()

    # Get the file encoding
    file_encoding = subprocess.check_output(["file", "-i", file])
    file_encoding = file_encoding.split(":")[1].strip()

    # Get the file size
    file_size = os.path.getsize(file)

    # Get the file permissions
    file_permissions = oct(os.stat(file).st_mode)[-3:]

    # Get the file owner
    file_owner = os.stat(file).st_uid
    file_owner = subprocess.check_output(["getent", "passwd", str(file_owner)])
    file_owner = file_owner.split(":")[0]

    # Get the file group
    file_group = os.stat(file).st_gid
    file_group = subprocess.check_output(["getent", "group", str(file_group)])
    file_group = file_group.split(":")[0]

    # Get the file creation time
    file_creation_time = os.stat(file).st_ctime

    # Get the file modification time
    file_modification_time = os.stat(file).st_mtime

    # Get the file access time
    file_access_time = os.stat(file).st_atime

    # Get the file inode
    file_inode = os.stat(file).st_ino

    # Get the file hard links
    file_hard_links = os.stat(file).st_nlink

    # Get the file device
    file_device = os.stat(file).st_dev

    # Get the file device type
    file_device_type = os.stat(file).st_rdev

    # Get the file blocks
    file_blocks = os.stat(file).st_blocks

    # Get the file block size
    file_block_size = os.stat(file).st_blksize

    # Get the file flags
    file_flags = os.stat(file).st_flags

    # Get the file gen
    file_gen = os.stat(file).st_gen

    # Get the file birth time
    file_birth_time = os.stat(file).st_birthtime

    # Get the file checksum
    file_checksum = subprocess.check_output(["md5sum", file])
    file_checksum = file_checksum.split(" ")[0]

    # Get the file entropy
    file_entropy = subprocess.check_output(["ent", file])
    file_entropy = file_entropy.split(" ")[1]

    