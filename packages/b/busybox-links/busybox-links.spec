#
# spec file for package busybox-links
#
# Copyright (c) 2023 SUSE LLC
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


Name:           busybox-links
Version:        %(rpm -q busybox --qf '%%{VERSION}')
Release:        0
Summary:        Links for busybox applets
License:        GPL-2.0-or-later
Source:         busybox-links-rpmlintrc
Source1:        zless
Source2:        zmore
Source3:        zgrep
BuildRequires:  attr
BuildRequires:  bc
BuildRequires:  bind-utils
BuildRequires:  busybox
BuildRequires:  bzip2
BuildRequires:  coreutils
BuildRequires:  cpio
BuildRequires:  diffutils
BuildRequires:  dos2unix
BuildRequires:  ed
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  grep
BuildRequires:  gzip
BuildRequires:  hexedit
BuildRequires:  hostname
BuildRequires:  iproute2
BuildRequires:  iputils
BuildRequires:  kbd
BuildRequires:  kmod
BuildRequires:  less
BuildRequires:  man
BuildRequires:  ncurses-utils
BuildRequires:  net-tools
BuildRequires:  net-tools-deprecated
BuildRequires:  netcat-openbsd
BuildRequires:  patch
BuildRequires:  policycoreutils
BuildRequires:  procps
BuildRequires:  psmisc
BuildRequires:  sed
BuildRequires:  selinux-tools
BuildRequires:  sendmail
BuildRequires:  sha3sum
BuildRequires:  shadow
BuildRequires:  sharutils
BuildRequires:  sysvinit-tools
BuildRequires:  tar
BuildRequires:  telnet
BuildRequires:  tftp
BuildRequires:  time
BuildRequires:  traceroute
BuildRequires:  tunctl
BuildRequires:  unzip
BuildRequires:  util-linux
BuildRequires:  util-linux-systemd
BuildRequires:  vim
BuildRequires:  vlan
BuildRequires:  wget
BuildRequires:  which
BuildRequires:  whois
BuildRequires:  xz
Requires:       busybox = %{version}
Requires:       busybox-adduser = %{version}
Requires:       busybox-attr = %{version}
Requires:       busybox-bc = %{version}
Requires:       busybox-bind-utils = %{version}
Requires:       busybox-bzip2 = %{version}
Requires:       busybox-coreutils = %{version}
Requires:       busybox-cpio = %{version}
Requires:       busybox-diffutils = %{version}
Requires:       busybox-dos2unix = %{version}
Requires:       busybox-ed = %{version}
Requires:       busybox-findutils = %{version}
Requires:       busybox-gawk = %{version}
Requires:       busybox-grep = %{version}
Requires:       busybox-gzip = %{version}
Requires:       busybox-hexedit = %{version}
Requires:       busybox-hostname = %{version}
Requires:       busybox-iproute2 = %{version}
Requires:       busybox-iputils = %{version}
Requires:       busybox-kbd = %{version}
Requires:       busybox-less = %{version}
Requires:       busybox-man = %{version}
Requires:       busybox-misc = %{version}
Requires:       busybox-ncurses-utils = %{version}
Requires:       busybox-net-tools = %{version}
Requires:       busybox-netcat = %{version}
Requires:       busybox-patch = %{version}
Requires:       busybox-policycoreutils = %{version}
Requires:       busybox-procps = %{version}
Requires:       busybox-psmisc = %{version}
Requires:       busybox-sed = %{version}
Requires:       busybox-selinux-tools = %{version}
Requires:       busybox-sendmail = %{version}
Requires:       busybox-sh = %{version}
Requires:       busybox-sha3sum = %{version}
Requires:       busybox-sharutils = %{version}
Requires:       busybox-syslogd = %{version}
Requires:       busybox-sysvinit-tools = %{version}
Requires:       busybox-tar = %{version}
Requires:       busybox-telnet = %{version}
Requires:       busybox-tftp = %{version}
Requires:       busybox-time = %{version}
Requires:       busybox-traceroute = %{version}
Requires:       busybox-tunctl = %{version}
Requires:       busybox-unzip = %{version}
Requires:       busybox-util-linux = %{version}
Requires:       busybox-vi = %{version}
Requires:       busybox-vlan = %{version}
Requires:       busybox-wget = %{version}
Requires:       busybox-which = %{version}
Requires:       busybox-whois = %{version}
Requires:       busybox-xz = %{version}
BuildArch:      noarch

