#
# spec file for package libsndfile-progs
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


Name:           libsndfile-progs
Version:        1.0.31
Release:        0
Summary:        Example Programs for libsndfile
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://libsndfile.github.io/libsndfile/
Source0:        https://github.com/libsndfile/libsndfile/releases/download/%{version}/libsndfile-%{version}.tar.bz2
Source1:        https://github.com/libsndfile/libsndfile/releases/download/%{version}/libsndfile-%{version}.tar.bz2.sig
Source2:        libsndfile.keyring
Patch34:        sndfile-deinterlace-channels-check.patch
# PATCH-FIX-OPENSUSE
Patch100:       sndfile-ocloexec.patch
BuildRequires:  alsa-devel
BuildRequires:  cmake
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  libjack-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel

%description
This package includes the example programs for libsndfile.

%prep
%setup -q -n libsndfile-%{version}
%patch34 -p1
%patch100 -p1

%build
%cmake -DENABLE_EXPERIMENTAL=ON -DBUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

# remove unnecessary files
rm -rf %{buildroot}%{_datadir}/doc/libsndfile
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_datadir}/doc/libsndfile1-dev

%files
%{_bindir}/*
%{_mandir}/man?/*

%changelog
