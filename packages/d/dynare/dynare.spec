#
# spec file for package dynare
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# Sphinx in Leap 15.x is too old
%bcond_with doc
%else
%bcond_without doc
%endif
Name:           dynare
Version:        6.5
Release:        0
Summary:        A platform for handling a wide class of economic models
License:        GPL-3.0-or-later
URL:            https://www.dynare.org/
Source:         %{name}-%{version}.tar.zst
# PATCH-FIX-UPSTREAM dynare-libdir.patch badshah400@gmail.com -- Use correct libdir instead of 'lib'
Patch0:         dynare-libdir.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  libboost_headers-devel
# Dummy BR, required due to meson bug https://github.com/mesonbuild/meson/issues/15470
BuildRequires:  libboost_thread-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  slicot-devel-static
BuildRequires:  suitesparse-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(matio)
BuildRequires:  pkgconfig(octave) >= 7.1.0
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
BuildArch:      noarch

%description doc-pdf
This package provides documentation for %{name} in PDF format.

%package doc-html
Summary:        Documentation for dynare in HTML format
BuildArch:      noarch

%description doc-html
This package provides documentation for %{name} in HTML format.

%prep
%autosetup -p1

%build
%meson \
  -Dbuild_for=octave \
  %{nil}
%meson_build
%if %{with doc}
%meson_build dynare-manual.pdf dynare-manual.html
%endif

%install
%meson_install
%fdupes %{buildroot}%{_libdir}/%{name}/
%if %{with doc}
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/
%fdupes %{buildroot}%{_docdir}/%{name}/dynare-manual.html/
rm %{buildroot}%{_docdir}/%{name}/dynare-manual.html/.buildinfo
%endif

%files
%license license.txt
%doc CONTRIBUTING.md NEWS.md README.md
%{_bindir}/dynare-preprocessor
%{_libdir}/dynare/

%if %{with doc}
%files doc-pdf
%{_docdir}/%{name}/*.pdf

%files doc-html
%{_docdir}/%{name}/dynare-manual.html/
%endif

%changelog
