#
# spec file for package xdiskusage
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xdiskusage
Version:        1.54
Release:        0
Summary:        Graphically displays the amount of disk space used by each subdirectory
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            http://xdiskusage.sourceforge.net/
Source:         http://xdiskusage.sourceforge.net/xdiskusage-%{version}.tgz
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  mesa-libGL-devel
%endif

%description
xdiskusage is a user-friendly program to show you what is using
up all your disk space. It is based on the design of xdu
written by Phillip C. Dykstra. Changes have been made so it runs
"du" for you, and can display the free space left on the disk,
and produce a PostScript version of the display.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
%configure
%make_build CXXFLAGS="%{optflags}"

%install
install -D -c xdiskusage %{buildroot}/%{_bindir}/xdiskusage
install -D -c -m0644 xdiskusage.1 %{buildroot}/%{_mandir}/man1/xdiskusage.1

%files
%doc README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
