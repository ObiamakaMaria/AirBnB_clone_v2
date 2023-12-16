#!/usr/bin/python3
"""
This Fabric script deploys an archive to web servers
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.197.207.15', '54.236.56.251']
env.user = 'ubuntu'
env.key_filename = '/etc/letsencrypt/live/www.obiamaka.tech/privkey.pem'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/<filename without extension>/
        archive_filename = archive_path.split("/")[-1]
        folder_name = archive_filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_filename, folder_name))

        # Remove the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move contents to the correct location
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(folder_name, folder_name))

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
