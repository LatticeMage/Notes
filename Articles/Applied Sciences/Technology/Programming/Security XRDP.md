# Security XRDP and force SSH tunnel

To enhance the security of your SSH and XRDP setup while ensuring the ability to remotely access your Linux Mint XFCE version system through an SSH tunnel, it's crucial to implement several configuration changes. These adjustments will not only secure SSH access by changing its default port and limiting authentication methods but will also configure XRDP to allow connections only from localhost (127.0.0.1), which necessitates an SSH tunnel for remote desktop access. The following guide outlines the steps required to achieve this configuration.

### Secure SSH Access

#### Changing the Default SSH Port

To reduce the risk of automated attacks, change the SSH service's default port from 22 to a non-standard port, such as 5566.

1. Open the SSH configuration file for editing:
    ```
    sudo nano /etc/ssh/sshd_config
    ```

2. Locate the line `#Port 22`. Uncomment it (remove the `#`) and change the port number to `5566`:
    ```
    Port 5566
    ```

#### Limit Authentication to Public Key and Specific Users

For increased security, disable password authentication and enable public key authentication. Additionally, restrict SSH access to specific user accounts.

1. Within the SSH configuration file (`/etc/ssh/sshd_config`), ensure the following settings are present and correct:
    ```
    PasswordAuthentication no
    PubkeyAuthentication yes
    ChallengeResponseAuthentication no
    ```

2. Append the following line to specify allowed users (replace `<your-user-name>` with your actual username):
    ```
    AllowUsers <your-user-name>
    ```

### Configuring XRDP for Secure Remote Access

#### Restricting UFW Access to localhost

To ensure XRDP connections can only originate from localhost, adjust the UFW rules accordingly.

1. Allow UFW access from localhost to port 3389:
    ```
    sudo ufw allow from 127.0.0.1 to any port 3389
    ```

2. Verify the UFW rule:
    ```
    sudo ufw status
    ```

    The output should include:
    ```
    3389                       ALLOW       127.0.0.1
    ```

#### Configure XRDP to Listen on localhost Only

Limit XRDP to accept connections from localhost by modifying its configuration.

1. Open the XRDP configuration file:
    ```
    sudo nano /etc/xrdp/xrdp.ini
    ```

2. Before the `port=3389` line, add `address=127.0.0.1`.

#### Setting Up XRDP with XFCE for Better Performance

To ensure a smoother remote desktop experience, install and configure XFCE for use with XRDP.

1. Install XFCE4:
    ```
    sudo apt-get install xfce4
    ```

2. Link XFCE4 with XRDP:
    ```
    echo xfce4-session > ~/.xsession
    ```

3. Backup the XRDP start script and edit it to start XFCE4:
    ```
    sudo cp /etc/xrdp/startwm.sh /etc/xrdp/startwm.sh.backup
    sudo nano /etc/xrdp/startwm.sh
    ```
   
    Find the lines that start the window manager and ensure XFCE4 is configured to start.

### Remote Desktop Access Via SSH Tunnel

#### Setting Up .ssh/config for Multiple Keys

Managing multiple keys and connections is simpler with a configured `.ssh/config` file.

1. Edit or create your `.ssh/config` file to include the new host configuration:
    ```
    Host <Any-Naming>
        HostName <ip of server>
        User <your-user-name>
        IdentityFile ~/.ssh/<key pair>
        Port 5566
    ```

#### Establishing the SSH Tunnel for Remote Desktop Access

To connect to your remote desktop securely through the SSH tunnel, forward the appropriate port.

1. Establish the SSH tunnel:
    ```
    ssh -L 3390:localhost:3389 <your-user-name>@<Any-Naming>
    ```

2. Connect via a remote desktop client to `localhost:3390`.

This setup ensures that remote desktop access is secured through SSH, with XRDP configured to only accept connections via the tunnel. By following these guidelines, you can enhance the security of your remote desktop setup while ensuring a smooth and secure access method.