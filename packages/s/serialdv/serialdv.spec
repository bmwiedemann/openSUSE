#
# spec file for package serialdv
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


%define sover   1
%define libname libserialdv%{sover}
Name:           serialdv
Version:        1.1.5
Release:        0
Summary:        Library for audio de-/encoding with ABME3000 based devices
License:        GPL-3.0-only
URL:            https://github.com/f4exb/serialDV
#Git-Clone:     https://github.com/f4exb/serialDV.git
Source:         https://github.com/f4exb/serialDV/archive/v%{version}.tar.gz#/serialDV-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++

%description
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.

%package -n %{libname}
Summary:        Library for audio de-/encoding with ABME3000 based devices

%description -n %{libname}
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.

%package devel
Summary:        Development files for libserialdv
Requires:       %{libname} = %{version}

%description devel
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.

This subpackage contains libraries and header files for developing
applications that want to make use of libserialdv.

%prep
%autosetup -n serialDV-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE
%doc Readme.md
%{_libdir}/libserialdv.so.%{sover}*

%files devel
%{_bindir}/dvtest
%{_includedir}/serialdv/
%{_libdir}/libserialdv.so

%changelog
