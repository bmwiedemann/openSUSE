#
# spec file for package R-openssl
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


%global packname  openssl
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        1.1
Release:        0
Summary:        Toolkit for Encryption, Signatures and Certificates Based on OpenSSL
License:        MIT
Group:          Development/Libraries/Other
URL:            https://cran.r-project.org/package=%{packname}
Source:         https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-base-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  openssl-devel >= 1.0.1
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-base

%description
Bindings to OpenSSL libssl and libcrypto, plus custom SSH pubkey parsers.
Supports RSA, DSA and EC curves P-256, P-384 and P-521. Cryptographic
signatures can either be created and verified manually or via x509
certificates. AES can be used in cbc, ctr or gcm mode for symmetric
encryption; RSA for asymmetric (public key) encryption or EC for Diffie
Hellman. High-level envelope functions combine RSA and AES for encrypting
arbitrary sized data. Other utilities include key generators, hash
functions (md5, sha1, sha256, etc), base64 encoder, a secure random number
generator, and 'bignum' math methods for manually performing crypto
calculations on large multibyte integers.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description    doc
Documentation and help files for %{name}.

%prep
%setup -q -c -n %{packname}

%build
#Not needed

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/cacert.pem
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/libs/

%files doc
%doc %{rlibdir}/%{packname}/doc/
%doc %{rlibdir}/%{packname}/html/

%changelog
