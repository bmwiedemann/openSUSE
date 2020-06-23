#
# spec file for package rear
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_without	use_mkisofs

Name:           rear
# When there are SUSE specific patches, add a trailing letter 'a' 'b' 'c' ...
# to the rear upstrea, version (e.g. "Version: 1.18.a"
# see https://github.com/rear/rear/issues/666
Version:        2.6
Release:        0
%define upstream_version 2.6
# Automatic version upgrades are not possible in practice.
# The user must explicitly specify his intended version.
# When users have a working disaster recovery procedure, they should not upgrade
# (see "Version upgrades" at http://en.opensuse.org/SDB:Disaster_Recovery).
# Users who already use it and like to upgrade, must re-validate that their
# particular disaster recovery procedure still works.
# For one product (e.g. SLE11 or SLE12) we provide several versions in parallel
# so that users where version N does not support their particular needs
# can upgrade to version M but on the other hand users who have a working
# disaster recovery procedure with version N do not need to upgrade.
# Therefore the package name contains the version and all packages conflict with each other
# to avoid that an installed version gets accidentally replaced with another version:
Provides:       rear = %{version}
Conflicts:      rear < %{version}
Conflicts:      rear > %{version}
Summary:        Relax-and-Recover (abbreviated rear) is a Linux Disaster Recovery framework
# Currently (as of this writing Tue Apr 26 2016) rear contains many files
# with explicit GPL-2.0+ or GPL-2.1+ licensing notes of the form
#   either version 2 of the License, or (at your option) any later version
#   either version 2.1 of the License, or (at your option) any later version
# so that some (older) rear files are still "GPL-2.0+" but some (newer) rear files are "GPL-3.0"
# according to the current COPYING file in rear that was changed from GPL version 2 (up to rear 1.17.2)
# to GPL version 3 (since rear 1.18) see the rear upstream issue https://github.com/rear/rear/pull/739
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            http://relax-and-recover.org/
# As GitHub stopped with download section we need to go back to Sourceforge for downloads.
# How to download Source0 from Sourceforge:
# wget --no-check-certificate -O rear-2.6.tar.gz http://sourceforge.net/projects/rear/files/rear/2.6/rear-2.6.tar.gz
Source0:        http://sourceforge.net/projects/rear/files/rear/%{upstream_version}/rear-%{upstream_version}.tar.gz
# Source999 rear-rpmlintrc filters false positives rpmlint warning messages, see
# https://en.opensuse.org/openSUSE:Packaging_checks#Building_Packages_despite_of_errors
Source999:      rear-rpmlintrc
# Rear contains only bash scripts plus documentation so that on first glance it could be "BuildArch: noarch"
# but actually it is not "noarch" because it only works on those architectures that are explicitly supported.
# Of course the rear bash scripts can be installed on any architecture just as any binaries can be installed on any architecture.
# But the meaning of architecture dependent packages should be on what architectures they will work.
# Therefore only those architectures that are actually supported are explicitly listed.
# This avoids that rear can be "just installed" on architectures that are actually not supported (e.g. ARM or IBM z Systems).
# ReaR does not support the 'ppc' architecture, cf. https://github.com/rear/rear/issues/1596#issuecomment-351698817
ExclusiveArch:  %ix86 x86_64 ppc64 ppc64le
# Furthermore for some architectures it requires architecture dependent packages (like syslinux for x86 and x86_64)
# so that rear must be architecture dependent because ifarch conditions never match in case of "BuildArch: noarch"
# see the GitHub issue https://github.com/rear/rear/issues/629
%ifarch %ix86 x86_64
Requires:       syslinux
%endif
# In the end this should tell the user that rear is known to work only on x86 x86_64 ppc ppc64 ppc64le
# and on x86 x86_64 syslinux is explicitly required to make the bootable ISO image
# (in addition to the default installed bootloader grub2) while on ppc ppc64 ppc64le the
# default installed bootloader yaboot is also useed to make the bootable ISO image.
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# LSB RPM Requires:
# Begin of "Requires: lsb" cleanup:
# Rear upstream has "Requires: lsb" but that requires much too much,
# see https://bugzilla.novell.com/show_bug.cgi?id=807747#c4
# "A distribution is LSB Certified or LSB compliant if and only if
#  the distribution provides all requirements as outlined in the
#  specification."
# Accordingly SUSE's lsb RPM requires tons of stuff that is not
# needed by Rear (in particular various graphical libraries,
# sound stuff, printing stuff, and so on).
# Therefore "Requires: lsb" is replaced by explicitly listing the RPM packages
# that are mandatory (in particular when a binary is called in a script) for Rear (as RPM Requires)
# plus what seems to be optional (nice to have) for Rear (as RPM Recommends)
# minus library packages because needed libraries should be automatically required.
# I <jsmeix@suse.de> think requiring RPM packages instead of binaries is better
# because it keeps the list shorter which is hopefully easier to maintain and
# the requirements are on a more higher level which is hopefully more unsusceptible against
# minor changes in what exact binaries names are actually called by Rear.
# To test if a binary is called by a Rear script the following was done (example for /usr/bin/bc):
#   BIN="bc"
#   for f in $( find /usr/share/rear/ )
#   do grep "\<$BIN\> " $f 2>/dev/null | grep -v '^[[:space:]]*#'
#   done
# What is not tested to find out if a binary is called by a Rear script is "eval" stuff,
# something like STRING=<result of whatever calls> ; eval $STRING
# Usually Rear calls "eval echo ..." or "eval "${EXTERNAL_whatever[@]}"
# except in /usr/share/rear/finalize/default/88_check_for_mount_by_id.sh that calls
#   eval "$(scsi_id ...
# where the only scsi_id that I could find is /usr/lib/udev/scsi_id
# which belongs to udev and I assume that udev is installed in any case
# so that there is no explicit RPM Requires for udev in Rear.
# What is also not tested to find out what Rear actually needs is
# which files (not only binaries) Rear needs to build up its recovery system
# (in particular tools for partitioning, creating filesystems, and bootloader installation).
# I assume what Rear needs to build up the system-specific recovery system is installed
# (e.g. if the ext4 filesystem is used, I assume mkfs.ext4 is installed)
# so that there are no explicit RPM Requires needed for that in Rear.
# The following list was derived from the RPM Requires of SUSE's lsb package
# (its last RPM changelog entry dated "Tue Oct  1 07:01:56 UTC 2013") as follows:
#   for r in $( grep ^Requires: lsb.spec | tr -s ' ' | cut -d ' ' -f2 )
#   do rpm -q --whatprovides $r
#   done | sort -u
# which results the following list where only what is needed for Rear is activated:
#   Mesa-9.2.3-61.9.1.i586
#   Mesa-libGL1-9.2.3-61.9.1.i586
#   at-3.1.13-5.4.1.i586
Requires:       bash
Requires:       bc
Requires:       binutils
Requires:       coreutils
Requires:       cpio
#   cronie-1.4.8-50.1.2.i586
#   cups-client-1.5.4-140.1.i586
Requires:       diffutils
#   ed-1.9-2.1.2.i586
Requires:       file
Requires:       findutils
#   fontconfig-2.11.0-1.1.i586
#   foomatic-filters-4.0.12-5.1.1.i586
Requires:       gawk
#   gettext-runtime-0.18.3.1-1.1.i586
#   ghostscript-9.10-45.4.i586
# Rear calls getent in /usr/share/rear/rescue/default/90_clone_users_and_groups.sh
Requires:       glibc
#   glibc-i18ndata-2.18-4.11.1.noarch
Requires:       grep
Requires:       gzip
#   libGLU1-9.0.0-7.1.2.i586
#   libXt6-1.1.4-2.1.2.i586
#   libXtst6-1.2.2-2.1.2.i586
#   libasound2-1.0.27.2-3.5.1.i586
#   libatk-1_0-0-2.10.0-1.1.i586
#   libglib-2_0-0-2.38.2-8.2.i586
#   libgtk-2_0-0-2.24.22-2.1.i586
#   libjpeg62-62.0.0-24.1.3.i586
#   libpango-1_0-0-1.36.1-4.2.i586
#   libpng12-0-1.2.50-6.1.2.i586
#   libqt4-4.8.5-5.6.1.i586
#   libqt4-sql-4.8.5-5.6.1.i586
#   libqt4-x11-4.8.5-5.6.1.i586
#   libxml2-tools-2.9.1-2.1.2.i586
# Rear calls "lsb_release" in /usr/share/rear/lib/config-functions.sh
Requires:       lsb-release
#   m4-1.4.16-14.1.2.i586
#   mailx-12.5-14.1.3.i586
#   make-3.82-160.2.1.i586
#   man-2.6.3-9.1.3.i586
#   mozilla-nss-3.15.3.1-8.1.i586
Requires:       net-tools
#   patch-2.7.1-4.1.2.i586
#   pax-3.4-155.1.2.i586
Requires:       perl-base
#   postfix-2.9.6-7.4.1.i586
Requires:       procps
#   psmisc-22.20-5.1.2.i586
#   python-2.7.5-8.3.1.i586
#   python3-3.3.2-5.1.3.i586
#   qt3-3.3.8c-128.1.2.i586
Requires:       rsync
Requires:       sed
#   shadow-4.1.5.1-8.1.2.i586
#   systemd-sysvinit-208-15.1.i586
#   sysvinit-tools-2.88+-89.1.2.i586
Requires:       tar
#   time-1.7-3.1.2.i586
Requires:       util-linux
#   xdg-utils-20121008-2.2.1.noarch
# End of "Requires: lsb" cleanup.
# Non-LSB RPM Requires:
# all RPM based systems seem to have this and call it the same
Requires:       ethtool
Requires:       iproute2
Requires:       iputils
%if 0%{?suse_version} >= 1230
Requires:       %{_sbindir}/agetty
%else
Requires:       /sbin/mingetty
%endif
%if %{with use_mkisofs}
Requires:       %{_bindir}/mkisofs
%else
Requires:       %{_bindir}/genisoimage
%endif
# Recent SUSE versions have an extra nfs-client package
Requires:       nfs-client
# Rear calls openssl in /usr/share/rear/rescue/default/50_ssh.sh
Requires:       openssl
# openSUSE from 11.1 and SLES from 11 uses rpcbind instead of portmap
Requires:       rpcbind

