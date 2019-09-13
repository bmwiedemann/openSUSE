#
# spec file for package R-httpuv
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global packname  httpuv
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.4.5.1
Release:        0
Summary:        HTTP and WebSocket server library
License:        GPL-3.0-only
Group:          Development/Libraries/Other
URL:            https://github.com/rstudio/httpuv
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-Rcpp-devel
BuildRequires:  R-base-devel
BuildRequires:  R-methods
BuildRequires:  R-promises R-later R-BH
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-Rcpp
Requires:       R-base
Requires:       R-methods
Requires:       R-promises R-later R-BH
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif

%description
httpuv provides low-level socket and protocol support for handling HTTP
and WebSocket requests directly from within R. It is primarily intended as
a building block for other packages, rather than making it particularly
easy to create complete web applications using httpuv alone. httpuv is
built on top of the libuv and http-parser C libraries, both of which were
developed by Joyent, Inc. (See LICENSE file for libuv and http-parser
license information.)

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/demo
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%changelog
