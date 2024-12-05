#
# spec file for package ZArchive
#
# Copyright (c) 2024 SUSE LLC
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


%define libpackage libzarchive0_1
Name:           ZArchive
Version:        0.1.2+git20240721.b467f7a
Release:        0
Summary:        Library and program for creating and reading .zar files
License:        MIT-0
URL:            https://github.com/Exzap/ZArchive
Source0:        ZArchive-%{version}.tar.xz
BuildRequires:  cmake >= 3.15
%if 0%{?suse_version} < 1550
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++ >= 11
%endif
BuildRequires:  pkgconfig(libzstd)

%description
Program and library for handling ZArchive .zar files. ZArchive files are zstd-compressed file archives.

%package -n %{libpackage}
Summary:        ZArchive library

%description -n %{libpackage}
This subpackage contains the ZArchive library

%package devel
Summary:        Devel package for ZArchive
Requires:       %{libpackage} = %{version}

%description devel
This subpackage contains the devel files for ZArchive

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1550
export CXX=g++-13
%endif
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n  %{libpackage}

%files
%license LICENSE
%doc README.md
%{_bindir}/zarchive

%files -n %{libpackage}
%license LICENSE
%{_libdir}/libzarchive.so.0.1
%{_libdir}/libzarchive.so.0.1.3

%files devel
%license LICENSE
%{_libdir}/libzarchive.so
%{_libdir}/pkgconfig/zarchive.pc
%dir %{_includedir}/zarchive
%{_includedir}/zarchive/zarchivecommon.h
%{_includedir}/zarchive/zarchivereader.h
%{_includedir}/zarchive/zarchivewriter.h

%changelog
