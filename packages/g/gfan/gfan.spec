#
# spec file for package gfan
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gfan
Version:        0.7
Release:        0
Summary:        Calculation of Gröbner fans
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://math.au.dk/~jensen/software/gfan/gfan.html
Source:         https://math.au.dk/~jensen/software/gfan/%name%version.tar.gz
Patch1:         gfan-automake.diff
# From fedora
Patch2:         gfan-warning.patch
Patch3:         gfan-soplex.patch
Patch4:         gfan-c++20.patch
Patch5:         gfan-gcd.patch
Patch6:         gfan-multiplicities.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(cddgmp)
%define with_pdf 1
%if 0%{?with_pdf}
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  texlive-ntgclass
BuildRequires:  texlive-ulem
BuildRequires:  tex(english.ldf)
%endif
# Software requires the presence of __int128; possibly relevant for armv7l too
ExcludeArch:    %ix86

%description
Gfan is a software package for computing Gröbner fans and tropical
varieties. These are polyhedral fans associated to polynomial ideals.

%prep
%autosetup -p1 -n %name%version

%build
autoreconf -fi
%configure
%make_build V=1
%if 0%{?with_pdf}
%make_build -C doc
%endif

%install
b="%buildroot"
%make_install
for i in $(src/gfan _list | grep ^gfan_); do
	ln -s gfan "$b/%_bindir/$i"
done

%files
%_bindir/gfan*
%license COPYING
%doc examples
%if 0%{?with_pdf}
%doc doc/manual.pdf
%endif

%changelog
