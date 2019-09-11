#
# spec file for package later
# This file is (mostly) auto-generated using information
# in the package source, esp. Description and Summary.
# Improvements in that area should be discussed with upstream.
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

%global packname  later
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.7.5
Release:        0
Summary:        Utilities for Delaying Function Execution
Group:          Development/Libraries/Other
License:        GPL-2.0+
URL:            http://cran.r-project.org/web/packages/%{packname}
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-base
Requires:       R-Rcpp R-rlang R-BH
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes
BuildRequires:  R-base-devel
BuildRequires:  R-Rcpp-devel R-rlang R-BH
BuildRequires:  gcc gcc-c++ gcc-fortran 

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

%files
%defattr(-, root, root, -)
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