%description
Relax-and-Recover (abbreviated rear) is the leading
Free Software disaster recovery framework.

Relax-and-Recover is written entirely in the native
language for system administration: as bash scripts.

Experienced users and system admins can adapt or extend
the rear scripts to make it work for their particular
cases.

Relax-and-Recover is a modular framework with
ready-to-go workflows for common situations.

The basic workflow is as follows:
Specify its configuration in /etc/rear/local.conf
(cf. /usr/share/rear/conf/examples) and run
"rear mkbackup" to create a backup.tar.gz on
a NFS server and a bootable recovery ISO image
for your system.
A recovery medium which is made from the ISO image
boots a special rear recovery system.
Log in as root and run "rear recover" which does
the following steps:
It runs the rear installer that recreates the basic
system, in particular the system disk partitioning
with filesystems and mount points, then it restores
the backup from the NFS server and finally it
installs the boot loader.
Finally remove the recovery medium and reboot the
recreated system.

Relax-and-Recover supports various kind of boot media
for the recovery system (incl. ISO, PXE, OBDR tape,
USB or eSATA storage), a variety of network protocols
(incl. sftp, ftp, http, nfs, cifs) for storage and backup
as well as various external third-party backup methods
(incl. IBM Tivoli Storage Manager, HP DataProtector,
Symantec NetBackup, EMC NetWorker, FDR/Upstream,
NovaBACKUP DC, Bareos, Bacula, rsync, rbme).