%description
This is a meta package requireing all packages providing busybox applets.

%package -n busybox-misc
Summary:        Busybox applets not fitting anywhere else
Requires:       busybox = %{version}
Conflicts:      binutils
Conflicts:      blog
Conflicts:      dosfstools
Conflicts:      e2fsprogs
Conflicts:      lsof
Conflicts:      lsscsi
Conflicts:      lzop
Conflicts:      nbd
Conflicts:      sysstat
Conflicts:      usbutils
Conflicts:      xterm-bin

%description -n busybox-misc
This package contains the symlinks to provide various busybox applets which
do not fit really to any other package.

%package -n busybox-attr
Summary:        Busybox applets replacing attr
Requires:       busybox = %{version}
Conflicts:      attr

%description -n busybox-attr
This package contains the symlinks to replace attr with busybox.

%package -n busybox-sh
Summary:        Busybox sh, ash and hush
Requires:       busybox = %{version}
Requires(post): busybox
Requires(preun):busybox
Provides:       alternative(sh)
Conflicts:      alternative(sh)
Obsoletes:      busybox-ash < %{version}

%description -n busybox-sh
This package contains the busybox sh, ash and hush.

%package -n busybox-bind-utils
Summary:        Busybox applets replacing bind-utils
Requires:       busybox = %{version}
Conflicts:      bind-utils

%description -n busybox-bind-utils
This package contains the symlinks to replace bind-utils with busybox.

%package -n busybox-coreutils
Summary:        Busybox applets replacing coreutils
Requires:       busybox = %{version}
Conflicts:      coreutils

%description -n busybox-coreutils
This package contains the symlinks to replace coreutils with busybox.

%package -n busybox-diffutils
Summary:        Busybox applets replacing diffutils
Requires:       busybox = %{version}
Conflicts:      diffutils

%description -n busybox-diffutils
This package contains the symlinks to replace diffutils with busybox.

%package -n busybox-findutils
Summary:        Busybox applets replacing findutils
Requires:       busybox = %{version}
Conflicts:      findutils

%description -n busybox-findutils
This package contains the symlinks to replace findutils with busybox.

%package -n busybox-util-linux
Summary:        Busybox applets replacing util-linux
Requires:       busybox = %{version}
Conflicts:      util-linux
Conflicts:      util-linux-systemd

%description -n busybox-util-linux
This package contains the symlinks to replace util-linux with busybox.

%package -n busybox-iputils
Summary:        Busybox applets replacing iputils
Requires:       busybox = %{version}
Conflicts:      iputils

%description -n busybox-iputils
This package contains the symlinks to replace iputils with busybox.

%package -n busybox-iproute2
Summary:        Busybox applets replacing iproute2
Requires:       busybox = %{version}
Conflicts:      bridge-utils
Conflicts:      iproute2
Conflicts:      wicked-service

%description -n busybox-iproute2
This package contains the symlinks to replace iproute2 with busybox.

%package -n busybox-gawk
Summary:        Busybox applets replacing gawk
Requires:       busybox = %{version}
Conflicts:      gawk
Conflicts:      mawk

%description -n busybox-gawk
This package contains the symlinks to replace gawk with busybox.

%package -n busybox-grep
Summary:        Busybox applets replacing grep
Requires:       busybox = %{version}
Conflicts:      grep

%description -n busybox-grep
This package contains the symlinks to replace grep with busybox.

%package -n busybox-gzip
Summary:        Busybox applets replacing gzip
Requires:       busybox = %{version}
Conflicts:      gzip

%description -n busybox-gzip
This package contains the symlinks to replace gzip with busybox.

%package -n busybox-sed
Summary:        Busybox applets replacing sed
Requires:       busybox = %{version}
Conflicts:      sed

%description -n busybox-sed
This package contains the symlinks to replace sed with busybox.

