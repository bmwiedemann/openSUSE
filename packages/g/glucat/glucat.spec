#
# spec file for package glucat
#
# Copyright (c) 2021 SUSE LLC
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


Name:           glucat
Version:        0.9.0
Release:        0
Summary:        Library of C++ templates implementing universal Clifford algebras
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            http://glucat.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
BuildRequires:  libboost_headers-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-numpy
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-metafont-bin
%if 0%{?suse_version} > 1500
BuildRequires:  tex(amsfonts.sty)
BuildRequires:  tex(auxhook.sty)
BuildRequires:  tex(bigintcalc.sty)
BuildRequires:  tex(bitset.sty)
BuildRequires:  tex(collectbox.sty)
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(etexcmds.sty)
BuildRequires:  tex(etoolbox.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(gettitlestring.sty)
BuildRequires:  tex(graphics.sty)
BuildRequires:  tex(hycolor.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(ifoddpage.sty)
BuildRequires:  tex(iftex.sty)
BuildRequires:  tex(infwarerr.sty)
BuildRequires:  tex(intcalc.sty)
BuildRequires:  tex(kvdefinekeys.sty)
BuildRequires:  tex(kvoptions.sty)
BuildRequires:  tex(kvsetkeys.sty)
BuildRequires:  tex(letltxmacro.sty)
BuildRequires:  tex(listofitems.sty)
BuildRequires:  tex(ltxcmds.sty)
BuildRequires:  tex(pdfescape.sty)
BuildRequires:  tex(pdftexcmds.sty)
BuildRequires:  tex(refcount.sty)
BuildRequires:  tex(rerunfilecheck.sty)
BuildRequires:  tex(uniquecounter.sty)
BuildRequires:  tex(url.sty)
BuildRequires:  tex(varwidth.sty)
BuildRequires:  tex(xcolor.sty)
BuildRequires:  tex(xkeyval.sty)
%endif
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(alphalph.sty)
BuildRequires:  tex(caption.sty)
BuildRequires:  tex(colortbl.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(float.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(natbib.sty)
BuildRequires:  tex(newunicodechar.sty)
BuildRequires:  tex(sectsty.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(tocloft.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  tex(wasysym.sty)
BuildRequires:  tex(xtab.sty)

%description
GluCat is a library of template classes which model the universal
Clifford algebras over the field of real numbers, with arbitrary
dimension and arbitrary signature. GluCat implements a model of each
Clifford algebra corresponding to each non-degenerate quadratic form
up to a maximum number of dimensions.

%package devel
Summary:        Library of C++ templates implementing universal Clifford algebras
Group:          Development/Libraries/C and C++
Recommends:     %{name}-doc = %{version}

%description devel
GluCat is a library of template classes which model the universal
Clifford algebras over the field of real numbers, with arbitrary
dimension and arbitrary signature. GluCat implements a model of each
Clifford algebra corresponding to each non-degenerate quadratic form
up to a maximum number of dimensions.

This package contains the header files required for developing
applications using the glucat library.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML

%description doc
GluCat is a library of template classes which model the universal
Clifford algebras over the field of real numbers, with arbitrary
dimension and arbitrary signature. GluCat implements a model of each
Clifford algebra corresponding to each non-degenerate quadratic form
up to a maximum number of dimensions.

This package provides the documentation for %{name}.

%package -n python3-glucat
Summary:        Library of C++ templates implementing universal Clifford algebras
Group:          Development/Libraries/C and C++
Requires:       python3-base
Recommends:     %{name}-doc = %{version}
Obsoletes:      python-glucat < %{version}
Provides:       python-glucat = %{version}

%description -n python3-glucat
GluCat is a library of template classes which model the universal
Clifford algebras over the field of real numbers, with arbitrary
dimension and arbitrary signature. GluCat implements a model of each
Clifford algebra corresponding to each non-degenerate quadratic form
up to a maximum number of dimensions.

This package contains the python-bindings for the package.

%prep
%setup -q

%build
sed -i "s|-march=native||g" configure
%configure \
  --docdir=%{_docdir}/%{name} \
  --enable-pyclical \
  --with-demo-dir=%{_docdir}/%{name}/demos

%make_build clean all
make %{?_smp_mflags} doc

%install
%make_install
make DESTDIR=%{buildroot} install-doc

# REMOVE FILES PKGED USING %%doc ANYWAY OR OTHERWISE NOT NEEDED
rm -fr %{buildroot}%{_docdir}/%{name}/{AUTHORS,COPYING,ChangeLog,glucat.lsm,INSTALL,NEWS,README,TODO,DESIGN}

%check
make %{?_smp_mflags} check

%fdupes %{buildroot}%{_docdir}/%{name}/html/

%files devel
%license COPYING
%doc AUTHORS ChangeLog README TODO NEWS DESIGN
%{_includedir}/%{name}/

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/pdf/

%files -n python3-glucat
%{python3_sitearch}/*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/demos/

%changelog
