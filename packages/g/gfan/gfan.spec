#
# spec file for package gfan
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


Name:           gfan
Version:        0.6.2
Release:        0
Summary:        Calculation of Gröbner fans
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            http://home.imf.au.dk/jensen/software/gfan/gfan.html

Source:         http://home.imf.au.dk/jensen/software/gfan/%name%version.tar.gz
Patch1:         gfan-automake.diff
Patch2:         gfan-warnings.diff
Patch3:         cddlib.patch
BuildRequires:  automake
BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
%define with_pdf 1
%if 0%{?with_pdf}
BuildRequires:  texlive-latex
%if 0%{?suse_version} >= 1230
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ntgclass
BuildRequires:  texlive-ulem
%if 0%{?suse_version} > 1230
BuildRequires:  tex(english.ldf)
%endif
%endif
%endif

%description
Gfan is a software package for computing Gröbner fans and tropical
varieties. These are polyhedral fans associated to polynomial ideals.

%prep
%autosetup -p1 -n %name%version

%build
autoreconf -fi
export CXXFLAGS="%optflags -Wno-sign-compare -Wno-reorder -Wno-unused -Wno-comment -Wno-misleading-indentation -std=gnu++11"
%configure
make %{?_smp_mflags} V=1
%if 0%{?with_pdf}
make -C doc %{?_smp_mflags}
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
