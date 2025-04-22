#
# spec file for package fuse-zip
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


Name:           fuse-zip
Version:        0.7.2+git.1733961742.3715770
Release:        0
Summary:        File System to Navigate, Extract, Create and Modify ZIP Archives
License:        GPL-3.0-or-later
Group:          System/Filesystems
URL:            https://bitbucket.org/agalanin/fuse-zip
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libzip) >= 0.11.2
BuildRequires:  pkgconfig(zlib)
BuildRequires:  tcl >= 8.6
BuildRequires:  tclx >= 8.4
# BuildRequires:  blt30 UNAVAILABLE IN OPENSUSE
BuildRequires:  tcllib
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  fuse

Requires:       fuse

%description
With fuse-zip you really can work with ZIP archives as real directories.
Unlike KIO or Gnome VFS, it can be used in any application without
modifications.
Unlike other FUSE filesystems, only fuse-zip provides write support to
ZIP archives. Also, fuse-zip is faster that all known implementations on
large archives with many files.

%prep
%setup -q

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
%make_install prefix=%{_prefix} DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/%{name}/

%check
make %{?_smp_mflags} CXXFLAGS="%{optflags}" -C tests/whitebox test

%files
%license LICENSE
%doc changelog README.md
%{_bindir}/%{name}
%{_mandir}/man?/*

%changelog
