#
# spec file for package R-RCurl
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


%global packname  RCurl
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.95_4.11
Release:        0
Summary:        General network (HTTP/FTP/...) client interface for R
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/Other
URL:            http://www.omegahat.net/RCurl
Source:         https://cran.r-project.org/src/contrib/%{packname}_1.95-4.11.tar.gz
BuildRequires:  R-base-devel
BuildRequires:  R-bitops
BuildRequires:  R-methods
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-base
Requires:       R-bitops
Requires:       R-methods
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif

%description
The package allows one to compose general HTTP requests and provides
convenient functions to fetch URIs, GET & POST forms, etc. and to process the
results returned by the Web server. This provides a great deal of control
over the HTTP/FTP/... connection and the form of the request while
providing a higher-level interface than is available just using R socket
connections. Additionally, the underlying implementation is
extensive, supporting FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS,
telnet, dict, ldap, and also supports cookies, redirects, authentication,

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/enums
%{rlibdir}/%{packname}/CurlSSL
%{rlibdir}/%{packname}/HTTPErrors
%{rlibdir}/%{packname}%{_sysconfdir}/

%changelog
