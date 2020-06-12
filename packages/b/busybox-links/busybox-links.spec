#
# spec file for package busybox-links
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


Name:           busybox-links
Version:        %(rpm -q busybox --qf '%%{VERSION}')
Release:        0
Summary:        Links for busybox applets
License:        GPL-2.0-or-later
Source:         busybox-links-rpmlintrc
BuildRequires:  attr
BuildRequires:  bind-utils
BuildRequires:  busybox
BuildRequires:  bzip2
BuildRequires:  coreutils
BuildRequires:  cpio
BuildRequires:  diffutils
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  grep
BuildRequires:  gzip
BuildRequires:  hostname
BuildRequires:  iproute2
BuildRequires:  iputils
BuildRequires:  kbd
BuildRequires:  kmod
BuildRequires:  man
BuildRequires:  ncurses-utils
BuildRequires:  net-tools
BuildRequires:  net-tools-deprecated
BuildRequires:  patch
BuildRequires:  procps
BuildRequires:  psmisc
BuildRequires:  sed
BuildRequires:  sendmail
BuildRequires:  sharutils
BuildRequires:  tar
BuildRequires:  traceroute
BuildRequires:  util-linux
BuildRequires:  which
BuildRequires:  xz
Requires:       busybox = %{version}
Requires:       busybox-adduser = %{version}
Requires:       busybox-ash = %{version}
Requires:       busybox-attr = %{version}
Requires:       busybox-bind-utils = %{version}
Requires:       busybox-bzip2 = %{version}
Requires:       busybox-coreutils = %{version}
Requires:       busybox-cpio = %{version}
Requires:       busybox-diffutils = %{version}
Requires:       busybox-findutils = %{version}
Requires:       busybox-gawk = %{version}
Requires:       busybox-grep = %{version}
Requires:       busybox-gzip = %{version}
Requires:       busybox-hostname = %{version}
Requires:       busybox-iproute2 = %{version}
Requires:       busybox-iputils = %{version}
Requires:       busybox-kbd = %{version}
Requires:       busybox-man = %{version}
Requires:       busybox-misc = %{version}
Requires:       busybox-ncurses-utils = %{version}
Requires:       busybox-net-tools = %{version}
Requires:       busybox-patch = %{version}
Requires:       busybox-procps = %{version}
Requires:       busybox-psmisc = %{version}
Requires:       busybox-sed = %{version}
Requires:       busybox-sendmail = %{version}
Requires:       busybox-sh = %{version}
Requires:       busybox-sharutils = %{version}
Requires:       busybox-tar = %{version}
Requires:       busybox-traceroute = %{version}
Requires:       busybox-util-linux = %{version}
Requires:       busybox-which = %{version}
Requires:       busybox-xz = %{version}
BuildArch:      noarch

%description
This is a meta package requireing all packages providing busybox applets.

%package -n busybox-misc
Summary:        Busybox applets not fitting anywhere else
Requires:       busybox = %{version}
Conflicts:      bc
Conflicts:      binutils
Conflicts:      blog
Conflicts:      dos2unix
Conflicts:      dosfstools
Conflicts:      e2fsprogs
Conflicts:      ed
Conflicts:      less
Conflicts:      lsof
Conflicts:      lsscsi
Conflicts:      nbd
Conflicts:      netcat-openbsd
Conflicts:      sysvinit-tools
Conflicts:      telnet
Conflicts:      tftp
Conflicts:      time
Conflicts:      tunctl
Conflicts:      unzip
Conflicts:      usbutils
Conflicts:      util-linux-systemd
Conflicts:      vim
Conflicts:      vlan
Conflicts:      wget
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

%package -n busybox-ash
Summary:        Busybox ash
Requires:       busybox = %{version}

%description -n busybox-ash
This package contains the busybox ash

%package -n busybox-sh
Summary:        Busybox sh
Requires:       busybox = %{version}
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n busybox-sh
This package contains the busybox sh.

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
Conflicts:      iproute2

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

%package -n busybox-sharutils
Summary:        Busybox applets replacing sharutils
Requires:       busybox = %{version}
Conflicts:      sharutils

%description -n busybox-sharutils
This package contains the symlinks to replace sharutils with busybox.

%package -n busybox-hostname
Summary:        Busybox applets replacing hostname
Requires:       busybox = %{version}
Conflicts:      hostname

%description -n busybox-hostname
This package contains the symlinks to replace hostname with busybox.

