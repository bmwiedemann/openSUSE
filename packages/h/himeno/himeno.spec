#
# spec file for package himeno
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           himeno
Version:        3
Release:        0
Summary:        Benchmark to evaluate the performance of incompressible fluid analysis code
License:        LGPL-2.0+
Group:          System/Benchmark
Url:            http://accc.riken.jp/HPC/HimenoBMT/index_e.html
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Benchmark to evaluate the performance of incompressible fluid analysis
code. This benchmark program measures the speed of major loops to solve
Poisson's equation folution using Jacobi iteration method.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -DSSMALL"

%install
install -D -m 0755 bmt %{buildroot}%{_bindir}/bmt

%files
%defattr(-, root, root)
%{_bindir}/bmt

%changelog
