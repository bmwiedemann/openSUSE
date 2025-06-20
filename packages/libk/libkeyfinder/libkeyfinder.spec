#
# spec file for package libkeyfinder
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

%define SOVERSION 2

Name:           libkeyfinder
Version:        2.2.7
Release:        0
Summary:        Library for estimating the musical key of digital audio
License:        GPL-3.0-or-later
URL:            https://mixxxdj.github.io/libkeyfinder/
Source0:        https://github.com/mixxxdj/libkeyfinder/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  fftw3-devel
BuildRequires:  cmake
%if 0%{?sle_version} == 150400 && 0%{?is_opensuse}
BuildRequires:  Catch2-devel
%else
BuildRequires:  Catch2-2-devel
%endif

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
%setup -q

chmod -x README.md

%build
%cmake
%cmake_build
%install

%cmake_install

%post -n %{name}%{SOVERSION} -p /sbin/ldconfig
%postun -n %{name}%{SOVERSION} -p /sbin/ldconfig

%files -n %{name}%{SOVERSION}
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
%{_libdir}/*.so

%changelog
