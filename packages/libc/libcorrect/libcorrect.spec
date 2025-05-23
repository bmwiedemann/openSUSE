#
# spec file for package libcorrect
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2018-2021, Martin Hauke <mardnh@gmx.de>
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


%define sover   0_0_0
Name:           libcorrect
Version:        20181010
Release:        0
Summary:        C library for Convolutional codes and Reed-Solomon
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/quiet/libcorrect
Source:         %{name}-%{version}.tar.xz
Patch0:         libcorrect-cmake-libsuffix.diff
Patch1:         libcorrect-cmake-set-soversion.diff
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

%package -n libcorrect%{sover}
Summary:        C library for Convolutional codes and Reed-Solomon
Group:          System/Libraries

%description -n libcorrect%{sover}
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

libcorrect accomplishes this task with two algorithms, Convolutional codes
and Reed-Solomon. Convolutional codes are robust to a constant background
noise, while Reed-Solomon error correction is effective at dealing with
noise that occurs in bursts. These algorithms have played an important role
in telecommunications. libcorrect uses a Viterbi algorithm decoder to decode
convolutional codes.

%package devel
Summary:        Development files for libcorrect
Group:          Development/Libraries/C and C++
Requires:       libcorrect%{sover} = %{version}

%description devel
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

This subpackage contains libraries and header files for developing
applications that want to make use of libcorrect.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# creates support file for pkg-config
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/libcorrect.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name:           libcorrect
Description: C library for Convolutional codes and Reed-Solomon
Version:        %{version}
Libs: -lcorrect
Cflags: -I${_includedir}/
EOF

%check
%ctest

%ldconfig_scriptlets -n libcorrect%{sover}

%files -n libcorrect%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libcorrect.so.0*

%files devel
%license LICENSE
%{_includedir}/correct*.h
%{_libdir}/libcorrect.so
%{_libdir}/pkgconfig/libcorrect.pc

%changelog
