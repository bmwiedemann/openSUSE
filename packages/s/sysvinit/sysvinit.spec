#
# spec file for package sysvinit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sysvinit
%define KPVER  2.23
%define SCVER  1.20
%define SIVER  2.96
%define START  0.63
Version:        %{SIVER}
Release:        0
Summary:        SysV-Style init
License:        GPL-2.0-or-later
Group:          System/Base
BuildRequires:  blog-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#!BuildIgnore:  sysvinit-tools
Url:            https://savannah.nongnu.org/projects/sysvinit/
Source:         sysvinit-%{SIVER}.tar.xz
Source1:        https://github.com/bitstreamout/killproc/archive/v%{KPVER}.tar.gz#/killproc-%{KPVER}.tar.gz
Source2:        startpar-%{START}.tar.xz
Patch:          %{name}-2.90.dif
Patch2:         %{name}-2.88dsf-suse.patch
Patch9:         %{name}-2.90-no-kill.patch
Patch50:        startpar-0.58.dif
Patch51:        startpar-sysmacros.patch

%description
System V style init programs by Miquel van Smoorenburg that control the
booting and shutdown of your system. These support a number of system
runlevels, each one associated with a specific set of utilities. For
example, the normal system runlevel is 3, which starts a getty on
virtual consoles tty1-tty6. Runlevel 5 starts xdm. Runlevel 0 shuts
down the system. See the individual man pages for inittab, initscript,
halt, init, powerd, reboot, runlevel, shutdown, and telinit for 
more information.

%package tools
Summary:        Tools for basic booting
Group:          System/Base
Requires:       blog

%description tools
Helper tools from sysvinit that support booting, including but not exclusive
to startpar, killproc and pidof. System V init specific programs are in the 
sysvinit package.

%prep
ls -l
rm -rf killproc-%{KPVER}
rm -rf startpar-%{START} startpar
ln -sf startpar startpar-%{START}
%setup -n %{name}-%{SIVER} -q -b 1 -b 2
%patch2  -p0 -b .suse
%patch9  -p0 -b .no-kill
%patch
pushd doc
  mkdir killproc
popd
pushd ../killproc-%{KPVER}
ln -t../%{name}-%{SIVER}/doc/killproc README.md
popd
pushd ../startpar-%{START}
%patch50
%patch51 -p1
popd
%_fixowner .
%_fixgroup .
/bin/chmod -Rf a+rX,g-w,o-w .

%build
  RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -std=gnu89 -D_FILE_OFFSET_BITS=64 -pipe"
  CC=%__cc
  export RPM_OPT_FLAGS CC
  make %{?_smp_mflags} WITH_SELINUX=yes DISTRO=SuSE
pushd ../killproc-%{KPVER}
  make %{?_smp_mflags} CC="%__cc"
popd
pushd ../startpar-%{START}
  make %{?_smp_mflags} CC="%__cc"
popd

%install
  make install -C src MANPATH=%{_mandir} ROOT=%{buildroot} DISTRO=SuSE
pushd ../killproc-%{KPVER}
  make install MANPATH=%{_mandir} INSTBINFLAGS="-m 0755" DESTDIR=%{buildroot}
popd
pushd ../startpar-%{START}
  make install DESTDIR=%{buildroot}
popd
#
# Remove files not packed:
#
  rm -vf %{buildroot}/usr/include/initreq.h

%files tools
%defattr (-,root,root,755)
%license COPYING COPYRIGHT
%doc doc/Propaganda doc/Changelog doc/killproc
/bin/pidof
/bin/usleep
/bin/fsync
/bin/startpar
/sbin/fstab-decode
/sbin/checkproc
/sbin/pidofproc
/sbin/killproc
/sbin/killall5
/sbin/pidof
/sbin/startproc
/sbin/rvmtab
/sbin/vhangup
/sbin/mkill
/sbin/start_daemon
%doc %{_mandir}/man1/usleep.1.gz
%doc %{_mandir}/man1/fsync.1.gz
%doc %{_mandir}/man1/startpar.1.gz
%doc %{_mandir}/man8/fstab-decode.8.gz
%doc %{_mandir}/man8/checkproc.8.gz
%doc %{_mandir}/man8/pidofproc.8.gz
%doc %{_mandir}/man8/killall5.8.gz
%doc %{_mandir}/man8/killproc.8.gz
%doc %{_mandir}/man8/pidof.8.gz
%doc %{_mandir}/man8/startproc.8.gz
%doc %{_mandir}/man8/start_daemon.8.gz
%doc %{_mandir}/man8/rvmtab.8.gz
%doc %{_mandir}/man8/vhangup.8.gz
%doc %{_mandir}/man8/mkill.8.gz

%changelog
