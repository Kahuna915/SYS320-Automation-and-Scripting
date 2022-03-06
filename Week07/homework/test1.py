import paramiko
from getpass import getpass

# Host Information
host = "192.168.6.71"
port = 2222
username = "noah.stiles"


# Create the password prompt
ssh_passwd = getpass(prompt="Please Enter your SSH Password: \n\n")
password = ssh_passwd


def kraken_scan():
    # attempt to get our ssh connection, exit on bad password
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
    except paramiko.AuthenticationException:
        print("Authentication Failed")
        exit(0)

    # Send our python script to the server:
    sftp = ssh.open_sftp()

    # The name of the script to upload
    file = "kraken"

    # upload the script
    sftp.put(file, "/home/noah.stiles/kraken")

    # close our sftp session
    sftp.close()
    # make the file executeable:
    command_exec = "sudo chmod +x ./kraken"
    stdin, stdout, stderr = ssh.exec_command(command_exec)

    # Run our hunt:
    command_hunt = "sudo ./kraken --folder /usr/bin --folder --folder /usr/sbin/ --folder /usr/local/bin --folder " \
      "/sbin --folder /usr/local/sbin --folder /bin > /home/noah.stiles/k_output.txt "

    # run our command that runs the script
    print("Running Kraken...\n")
    stdin, stdout, stderr = ssh.exec_command(command_hunt)
    stdin.write(ssh_passwd + "/n")

    # Wait until the command is done before exiting
    exit_status = stdout.channel.recv_exit_status()
    if exit_status == 0:
        print("Done Running Kraken... \n")
    else:
        print("Error", exit_status)


    # open a new sftp session
    sftp = ssh.open_sftp()

    # get our results from the system

    sftp.get("/home/noah.stiles/k_output.txt", "k_output.txt")

    # close the second sftp session
    sftp.close()

    # cose the ssh connection.
    ssh.close()


kraken_scan()