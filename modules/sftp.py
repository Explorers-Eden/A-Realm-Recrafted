import os
import paramiko

SFTP_PORT = int(os.getenv("SFTP_PORT", "22"))

def fetch_files_via_sftp(remote_files, input_dir):
    host = os.getenv("SFTP_HOST")
    user = os.getenv("SFTP_USER")
    password = os.getenv("SFTP_PASS")

    if not host or not user or not password:
        print("Missing SFTP credentials")
        return

    transport = paramiko.Transport((host, SFTP_PORT))

    try:
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        for remote, local in remote_files:
            try:
                sftp.get(remote, local)
                print(f"Downloaded: {remote}")
            except Exception as e:
                print(f"Failed: {remote} -> {e}")

        sftp.close()
    finally:
        transport.close()