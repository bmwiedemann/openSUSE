#
# spec file for package mtree
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010 Archie L. Cobbs.
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


Name:           mtree
Version:        1.0.4
Release:        0
Summary:        Tool for creating and verifying file hierarchies
License:        BSD-3-Clause
Group:          Productivity/File utilities
URL:            https://github.com/archiecobbs/mtree-port
Source:         https://github.com/archiecobbs/mtree-port/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libopenssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The %{name} utility compares the file hierarchy rooted in the current
directory against a specification read from the standard input. Messages
are written to the standard output for any files whose characteristics do
not match the specifications, or which are missing from either the file
hierarchy or the specification.

Note: This is an older FreeBSD version of mtree; a newer NetBSD version
is also available in the package "nmtree".

%prep
%setup -q -n mtree-port-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR='%{buildroot}'
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_docdir}/%{name}

%changelog
