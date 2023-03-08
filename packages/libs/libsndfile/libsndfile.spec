#
# spec file for package libsndfile
#
# Copyright (c) 2023 SUSE LLC
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


%define lname	%{name}1
Name:           libsndfile
Version:        1.2.0
Release:        0
Summary:        Development/Libraries/C and C++
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://libsndfile.github.io/libsndfile/
Source0:        https://github.com/libsndfile/libsndfile/releases/download/%{version}/libsndfile-%{version}.tar.xz
Source1:        https://github.com/libsndfile/libsndfile/releases/download/%{version}/libsndfile-%{version}.tar.xz.asc
Source2:        libsndfile.keyring
Source3:        baselibs.conf
# PATCH-FIX-OPENSUSE
Patch100:       sndfile-ocloexec.patch
BuildRequires:  cmake
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  libopus-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  speex-devel
Obsoletes:      libsnd
Provides:       libsnd

%description
Libsndfile is a C library for reading and writing sound files, such as
AIFF, AU, and WAV files, through one standard interface.  It can
currently read and write 8, 16, 24, and 32-bit PCM files as well as
32-bit floating point WAV files and a number of compressed formats.

%package -n %{lname}
Summary:        A Library to Handle Various Audio File Formats
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= 1.0.25

%description -n %{lname}
Libsndfile is a C library for reading and writing sound files, such
as AIFF, AU, and WAV files, through one standard interface. It can
currently read and write 8, 16, 24, and 32-bit PCM files as well as
32-bit floating point WAV files and a number of compressed formats.

%package devel
Summary:        Development package for the libsndfile library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Requires:       libstdc++-devel
Obsoletes:      libsndd
Provides:       libsndd

%description devel
This package contains the files needed to compile programs that use the
libsndfile library.

%prep
%autosetup -p1

%build
%cmake -DENABLE_EXPERIMENTAL=ON -DBUILD_EXAMPLES=OFF -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/libsndfile
%cmake_build

%install
%cmake_install

# remove programs; built in another spec file
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_mandir}/man1
rm -rf %{buildroot}%{_datadir}/doc/libsndfile

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%check
# ctest fails?!

%files -n %{lname}
%{_libdir}/libsndfile.so.1*

%files devel
%doc AUTHORS CHANGELOG.md README
%license COPYING
%{_libdir}/libsndfile.so
%{_includedir}/sndfile.h
%{_includedir}/sndfile.hh
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/SndFile
%doc examples
%doc %{_defaultdocdir}/libsndfile

%changelog
