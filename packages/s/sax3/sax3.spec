#
# spec file for package sax3
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


Name:           sax3
Version:        0.1.2
Release:        0
Summary:        A Graphical Configuration Tool for X
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://www.ohloh.net/p/sax3
Source:         %{name}-%{version}.tar.gz
#               https://github.com/openSUSE/%{name}/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM sax3-gcc6.patch
Patch0:         sax3-gcc6.patch
BuildRequires:  augeas-devel
BuildRequires:  augeas-lenses
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  libyui-devel
Requires:       augeas
Requires:       augeas-lenses
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A graphical utility for configuring X server settings. It can run without X with a graphical interface.

Authors:
_______
Manu Gupta
Michal Hrusecky

%prep
%autosetup -p1

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_SKIP_RPATH=true \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
    -DCMAKE_VERBOSE_MAKEFILE=true \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
%if "%{_lib}" == "lib64"
    -DLIB_SUFFIX="64" \
%endif
    .
make

%install
%make_install
echo '' > lenses
for i in desktop.aug xorg.aug; do
if [ \! -f %{_datadir}/augeas/lenses/dist/$i ]; then
mkdir -p %buildroot/%{_datadir}/augeas/lenses/dist
install -m 0644 src/lens/$i %buildroot/%{_datadir}/augeas/lenses/dist
echo %{_datadir}/augeas > lenses
fi
done

%files -f lenses
%defattr(-,root,root)
%doc COPYING.GPL-3.0
%{_sbindir}/sax3*
%{_datadir}/sax3
%{_libdir}/libsax3-yuif.so
%{_datadir}/applications/sax3.desktop
%{_datadir}/icons/*
%_mandir/man1/*

%changelog
