#
# spec file for package nmtree
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2020 Archie L. Cobbs <archie@dellroad.org>
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

Name:           nmtree
Version:        1.0.0
Release:        0
Summary:        Utility for mapping directory hierarchies
License:        BSD-3-Clause
Group:          Productivity/File utilities
Url:            https://github.com/archiecobbs/%{name}
Source:         https://github.com/archiecobbs/%{name}/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libnbcompat-devel
BuildRequires:  make

%description
The mtree utility compares the file hierarchy rooted in the current
directory against a specification read from the standard input. Messages
are written to the standard output for any files whose characteristics do
not match the specification, or which are missing from either the file
hierarchy or the specification.

This is a port of the NetBSD version of mtree.

%prep
%setup -q

%build
autoreconf -vfi -I .
%configure --program-prefix=n
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}%{_datadir}/doc/packages/{,n}mtree

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man5/%{name}.5.gz
%attr(0644,root,root) %{_mandir}/man8/%{name}.8.gz
%defattr(0644,root,root,0755)
%doc %{_datadir}/doc/packages/%{name}

%changelog
