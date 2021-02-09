%DOLLY(1) Version 0.59 | Dolly file transfer

DOLLY
=====
A program to clone disks / partitions

SYNOPSIS
========

|dolly | \[**-f** config\]


24 March 2005


DESCRIPTION
===========

Dolly is used to clone the installation of one machine to (possibly
many) other machines. It can distribute image-files (even gnu-zipped),
partitions or whole hard disk drives to other partitions or hard disk
drives. As it forms a "virtual TCP ring" to distribute data, it works
best with fast switched networks (we were able to clone a 2 GB Windows
NT partition to 15 machines in our cluster over Gigabit Ethernet in
less than 4 minutes).

As dolly clones whole partitions block-wise it works for most
filesystems. We used it to clone partitions of the following type:
Linux, Windows NT, Oberon, Solaris (most of our machines have multi
boot setups). We have a small (additional) Linux installation on all
of our machines or use a small one-floppy-disk-linux (e.g. muLinux) to
do the cloning. On newer machines we use PXE to boot a small system in
a RAM disk. From that system we then clone the hard disks in the
machines.

Configuration file
------------------

You need a configuration file for the cloning process. Its format is
strict, but easy. It contains the following entries (note that the
order of the entries is fix):
(The text after "Syntax:" explains the syntax of the entry, the lines
following "EG:" are example lines)

1. The file/partition you want to clone, preceeded by the keywords
   "infile" or "compressed infile" in case of a compressed image.
   This file or partitions needs to be available on the master only.
   Dolly will warn you if you try to use a compressed infile which
   does not end with ".gz". The compressed keyword is important so
   that the master can inform the clients when they have to use gunzip
   before writing a file. The optional keyword "split" after the
   filename instructs Dolly to read all files with the given name and
   an appended number, separated by an underscore.
   Syntax: [compressed] infile <input file or device> [split]
   EG: infile /dev/sda10
       Will just send the partition /dev/sda10 to all clients.
   EG: compressed infile /images/cloneimages/sda10_WinNTRes.gz
       Will send the given file compressed to all the clients,
       instructing them to uncompress the image before writing it.
   EG: infile /images/cloneimages/sda split
       Will send all files of the form /images/cloneimages/sda_<number>
       in order to the clients.
   EG: compressed infile /images/cloneimages/sda.gz split
       Will send all files of the form /images/cloneimages/sda.gz_<number>
       in order to the clients, instructing them to decompress the
       incoming stream before writing it.

2. The file or partition you want to write (usually its a partition,
   but you can also write to a file) after the keyword "outfile". This
   file needs to be available on the clients only. The optional
   keyword "compressed" instructs the server to compress the data
   before sending it, so the client will store the data
   compressed. The optional keyword "split" after the filename,
   followed by a number and a multiplier, instructs the client to
   write the data in junks of no more than the given size. This is
   useful if the file system on your client does not allow files
   greater than a certain size. The files will be stored with the
   given namen and an appended "_<number>".
   Syntax: [compressed] outfile <output file or device> [split <n>(k|M|G|T)]
   EG: outfile /dev/sda10
       Will store the incoming data stream to the partition sda10.
   EG: compressed outfile /images/cloneimages/sda10_SuSE81.gz
       Will store the compressed data stream in the given file.
   EG: compressed outfile /images/cloneimages/sda_all.gz split 2G
       Will store the incoming compressed data stream in the directory
      /images/cloneimages/ in files sda_all.gz_0, sda_all.gz_1 and so on.

-. Instead of the first two entries ("infile" and "outfile") it is
   also possible to use the single line "dummy [<MB>]", where <MB> is
   the number of Megabytes to transfer in dummy mode. If <MB> is set
   to 0, then the clients will just terminate. This is useful when
   benchmarking with different options, so the clients can run all the
   time. To finally terminate them on all clients, just set dummy to 0.
   NOTE: It is probably better to use the newer "-t" switch on the
   server to specify the number of seconds the benchmarks should
   run. In that case you can leave the <MB> blank.
   Syntax: dummy [<MB>]
   EG: dummy 128

-. The optional keyword "segsize" is mostly used to benchmark
   switches. It specifies the maximal size of TCP segments during the
   network transfer. Usually you don't need to specify this option at
   all.
   Syntax: segsize <TCP_MAXSEG size>
   EG: segsize 128
   
