#
# spec file for package libsrtp2
#
# Copyright (c) 2020 SUSE LLC
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
Version:        2.3.0
Release:        0
Summary:        Secure Real-Time Transport Protocol (SRTP) library v2
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/cisco/libsrtp

Source:         https://github.com/cisco/libsrtp/archive/v%version.tar.gz
Source99:       baselibs.conf
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(openssl) >= 1.0.1
# srtp was last used in openSUSE 13.1.
Provides:       srtp = %version
Obsoletes:      srtp < %version

%description
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

%package -n %lname
Summary:        Secure Real-Time Transport Protocol (SRTP) library v2
Group:          System/Libraries

%description -n %lname
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is
specified in RFC 3711. More information about the SRTP protocol
itself can be found on the Secure RTP page.

%package devel
Summary:        Development files for the Secure Real-Time Transport Protocol (SRTP) library v2
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

This subpackage contains the development headers.

%prep
%autosetup -p1 -n libsrtp-%version

%build
%configure --enable-openssl
%make_build shared_library

%install
%make_install

# Same post-install modifications as for libsrtp v1.
#
# Including of files with generic names and quotes is unsafe and can cause include clashes.
# Do it in install phase, because rewriting of the source code before building would require deeper changes.
# %%_includedir is included automatically, so we don't modify .pc file. (bnc#839475#c2)
echo "Rewriting #include \"{foo}.h\" to #include <srtp/{foo}.h>..."
sed -i 's|\( *# *include *\)"\([^"]*\.h\)"|\1 <srtp/\2>|' %buildroot/%_includedir/srtp2/*.h

# Rewrite FOO_H just to make things consistent and prevent name clashes.
echo "Rewriting header include check tags from {FOO_H} to SRTP_{FOO_H}..."
sed -i 's|\(# *\(ifdef\|ifndef\|define\|endif */\*\) *\)\([A-Z0-9_]*_H\)\($\| *\*/\)|\1SRTP_\3\4|' %buildroot/%_includedir/srtp2/*.h

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