%package -n busybox-man
Summary:        Busybox applets replacing man
Requires:       busybox = %{version}
Conflicts:      mandoc
Conflicts:      man

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
Conflicts:      sendmail
Conflicts:      postfix
Conflicts:      exim
Conflicts:      msmtp-mta

%description -n busybox-sendmail
This package contains the symlinks to replace sendmail with busybox.

%package -n busybox-adduser
Summary:        Busybox applets containing adduser and some shadow tools
Requires:       busybox = %{version}
Conflicts:      shadow

%description -n busybox-adduser
This package contains the symlinks for adduser and some tools from the
shadow suite.


%prep
%setup -q -c -T

%build
mkdir apps
mkdir used
mkdir missing
for i in `cat %{_datadir}/busybox/busybox.links` ; do touch apps/`basename $i`; done
# No rpm/rpm2cpio, will break build service
rm apps/rpm apps/rpm2cpio
# No /linuxrc
rm -f apps/linuxrc
# Does not really fit
rm apps/[[
for package in coreutils diffutils findutils grep util-linux iputils iproute2 gzip sed cpio procps xz bzip2 psmisc kbd sharutils hostname net-tools net-tools-deprecated traceroute ncurses-utils kmod tar gawk patch attr which bind-utils man sendmail shadow; do
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
echo -e "%{_bindir}/ash" > filelist-ash.txt
touch used/ash
echo -e "/usr/bin/sh\n/bin/sh" > filelist-sh.txt
touch used/sh
echo -e "/sbin/loadkmap\n/usr/sbin/loadfont" >> filelist-kbd.txt
touch used/loadkmap used/loadfont

echo -e "/usr/sbin/addgroup\n/usr/sbin/adduser\n/usr/sbin/delgroup\n/usr/sbin/deluser" >> filelist-shadow.txt
touch used/addgroup used/adduser used/delgroup used/deluser

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
# sh needs to be handled by update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
#ln -sf %{_bindir}/busybox %{buildroot}%{_sysconfdir}/alternatives/sh
ln -sf %{_sysconfdir}/alternatives/sh %{buildroot}%{_bindir}/sh
ln -sf %{_bindir}/sh   %{buildroot}/bin/sh

%post -n busybox-ash -p /usr/bin/ash
%{_sbindir}/update-alternatives --quiet --force \
        --install %{_bindir}/sh sh %{_bindir}/busybox 10000

%preun -n busybox-ash -p /usr/bin/ash
if test "$1" = 0; then
        %{_sbindir}/update-alternatives --quiet --remove sh %{_bindir}/busybox
fi

%files

%files -n busybox-adduser -f filelist-shadow.txt
%files -n busybox-ash -f filelist-ash.txt
%files -n busybox-attr -f filelist-attr.txt
%files -n busybox-bind-utils -f filelist-bind-utils.txt
%files -n busybox-bzip2 -f filelist-bzip2.txt
%files -n busybox-coreutils -f filelist-coreutils.txt
%files -n busybox-cpio -f filelist-cpio.txt
%files -n busybox-diffutils -f filelist-diffutils.txt
%files -n busybox-findutils -f filelist-findutils.txt
%files -n busybox-gawk -f filelist-gawk.txt
%files -n busybox-grep -f filelist-grep.txt
%files -n busybox-gzip -f filelist-gzip.txt
%files -n busybox-hostname -f filelist-hostname.txt
%files -n busybox-iproute2 -f filelist-iproute2.txt
%files -n busybox-iputils -f filelist-iputils.txt
%files -n busybox-kbd -f filelist-kbd.txt
%files -n busybox-kmod -f filelist-kmod.txt
%files -n busybox-man -f filelist-man.txt
%files -n busybox-misc -f filelist-misc.txt
%files -n busybox-ncurses-utils -f filelist-ncurses-utils.txt
%files -n busybox-net-tools -f filelist-net-tools.txt
%files -n busybox-patch -f filelist-patch.txt
%files -n busybox-procps -f filelist-procps.txt
%files -n busybox-psmisc -f filelist-psmisc.txt
%files -n busybox-sed -f filelist-sed.txt
%files -n busybox-sendmail -f filelist-sendmail.txt
%files -n busybox-sh -f filelist-sh.txt
%ghost %config %{_sysconfdir}/alternatives/sh

%files -n busybox-sharutils -f filelist-sharutils.txt
%files -n busybox-tar -f filelist-tar.txt
%files -n busybox-traceroute -f filelist-traceroute.txt
%files -n busybox-util-linux -f filelist-util-linux.txt
%files -n busybox-which -f filelist-which.txt
%files -n busybox-xz -f filelist-xz.txt

%changelog
