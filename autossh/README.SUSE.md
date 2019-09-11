
This README is written in markdown format.  The retext editor in "preview" mode is one method of viewing it properly.
Anyone editing this document should verify it displays properly in retext preview mode before submitting changes.

# autossh

autossh is designed to let you setup both normal encrypted and reverse encrypted tunnels.

## autossh with systemd

To use autossh as a systemd service the following MUST be done at a minimum:

autossh is an "instantiated" service with systemd meaning you can instantiate
it multiple times in order to create multiple tunnels

The below is psuedo code that shows what YOU need to do.
The values for my_tunnel should be whatever you desire them to be

for (my_tunnel in ssh http imap pop) {
>  	sytemctl enable autossh@${my-tunnel}.service

>	mkdir /etc/systemd/system/autossh@${my-tunnel}.service.d
	cp /usr/share/doc/packages/autossh/my.conf /etc/systemd/system/autossh@${my-tunnel}.service.d
	edit /etc/systemd/system/autossh@${my-tunnel}.service.d/my.conf to reflect your needs

>	sytemctl start autossh@${my-tunnel}.service

}

The author of this README only uses autossh for reverse tunnels, so see
the below reverse tunnels description for detailed instructions of that usage.

## autossh to create reverse encrypted tunnels

This README supplements the above.

You should read and understand the instructions in the above before reading these.

These are detailed steps you must do to actually use autossh in openSUSE.

### Reverse tunnel overview

autossh is designed to let you setup both normal encrypted and reverse encrypted tunnels.

With a reverse encrypted tunnel you can, as an example, have a machine behind
a NAT firewall expose a ssh listening port by tunneling it through a well known
server to a public facing port on the internet.

This README is setup to expose port 22 (the ssh port) of a target openSUSE
PC to the world by opening a port 2222 tunnel port on a public facing
openSUSE server in the cloud.  It is assumed port 2222 will be where
ssh clients will connect to.  Those connections will be forwarded via
the ssh reverse tunnel to port 22 on the target PC hidden behind the firewall.

### Step one goal

From the target openSUSE PC ensure root can issue a ssh command to your public openSUSE server and not have a password be requested.

ssh -i /root/.ssh/id_rsa.autossh autossh@my.cloud.server

autossh can be any user account on both the target and public servers, but it is recommended it be one dedicated to providing tunnels and not allow interactive login.

my.cloud.server  => replace with the fqdn of your public server.

### Step one

on the public (cloud) PC:
>   sudo /usr/sbin/useradd -m autossh    (or other as you desire) <br>
   sudo passwd autossh   # set a tempory password

on the target PC:
>   sudo /usr/sbin/useradd -m autossh    (or other as you desire)  <br>
>   sudo passwd autossh   # set a tempory password   <br>
>   start a command line as autossh (or su - autossh) <br>
>   ssh-keygen  (take defaults for all questions) <br>
>   scp /home/autossh/.ssh/id_rsa.pub autossh@my.cloud.server:id_rsa.pub <br>
>   ssh autossh@my.cloud.server  <br>
>>	  (accept the cert and enter password) <br>
	   mkdir .ssh  <br>
	   cat id_rsa.pub >>  .ssh/authorized_keys <br>
	   rm id_rsa.pub  <br>
	   logout

>   ssh autossh@my.cloud.server <br>
>>	   (password should not be required)
>>	   logout

>   sudo cp /home/autossh/.ssh/id_rsa /root/.shh/id_rsa.autossh <br>
>   sudo ssh -i /root/.ssh/id_rsa.autossh autossh@my.cloud.server <br>
>>	   (password should not be required)
>>	   logout

### Step two

on the public (cloud) PC:
>   sudo /usr/sbin/usermod -s /sbin/nologin autossh

on the target PC:
>   test that ssh connects, but the connection is immediately closed  <br>
   sudo ssh -i /root/.ssh/id_rsa.autossh autossh@my.cloud.server

### Step three
Assuming you are using systemd:

on the target PC:
> sudo systemctl enable autossh@ssh.service <br>
> sudo mkdir /etc/systemd/system/autossh@ssh.service.d  <br>
> sudo cp /usr/share/doc/packages/autossh/my.conf /etc/systemd/system/autossh@ssh.service.d  <br>
> sudo vi /etc/systemd/system/autossh@ssh.service.d/my.conf

>> replace ExecStart line with:

>>ExecStart=/usr/bin/autossh -i /root/.ssh/id_rsa.autossh -M 0 -NR *:2222:localhost:22 -o TCPKeepAlive=yes autossh@my.cloud.server

>> and of course replace the server name.

>>fyi: this command says  <br>
 * - On the public facing server allow all IPs to connect  <br>
 2222 - On the public facing server listen on port 2222  <br>
 localhost - name of local PC the tunnel is exposing  <br>
 22 - port on local PC the tunnel is exposing

> sudo systemctl start autossh@ssh.service


### Step four

test

In order to eliminate firewall issues test first directly on the public facing server:

On public (cloud) server -
ssh -l <valid_user> -p 2222 localhost

That should open a ssh connection from the public server through the ssh reverse tunnel to the target PC.

Once that works, expand your testing to other client machines.  If you have issues be sure to check the firewall status of your public facing server.
