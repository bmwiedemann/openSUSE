#
# spec file for package samtools
#
# Copyright (c) 2022 SUSE LLC
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


%define htsminversion 1.16

Name:           samtools
Version:        1.16.1
Release:        0
Summary:        Tools for manipulating next-generation sequencing data
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://github.com/samtools/samtools
Source:         https://github.com/samtools/samtools/releases/download/%{version}/samtools-%{version}.tar.bz2
BuildRequires:  ncurses-utils
BuildRequires:  perl
BuildRequires:  pkgconfig(htslib) >= %{htsminversion}
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)
Requires:       bgzip
Requires:       libhts3 >= %{htsminversion}
Requires:       perl
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

%install
%make_install

# CONVERT env HASHBANGS TO USE DIRECT EXECUTABLE
perlbin=`which perl`
sed -i "s:/usr/bin/env perl:${perlbin}:" %{buildroot}/%{_bindir}/*.pl
sed -i "s:/usr/bin/env perl:${perlbin}:" %{buildroot}/%{_bindir}/plot-bamstats
sed -i "s:/usr/bin/env perl:${perlbin}:" %{buildroot}/%{_bindir}/plot-ampliconstats

%files
%license LICENSE
%doc NEWS README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
