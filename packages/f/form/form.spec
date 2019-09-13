#
# spec file for package form
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# Documentation building fails due to LaTeX errors; disable for now
%define with_doc 0

%define reldate 20190212
Name:           form
Version:        4.2.1
Release:        0
Summary:        A Symbolic Manipulation System
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            https://github.com/vermaseren/form/
Source0:        https://github.com/vermaseren/form/archive/v%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  openmpi-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
%if %{with_doc}
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
%setup -q

# REPLACE __DATE__ BY %%{reldate} USED TO TAG THE SOURCE TARBALL
sed -i "s/PRODUCTIONDATE __DATE__/PRODUCTIONDATE %{reldate}/" sources/form3.h
sed -i "s/PRODUCTIONDATE __DATE__/PRODUCTIONDATE %{reldate}/" configure.ac

%build
if [ -f %{_libdir}/mpi/gcc/openmpi/bin/mpivars.sh ]; then
  source %{_libdir}/mpi/gcc/openmpi/bin/mpivars.sh
fi

sed -i "s|-march=native||g" configure.ac
autoreconf -fvi
%configure --enable-parform
make %{?_smp_mflags}

%if %{with_doc}
# MAKE DOCUMENTATION
pushd doc
make %{?_smp_mflags} pdf
make %{?_smp_mflags} html
popd
%endif

%install
%make_install

%fdupes -s doc

%files
%doc AUTHORS README.md COPYING
%if %{with_doc}
%doc doc/manual/manual.pdf
%doc doc/manual/html/
%endif
%{_bindir}/form
%{_bindir}/tform
%{_bindir}/parform
%{_mandir}/man1/form.1%{ext_man}

%if %{with_doc}
%files doc
%doc doc/doxygen/html/
%doc doc/devref/devref.pdf
%doc doc/devref/html/
%endif

%changelog
