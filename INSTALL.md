# root:
zypper in git-core mosh screen rsync kexec-tools glibc-locale nfs-client procmail perl-Text-Glob perl-core-DB_File osc python3-pika
useradd -m opensusegit
useradd -m opensuserabbit
echo 'hilbert.suse.de.:/work /mounts/work/ nfs4 defaults 0 0' >> /etc/fstab
mkdir /mounts/work/
mount /mounts/work/

# non-root
ipfs init
