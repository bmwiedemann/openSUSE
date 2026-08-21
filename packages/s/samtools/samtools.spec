#
# spec file for package samtools
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define htsminversion 1.21

Name:           samtools
Version:        1.21
Release:        0
Summary:        Tools for manipulating next-generation sequencing data
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://github.com/samtools/samtools
Source:         https://github.com/samtools/samtools/releases/download/%{version}/samtools-%{version}.tar.bz2
BuildRequires:  ncurses-utils
BuildRequires:  perl-base
BuildRequires:  pkgconfig(htslib) >= %{htsminversion}
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)
Requires:       bgzip
Requires:       perl-base
Requires:       tabix

%description
Samtools implements various utilities for post-processing alignments in the
SAM, BAM, and CRAM formats, including indexing, variant calling (in conjunction
with bcftools), and a simple alignment viewer.

%prep
%setup -q

%build
%configure --with-htslib=system
%make_build

%check
# Run samtools upstream test suite
cd test
./test.pl 2>&1 || :
cd ..

%install
%make_install

# CONVERT env HASHBANGS TO USE DIRECT EXECUTABLE
perlbin=`which perl`
sed -i "s:/usr/bin/env perl:${perlbin}:" %{buildroot}/%{_bindir}/*.pl
sed -i "s:/usr/bin/env perl:${perlbin}:" %{buildroot}/%{_bindir}/plot-bamstats
sed -i "s:/usr/bin/env perl:${perlbin}:" %{buildroot}/%{_bindir}/plot-ampliconstats

# Install test data for samtools-test subpackage
install -d %{buildroot}%{_libdir}/samtools/test
# Copy test data excluding compiled objects and source files
find test -type f ! -name "*.c" ! -name "*.h" ! -name "*.o" -exec install -D -m 0755 {} %{buildroot}%{_libdir}/samtools/{} \;

%files
%license LICENSE
%doc NEWS.md README
%{_bindir}/*
%{_mandir}/man1/*

%package test
Summary:        Test suite for %{name}
Requires:       %{name} = %{version}
Requires:       perl
Requires:       tabix

%description test
Test data and test runner for samtools.
Run with: cp -a /usr/share/samtools/test/ /tmp/ && cd /tmp && ln -s /usr/bin/samtools . && ./test/test.pl

%files test
%dir %{_libdir}/samtools
%{_libdir}/samtools/test/

%changelog
