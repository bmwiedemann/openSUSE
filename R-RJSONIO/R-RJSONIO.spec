#
# spec file for package R-RJSONIO
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


%global packname  RJSONIO
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        1.3_0
Release:        1
Summary:        Serialize R objects to JSON, JavaScript Object Notation
Group:          Development/Libraries/Other
License:        BSD-3-Clause
URL:            http://cran.r-project.org/web/packages/RJSONIO/index.html
Source:         https://cran.r-project.org/src/contrib/RJSONIO_1.3-0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-base
Requires:       R-methods 
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif
BuildRequires:    R-base-devel R-methods

%description
This is a package that allows conversion to and from data in Javascript
object notation (JSON) format.  This allows R objects to be inserted into
Javascript/ECMAScript/ActionScript code and allows R programmers to read
and convert JSON content to R objects.  This is an alternative to rjson
package. That version was too slow for converting large R objects to JSON
and is not extensible, but a very useful prototype.  It is fast for
parsing.  This package uses methods, vectorized operations and C code and
callbacks to R functions for deserializing JSON objects to R.  Verison 0.4
of this package uses a new native parser, implements the transformation
code in C and allocates memory efficiently (rather than concatenating
because of event driven parsing).  The result is a significantly faster
parsing of large JSON documents.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/sampleData
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%changelog
