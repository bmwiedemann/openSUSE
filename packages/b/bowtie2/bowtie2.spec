#
# spec file for package bowtie2
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


%global simde_version 0.7.2
%ifarch aarch64
%define _lto_cflags %{nil}
%endif
Name:           bowtie2
Version:        2.5.0
Release:        0
Summary:        Fast and memory-efficient short read aligner
License:        GPL-3.0-only
Group:          Productivity/Scientific/Other
URL:            http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
Source0:        https://github.com/BenLangmead/bowtie2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/simd-everywhere/simde/archive/v%{simde_version}.tar.gz#/simde-%{simde_version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
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
%setup -q -b 1
pushd third_party
rmdir simde
ln -s ../../simde-*/ simde
popd
# Workaround to find simde/x86/*.h on aarch64
ln -s ../simde-*/simde simde

%build
%ifarch aarch64
sed -i -e 's/-msse2//' CMakeLists.txt
sed -i -e 's/-m64//' CMakeLists.txt
%endif
# Note: RelWithDebInfo isn't supported and assumes fully unoptimised DEBUG mode; use Release mode instead
%cmake \
%ifarch aarch64
  -DNO_POPCNT_CAPABILITY=1 \
%endif
  -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

# CONVERT env HASHBANGS TO USE DIRECT EXECUTABLE
perlbin=`which perl`
sed -i "s:%{_bindir}/env perl:${perlbin}:" %{buildroot}%{_bindir}/bowtie2
sed -i "s:%{_bindir}/env python:%{_bindir}/python:" %{buildroot}%{_bindir}/bowtie2-{build,inspect}

%fdupes %{buildroot}%{_bindir}

%files
%doc AUTHORS MANUAL NEWS TUTORIAL BOWTIE2_VERSION README.md
%license LICENSE
%{_bindir}/bowtie2
%{_bindir}/bowtie2-build*
%{_bindir}/bowtie2-inspect*
%{_bindir}/bowtie2-align*

%changelog