-. With the optional keyword "add" it is possible to add more
   interfaces to use. The network traffic is then evenly distributed
   across the interfaces. This option is useful if you have for
   example two fast ethernet interfaces in your machines: One for
   administrative purposes and one for your main application on the
   cluster. This option is not so useful if you have multiple
   interfaces with different bandwidths. In this case just use the
   fastest available.
   You have to specify the number of additional interfaces and the
   suffixes of thouse interfaces. For example, in a cluster where the
   machines are named slave0..slave15 on their default interfaces and
   all the machines have a second interface named
   slave0-fast..slave15-fast, you should use the line specified below
   (EG).
   Syntax: add <nr>:<suffix>{:<suffix>}
   EG: add 1:-fast

-. The optional keyword "fanout" was mostly used during performance
   tests of different network topologies. You barely need it in
   practice. Fanout specifies the number of outlinks from the server
   and the following machines (except the leafes). A fanout of 1 is a
   linear list (the default behaviour of Dolly and usually the
   fastest), 2 is a binary tree, 3 is a ternary tree, etc. Dolly
   automatically connects all the specified clients with the desired
   topology.
   Syntax: fanout <fanout>
   EG: fannout 1

-. The optional keyword "hypennormal" instructs Dolly to treat the '-'
   character in hostnames as any other character. By default the
   hyphen is used to separate the base hostnames from the names of the
   different interface (e.g. "node12-giga"). You might use this
   paramater if your hostnames include a hypen (like e.g. "node-12").
   Syntax: hyphennormal
   EG: hyphennormal
   
3. After the keyword "server" follows the hostname of the server (or
   master). This is required for the last machine in the ring to be
   able to send the end-acknowledge back to the server.
   Syntax: server <master machine>
   EG: server cluster-master

4. This entry has the keyword "firstclient" followed by the hostname
   of the first client in the ring. You should use the hostname of the
   machine here, not the name of the interface where you want to
   connect.
   Syntax: firstclient <name of first machine>
   EG: firstclient cluster-1

5. This entry has the keyword "lastclient" followed by the hostname of
   the last client in the ring. You should use the hostname of the
   machine here, not the name of the interface where you want to
   connect.
   Syntax: lastclient <name of last machine>
   EG: lastclient cluster-9

6. This entry specifies how many clients are in the ring. The keyword
   is "clients" followed by the actual number of clients. This number
   does not include the master.
   Syntax: clients <number of clients>
   EG: clients 9

7. The following lines contain the interface-names of the client
   machines. The number of machines must match the above number of
   clients (see 6.). You should use the name of the interface on
   which the machines will receive the data.   
   Syntax: <name of client 1>
           <name of client 2>
           [...]
           <name of client n>
   EG: cluster-1-giga
       cluster-2-giga
       [...]
       cluster-9-giga

8. The last entry in the config file consists of the keyword
   "endconfig" and marks the end of the configuration file.
   Syntax: endconfig
   EG: endconfig


Note on nodes' hostnames
------------------------

