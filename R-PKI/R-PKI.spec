#
# spec file for package R-PKI
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

%global packname  PKI
%global rlibdir   %{_libdir}/R/library

Name:           R-%{packname}
Version:        0.1_5
Release:        0
Summary:        Public Key Infrastucture for R Based on the X.509 Standard
Group:          Development/Libraries/Other
License:        GPL-2.0+
URL:            http://www.rforge.net/PKI/
Source:         http://www.rforge.net/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       R-base
Requires:       R-base64enc 
BuildRequires:  texlive
BuildRequires:  texinfo
BuildRequires:  fdupes
BuildRequires:  openssl-devel
%if 0%{?suse_version} <= 1220 && 0%{?suse_version} != 1110
BuildRequires:  texlive-fonts-extra
%endif
BuildRequires:  R-base-devel R-base64enc
BuildRequires:  gcc-c++
 

%description
PKI functions such as verifying certificates, RSA encription and signing
which can be used to build PKI infrastructure and perform cryptographic tasks.

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
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/certs

%changelog
