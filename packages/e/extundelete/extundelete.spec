#
# spec file for package extundelete
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           extundelete
Version:        0.2.4
Release:        0
Summary:        Recovery tool for ext4 and ext3 filesystems
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            http://extundelete.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM fix_ftbfs.patch asterios.dramis@gmail.com -- Fix FTBFS with new e2fsprogs (patch taken from Debian)
Patch0:         fix_ftbfs.patch
# Kept for compatibility reasons
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libext2fs-devel
BuildRequires:  libstdc++-devel

%description
extundelete is a utility that can recover deleted files from an ext3 or ext4
partition. extundelete uses the information stored in the partition's journal
to attempt to recover a file that has been deleted from the partition. There is
no guarantee that any particular file will be able to be undeleted, so always
try to have a good backup system in place, or at least put one in place after
recovering your files!

%prep
%setup -q
%patch0 -p1

%build
# Be verbose
sed -i "s/^silent=yes/silent=no/" configure
%configure
# Be verbose
sed -i "s/^AM_MAKEFLAGS = -s/AM_MAKEFLAGS = /" Makefile
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README
%{_bindir}/extundelete

%changelog
