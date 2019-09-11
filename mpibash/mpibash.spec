#
# spec file for package mpibash
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%ifarch ppc64
%define mpi_implem openmpi
%else
%define mpi_implem openmpi2
%endif

Name:           mpibash
Version:        1.3
Release:        0
Summary:        Parallel scripting right from the Bourne-Again Shell
License:        GPL-3.0+
Group:          Productivity/Networking/Other
Url:            https://github.com/lanl/MPI-Bash
Source0:        https://github.com/lanl/MPI-Bash/releases/download/v%{version}/mpibash-%{version}.tar.gz
BuildRequires:  bash-devel >= 4.4
BuildRequires:  %{mpi_implem}
BuildRequires:  %{mpi_implem}-devel
BuildRequires:  libcircle-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MPI-Bash makes it possible to parallelize Bash scripts which run a set of
Linux commands independently over a large number of input files.
Because MPI-Bash includes various MPI functions for data transfer and
synchronization, it is not limited to parallel workloads
but can incorporate phased operations (i.e. all workers must finish
operation X before any worker is allowed to begin operation Y).

%package examples
Summary:        Example Scripts for %{name}
Group:          Productivity/Scientific/Chemistry
Requires:       %{name} = %{version}

%description examples
MPI-Bash makes it possible to parallelize Bash scripts which run a set of
Linux commands independently over a large number of input files.

This package contains example scripts for mpibash.


%prep
%setup -q

%build
. %{_libdir}/mpi/gcc/%{mpi_implem}/bin/mpivars.sh
%configure --docdir=%{_docdir}/%{name} --with-plugindir=%{_libdir}/%{name}/ CC=mpicc
%make_build

%install
%make_install
# Fix shebang
sed -i '1s@/usr/bin/env bash@/bin/bash@' %{buildroot}/%{_bindir}/mpibash
sed -i '1s@env mpibash@mpibash@' %{buildroot}/%{_docdir}/%{name}/examples/* %{buildroot}/%{_bindir}/m*

%files
%defattr(-,root,root,-)
%{_bindir}/m*
%{_libdir}/%{name}/
%{_mandir}/man1/m*
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/examples

%files examples
%defattr(-,root,root,-)
%{_docdir}/%{name}/examples
