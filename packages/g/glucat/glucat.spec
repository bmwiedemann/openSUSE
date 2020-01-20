#
# spec file for package glucat
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


# SECTION DISABLE pyclical FOR openSUSE >= 1550: DOESN'T BUILD WITH PYTHON3
%if 0%{?suse_version} < 1550
%bcond_without python2
%else
%bcond_with python2
%endif
# /SECTION

Name:           glucat
Version:        0.8.2
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
%if %{with python2}
BuildRequires:  python-Cython
BuildRequires:  python-devel
BuildRequires:  python-numpy
%endif
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-metafont-bin
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(caption.sty)
BuildRequires:  tex(colortbl.sty)
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

%package -n python-glucat
Summary:        Library of C++ templates implementing universal Clifford algebras
Group:          Development/Libraries/C and C++
%if %{with python2}
Requires:       python-base = %{py_ver}
%endif
Recommends:     %{name}-doc = %{version}

%description -n python-glucat
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
%if %{without python2}
  --disable-pyclical \
%endif
  --with-demo-dir=%{_docdir}/%{name}/demos

# FIX A NON-UNIX EOF ENCODING
sed -i 's/\r$//' ./pyclical/demos/plotting_demo_mayavi.py

make %{?_smp_mflags} clean all
make %{?_smp_mflags} doc

%install
%make_install
make DESTDIR=%{buildroot} install-doc

# REMOVE FILES PKGED USING %%doc ANYWAY OR OTHERWISE NOT NEEDED
rm -fr %{buildroot}%{_docdir}/%{name}/{AUTHORS,COPYING,ChangeLog,glucat.lsm,INSTALL,NEWS,README,TODO}

%check
make %{?_smp_mflags} check

%fdupes %{buildroot}%{_docdir}/%{name}/html/

%files devel
%license COPYING
%doc AUTHORS ChangeLog README TODO NEWS
%{_includedir}/%{name}/

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/pdf/

%if %{with python2}
%files -n python-glucat
%{python_sitearch}/*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/demos/
%endif

%changelog