On some machines (e.g. with very small maintenance installations),
gethostbyname() does not return the hostname (I don't know why). If
you have that problem, you should make sure that the environment
variables MYNODENAME or HOST are set accordingly. Dolly first tries to
get the environment variable MYNODENAME, then HOST, then it tries
gethostbyname(). This feature was introduced in dolly version 0.58.


OPTIONS
=============

Dolly has a few options which are explained here:

  -h
 :   Prints a short help and exits.

  -V
 :   Prints the version number as well as the date of that version and exits.

  -v
 :  This switches to verbose mode in which dolly prints out a little
    bit more information. This option is recommended if you want to
    know what's going on during cloning and it might be helpful during
    debugging.

  -s
 :  This option specifies the server machine and should only be used
    on the master. Dolly will warn you if the config file specifies
    another master than the machine on which this option is set.
    This option must be secified before the "-f" option!

  -S
 :  Same as "-s", but dolly will not warn you if the server's hostname
    and the name specified in the config file do not match.

  -q
 :  Usually dolly will print a warning when the select() system call
    is interrupted by a signal. This option suppresses these warnings.

  -c
 :  With this option it is possible to specify the uncompressed size
    of a compressed file. It's only needed for performance statistics
    at the end of a cloning process and not important if you are not
    interested in the statistics.

  -d
 :  The "Dummy" option disables all disk accesses. It can be used to
    benchmark the throughput of your system (computers, network,
    switches). This option must be specified before the "-f" option!

  -t <seconds>
 :  When in dummy mode, this option allows to specify how long the
    testrun should approximately take. Since the dummy mode is mostly
    used for benchmarking purposes and single runs might result in
    different speeds (especially with many machines and bad switches
    or with small TCP segment sizes), it's more convenient to specify
    the run-lenght in seconds, as the benchmark-time becomes more
    predictable.
    
  -f <config file>
 :  This option is used to select the config file for this cloning
    process. This option makes only sense on the master machine and
    the configuration file must exist on the master.

  -o <logfile>
 :  This option specifies the logfile. Dolly will write some
    statistical information into the logfile. it is mostly
    used when benchmarking switches. The format of the lines in the
    logfile is as follows:
    Trans. data  Segsize Clients Time      Dataflow  Agg. dataflow
    [MB]         [Byte]  [#]     [s]       [MB/s]    [MB/s]

  -a <timeout>
 :  Sometimes it might be useful if Dolly would terminate instead of
    waiting indefinitely in case something goes wrong. This option
    lets you specify this timeout. If dolly could not transfer any
    data after <timeout> seconds, then it will simply print an error
    message and terminate. This feature might be especially useful for
    scripted and automatic installations (such as "CloneSys"), where
    you don't want to have dolly-processes hang around if a machine
    hangs.

  -n
 :  Do not sync() before exit. Thus, dolly will exit sooner, but data
    may not make it to disk if power fails soon after dolly exits.

  -u <size>
 :  Specify the size of buffers for TCP sockets. Should be a Multiple
    of 4K.

  -b <size>
 :  option to specify the TRANSFER_BLOCK_SIZE. Should be a multiple of
    the size of buffers for TCP sockets.



How it works
============

Setting up or upgrading a cluster of PCs typically leads to the
problem that many machines need the exact same files. There are
different approaches to distribute the setup of one "master" machine
to all the other machines in the cluster. Our approach is not
sophisticated, but simple and fast (at least for fast switched
networks). We send the data around in a "virtual TCP ring" from the
server to all the clients which store tha received data on their local
disks.

One machine is the master and distributes the data to the others. The
master can be a machine of the cluster or some other machine (in the
current version of dolly it should be the same architecture
though). It stores the image of the partition or disk to be cloned or
has the partition on a local disk. The server should be on a fast
switched network (as all the other machines too) for fast cloning.

All other machines are clients. They receive the data from the ring,
store it to the local disk and send it to the next machine in the
ring. It is important to note that all of this happens at the same
time.

The cloning process is depicted in the following two figures. Usually
there are more than two clients, but you get the idea:

      +========+  +==========+ +==========+
      | Master |  | Client 1 | | Client 2 |
      +====+===+  +===|======+ +====+=====+
            \         |            /
             \    +===+====+      /
              +===+ Switch |=====+
                  +========+

        Cloning process, physical network


     +========+  Data   +==========+  Data  +==========+
     | Master |========>| Client 1 |=======>| Client 2 |
     +========+         +==========+        +==========+
         ^                   |                   |
         | Data              | Data              | Data
         |                   V                   V
      +======+            +======+            +======+
      | Disk |            | Disk |            | Disk |
      +======+            +======+            +======+

     Cloning process, virtual network with TCP connections


We choose this method instead of a multicast scheme because it is
simple to implement, doesn't require the need to write a reliable
multicast protocol and works quite well with existing
technologies. One could also use the master as an NFS server and copy
the data to each client, but this puts quite a high load on the server
and makes it the bottleneck. Furthermore, it would not be possible to
directly clone partitions from one machine to some others without any
filesystem in the partition.


Different cloning possibilities
-------------------------------

There are different possibilities to clone your master machine:

- You already have an image of the partition which you want to clone
  on your master (raw or compressed). In this case you need Linux
  (some other UNIX might also work, but we haven't tested that yet) on
  your master and a Linux on each client.

- You want to clone a partition which is on a local disk of your
  master. In this case you need Linux (or probably another UNIX, we
  haven't tried that) on your master as well as on all the clients.
  You can use any Linux installation as long as it's not the one you
  want to clone (i.e. you can not clone the Linux which you are
  currently running in. See the warning below).

- You want to clone a whole disk including all the partitions. In this
  case you either need a second disk on all machines where your Linux
  used for the cloning process runs on (not the one you want to clone)
  or you need a small one-floppy-disk-Linux which you boot on all
  machines. In the later case you also need dolly on all machines
  (copy it to your floppy disk or mount it with NFS) and the
  config-file on the master.

WARNING: You can NOT clone an OS which is currently in use. That is why
         we have a small second Linux installation on all of our machines
         (or a small system that can be booted over the network by PXE),
         which we can boot to clone our regular Linux partition.


CHANGES 
=======
version 0.2
------------------

We applied some changes to Dolly since version 0.2. Most of them are
not very important.

- Dolly as a benchmarking tool.
  Dolly can now be used to benchmark your network. In the dummy mode,
  Dolly will not access the hard disk, neither for reading nor for
  writing. It just transfers data between your machines. This might be
  useful for testing the throughput of your switch. The running time
  for such a run can be specified with the "-t" option on the command
  line. With the "-o" option you can specify a logfile where Dolly
  will write some statistical information.

- Using extra network interfaces.
  It's now possible to use multiple network interfaces for the data
  transfer. This is mostly useful if you have multiple network
  interfaces with similar speeds, e.g. two fast ethernet networks (one
  for administration/logins and the other for your applications
  communication). For example: If your machines are connected with two
  fast ethernet links, then you should be able to increase the
  thourghput of the cloning process from 10 to 20 MB/s, therefore
  cutting the cloning-time by half.
  You need the "add" option in the config file to use this feature.
  WARNING: This feature has only been tested with the linear network
  topology (no fanout option or "fanout 1" option in the config file).

- Different networking topologies.
  We tried different topologies (binary trees, ternary trees, ...) to
  get somre more results in a paper, but the initial multi-drop chain
  (virtual TCP ring) is still the best. You will most likely not need
  this feature.


version 0.57
------------

Besides some bug-files and smaller improvements, it's now possible to
split an image in multiple files for archival and send the
multiple-file image to the clients. This allows to story arbitrary
long partitions on file systems with a file size limit. For details
and examples, see the section about the configuration file below
(parameters infile and outfile).


version 0.58
------------

Thanks to David Mathog, dolly is now able to read or write data from
its standard input or to its standard output. That means that you can
e.g. pipe a tar stream through dolly. Whether that feature is useful
or not depends on your situation. By using tar (instead of cloning the
whole partition) your disks' reads and writes will be slower, but you
only transfer the data that is actually needed. This feature might be
most useful in situations where e.g. your disks/partitions are mostly
empty or have different sizes/geometries.

Please note that version 0.58 has not yet been thoroughly tested (I'm
no longer working with clusters). E.g. it is not yet clear what
happens when somebody tries to reach you with the "write", "talk" or
"wall" commands while dolly is running (which might potentially
interfere with with your stdin/stdout, see below).

Note also, that since all of dolly's output is now written to stderr
(instead of stdout as before), some third-party scripts might no
longer work.

To use the feature, you should specify /dev/stdin as your infile
and/or /dev/stdout as your outfile.


version 0.58C
-------------

Again, thanks to David Mathog, dolly can now be run without explicit
sync() at the end of the cloning process (option "-n"). This can speed
up dolly's runtime considerably when cloning smaller files, but there
is no garantuee that the data actually made it to the disk if there is
e.g. a power loss right after dolly finished.

version 0.59
------------

Some output improvments and add some options to deal with socket and 
buffer size to experiment some parameter on the fly. Done some cleanup
in the C code to get less warning in building with recent GCC7.



EXAMPLE
=======

In this example we assume a cluster of 16 machines, named
node0..node15. We want to clone the partition sda5 from node0 to all
other nodes. The configuration file (let's name it dollytab.cfg)
should then look as follows:
  infile /dev/sda5
  outfile /dev/sda5
  server node0
  firstclient node1
  lastclient node15
  clients 15
  node1
  node2
  node3
  node4
  node5
  node6
  node7
  node8
  node9
  node10
  node11
  node12
  node13
  node14
  node15
  endconfig
Next, we start Dolly on all the clients. No options are required for
the clients (but you might want to add the "-v" option for verbose
progress reports). Finally, Dolly is started on the server as follows:
  dolly -v -s -f dollytab.cfg
That's all.


Bibliography
============

Felix Rauch, Christian Kurmann, Thomas M. Stricker: <em>Optimizing the
distribution of large data sets in theory and practice</em>. Concurrency
and Computation: Practice and Experience, volume 14, issue 3, pages
165-181, april 2002. (c) John Wiley & Sons, Ltd.

Maintained by Felix Rauch.
http://www.cs.inf.ethz.ch/~rauch/
Felix Rauch <rauch@inf.ethz.ch>

AUTHORS
=======
Antoine Aginies <agines@suse.com>
Christian Goll <cgoll@suse.com>
