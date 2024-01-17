#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%define pname glucat

# Note: Blank flavor needs to build python bindings so that auto-generated python package names come out right
%if "%{flavor}" == "main"
%bcond_with    python
%define psuffix -main
%else
%bcond_without python
%define skip_python2 1
%endif

# Build failures when building doc for 15.4
%if (0%{?is_opensuse} && 0%{?sle_version} >= 150400)
%bcond_with pdfdoc
%else
%bcond_without pdfdoc
%endif

Name:           %{pname}%{?psuffix}
Version:        0.12.0
Release:        0
Summary:        Library of C++ templates implementing universal Clifford algebras
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            http://glucat.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{pname}/%{pname}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE glucat-disable-doxygen-html-timestamp.patch badshah400@gmail.com -- Disable timestamps from html footer to make build reproducible
Patch0:         glucat-disable-doxygen-html-timestamp.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libboost_headers-devel
%if %{with python}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%python_subpackages
%else
BuildRequires:  doxygen
BuildRequires:  graphviz-gnome
%if %{with pdfdoc}
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-metafont-bin
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(alphalph.sty)
BuildRequires:  tex(amsfonts.sty)
BuildRequires:  tex(auxhook.sty)
BuildRequires:  tex(bigintcalc.sty)
BuildRequires:  tex(bitset.sty)
BuildRequires:  tex(caption.sty)
BuildRequires:  tex(changepage.sty)
BuildRequires:  tex(collectbox.sty)
BuildRequires:  tex(colortbl.sty)
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(etexcmds.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(etoolbox.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(float.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(gettitlestring.sty)
BuildRequires:  tex(graphics.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(helvet.sty)
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
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(natbib.sty)
BuildRequires:  tex(newunicodechar.sty)
BuildRequires:  tex(pdfescape.sty)
BuildRequires:  tex(pdftexcmds.sty)
BuildRequires:  tex(refcount.sty)
BuildRequires:  tex(rerunfilecheck.sty)
BuildRequires:  tex(sectsty.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(tocloft.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  tex(uniquecounter.sty)
BuildRequires:  tex(url.sty)
BuildRequires:  tex(varwidth.sty)
BuildRequires:  tex(wasysym.sty)
BuildRequires:  tex(xcolor.sty)
BuildRequires:  tex(xkeyval.sty)
BuildRequires:  tex(xtab.sty)
%endif
%endif

%description
GluCat is a library of template classes which model the universal
Clifford algebras over the field of real numbers, with arbitrary
dimension and arbitrary signature. GluCat implements a model of each
Clifford algebra corresponding to each non-degenerate quadratic form
up to a maximum number of dimensions.

%package -n %{pname}-devel
Summary:        Library of C++ templates implementing universal Clifford algebras
Group:          Development/Libraries/C and C++
Recommends:     %{name}-doc = %{version}

%description -n %{pname}-devel
GluCat is a library of template classes which model the universal
Clifford algebras over the field of real numbers, with arbitrary
dimension and arbitrary signature. GluCat implements a model of each
Clifford algebra corresponding to each non-degenerate quadratic form
up to a maximum number of dimensions.

This package contains the header files required for developing
applications using the glucat library.

%package -n %{pname}-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML

%description -n %{pname}-doc
GluCat is a library of template classes which model the universal
Clifford algebras over the field of real numbers, with arbitrary
dimension and arbitrary signature. GluCat implements a model of each
Clifford algebra corresponding to each non-degenerate quadratic form
up to a maximum number of dimensions.

This package provides the documentation for %{name}.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%if %{with python}
%{python_expand # Apply to all supported python flavors
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
%configure \
  --docdir=%{_docdir}/%{pname} \
  --enable-pyclical \
  --with-demo-dir=%{_docdir}/%{pname}-python%{$python_version}/demos

sed -i "s|-march=native||g" configure

%make_build clean all
popd
}
%else
%configure \
  --docdir=%{_docdir}/%{pname} \
  --disable-pyclical

sed -i "s|-march=native||g" configure

%make_build clean all
# Build doc only for main flavor
%make_build -C doc/ html %{?with_pdfdoc:doc} || (cat doc/api/latex/*.log ; false)
%endif

%install
%if %{with python}
%{python_expand #  all python flavors as configured above
export PYTHON=$python
pushd ../${PYTHON}_build
%make_install
# Remove non-python elements to be installed by main flavor
rm -fr %{buildroot}%{_includedir}/
popd
}
%else
%make_install
# Manually install doc files
mkdir -p %{buildroot}%{_docdir}/%{pname}
cp -pr doc/api/html %{buildroot}%{_docdir}/%{pname}/
%endif

# REMOVE FILES PKGED USING %%doc ANYWAY OR OTHERWISE NOT NEEDED
rm -fr %{buildroot}%{_docdir}/%{pname}/{AUTHORS,DESIGN,INSTALL,README,TODO}.md
rm -fr %{buildroot}%{_docdir}/%{pname}/{AUTHORS,DESIGN,INSTALL,README,TODO}
rm -fr %{buildroot}%{_docdir}/%{pname}/{COPYING,ChangeLog,NEWS,glucat.lsm}

%fdupes %{buildroot}%{_docdir}/%{pname}/html/

%if %{with python}
%check
%{python_expand #  all python flavors as configured above
export PYTHON=$python
pushd ../${PYTHON}_build
make %{?_smp_mflags} check
popd
}
%endif

%if %{without python}
%files -n %{pname}-devel
%license COPYING
%doc AUTHORS.md ChangeLog README.md TODO.md NEWS DESIGN.md
%{_includedir}/%{pname}/

%files -n %{pname}-doc
%dir %{_docdir}/%{pname}
%doc %{_docdir}/%{pname}/html/
%if %{with pdfdoc}
%doc doc/api/GluCat*.pdf
%endif

%else

%files %{python_files}
%{python_sitearch}/*
%{_docdir}/%{pname}-python%{python_version}/
%endif

%changelog
