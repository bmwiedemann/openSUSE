#
# spec file for package ext3grep
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ext3grep
Version:        0.10.2
Release:        0
Summary:        A tool to possibly recover deleted content on ext3 file systems
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            http://code.google.com/p/ext3grep/
Source:         %{name}-%{version}.tar.bz2
Source1:        Readme.SuSE
Patch0:         e2fsprogs-1.42.patch
# PATCH-FIX-UPSTREAM ext3grep-0.10.2-rename-i_dir_acl.patch -- Fix FTBFS (boo#1115054)
Patch1:         ext3grep-0.10.2-rename-i_dir_acl.patch
BuildRequires:  gcc-c++
BuildRequires:  libext2fs-devel
ExcludeArch:    ppc ppc64 s390 s390x

%description
A tool to investigate an ext3 file system for deleted content and possibly recover it.

Also see http://www.xs4all.nl/~carlo17/howto/undelete_ext3.html

%prep
%autosetup -p1
cp %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install

%files
%doc NEWS README Readme.SuSE
%license LICENSE.GPL2
%{_bindir}/ext3grep

%changelog
