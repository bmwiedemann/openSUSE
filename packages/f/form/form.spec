#
# spec file for package form
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


%bcond_without doc

Name:           form
Version:        4.3.0
Release:        0
Summary:        A Symbolic Manipulation System
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/vermaseren/form/
Source0:        https://github.com/vermaseren/form/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE form-dont-use-DATE.patch badshah400@gmail.com -- Do not use __DATE__ in source code to avoid issues with reproducibility
Patch0:         form-dont-use-DATE.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  openmpi-macros-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
%if %{with doc}
BuildRequires:  texlive-tex4ht
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(calc.sty)
BuildRequires:  tex(caption.sty)
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fixltx2e.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(ifpdf.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(makeidx.sty)
BuildRequires:  tex(multicol.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(natbib.sty)
BuildRequires:  tex(sectsty.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(tocloft.sty)
BuildRequires:  tex(wasysym.sty)
BuildRequires:  tex(xcolor.sty)
%endif
Recommends:     %{name}-doc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# i586 compilation errors need to be investigated, disable for now
ExcludeArch:    %ix86
%openmpi_requires

%description
FORM is a Symbolic Manipulation System. It reads symbolic expressions from files
and executes symbolic/algebraic transformations upon them. The answers are
returned in a textual mathematical representation. As its landmark feature, the
size of the considered expressions in FORM is only limited by the available
disk space and not by the available RAM.

%package doc
Summary:        Additional documentation for %{name} - A Symbolic Manipulation System
Group:          Documentation/HTML

%description doc
FORM is a Symbolic Manipulation System. It reads symbolic expressions from files
and executes symbolic/algebraic transformations upon them. The answers are
returned in a textual mathematical representation. As its landmark feature, the
size of the considered expressions in FORM is only limited by the available
disk space and not by the available RAM.

This package provides additional documentation for %{name}.

%prep
%autosetup -p1

%build
%setup_openmpi

sed -i "s|-march=native||g" configure.ac

# Fix some TeX directives
sed -i "s/\\\\\([a-z]\)/\\1/g" configure.ac

autoreconf -fvi
%configure --enable-parform
%make_build

%if %{with doc}
# MAKE DOCUMENTATION
%make_build -C doc html pdf
%endif

%install
%make_install

%fdupes -s doc

%files
%license COPYING
%doc AUTHORS README.md
%if %{with doc}
%doc doc/manual/manual.pdf
%doc doc/manual/html/
%endif
%{_bindir}/form
%{_bindir}/tform
%{_bindir}/parform
%{_mandir}/man1/form.1%{ext_man}

%if %{with doc}
%files doc
%doc doc/doxygen/html/
%doc doc/devref/devref.pdf
%doc doc/devref/html/
%endif

%changelog
