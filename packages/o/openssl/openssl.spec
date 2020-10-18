#
# spec file for package openssl
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _sonum  1_1
Name:           openssl
Version:        1.1.1h
Release:        0
Summary:        Secure Sockets and Transport Layer Security
# Yes there is no license but to not confuse people keep it aligned to the pkg
License:        OpenSSL
Group:          Productivity/Networking/Security
Url:            https://www.openssl.org/
Source0:        README.SUSE
Source99:       baselibs.conf
BuildRequires:  libopenssl%{_sonum} = %{version}
Requires:       openssl-%{_sonum} = %{version}
# the debuginfo package is now openssl-%{_sonum}-debuginfo (boo#1040172)
Obsoletes:      openssl-debuginfo
BuildArch:      noarch

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
Provides:       pkgconfig(libssl) = %{version}
Provides:       pkgconfig(libopenssl) = %{version}
Provides:       pkgconfig(libcrypto) = %{version}
Provides:       pkgconfig(openssl) = %{version}

%description -n libopenssl-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
cp %{SOURCE0} .

%build
:

%install
:

%files
%defattr(-, root, root)
%doc README.SUSE

%files -n libopenssl-devel
%defattr(-, root, root)
%doc README.SUSE

%changelog
