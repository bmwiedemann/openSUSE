#
# spec file for package bowtie
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


Name:           bowtie
Version:        1.3.0
Release:        0
Summary:        Fast and memory-efficient short read aligner
License:        Artistic-1.0
Group:          Productivity/Scientific/Other
URL:            http://bio-bowtie.sourceforge.net/
Source:         https://github.com/BenLangmead/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  x86_64 aarch64

%description
Bowtie is an ultrafast, memory-efficient short read aligner. It aligns short
DNA sequences (reads) to the human genome at a rate of over 25 million 35-bp
reads per hour. Bowtie indexes the genome with a Burrows-Wheeler index to keep
its memory footprint small: typically about 2.2 GB for the human genome
(2.9 GB for paired-end).

%prep
%autosetup -p1

%build
%make_build

%install
%make_install prefix=%{_prefix}
sed -i '1{s|^#!.*env python|#!%{_bindir}/python|}' %{buildroot}%{_bindir}/bowtie*

%files
%doc README MANUAL AUTHORS NEWS TUTORIAL VERSION
%license LICENSE
%{_bindir}/*

%changelog
