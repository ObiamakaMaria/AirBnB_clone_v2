#!/usr/bin/python3
# This function generates a .tgz arhcive from the files in web_static
from fabric.api import local, env
from datetime import datetime
import os

env.hosts = ['localhost']  # You can add remote servers if needed

def do_pack():
    """
    Compresses the web_static folder into a .tgz archive.
    """
    # Get the current working directory
    current_dir = local("pwd", capture=True)

    # Create the 'versions' folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the timestamp for the archive name
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    # Name of the archive
    archive_name = f"web_static_{timestamp}.tgz"

    # Path to the archive
    archive_path = os.path.join(current_dir, "versions", archive_name)

    # Path to the web_static folder
    web_static_path = os.path.join(current_dir, "web_static")

    # Compress the web_static folder into the archive
    result = local(f"tar -cvzf {archive_path} -C {current_dir} web_static")

    if result.succeeded:
        print(f"New version packed: {archive_path}")
        return archive_path
    else:
        print("Packing failed.")
        return None
