# root:
zypper in git-core mosh screen rsync kexec-tools glibc-locale nfs-client procmail perl-Text-Glob perl-core-DB_File osc python3-pika
useradd -m opensusegit
useradd -m opensuserabbit
echo 'hilbert.suse.de.:/work /mounts/work/ nfs4 defaults 0 0' >> /etc/fstab
mkdir /mounts/work/
mount /mounts/work/

# non-root
ipfs init

# How it works
scripts/syncloop runs scripts/sync hourly: rsync Factory to in/, scripts/mappkgs.pl
maps it to packages/<letter>/<pkg>/ (sources hardlinked, binaries as /ipfs symlinks),
one monorepo commit per run. The rabbithandle service does the same per package on
OBS events (scripts/syncone). Each package also has a repo on
https://code.opensuse.org/package/<pkg>.git: it is the ref refs/pkg/<pkg>.git in this
repository, made from the package subtree in HEAD and pushed by scripts/pkgcommit
(refs/pkg-pushed/ records what was accepted). pagure-new-package needs ~/.pagureapitoken.
Migrating a checkout that still has nested .git dirs: scripts/pkgimport (see its header).
