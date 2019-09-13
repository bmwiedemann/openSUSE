#
# spec file for package elementary-cmake-modules
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           elementary-cmake-modules
Summary:        Elementary CMake modules
License:        GPL-3.0
Group:          Development/Tools/Other
Url:            https://code.launchpad.net/~elementary-os/+junk/cmake-modules
Version:        0.1.0.bzr.25
Release:        0
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
CMake modules shared in Elementary projects.

%prep
%setup -q

%build
%cmake
make

%install
%cmake_install

%files
%defattr(-,root,root,-)
%doc README README.Vala.rst
%{_datadir}/cmake/Modules/*

%changelog

