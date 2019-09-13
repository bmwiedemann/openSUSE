#
# spec file for package R-digest
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


%global packname  digest
%global rlibdir   %{_libdir}/R/library
Name:           R-%{packname}
Version:        0.6.18
Release:        0
Summary:        R package to create compact hash digests of R objects
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            https://cran.r-project.org/package=%{packname}
Source:         https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:  R-base-devel >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  texinfo
BuildRequires:  texlive
Requires:       R-base >= 3.1.0

%description
The digest package provides a function 'digest()' for the creation of hash
digests of arbitrary R objects (using the md5, sha-1, sha-256 and crc32
algorithms) permitting easy comparison of R language objects, as well as a
function 'hmac()' to create hash-based message authentication code. The
md5 algorithm by Ron Rivest is specified in RFC 1321, the sha-1 and
sha-256 algorithms are specified in FIPS-180-1 and FIPS-180-2, and the
crc32 algorithm is described in
ftp://ftp.rocksoft.com/cliens/rocksoft/papers/crc_v3.txt. . For md5,
sha-1, sha-256 and aes, this package uses a small standalone
implementations that were provided by Christophe Devine. For crc32, code
from the zlib library is used. For sha-512, an implementation by Aaron D.
Gifford is used. . Please note that this package is not meant to be
deployed for cryptographic purposes for which more comprehensive (and
widely tested) libraries such as OpenSSL should be used.

%package        devel
Summary:        Include files for R-digest
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
The digest package provides a function 'digest()' for the creation of hash
digests of arbitrary R objects (using the md5, sha-1, sha-256 and crc32
algorithms) permitting easy comparison of R language objects, as well as a
function 'hmac()' to create hash-based message authentication code.

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
%doc %{rlibdir}/%{packname}/doc/
%doc %{rlibdir}/%{packname}/html/
%doc %{rlibdir}/%{packname}/DESCRIPTION
%if 0%{?suse_version} == 1230
%doc %{rlibdir}/%{packname}/GPL-2
%else
%license %{rlibdir}/%{packname}/GPL-2
%endif
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/libs/

%files devel
%{rlibdir}/%{packname}/include/

%changelog
