#
# spec file for package PlatformFolders
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2022 Fabio Pesari
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


Name:           PlatformFolders
Version:        4.2.0
Release:        0
Summary:        Library for cross-platform detection of special directories
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/sago007/PlatformFolders
Source0:        https://github.com/sago007/PlatformFolders/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
C++ library to look for directories like My Documents,
~/.config, etc. so that you do not need to write
platform-specific code.

%package devel
Summary:        Library for cross-platform detection of special directories (development files)
Requires:       %{name} = %{version}

%description devel
C++ library to look for directories like My Documents,
~/.config, etc. so that you do not need to write
platform-specific code.

These are Development files for the PlatformFolders library.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libplatform_folders.so

%files devel
%{_includedir}/*
%{_libdir}/cmake/platform_folders

%changelog
