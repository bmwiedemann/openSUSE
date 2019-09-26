#
# spec file for package R-later
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global packname  later
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        0.8.0
Release:        0
Summary:        Utilities for Delaying Function Execution
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            http://cran.r-project.org/web/packages/%{packname}
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-BH
BuildRequires:  R-Rcpp-devel
BuildRequires:  R-knitr
BuildRequires:  R-rlang
BuildRequires:  R-testthat
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  texinfo
Requires:       R-BH
Requires:       R-Rcpp
Requires:       R-rlang
%if 0%{?sle_version} > 120400 || 0%{?is_opensuse}
BuildRequires:  tex(inconsolata.sty)
%else
BuildRequires:  texlive
%endif

%description
Executes arbitrary R or C functions some time after the current time,
after the R execution stack has emptied.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
%fdupes %{buildroot}%{rlibdir}/%{packname}

%check
export LANG=en_US.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=false
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bgtest.cpp
%{rlibdir}/%{packname}/include/
%{rlibdir}/%{packname}/libs/

%changelog
