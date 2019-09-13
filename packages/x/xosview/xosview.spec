#
# spec file for package xosview
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _appdefdir  %{_datadir}/X11/app-defaults
Name:           xosview
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
# NOTE: We don't want this dependency and desktop-data-SuSE is in all
# desktop selections.
#Requires:    desktop-data-SuSE
# /usr/bin/xrdb
Requires:       xrdb
Version:        1.21
Release:        0
Summary:        System Load Information
License:        GPL-2.0-or-later
Group:          System/Monitoring
Url:            https://github.com/hills/%{name}
Source:         https://github.com/hills/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        rc.config.xosview
Source2:        xosview.png
Source3:        xosview.desktop
Source4:        xosview.sh
Source5:        xosview-rpmlintrc
Patch0:         xosview-1.19.dif
Patch10:        xosview-1.19-appdef.patch
Patch11:        xosview-1.16-diskstat.patch
# NOTE: We don't want this dependency and desktop-data-SuSE is in all
# desktop selections.
#Requires:    desktop-data-SuSE
# /usr/bin/xrdb
Requires:       xrdb
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A small program which is mostly configurable using resources via
~/.Xresources. It shows actual CPU, swap, memory, active interrupts,
and, if desired, netpacket statistics in a graphical manner.

%prep
%setup -q
%patch10  -b .appdef
%patch11  -b .diskstat
%patch0   -b .p0

%build
  OPTFLAGS="%{optflags}"
export OPTFLAGS
case "%{optflags}" in
*-fno-const-strings*) ;;
*)
    if $CXX $OPTFLAGS -fno-const-strings -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	OPTFLAGS="$OPTFLAGS -fno-const-strings"
    fi
esac
make %{?_smp_mflags} clean
make %{?_smp_mflags} PLATFORM=linux OPTFLAGS="$OPTFLAGS" PREFIX=%{_prefix} USE_SYSCALLS=1

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_appdefdir}
mkdir -p %{buildroot}%{_docdir}/xosview
make PREFIX=%{_prefix} \
     MANDIR=%{_mandir} \
     XAPPLOADDIR=%{_appdefdir} \
     USE_SYSCALLS=1 \
     DESTDIR=%{buildroot} \
     install
install -m 0444 Xdefaults         %{buildroot}%{_appdefdir}/XOsview
install -m 0444 README            %{buildroot}%{_docdir}/xosview/
install -m 0444 README.linux      %{buildroot}%{_docdir}/xosview/
mv %{buildroot}%{_bindir}/xosview %{buildroot}%{_bindir}/xosview.bin
sed 's|@@BINDIR@@|%{_bindir}|' < %{SOURCE4} > %{buildroot}%{_bindir}/xosview
chmod 0755 %{buildroot}%{_bindir}/xosview
chmod 0755 %{buildroot}%{_bindir}/xosview.bin
mkdir -p   %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/applications

%files
%defattr(-,root,root)
%{_datadir}/pixmaps/xosview.png
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%{_datadir}/icons/hicolor/32x32/apps/xosview.png
%{_datadir}/applications/xosview.desktop
%{_bindir}/xosview
%{_bindir}/xosview.bin
%dir %{_appdefdir}
%config %{_appdefdir}/XOsview
%{_mandir}/man1/xosview.1%{ext_man}
%dir %{_docdir}/xosview/
%doc %{_docdir}/xosview/README
%doc %{_docdir}/xosview/README.linux

%changelog
