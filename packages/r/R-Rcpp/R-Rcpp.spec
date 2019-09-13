#
# spec file for package R-Rcpp
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


%global packname  Rcpp
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.0.1
Release:        0
Summary:        Seamless R and C++ Integration
License:        GPL-2.0+
Group:          Development/Libraries/Other
URL:            https://cran.r-project.org/package=%{packname}
Source:         https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Source1:        R-Rcpp-rpmlintrc
BuildRequires:  R-base-devel >= 3.0.0
BuildRequires:  R-methods
BuildRequires:  R-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-base >= 3.0.0
Requires:       R-methods
Requires:       R-utils

%description
The 'Rcpp' package provides R functions as well as C++ classes which offer
a seamless integration of R and C++. Many R data types and objects can be
mapped back and forth to C++ equivalents which facilitates both writing of
new code as well as easier integration of third-party libraries.
Documentation about 'Rcpp' is provided by several vignettes included in
this package, via the 'Rcpp Gallery' site at <http://gallery.rcpp.org>,
the paper by Eddelbuettel and Francois (2011,
<doi:10.18637/jss.v040.i08>), the book by Eddelbuettel (2013,
<doi:10.1007/978-1-4614-6868-4>) and the paper by Eddelbuettel and
Balamuta (2017, <doi:10.7287/peerj.preprints.3188v1>); see
'citation("Rcpp")' for details.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
Development files and headers needed to build software using %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description    doc
Documentation, help files, and examples for %{name}.

%prep
%setup -q -c -n %{packname}
sed -i -e '/^#!\//, 1d' %{packname}/inst/discovery/*.R
sed -i -e '/^#!\//, 1d' %{packname}/inst/examples/*/*.R
sed -i -e '/^#!\//, 1d' %{packname}/inst/examples/*/*.r
sed -i -e '/^#!\//, 1d' %{packname}/inst/unitTests/*.R
chmod a-x %{packname}/inst/discovery/*.R
chmod a-x %{packname}/inst/examples/*/*.R
chmod a-x %{packname}/inst/examples/*/*.r
chmod a-x %{packname}/inst/unitTests/*.R

%build
#Not needed

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
%fdupes %{buildroot}%{rlibdir}/%{packname}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/bib/
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/libs/
%{rlibdir}/%{packname}/unitTests/
%{rlibdir}/%{packname}/skeleton/
%{rlibdir}/%{packname}/discovery/
%{rlibdir}/%{packname}/prompt/

%files devel
%defattr(-, root, root, -)
%{rlibdir}/%{packname}/include/

%files doc
%defattr(-, root, root, -)
%doc %{rlibdir}/%{packname}/announce/
%doc %{rlibdir}/%{packname}/doc/
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/html/

%changelog