%package -n busybox-cpio
Summary:        Busybox applets replacing cpio
Requires:       busybox = %{version}
Conflicts:      cpio

%description -n busybox-cpio
This package contains the symlinks to replace cpio with busybox.

%package -n busybox-patch
Summary:        Busybox applets replacing patch
Requires:       busybox = %{version}
Conflicts:      patch

%description -n busybox-patch
This package contains the symlinks to replace patch with busybox.

%package -n busybox-procps
Summary:        Busybox applets replacing procps
Requires:       busybox = %{version}
Conflicts:      procps

%description -n busybox-procps
This package contains the symlinks to replace procps with busybox.

%package -n busybox-which
Summary:        Busybox applets replacing which
Requires:       busybox = %{version}
Conflicts:      which

%description -n busybox-which
This package contains the symlinks to replace which with busybox.

%package -n busybox-xz
Summary:        Busybox applets replacing xz
Requires:       busybox = %{version}
Conflicts:      xz

%description -n busybox-xz
This package contains the symlinks to replace xz with busybox.

%package -n busybox-bzip2
Summary:        Busybox applets replacing bzip2
Requires:       busybox = %{version}
Conflicts:      bzip2

%description -n busybox-bzip2
This package contains the symlinks to replace bzip2 with busybox.

%package -n busybox-psmisc
Summary:        Busybox applets replacing psmisc
Requires:       busybox = %{version}
Conflicts:      psmisc

%description -n busybox-psmisc
This package contains the symlinks to replace psmisc with busybox.

%package -n busybox-kbd
Summary:        Busybox applets replacing kbd
Requires:       busybox = %{version}
Conflicts:      kbd

%description -n busybox-kbd
This package contains the symlinks to replace kbd with busybox.

%package -n busybox-less
Summary:        Busybox applets replacing less
Requires:       busybox = %{version}
Conflicts:      less

%description -n busybox-less
This package contains the symlinks to replace less with busybox.

%package -n busybox-sharutils
Summary:        Busybox applets replacing sharutils
Requires:       busybox = %{version}
Conflicts:      sharutils

%description -n busybox-sharutils
This package contains the symlinks to replace sharutils with busybox.

%package -n busybox-syslogd
Summary:        Busybox applets providing syslogd
Requires:       busybox = %{version}
Conflicts:      syslogd

%description -n busybox-syslogd
This package contains the symlinks to provide syslogd with busybox.

%package -n busybox-hexedit
Summary:        Busybox applets replacing hexedit
Requires:       busybox = %{version}
Conflicts:      hexedit

%description -n busybox-hexedit
This package contains the symlinks to replace hexedit with busybox.

%package -n busybox-hostname
Summary:        Busybox applets replacing hostname
Requires:       busybox = %{version}
Conflicts:      hostname

%description -n busybox-hostname
This package contains the symlinks to replace hostname with busybox.

%package -n busybox-man
Summary:        Busybox applets replacing man
Requires:       busybox = %{version}
Conflicts:      man
Conflicts:      mandoc

%description -n busybox-man
This package contains the symlinks to replace man with busybox.

%package -n busybox-net-tools
Summary:        Busybox applets replacing net-tools
Requires:       busybox = %{version}
Conflicts:      net-tools
Conflicts:      net-tools-deprecated

%description -n busybox-net-tools
This package contains the symlinks to replace net-tools with busybox.

%package -n busybox-traceroute
Summary:        Busybox applets replacing traceroute
Requires:       busybox = %{version}
Conflicts:      traceroute

%description -n busybox-traceroute
This package contains the symlinks to replace traceroute with busybox.

%package -n busybox-ncurses-utils
Summary:        Busybox applets replacing ncurses-utils
Requires:       busybox = %{version}
Conflicts:      ncurses-utils

%description -n busybox-ncurses-utils
This package contains the symlinks to replace ncurses-utils with busybox.

%package -n busybox-kmod
Summary:        Busybox applets replacing kmod
Requires:       busybox = %{version}
Conflicts:      kmod

%description -n busybox-kmod
This package contains the symlinks to replace kmod with busybox.

%package -n busybox-tar
Summary:        Busybox applets replacing tar
Requires:       busybox = %{version}
Conflicts:      tar

