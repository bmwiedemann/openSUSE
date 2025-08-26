#
# spec file for package libkeyfinder
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define SOVERSION 2
Name:           libkeyfinder
Version:        2.2.8
Release:        0
Summary:        Library for estimating the musical key of digital audio
License:        GPL-3.0-or-later
URL:            https://mixxxdj.github.io/libkeyfinder/
Source0:        https://github.com/mixxxdj/libkeyfinder/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(Catch2) >= 3.0.0
BuildRequires:  pkgconfig(fftw3)

%description
libkeyfinder is a small C++11 library for estimating the musical key of digital audio.

%package        -n %{name}%{SOVERSION}
Summary:        Library for estimating the musical key of digital audio
Provides:       %{name}

%description    -n %{name}%{SOVERSION}
libkeyfinder is a small C++11 library for estimating the musical key of digital audio

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{SOVERSION} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
chmod -x README.md

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ifnarch %ix86
%ctest
%endif

%ldconfig_scriptlets -n %{name}%{SOVERSION}

%files -n %{name}%{SOVERSION}
%license LICENSE
%doc README.md
%{_libdir}/*.so.%{SOVERSION}{,.*}

%files devel
%license LICENSE
%{_includedir}/keyfinder
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/KeyFinder
%{_libdir}/*.so

%changelog
