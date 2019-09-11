#
# spec file for package mpi-selector
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mpi-selector
Url:            http://www.openfabrics.org
Summary:        Tool to provide defaults for which MPI implementation to use
Version:        1.0.3
Release:        0
License:        BSD-3-Clause
Group:          System/Console
Source:         http://www.openfabrics.org/downloads/mpi-selector/%{name}-%{version}.tar.gz
Patch3:         mpi-selector-perl_path.patch
Patch4:         mpi-selector-no_bang_line.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake autoconf libtool
%{perl_requires}

%description
A simple tool that allows system administrators to set a site-wide
default for which MPI implementation is to be used, but also allow
users to set their own defaults MPI implementation, thereby overriding
the site-wide default.

The default can be changed easily via the mpi-selector command --
editing of shell startup files is not required.

%prep
%setup -q 
%patch3
%patch4

%build
%configure --with-shell-startup-dir=/etc/profile.d
make

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-, root, root, -)
%doc README LICENSE
%{_bindir}/mpi-selector
%{_bindir}/mpi-selector-menu
%{_mandir}/man1/mpi-selector.*
%{_mandir}/man1/mpi-selector-menu.*
%config %attr(644,root,root) /etc/profile.d/*

%changelog
