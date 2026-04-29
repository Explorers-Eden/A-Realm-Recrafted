import os
import paramiko

SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_PORT = int(os.getenv("SFTP_PORT", "22"))
SFTP_USER = os.getenv("SFTP_USER")
SFTP_PASS = os.getenv("SFTP_PASS")

REMOTE_FILES = {
    "game_rules.dat": "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/minecraft/game_rules.dat",
    "command_storage.dat": "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/world/data/eden/command_storage.dat",
    "getoffmylawn.json": "/srv/docker/crafty-4/servers/bb1e3d6f-d50b-48d7-84df-8b959126b4c9/config/getoffmylawn.json",
}


def fetch_files_via_sftp(input_dir):
    if not SFTP_HOST or not SFTP_USER or not SFTP_PASS:
        print("Missing SFTP credentials")
        return

    transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))

    try:
        transport.connect(username=SFTP_USER, password=SFTP_PASS)
        sftp = paramiko.SFTPClient.from_transport(transport)

        for local_name, remote in REMOTE_FILES.items():
            local = os.path.join(input_dir, local_name)
            try:
                sftp.get(remote, local)
                print(f"Downloaded: {remote}")
            except Exception as e:
                print(f"Failed: {remote} -> {e}")

        sftp.close()
    finally:
        transport.close()