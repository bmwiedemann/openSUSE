#
# spec file for package kdumpid
#
# Copyright (c) 2024 SUSE LLC
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


# Begin compatibility cruft
#

%if 0%{!?have_zstd:1}
%if 0%{?sle_version} >= 152000
%define have_zstd 1
%else
%define have_zstd 0
%endif
%endif

#
# End compatibility cruft

#Url:

Name:           kdumpid
BuildRequires:  binutils-devel
BuildRequires:  libkdumpfile-devel
BuildRequires:  zlib-devel
Version:        1.6
Release:        0
Summary:        Utility to extract information from vmcores
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            http://sourceforge.net/p/kdumpid
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2

%description
Kdumpid extracts information such as type of dump, architecture
and kernel version from raw vmcores (Kernel memory dumps).

%prep
%setup
%autopatch -p1

chmod +x libs.sh

%build
make CUSTOM_CFLAGS="${CFLAGS:-%optflags}"

%install
export BINDIR=%{_bindir}
export MANDIR=%{_mandir}
%{?make_install} %{!?make_install:make install DESTDIR=$RPM_BUILD_ROOT}

%files
%defattr (-, root, root)
%{_bindir}/*
%{_mandir}/man1/*

%changelog
