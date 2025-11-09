
# spec file for package mpibash
#
# Copyright (c) 2025 SUSE LLC
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


Name:           mpibash
Version:        1.5
Release:        0
Summary:        Parallel scripting right from the Bourne-Again Shell
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/lanl/MPI-Bash
Source0:        https://github.com/lanl/MPI-Bash/releases/download/v%{version}/mpibash-%{version}.tar.gz
Source100:      README.md
BuildRequires:  bash-devel >= 5.2
BuildRequires:  libcircle-devel
BuildRequires:  openmpi-macros-devel
%openmpi_requires
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1600
ExcludeArch:    %ix86 %arm
%else
# Do not built for SLE/Leap < 16, they do not provide bash >= 5.2
ExclusiveArch: do_not_build
%endif

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
%autosetup -p0

%build
%setup_openmpi
%if 0%{?suse_version} > 1500
export CFLAGS="-std=gnu17 $CFLAGS"
%endif
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

%changelog
