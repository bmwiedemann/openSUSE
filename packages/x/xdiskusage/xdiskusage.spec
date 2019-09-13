#
# spec file for package xdiskusage
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xdiskusage
Version:        1.51
Release:        0
Summary:        Graphically displays the amount of disk space used by each subdirectory
License:        GPL-2.0
Group:          Applications/System
Url:            http://xdiskusage.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
make %{?_smp_mflags} CXXFLAGS="%optflags"

%install
%{__install} -D -c xdiskusage %{buildroot}/%{_bindir}/xdiskusage
%{__install} -D -c -m0644 xdiskusage.1 %{buildroot}/%{_mandir}/man1/xdiskusage.1

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
