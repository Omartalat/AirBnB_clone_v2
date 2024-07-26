#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py)
 that distributes an archive to your web servers, using the function do_deploy
"""
from datetime import datetime
from fabric.api import local, put, run, env
from os.path import isdir, exists
env.hosts = ['100.26.142.122', '54.157.158.117']


def do_pack():
    """Compresses the web_static folder into a .tgz archive"""
    try:
        day = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_N = "versions/web_static_{}.tgz".format(day)
        local("tar -czvf {} web_static".format(file_N))
        return file_N
    except FileNotFoundError:
        return None


def do_deploy(archive_path):
    """distributes an archive to web server"""
    if not exists(archive_path):
        return False
    else:
        try:
            put(archive_path, '/tmp/')
            path_end = archive_path.split('/')[-1].split('.')[0]
            full_path = '/data/web_static/releases/{}'.format(path_end)
            run('mkdir -p {}'.format(full_path))
            run('tar -xzvf /tmp/{}.tgz -C {}'.format(path_end, full_path))
            run('rm /tmp/{}.tgz'.format(path_end))
            run('mv {}/web_static/* {}/'.format(full_path, full_path))
            run('rm -rf {}/web_static'.format(full_path))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(full_path))
            return True
        except Exception as e:
            return False


def deploy():
    """ creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    val = do_deploy(archive_path)
    return val
