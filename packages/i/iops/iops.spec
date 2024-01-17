#
# spec file for package iops
#
# Copyright (c) 2021 SUSE LLC
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


Name:           iops
Version:        0.0+git.20200324
Release:        0
Summary:        Disk I/O Benchmark
License:        ISC
Group:          System/Benchmark
URL:            https://benjamin-schweizer.de/measuring-disk-io-performance.html
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

%description
Benchmark script to measure disk I/O performance.

%prep
%autosetup
sed -i 's|env python2|python3|g' iops

%build

%install
install -Dpm 0755 iops \
  %{buildroot}%{_sbindir}/iops

%files
%doc README.md
%{_sbindir}/iops

%changelog
