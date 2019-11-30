#
# spec file for package bowtie2
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


Name:           bowtie2
Version:        2.3.5.1
Release:        0
Summary:        Fast and memory-efficient short read aligner
License:        GPL-3.0
Group:          Productivity/Scientific/Other
Url:            http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
Source0:        https://github.com/BenLangmead/bowtie2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  tbb-devel
BuildRequires:  zlib-devel
ExclusiveArch:  x86_64 s390x ppc64le ppc64 aarch64

%description
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing
reads to long reference sequences. It is particularly good at aligning
reads of about 50 up to 100s or 1,000s of characters, and particularly good
at aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes
the genome with an FM Index to keep its memory footprint small: for the
human genome, its memory footprint is typically around 3.2 GB. Bowtie 2
supports gapped, local, and paired-end alignment modes.

%prep
%setup -q

%build
make %{?_smp_mflags} RELEASE_FLAGS="%{optflags}"

%install
%make_install prefix=%{_prefix}

# CONVERT env HASHBANGS TO USE DIRECT EXECUTABLE
perlbin=`which perl`
sed -i "s:/usr/bin/env perl:${perlbin}:" %{buildroot}%{_bindir}/bowtie2
sed -i "s:/usr/bin/env python:/usr/bin/python:" %{buildroot}%{_bindir}/bowtie2-{build,inspect}

%files
%doc AUTHORS LICENSE MANUAL NEWS TUTORIAL VERSION
%{_bindir}/bowtie2
%{_bindir}/bowtie2-align-l
%{_bindir}/bowtie2-align-s
%{_bindir}/bowtie2-build
%{_bindir}/bowtie2-build-l
%{_bindir}/bowtie2-build-s
%{_bindir}/bowtie2-inspect
%{_bindir}/bowtie2-inspect-l
%{_bindir}/bowtie2-inspect-s

%changelog
