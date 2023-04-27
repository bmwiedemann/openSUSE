#
# spec file for package libsrtp2
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libsrtp2
%define lname	libsrtp2-1
Version:        2.5.0
Release:        0
Summary:        Secure Real-Time Transport Protocol (SRTP) library v2
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/cisco/libsrtp

Source:         https://github.com/cisco/libsrtp/archive/v%version.tar.gz
Source99:       baselibs.conf
Patch1:         libsrtp2-test-verbose.patch
BuildRequires:  libpcap-devel
BuildRequires:  pkg-config
BuildRequires:  procps
BuildRequires:  pkgconfig(openssl) >= 1.1.0

%description
libsrtp is Cisco's implementation of the Secure Real-time Transport
Protocol (SRTP), the Universal Security Transform (UST), and a
supporting cryptographic kernel.

%package -n %lname
Summary:        Secure Real-Time Transport Protocol (SRTP) library v2
Group:          System/Libraries

%description -n %lname
libsrtp is Cisco's implementation of the Secure Real-time Transport
Protocol (SRTP), the Universal Security Transform (UST), and a
supporting cryptographic kernel.

SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is
specified in RFC 3711. More information about the SRTP protocol
itself can be found on the Secure RTP page.

%package devel
Summary:        Development files for the Secure Real-Time Transport Protocol (SRTP) library v2
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libsrtp is Cisco's implementation of the Secure Real-time Transport
Protocol (SRTP), the Universal Security Transform (UST), and a
supporting cryptographic kernel.

This subpackage contains the development headers.

%prep
%autosetup -p1 -n libsrtp-%version

%build
%configure --enable-openssl
%make_build shared_library

%install
%make_install

%check
%make_build runtest

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libsrtp2.so.1

%files devel
%doc CHANGES README.md doc/*.txt
%license LICENSE
%_includedir/srtp2/
%_libdir/libsrtp2.so
%_libdir/pkgconfig/libsrtp2.pc

%changelog
