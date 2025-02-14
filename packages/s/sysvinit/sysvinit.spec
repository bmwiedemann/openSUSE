#
# spec file for package sysvinit
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} >= 1550
%define sbindir %_sbindir
%define bindir %_bindir
%else
%define sbindir /sbin
%define bindir /bin
%endif

Name:           sysvinit
%define KPVER  2.23
%define SIVER  3.14
%define START  0.65
Version:        %{SIVER}
Release:        0
Summary:        SysV-Style init
License:        GPL-2.0-or-later
Group:          System/Base
BuildRequires:  blog-devel
BuildRequires:  po4a
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#!BuildIgnore:  sysvinit-tools
URL:            https://savannah.nongnu.org/projects/sysvinit/
Source0:        https://github.com/slicer69/sysvinit/releases/download/%{SIVER}/sysvinit-%{SIVER}.tar.xz
Source1:        https://github.com/bitstreamout/killproc/archive/v%{KPVER}.tar.gz#/killproc-%{KPVER}.tar.gz
Source2:        https://download.savannah.nongnu.org/releases/sysvinit/startpar-%{START}.tar.xz
Source3:        https://github.com/slicer69/sysvinit/releases/download/%{SIVER}/sysvinit-%{SIVER}.tar.xz.sig
Source4:        https://download.savannah.nongnu.org/releases/sysvinit/startpar-%{START}.tar.xz.sig
Source5:        %{name}.keyring
Patch0:         %{name}-2.90.dif
Patch2:         %{name}-2.88dsf-suse.patch
Patch9:         %{name}-2.90-no-kill.patch
Patch20:        killproc-2.23.dif
Patch50:        startpar-0.58.dif

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
Suggests:       %{name}-tools-doc
Requires:       blog

%description tools
Helper tools from sysvinit that support booting, including but not exclusive
to startpar and killproc. System V init specific programs are in the
sysvinit package.

%package tools-doc
Summary:        Documentation of tools for basic booting
Group:          Documentation/Other
Requires:       %{name}-tools
BuildArch:      noarch

%description tools-doc
Documentation of helper tools from sysvinit that support booting, including but not exclusive
to startpar and killproc.

%prep
ls -l
rm -rf killproc-%{KPVER}
rm -rf startpar-%{START} startpar
ln -sf startpar startpar-%{START}
%setup -n %{name}-%{SIVER} -q -b 1 -b 2
%patch -P 2  -p0 -b .suse
%patch -P 9  -p0 -b .no-kill
%patch -P 0  -b .p0
pushd doc
  mkdir killproc
popd
pushd ../killproc-%{KPVER}
%patch -P 20
ln -t../%{name}-%{SIVER}/doc/killproc README.md
popd
pushd ../startpar-%{START}
%patch -P 50
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
%if 0%{?suse_version} && %suse_version > 1500
# pidof is part of procps-ng; let's remove the symlinks to killproc5 here
rm -f %{buildroot}{/sbin,/bin,%{_mandir}/man8}/pidof{,.8}
%endif
%if 0%{?suse_version} >= 1550
# it's all hardcoded in Makefiles so move here
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}/bin/* %{buildroot}%{_bindir}
mv %{buildroot}/sbin/* %{buildroot}%{_sbindir}
%endif

%files tools
%defattr (-,root,root,755)
%license COPYING COPYRIGHT
%doc doc/Propaganda doc/Changelog doc/killproc
%{bindir}/usleep
%{bindir}/fsync
%{sbindir}/fstab-decode
%{sbindir}/checkproc
%{sbindir}/pidofproc
%{sbindir}/killproc
%{sbindir}/killall5
%{sbindir}/startproc
%{sbindir}/rvmtab
%{sbindir}/vhangup
%{sbindir}/mkill
%{sbindir}/start_daemon
%{_bindir}/startpar
%if 0%{?suse_version} && %suse_version <= 1500
%{bindir}/pidof
%{sbindir}/pidof
%doc %{_mandir}/man8/pidof.8%{?ext_man}
%endif

%files tools-doc
%doc %{_mandir}/man1/*.1%{?ext_man}
%doc %{_mandir}/man8/*.8%{?ext_man}
%doc %{_mandir}/*/man8/*.8%{?ext_man}

%changelog
