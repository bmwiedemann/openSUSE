#
# spec file for package charliecloud
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


Name:           charliecloud
Version:        0.20
Release:        0
Summary:        User-defined software stacks (UDSS) for HPC centers
License:        Apache-2.0
Group:          Productivity/Clustering/Computing
URL:            https://hpc.github.io/charliecloud/
Source0:        https://github.com/hpc/charliecloud/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         Replace-hardcode-path.patch
BuildRequires:  python3-base
# Recommend for ch-grow
# used to build images
Requires:       fakeroot
Recommends:     docker
Recommends:     buildah >= 1.11.2
Recommends:     python3-requests >= 2.6.0
Recommends:     squashfs >= 4.2
%if !(0%{?sle_version} <= 120400 && 0%{?is_backports})
Recommends:     python3-lark-parser >= 0.7.1
%endif
# Build the documentation
%if !(0%{?sle_version} <= 120400 && 0%{?is_backports})
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  rsync
%endif

%description
Charliecloud provides user-defined software stacks (UDSS)
for high-performance computing (HPC) centers. This "bring your own
software stack" functionality addresses needs such as: software
dependencies that are numerous, complex, unusual, differently configured,
or simply newer/older than what the center provides; build-time
requirements unavailable within the center, such as relatively
unfettered internet access; validated software stacks and configuration
to meet the standards of a particular field of inquiry; portability of
environments between resources, including workstations and other test
and development system not managed by the center; consistent
environments, even archivally so, that can be easily, reliabily, and
verifiably reproduced in the future; and/or usability and
comprehensibility.

%package doc
Summary:        Documentation files for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Charliecloud provides user-defined software stacks (UDSS)
for high-performance computing (HPC) centers.
This package provides documentation files for Charliecloud.

%package examples
Summary:        Example files for %{name}
Group:          Documentation/Other
BuildArch:      noarch

%description examples
Charliecloud provides user-defined software stacks (UDSS)
for high-performance computing (HPC) centers.
This package provides example files for Charliecloud.

%prep
%setup -q
%patch0 -p 1

%build
%configure --disable-test
make %{?_smp_mflags}

%install
%make_install

# Documentation won't build on SLE-12
%if !(0%{?sle_version} <= 120400 && 0%{?is_backports})
mv %{buildroot}%{_datadir}/doc/charliecloud/html .
%endif

# Fix shebangs
sed -E -i "s|^#!/usr/bin/env python3|#!/usr/bin/python3|" %{buildroot}%{_bindir}/ch-*

## Remove built examples
rm -rf  %{buildroot}%{_datadir}/doc/charliecloud/examples
## Remove Makefile scripts from the examples package
rm -rf examples/Makefile*
# Fix shebangs in examples
sed -E -i "s|^#!/usr/bin/env python3|#!/usr/bin/python3|" examples/chtest/*

## Remove test related files
rm -rf %{buildroot}%{_bindir}/ch-test %{buildroot}%{_libdir}/charliecloud/contributors.bash

%files
%license LICENSE
%doc README.rst
%{_bindir}/*
%dir %{_libdir}/charliecloud/
%{_libdir}/charliecloud/*

%if !(0%{?sle_version} <= 120400 && 0%{?is_backports})
%{_mandir}/man1/*

%files doc
%license LICENSE
%doc html
%endif

%files examples
%license LICENSE
%doc examples

%changelog
