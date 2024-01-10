#
# spec file for package mpi-selector
#
# Copyright (c) 2022 SUSE LLC
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


%define old_datadir %{_localstatedir}
%define data_dir    %{_sysconfdir}

Name:           mpi-selector
URL:            http://www.openfabrics.org
Summary:        Tool to provide defaults for which MPI implementation to use
Version:        1.0.3
Release:        0
License:        BSD-3-Clause
Group:          System/Console
Source:         http://www.openfabrics.org/downloads/mpi-selector/%{name}-%{version}.tar.gz
Patch3:         mpi-selector-perl_path.patch
Patch4:         mpi-selector-no_bang_line.patch
Patch5:         reproducible.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%{perl_requires}

%description
A simple tool that allows system administrators to set a site-wide
default for which MPI implementation is to be used, but also allow
users to set their own defaults MPI implementation, thereby overriding
the site-wide default.

The default can be changed easily via the mpi-selector command --
editing of shell startup files is not required.

%prep
%autosetup -p1

%build
%configure --with-shell-startup-dir=/etc/profile.d --localstatedir=%{data_dir}
make

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{data_dir}/%{name}/data

%post
if [ $1 == 2 ]; then
    # During update, migrate file from older path if necessary
    if [ -d "%{old_datadir}/%{name}/data" ]; then
	mv -u %{old_datadir}/%{name}/data/* %{data_dir}/%{name}/data
	rm -Rf %{old_datadir}/%{name}/data/
    fi
fi

%files
%defattr(-, root, root, -)
%doc README
%license LICENSE
%{_bindir}/mpi-selector
%{_bindir}/mpi-selector-menu
%{_mandir}/man1/mpi-selector.*
%{_mandir}/man1/mpi-selector-menu.*
%config %attr(644,root,root) /etc/profile.d/*
%dir %{data_dir}/%{name}
%dir %{data_dir}/%{name}/data

%changelog