%description -n busybox-tar
This package contains the symlinks to replace tar with busybox.

%package -n busybox-sendmail
Summary:        Busybox applets replacing sendmail
Requires:       busybox = %{version}
Provides:       smtp_daemon
Conflicts:      exim
Conflicts:      msmtp-mta
Conflicts:      postfix
Conflicts:      postfix-bdb
Conflicts:      sendmail

%description -n busybox-sendmail
This package contains the symlinks to replace sendmail with busybox.

%package -n busybox-adduser
Summary:        Busybox applets containing adduser and some shadow tools
Requires:       busybox = %{version}
Requires:       group(nogroup)
Conflicts:      shadow

%description -n busybox-adduser
This package contains the symlinks for adduser and some tools from the
shadow suite.

%package -n busybox-sha3sum
Summary:        Busybox applets replacing sha3sum
Requires:       busybox = %{version}
Conflicts:      perl-Digest-SHA3
Conflicts:      sha3sum

%description -n busybox-sha3sum
This package contains the symlinks to replace sha3sum with busybox.

%package -n busybox-whois
Summary:        Busybox applets replacing whois
Requires:       busybox = %{version}
Conflicts:      whois

%description -n busybox-whois
This package contains the symlinks to replace whois with busybox.

%package -n busybox-unzip
Summary:        Busybox applets replacing unzip
Requires:       busybox = %{version}
Conflicts:      unzip

%description -n busybox-unzip
This package contains the symlinks to replace unzip with busybox.

%package -n busybox-wget
Summary:        Busybox applets replacing wget
Requires:       busybox = %{version}
Conflicts:      wget

%description -n busybox-wget
This package contains the symlinks to replace wget with busybox.

%package -n busybox-vi
Summary:        Busybox applets replacing vim
Requires:       busybox = %{version}
Conflicts:      gvim
Conflicts:      vim
Conflicts:      vim-nox11
Conflicts:      vim-small

%description -n busybox-vi
This package contains the symlinks to provide vi with busybox.

%package -n busybox-ed
Summary:        Busybox applets replacing ed
Requires:       busybox = %{version}
Conflicts:      ed

%description -n busybox-ed
This package contains the symlinks to provide ed with busybox.

%package -n busybox-bc
Summary:        Busybox applets replacing bc
Requires:       busybox = %{version}
Conflicts:      bc

%description -n busybox-bc
This package contains the symlinks to provide bc with busybox.

%package -n busybox-netcat
Summary:        Busybox applets replacing netcat
Requires:       busybox = %{version}
Conflicts:      netcat-openbsd

%description -n busybox-netcat
This package contains the symlinks to provide nc with busybox.

%package -n busybox-dos2unix
Summary:        Busybox applets replacing dos2unix
Requires:       busybox = %{version}
Conflicts:      dos2unix

%description -n busybox-dos2unix
This package contains the symlinks to provide dos2unix with busybox.

%package -n busybox-telnet
Summary:        Busybox applets replacing telnet
Requires:       busybox = %{version}
Conflicts:      telnet

%description -n busybox-telnet
This package contains the symlinks to provide telnet with busybox.

%package -n busybox-tftp
Summary:        Busybox applets replacing tftp
Requires:       busybox = %{version}
Conflicts:      tftp

%description -n busybox-tftp
This package contains the symlinks to provide tftp with busybox.

%package -n busybox-time
Summary:        Busybox applets replacing time
Requires:       busybox = %{version}
Conflicts:      time

%description -n busybox-time
This package contains the symlinks to provide time with busybox.

%package -n busybox-tunctl
Summary:        Busybox applets replacing tunctl
Requires:       busybox = %{version}
Conflicts:      tunctl

%description -n busybox-tunctl
This package contains the symlinks to provide tunctl with busybox.

%package -n busybox-vlan
Summary:        Busybox applets replacing vlan
Requires:       busybox = %{version}
Conflicts:      vlan

%description -n busybox-vlan
This package contains the symlinks to provide vlan with busybox.

%package -n busybox-sysvinit-tools
Summary:        Busybox applets replacing sysvinit-tools
Requires:       busybox = %{version}
Conflicts:      sysvinit-tools

