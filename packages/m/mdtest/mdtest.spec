#
# spec file for package mdtest
#
# Copyright (c) 2019 SUSE LLC
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


Name:           mdtest
Version:        1.9.3
Release:        0
Summary:        An MPI-coordinated test that performs operations on files and directories
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            http://mdtest.sourceforge.net/
Source:         http://sourceforge.net/projects/mdtest/files/mdtest%%20latest/%{name}-%{version}/%{name}-%{version}.tgz
BuildRequires:  openmpi-macros-devel

%description
mdtest is an MPI-coordinated metadata benchmark test that performs
open/stat/close operations on files and directories and then reports the
performance.

%prep
%setup -q -c
chmod -x RELEASE_LOG README COPYRIGHT

%build
%setup_openmpi
make %{?_smp_mflags} MDTEST_FLAGS="%{optflags}" CC="mpicc"

%install
install -Dpm 0755 mdtest \
  %{buildroot}%{_bindir}/mdtest
install -Dpm 0644 mdtest.1 \
  %{buildroot}%{_mandir}/man1/mdtest.1

%files
%license COPYRIGHT
%doc RELEASE_LOG README
%{_bindir}/mdtest
%{_mandir}/man1/mdtest.1%{?ext_man}

%changelog
