#
# spec file for package R-BH
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


%global packname  BH
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.69.0.1
Release:        0
Summary:        Boost C++ Header Files
License:        BSL-1.0
Group:          Development/Libraries/Other
URL:            http://cran.r-project.org/web/packages/%{packname}
Source:         http://cran.r-project.org/src/contrib/%{packname}_1.69.0-1.tar.gz
Source2:        R-BH-rpmlintrc
BuildRequires:  R-base-devel
BuildRequires:  fdupes
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-base

%description
Boost provides free peer-reviewed portable C++ source libraries.  A large
part of Boost is provided as C++ template code which is resolved entirely
at compile-time without linking.  This package aims to provide the most
useful subset of Boost libraries for template use among CRAN package. By
placing these libraries in this package, we offer a more efficient
distribution system for CRAN as replication of this code in the sources of
other packages is avoided. As of release 1.69.0-1, the following Boost
libraries are included: 'algorithm' 'align' 'any' 'atomic' 'bimap' 'bind'
'circular_buffer' 'compute' 'concept' 'config' 'container' 'date_time'
'detail' 'dynamic_bitset' 'exception' 'filesystem' 'flyweight' 'foreach'
'functional' 'fusion' 'geometry' 'graph' 'heap' 'icl' 'integer'
'interprocess' 'intrusive' 'io' 'iostreams' 'iterator' 'math' 'move' 'mpl'
'multiprcecision' 'numeric' 'pending' 'phoenix' 'preprocessor'
'propery_tree' 'random' 'range' 'scope_exit' 'smart_ptr' 'sort' 'spirit'
'tuple' 'type_traits' 'typeof' 'unordered' 'utility' 'uuid'.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
%fdupes %{buildroot}%{rlibdir}/%{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/BH/html
%{rlibdir}/BH/NAMESPACE
%{rlibdir}/BH/Meta
%{rlibdir}/BH/NEWS.Rd
%{rlibdir}/BH/DESCRIPTION
%{rlibdir}/BH/INDEX
%{rlibdir}/BH/help
%{rlibdir}/BH/include

%changelog
