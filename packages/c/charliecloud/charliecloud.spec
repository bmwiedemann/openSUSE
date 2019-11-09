#
# spec file for package charliecloud
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.12
Release:        0
Summary:        User-defined software stacks (UDSS) for HPC centers
License:        Apache-2.0
Group:          Productivity/Clustering/Computing
URL:            https://hpc.github.io/charliecloud/
Source0:        https://github.com/hpc/charliecloud/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python2-base
# Docker and buildah are not needed to run charliecloud but can be 
# used to build images
Recommends:     docker
Recommends:     buildah >= 1.11.2
# Build the documentation
%if !(0%{?sle_version} <= 120400 && 0%{?is_backports})
BuildRequires:  python2-Sphinx
BuildRequires:  python2-sphinx_rtd_theme
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

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} LIBEXEC_DIR=lib/charliecloud

# Build documentation, disabled on SLE-12
%if !(0%{?sle_version} <= 120400 && 0%{?is_backports})
make -C doc-src

# Rename documentation dir to html
mv doc html
rm html/.nojekyll

# Copy manpages
mkdir -p %{buildroot}%{_mandir}/man1
cp -a man/*.1 %{buildroot}%{_mandir}/man1
%endif

# Fix shebangs
sed -E -i "s|^#!/usr/bin/env python3|#!/usr/bin/python3|" %{buildroot}%{_bindir}/ch-*

# Remove files installed later with %%doc and %%licence
rm -rf %{buildroot}%{_datadir}/doc/charliecloud-%{version}/*

# Do not ship the tests
rm -rf %{buildroot}%{_libexecdir}/charliecloud/test/

# Ship examples without binaries
rm -rf %{buildroot}%{_libexecdir}/charliecloud/examples/

%files
%license LICENSE
%doc README.rst
%{_bindir}/*
%exclude %{_bindir}/ch-test
%dir %{_libexecdir}/charliecloud/
%{_libexecdir}/charliecloud/*.sh
%{_mandir}/man1/*

%if !(0%{?sle_version} <= 120400 && 0%{?is_backports})
%files doc
%license LICENSE
%doc html
%endif

%files examples
%license LICENSE
%doc examples

%changelog
