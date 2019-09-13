#
# spec file for package promises
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

%global packname  promises
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        1.0.1
Release:        0
Summary:        Abstractions for Promise-Based Asynchronous Programming
Group:          Development/Libraries/Other
License:        MIT
URL:            http://cran.r-project.org/web/packages/%{packname}
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-base
Requires:       R-R6 R-Rcpp R-later R-rlang R-stats R-magrittr 
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes
BuildRequires:  R-base-devel
BuildRequires:  R-R6 R-Rcpp-devel R-later R-rlang R-stats R-magrittr 
BuildRequires:  gcc gcc-c++ gcc-fortran 

%description
Provides fundamental abstractions for doing asynchronous programming in R
using promises. Asynchronous programming is useful for allowing a single R
process to orchestrate multiple tasks in the background while also
attending to something else. Semantics are similar to 'JavaScript'
promises, but with a syntax that is idiomatic R.

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
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs/

%changelog