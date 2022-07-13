# Running the Slurm 'expect' Testsuite

The ```slurm-testsuite``` package contains the Slurm expect test suite.
This package is meant to be installed on a test setup only, it should
NEVER BE INSTALLED ON A REGULAR OR EVEN PRODUCTION SYSTEM.
SUSE uses this package to determine regressions and for quality assurance.
The results are monitored and evaluated regularly in house.
A specific configuration is required to run this test suite, this document
attempts to describe the steps needed.
A small subset of tests is currently failing. The reasons are yet to be
determined.

Please do not file bug reports based on test results!

The testsuite is preconfigured to work with 4 nodes: ```node01```,...,
```node04```. ```node01``` serves as control and compute node. The slurm
configuration, home, and the test suite are shared across the nodes.
The test suite should be mounted under /home (to make ```sgather``` work
correctly).

For tests involving MPI this test suite currently uses OpenMPI version 4.

## Install and set up the Base System

1. Prepare image with a minimal minimal text mode installation.
2. Add NFS kernel server support:
   ```
    # zypper install nfs-kernel-server
	```
3. Install, enable and start sshd and make sure root is able to log in
   without password across all nodes.
    ```
	 # zypper install openssh-server openssh-clients
	 # systemctl enable --now sshd
	 # ssh-keygen -t rsa -f .ssh/id_rsa -N
	 # cat .ssh/id_rsa.pub >> .ssh/authorized_keys
	```
4. Create a test user 'auser' allow ssh from/to root:
   ```
     # useradd -m auser
	 # cp -r /root/.ssh /home/auser
   ```
5. Set up a persistent network if to obtain the network address and
   hostname thru DHCP:
   ```
    # echo 'SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", '\
	  'ATTR{address}=="?*", ATTR{dev_id}=="0x0", ATTR{type}=="1",'\
	  ' KERNEL=="?*", NAME="lan0"
    # cat > root/etc/sysconfig/network/ifcfg-lan0 <<EOF
	BOOTPROTO='dhcp'
	MTU=''
	REMOTE_IPADDR=''
	STARTMODE='onboot'
	EOF
	# sed -i 's/DHCLIENT_SET_HOSTNAME="no"/DHCLIENT_SET_HOSTNAME="yes"/' \
	  /etc/sysconfig/network/dhcp
   ```

## Install and set up the Slurm specific Environment

1. Install package slurm-testsuite.
2. Set up, enable mariadb, add slurm accounting database:
   ```
    # sed -i -e "/^bind-address/s@\(^.*$\)@# \1@" /etc/my.cnf
    # systemctl start maridb
	# mysql -uroot -e "create user 'slurm'@'node01' identified by 'linux';"
	# mysql -uroot -e "create database slurm_acct_db;"
	# mysql -uroot -e "grant all on slurm_acct_db.* TO 'slurm'@'node01';"
	```
3. Set up shared home, testsuite and slurm config directories, enable
   NFS server:
   ```
   # mkdir -p /srv/home
   # mv /home/auser /srv/home
   # mkdir /home/slurm-testsuite
   # chown slurm:slurm /home/slurm-testsuite
   # cat >> /etc/exports <<EOF
     /srv/home *(rw,no_subtree_check,sync,no_root_squash)
     /srv/slurm-testsuite *(rw,no_subtree_check,sync,no_root_squash)
     /srv/slurm-testsuite/shared *(rw,no_subtree_check,sync,no_root_squash)
     /srv/slurm-testsuite/config *(rw,no_subtree_check,sync,no_root_squash)
     EOF
   # cat >> /etc/fstab <<EOF
     node01:/srv/home /home nfs sync,hard,rw 0 0
     node01:/srv/slurm-testsuite/config /etc/slurm nfs sync,hard,rw 0 0
     node01:/srv/slurm-testsuite/shared /var/lib/slurm/shared nfs sync,hard,rw 0 0
     node01:/srv/slurm-testsuite /home/slurm-testsuite nfs sync,hard,rw 0 0
   # systemctl enable nfs-server

   ```
# Clone Nodes and bring up Test System

1. Now halt the system and duplicate it 3 times.

2. Set up the dhcp server and make sure the nodes receive the hostnames
   ``node01```,..., ```node04```.

3. Enable munge and slurmd:
    ```
	# systemctl enable munge
	# systemctl enable slurmd
	```

4. Boot all 4 nodes (start with ```node01```).
5. On ```node01```, log in as ```root``` and run ```setup-testsuite.sh```:
   ```
   # ./setup-testsuite.sh
   ```
6. Load the environment and run the tests as user 'slurm':
   ```
   # sudo -s -u slurm
   $ module load gnu openmpi
   $ cd /home/test/home/slurm-testsuite/testsuite/expect
   $ ./regression.py
   ```

There are a number of tests which require a different configuration
and thus will be skipped.
For a number of these, the alternatives are documented in the config
file shipped with this package.
A small number of tests fail for yet unknown reasons.
Also, when run sequentially, some tests may fail intermittendly as the
test suite is not race free. Often the reason for this is that tests
try to determine the availability of resources and may behave incorrectly
if an insufficient number is marked 'idle'. This problem may be less
pronounced when more resources (nodes) are available. Usually, these
issues will not show when tests are run manually. Therefore, it is important
the re-check failed tests manually.
