#
# spec file for package grommunio-index
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


Name:           grommunio-index
Version:        0.1.16.e01e06c
Release:        0
Summary:        Generator for grommunio-web search indexes
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://grommunio.com/
Source:         %name-%version.tar.xz
BuildRequires:  cmake
%if 0%{?suse_version} && 0%{?suse_version} < 1550
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libexmdbpp-devel >= 1.8.0
BuildRequires:  libexmdbpp0 >= 1.8.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
Requires:       libexmdbpp0 >= 1.8.0
%define services grommunio-index.service grommunio-index.timer

%description
A C++17 program for the generation of grommunio-web fulltext search indexes.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1550
%cmake -DCMAKE_CXX_COMPILER=%_bindir/g++-11
%else
%if 0%{?centos_version} == 800
echo '#!/bin/sh -ex' >cxx
echo 'exec g++ "$@" -lstdc++fs' >>cxx
ls -al cxx
chmod a+x cxx
export CXX="$PWD/cxx"
%cmake
%else
%cmake
%endif
%endif
%cmake_build

%install
%if 0%{?centos_version} == 800
export CXX="$PWD/cxx"
%endif
%cmake_install
mkdir -p "%buildroot/%_datadir/%name"

%pre
%service_add_pre %services

%post
%service_add_post %services
if test -x /bin/systemctl; then
	systemctl enable --now grommunio-index.timer || :
fi

%preun
%service_del_preun %services

%postun
%service_del_postun %services

%files
%_bindir/grommunio-index*
%_sbindir/grommunio-index*
%_datadir/%name/
%_unitdir/*
%license LICENSE.txt

%changelog