Warning for users who like to upgrade Relax-and-Recover:
Users who already use it must re-validate that their
particular disaster recovery procedure still works.

Additionally when you already use Relax-and-Recover and
you upgrade software that is related to the basic system
(e.g. kernel, storage, bootloader, init, networking) or
you do other changes in your basic system, you must also
re-validate that your particular disaster recovery
procedure still works for you.

You must test in advance that it works in your particular
case to recreate your particular system with your
particular recovery medium and that the recreated system
can boot on its own and that the recreated system with
all its system services still work as you need it in your
particular case.

You must have replacement hardware available on which your
system can be recreated and you must try out if it works
to recreate your system with your recovery medium on your
replacement hardware.

Be prepared that your system recovery fails to recreate
your system. When it fails to recreate your system
it is usually a dead end. Be prepared for a manual
recreation from scratch. Always have all information
available that you need to recreate your particular
system manually. Manually recreate your system on your
replacement hardware as an exercise.

For more information see
http://en.opensuse.org/SDB:Disaster_Recovery

Relax-and-Recover comes with ABSOLUTELY NO WARRANTY;
for details see the GNU General Public License.

%prep
%setup -q -n rear-%{upstream_version}
# Add a specific os.conf to not depend on LSB dependencies
# (otherwise it calls "lsb_release" in /usr/share/rear/lib/config-functions.sh)
# for the suse_version values see the listings at
# https://en.opensuse.org/openSUSE:Packaging_for_Leap#RPM_Distro_Version_Macros
# and
# http://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
# in particular in the latter see there the "Note" that reads
# "sles_version is no longer set in SLES 11. Use suse_version == 1110 instead."
# and use that also for all older SUSE distributions:
%if 0%{?suse_version} <= 1110
# SLE 11 and openSUSE 11.1
OS_VERSION="11"
%endif
%if 0%{?suse_version} == 1310
# openSUSE 13.1
OS_VERSION="13.1"
%endif
%if 0%{?suse_version} == 1320
# openSUSE 13.2
OS_VERSION="13.2"
%endif
%if 0%{?suse_version} == 1315
# SLE 12 and openSUSE Leap 42.x
OS_VERSION="12"
%endif
%if 0%{?suse_version} == 1500
# SLE 15 and openSUSE Leap 15.x
OS_VERSION="15"
%endif
%if 0%{?suse_version} > 1500
# openSUSE Factory - current upcoming release (changing)
# treat it same as SLE 15 and openSUSE Leap 15.x:
OS_VERSION="15"
%endif
echo -e "OS_VENDOR=SUSE_LINUX\nOS_VERSION=$OS_VERSION" >etc/rear/os.conf

%build
# No code to compile - all bash scripts - but at least run "make validate"
# that runs "bash -n" for all bash files to test if the plain syntax is o.k.
make validate

%install
make install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root,-)
%doc MAINTAINERS COPYING README.adoc doc/*.txt doc/*.adoc doc/user-guide/*.adoc doc/mappings/
%{_mandir}/man8/rear.8*
%config(noreplace) %{_sysconfdir}/rear/
%config(noreplace) %{_datadir}/rear/
%{_localstatedir}/lib/rear/
%{_sbindir}/rear

%changelog