%description -n busybox-sysvinit-tools
This package contains the symlinks to provide sysvinit-tools with busybox.

%package -n busybox-selinux-tools
Summary:        Busybox applets replacing selinux-tools
Requires:       busybox = %{version}
Conflicts:      selinux-tools

%description -n busybox-selinux-tools
This package contains the symlinks to provide selinux-tools with busybox.

%package -n busybox-policycoreutils
Summary:        Busybox applets replacing policycoreutils
Requires:       busybox = %{version}
Conflicts:      policycoreutils

%description -n busybox-policycoreutils
This package contains the symlinks to provide policycoreutils with busybox.

%prep
%setup -q -c -T

%build
mkdir apps
mkdir used
mkdir missing
for i in `cat %{_datadir}/busybox/busybox.links` ; do touch apps/`basename $i`; done
# No rpm/rpm2cpio, will break build service
rm -f apps/rpm apps/rpm2cpio
# No /linuxrc
rm -f apps/linuxrc
# Does not really fit
rm apps/[[
for package in coreutils diffutils findutils grep util-linux util-linux-systemd iputils iproute2 gzip sed cpio procps xz bzip2 psmisc kbd sharutils hexedit hostname net-tools net-tools-deprecated traceroute ncurses-utils kmod tar gawk patch attr which bind-utils man sendmail sha3sum shadow less whois unzip vim wget ed bc netcat-openbsd dos2unix telnet tftp time tunctl vlan sysvinit-tools selinux-tools policycoreutils; do
    for i in `rpm -ql $package |grep "bin/"` ; do
	prog=`basename $i`
	if [ -f apps/$prog ]; then
	    touch used/$prog
	    echo $i >> filelist-$package.txt
	else
	    touch missing/$prog
	fi
    done
done
# Merge net-tools sub-packages
cat filelist-net-tools-deprecated.txt >> filelist-net-tools.txt
rm filelist-net-tools-deprecated.txt
# Create some extra sub-packages
echo -e "%{_bindir}/ash" > filelist-sh.txt
touch used/ash
echo -e "%{_bindir}/hush" >> filelist-sh.txt
touch used/hush
%if 0%{?suse_version} < 1550
echo "/bin/sh" >> filelist-sh.txt
%endif
echo -e "%{_bindir}/sh" >> filelist-sh.txt
touch used/sh
%if 0%{?suse_version} < 1550
echo -e "/sbin/loadkmap" >> filelist-kbd.txt
%endif
echo -e "%{_sbindir}/loadfont" >> filelist-kbd.txt
touch used/loadkmap used/loadfont

echo -e "/usr/sbin/addgroup\n/usr/sbin/adduser\n/usr/sbin/delgroup\n/usr/sbin/deluser" >> filelist-shadow.txt
touch used/addgroup used/adduser used/delgroup used/deluser

echo -e "/usr/sbin/syslogd" > filelist-syslogd.txt
touch used/syslogd

# Some iproute2 commands are named sligthly different
echo -e "/usr/sbin/ifdown\n/usr/sbin/ifenslave\n/usr/sbin/ifup\n/usr/sbin/ipaddr\n/usr/sbin/iplink\n/usr/sbin/ipneigh\n/usr/sbin/iproute\n/usr/sbin/iprule\n/usr/sbin/brctl" >> filelist-iproute2.txt
touch used/ifdown used/ifenslave used/ifup used/ipaddr used/iplink used/ipneigh used/iproute used/iprule used/brctl

for i in `/bin/ls used/` ; do
    rm apps/$i
done

for i in `cat %{_datadir}/busybox/busybox.links` ; do
    prog=`basename $i`
    if [ -f apps/$prog ]; then
	echo $i >> filelist-misc.txt
    fi
done

cp  %{_datadir}/licenses/busybox/LICENSE .
sed -e 's|$prefix/bin/busybox|$prefix/usr/bin/busybox|g' -e 's|"bin/busybox"|"..%{_bindir}/busybox"|g' -e 's|"busybox"|"..%{_bindir}/busybox"|g' -e 's|"../bin/busybox"|"..%{_bindir}/busybox"|g' -e 's|"../../bin/busybox"|"../bin/busybox"|g' -e 's|%{_datadir}/busybox/busybox.links|filelist.txt|g' %{_bindir}/busybox.install > busybox.install

cat filelist-*.txt | sort -u > filelist.txt

/bin/ls missing/

%install
mkdir -p %{buildroot}%{_bindir}
bash ./busybox.install %{buildroot} --symlinks
rm %{buildroot}%{_bindir}/busybox
ln -sf %{_bindir}/busybox %{buildroot}%{_bindir}/sh
%if 0%{?suse_version} < 1550
ln -sf %{_bindir}/sh   %{buildroot}/bin/sh
%endif
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/zless
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/zmore
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}/zgrep

%files

%files -n busybox-adduser -f filelist-shadow.txt

%files -n busybox-attr -f filelist-attr.txt

%files -n busybox-bc -f filelist-bc.txt

%files -n busybox-bind-utils -f filelist-bind-utils.txt

%files -n busybox-bzip2 -f filelist-bzip2.txt

%files -n busybox-coreutils -f filelist-coreutils.txt

%files -n busybox-cpio -f filelist-cpio.txt

%files -n busybox-diffutils -f filelist-diffutils.txt

%files -n busybox-dos2unix -f filelist-dos2unix.txt

%files -n busybox-ed -f filelist-ed.txt

%files -n busybox-findutils -f filelist-findutils.txt

%files -n busybox-gawk -f filelist-gawk.txt

%files -n busybox-grep -f filelist-grep.txt

%files -n busybox-gzip -f filelist-gzip.txt
%{_bindir}/zgrep
%{_bindir}/zless
%{_bindir}/zmore

%files -n busybox-hexedit -f filelist-hexedit.txt

%files -n busybox-hostname -f filelist-hostname.txt

%files -n busybox-iproute2 -f filelist-iproute2.txt

%files -n busybox-iputils -f filelist-iputils.txt

%files -n busybox-kbd -f filelist-kbd.txt

%files -n busybox-kmod -f filelist-kmod.txt

%files -n busybox-less -f filelist-less.txt

%files -n busybox-man -f filelist-man.txt

%files -n busybox-misc -f filelist-misc.txt

%files -n busybox-ncurses-utils -f filelist-ncurses-utils.txt

%files -n busybox-net-tools -f filelist-net-tools.txt

%files -n busybox-netcat -f filelist-netcat-openbsd.txt

%files -n busybox-patch -f filelist-patch.txt

%files -n busybox-policycoreutils -f filelist-policycoreutils.txt

%files -n busybox-procps -f filelist-procps.txt

%files -n busybox-psmisc -f filelist-psmisc.txt

%files -n busybox-sed -f filelist-sed.txt

%files -n busybox-selinux-tools -f filelist-selinux-tools.txt

%files -n busybox-sendmail -f filelist-sendmail.txt

%files -n busybox-sha3sum -f filelist-sha3sum.txt

%files -n busybox-sharutils -f filelist-sharutils.txt

%files -n busybox-syslogd -f filelist-syslogd.txt

%files -n busybox-sysvinit-tools -f filelist-sysvinit-tools.txt

%files -n busybox-tar -f filelist-tar.txt

%files -n busybox-telnet -f filelist-telnet.txt

%files -n busybox-tftp -f filelist-tftp.txt

%files -n busybox-time -f filelist-time.txt

%files -n busybox-traceroute -f filelist-traceroute.txt

%files -n busybox-tunctl -f filelist-tunctl.txt

%files -n busybox-unzip -f filelist-unzip.txt

%files -n busybox-util-linux -f filelist-util-linux.txt -f filelist-util-linux-systemd.txt

%files -n busybox-vi -f filelist-vim.txt

%files -n busybox-vlan -f filelist-vlan.txt

%files -n busybox-wget -f filelist-wget.txt

%files -n busybox-which -f filelist-which.txt

%files -n busybox-whois -f filelist-whois.txt

%files -n busybox-xz -f filelist-xz.txt

%files -n busybox-sh -f filelist-sh.txt

%changelog
