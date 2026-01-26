#
# spec file for package libbbf
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           libbbf
Version:        1.1.0
Release:        0
Summary:        Bound Book Format container for comics and manga
License:        MIT
URL:            https://github.com/ef1500/libbbf/
Source:         https://github.com/ef1500/libbbf/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/ef1500/libbbf/pull/2/commits/010b08997edba655246ce6d10abdd581dbcf3ff4
Patch0:         libbbf-1.1.0-add_cmake.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.16
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxxhash)
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
Bound Book Format (.bbf) is a high-performance binary container designed
specifically for digital comic books and manga. Unlike CBR/CBZ, BBF is built
for DirectSotrage/mmap, easy integrity checks, and mixed-codec
containerization.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_bindir}/bbfmux

%changelog
