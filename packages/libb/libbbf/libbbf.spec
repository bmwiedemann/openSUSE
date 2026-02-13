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


%define sover 3
Name:           libbbf
Version:        3.0.1
Release:        0
Summary:        Bound Book Format container for comics and manga
License:        MIT
URL:            https://github.com/ef1500/libbbf/
Source:         https://github.com/ef1500/libbbf/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         libbbf-3.0.1-cmake_install.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.20
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

%package -n %{name}%{sover}
Summary:        Bound Book Format container for comics and manga

%description -n %{name}%{sover}
Bound Book Format (.bbf) is a high-performance binary container designed
specifically for digital comic books and manga. Unlike CBR/CBZ, BBF is built
for DirectSotrage/mmap, easy integrity checks, and mixed-codec
containerization.

This package contains the shared library

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
Bound Book Format (.bbf) is a high-performance binary container designed
specifically for digital comic books and manga. Unlike CBR/CBZ, BBF is built
for DirectSotrage/mmap, easy integrity checks, and mixed-codec
containerization.

This package contains the files needed to build using %{name}.

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

%ldconfig_scriptlets -n %{name}%{sover}

%files
%license LICENSE
%{_bindir}/bbfmux

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/liblibbbf.so.%{sover}{,.*}
%{_libdir}/liblibbbf_shared.so.%{sover}{,.*}

%files devel
%license LICENSE
%{_libdir}/liblibbbf.so
%{_libdir}/liblibbbf_shared.so
%{_includedir}/libbbf.h

%changelog
