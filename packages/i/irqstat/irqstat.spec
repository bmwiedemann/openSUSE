#
# spec file for package irqstat
#
# Copyright (c) 2020 SUSE LLC
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


Name:           irqstat
Version:        1.0.0+git4cd6854
Release:        0
Summary:        Script to better monitor interrupts in large systems
License:        MIT
URL:            https://github.com/lanceshelton/irqstat
Source0:        irqstat-%{version}.tar.xz
Patch1:         python-to-python3.patch
# Submitted upstream as part of https://github.com/lanceshelton/irqstat/pull/7
Patch2:         fix-python3-and-unbuffered-io.patch
Requires:       numactl
BuildArch:      noarch

%description
A better way to watch /proc/interrupts, designed for NUMA systems with many processors.

%prep
%setup -q -n irqstat-%{version}
%patch1 -p1
%patch2 -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 irqstat %{buildroot}%{_bindir}/irqstat

%files
%license LICENSE
%doc README.md
%{_bindir}/irqstat

%changelog
