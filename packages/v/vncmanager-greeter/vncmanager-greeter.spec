#
# spec file for package vncmanager-greeter
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           vncmanager-greeter
Version:        1.0.0
Release:        0
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libQt5Core-devel libQt5Widgets-devel

Url:            https://github.com/michalsrb/vncmanager-greeter
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Greeter for VNC session manager
License:        MIT
Group:          System/X11/Utilities
Source:         vncmanager-greeter-%{version}.tar.gz

%description
This is graphical greeter that appears when VNC client connects to VNC manager.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_VERBOSE_MAKEFILE=ON
make %{?_smp_mflags}

%install
%cmake_install

%files
%defattr(-,root,root)
%{_bindir}/vncmanager-greeter
%doc LICENSE

%changelog
