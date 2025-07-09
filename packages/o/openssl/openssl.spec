#
# spec file for package openssl
#
# Copyright (c) 2025 SUSE LLC
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


%define _sonum  3
Name:           openssl
Version:        3.5.1
Release:        0
Summary:        Secure Sockets and Transport Layer Security
# Yes there is no license but to not confuse people keep it aligned to the pkg
License:        Apache-2.0
Group:          Productivity/Networking/Security
URL:            https://www.openssl.org/
Source0:        README.SUSE
Source99:       baselibs.conf
BuildRequires:  libopenssl%{_sonum} = %{version}
Requires:       openssl-%{_sonum} = %{version}
# the debuginfo package is now openssl-%%{_sonum}-debuginfo (boo#1040172)
Obsoletes:      openssl-debuginfo
BuildArch:      noarch
Conflicts:      openssl(cli)
Provides:       openssl(cli)

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, full-featured, and open source toolkit implementing
the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS
v1) protocols with full-strength cryptography. The project is managed
by a worldwide community of volunteers that use the Internet to
communicate, plan, and develop the OpenSSL toolkit and its related
documentation.

%package -n libopenssl-devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libopenssl%{_sonum} = %{version}
Requires:       libopenssl-%{_sonum}-devel = %{version}
Requires:       pkgconfig
Obsoletes:      openssl-devel < %{version}
Provides:       openssl-devel = %{version}
Provides:       pkgconfig(libcrypto) = %{version}
Provides:       pkgconfig(libopenssl) = %{version}
Provides:       pkgconfig(libssl) = %{version}
Provides:       pkgconfig(openssl) = %{version}

%description -n libopenssl-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libopenssl-fips-provider
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} >= 3.0.0
Requires:       libopenssl%{_sonum} >= 3.0.0
Requires:       pkgconfig

%description -n libopenssl-fips-provider
This package contains OpenSSL FIPS provider.

%prep
cp %{SOURCE0} .

%build
:

%install
:

%files
%doc README.SUSE

%files -n libopenssl-devel
%doc README.SUSE

%files -n libopenssl-fips-provider
%doc README.SUSE

%changelog
