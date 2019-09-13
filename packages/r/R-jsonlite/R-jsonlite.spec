#
# spec file for package R-jsonlite
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

%global packname  jsonlite
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        1.6
Release:        0
Summary:        A JSON parser and generator for R
Group:          Development/Libraries/Other
License:        MIT
URL:            http://cran.r-project.org/web/packages/%{packname}
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-base
Requires:       R-methods 
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes

%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif

BuildRequires:    R-base-devel R-methods
BuildRequires:    gcc-c++

%description
A JSON parser and generator optimized for statistical data and the
web. The package offers tools for working with JSON in R and is for building
pipelines and interacting with a web API. The implementation is based on
the mapping described in the vignette (Ooms, 2014). In addition to
converting JSON data from/to R objects, 'jsonlite' contains functions to
stream, validate, and prettify JSON data. The unit tests included with the
package verify that all edge cases are encoded and decoded consistently
for use with dynamic data in systems and applications.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%changelog
