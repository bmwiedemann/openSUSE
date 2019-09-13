#
# spec file for package curl
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

%global packname  curl
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        3.2
Release:        0
Summary:        A Web Client for R
Group:          Development/Libraries/Other
License:        MIT
URL:            http://cran.r-project.org/web/packages/%{packname}
Source:         http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-base
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes
BuildRequires:  R-base-devel
BuildRequires:  libcurl-devel
BuildRequires:  gcc-c++

%description
The curl() and curl_download() functions provide configurable
drop-in replacements for base url() and download.file() with better
performance, support for encryption (https, ftps), gzip compression,
authentication, and other 'libcurl' goodies. The core of the package
implements a framework for performing customized requests where data
can be processed either in memory, on disk, or streaming via the callback
or connection interfaces. Some knowledge of 'libcurl' is recommended; for
a more-user-friendly web client, see the 'httr' package which builds on
this package with http specific tools and logic.

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
%doc %{rlibdir}/curl/html
%doc %{rlibdir}/curl/doc
%doc %{rlibdir}/curl/NEWS
%{rlibdir}/curl/help
%{rlibdir}/curl/INDEX
%{rlibdir}/curl/LICENSE
%{rlibdir}/curl/WORDLIST
%{rlibdir}/curl/libs
%{rlibdir}/curl/Meta
%{rlibdir}/curl/data
%{rlibdir}/curl/DESCRIPTION
%{rlibdir}/curl/R
%{rlibdir}/curl/NAMESPACE

%changelog
