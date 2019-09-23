#
# spec file for package mdtest
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


Name:           mdtest
Version:        1.9.3
Release:        0
Summary:        An MPI-coordinated test that performs operations on files and directories
License:        GPL-2.0
Group:          System/Benchmark
Url:            http://mdtest.sourceforge.net/
Source:         http://sourceforge.net/projects/mdtest/files/mdtest%%20latest/%{name}-%{version}/%{name}-%{version}.tgz
BuildRequires:  openmpi2-devel
Requires:       openmpi2

%description
mdtest is an MPI-coordinated metadata benchmark test that performs
open/stat/close operations on files and directories and then reports the
performance.

%prep
%setup -q -c
chmod -x RELEASE_LOG README COPYRIGHT

%build
make %{?_smp_mflags} MDTEST_FLAGS="%{optflags}" MPI_CC="%{_libdir}/mpi/gcc/openmpi2/bin/mpicc"

%install
install -D -p -m 0755 mdtest   %{buildroot}%{_bindir}/mdtest
install -D -p -m 0644 mdtest.1 %{buildroot}%{_mandir}/man1/mdtest.1

%files
%doc RELEASE_LOG README COPYRIGHT
%{_bindir}/mdtest
%{_mandir}/man1/mdtest.1%{ext_man}

%changelog
