#
# spec file for package bloaty
#
# Copyright (c) 2020 SUSE LLC
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


Name:           bloaty
Version:        1.1
Release:        0
Summary:        Bloaty McBloatface: a size profiler for binaries
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/google/bloaty
Source:         https://github.com/google/bloaty/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)

%description
Bloaty McBloatface will show you a size profile of ELF or Mach-O
binaries so you can understand what is taking up space inside.

%prep
%autosetup -p1

%build
# CMakeLists.txt relies on libbloaty being a static lib (broken link deps).
# We don't need libbloaty anywhere else though so it's fine.
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DBLOATY_ENABLE_CMAKETARGETS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/bloaty

%changelog
