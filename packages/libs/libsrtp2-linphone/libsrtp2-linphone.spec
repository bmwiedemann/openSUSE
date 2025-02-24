#
# spec file for package libsrtp2-linphone
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


%define so_ver	1
Name:           libsrtp2-linphone
Version:        2.4.2~git.20240220
Release:        0
Summary:        BC's fork of the Secure Real-Time Transport Protocol (SRTP) library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://gitlab.linphone.org/BC/public/external/srtp
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf
Patch0:         change-name.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libopenssl-devel
BuildRequires:  libpcap-devel
BuildRequires:  meson >= 0.52.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

%package -n     %{name}%{so_ver}
Summary:        Secure Real-Time Transport Protocol (SRTP) library
Group:          System/Libraries

%description -n %{name}%{so_ver}
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is
specified in RFC 3711. More information about the SRTP protocol
itself can be found on the Secure RTP page.

%package devel
Summary:        Development files for the Secure Real-Time Transport Protocol (SRTP) library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{so_ver} = %{version}

%description devel
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

This subpackage contains the development headers.

%prep
%autosetup -p1

%build
%meson \
  -Dcrypto-library=openssl \
  -Dcrypto-library-kdf=disabled \
  -Ddoc=disabled
%meson_build

%install
%meson_install

%post -n %{name}%{so_ver} -p /sbin/ldconfig
%postun -n %{name}%{so_ver} -p /sbin/ldconfig

%files -n %{name}%{so_ver}
%{_libdir}/%{name}.so.%{so_ver}

%files devel
%license LICENSE
%doc CHANGES
%{_libdir}/%{name}.so
%dir %{_includedir}/srtp2-linphone
%{_includedir}/srtp2-linphone/auth.h
%{_includedir}/srtp2-linphone/cipher.h
%{_includedir}/srtp2-linphone/crypto_types.h
%{_includedir}/srtp2-linphone/srtp.h
%{_libdir}/pkgconfig/libsrtp2-linphone.pc

%changelog
