#
# spec file for package dynare
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


%if 0%{?suse_version} < 1550
# GCC 9 or higher required
%define gccver 9
# Sphinx in Leap 15.x is too old
%bcond_with doc
%else
%define gccver %{nil}
%bcond_without doc
%endif
Name:           dynare
Version:        5.3
Release:        0
Summary:        A platform for handling a wide class of economic models
License:        GPL-3.0-or-later
URL:            https://www.dynare.org/
Source:         https://www.dynare.org/release/source/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM dynare-no-return-in-non-void-function.patch badshah400@gmail.com -- Return trivial value from a function that is not declared as returning void
Patch0:         dynare-no-return-in-non-void-function.patch
BuildRequires:  fdupes
BuildRequires:  gcc%{gccver}-c++
BuildRequires:  gcc%{gccver}-fortran
BuildRequires:  lapack-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  suitesparse-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(matio)
BuildRequires:  pkgconfig(octave)
%if %{with doc}
# SECTION Required for docs
BuildRequires:  python3-Sphinx-latex
BuildRequires:  texlive-beamer
BuildRequires:  texlive-bibtex-bin
BuildRequires:  texlive-latex-bin
BuildRequires:  tex(ccicons.sty)
BuildRequires:  tex(doi.sty)
BuildRequires:  tex(elsarticle.cls)
BuildRequires:  tex(epsf.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(psfrag.sty)
BuildRequires:  tex(tgtermes.sty)
# /SECTION
%endif

%description
Dynare is a software platform for handling a wide class of economic models, in
particular dynamic stochastic general equilibrium (DSGE) and overlapping
generations (OLG) models.

%package doc-pdf
Summary:        Documentation for dynare in PDF format

%description doc-pdf
This package provides documentation for %{name} in PDF format.

%package doc-html
Summary:        Documentation for dynare in HTML format

%description doc-html
This package provides documentation for %{name} in HTML format.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fvi
%if 0%{?suse_version} < 1550
export CXX=g++-%{gccver}
export CXXFLAGS+=' -std=c++17'
%endif
%configure \
  --docdir=%{_docdir}/%{name} \
  --disable-matlab \
  --disable-mex-kalman-steady-state \
  %{!?with_doc:--disable-doc} \
  %{nil}
%make_build
%if %{with doc}
%make_build pdf html
%endif

%install
%make_install
%fdupes %{buildroot}%{_libdir}/%{name}/
%if %{with doc}
%fdupes %{buildroot}%{_docdir}/%{name}/dynare-manual.html/
rm %{buildroot}%{_docdir}/%{name}/dynare-manual.html/.buildinfo
%endif

%files
%license license.txt
%doc CONTRIBUTING.md NEWS.md README.md
%{_bindir}/dynare++
%{_bindir}/dynare-preprocessor
%{_libdir}/dynare/

%if %{with doc}
%files doc-pdf
%{_docdir}/%{name}/*.pdf
%{_docdir}/%{name}/dynare++/

%files doc-html
%{_docdir}/%{name}/dynare-manual.html/
%endif

%changelog
