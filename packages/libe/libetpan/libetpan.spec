#
# spec file for package libetpan
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_with     libetpan_fsanitize
%define sover 26
Name:           libetpan
Version:        1.10.1
Release:        0
Summary:        Mail Handling Library
License:        BSD-3-Clause
URL:            https://www.etpan.org/libetpan.html
Source0:        %name-%version.tar.xz
Patch0:         %name.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  db-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(zlib)

%description
libEtPan is a mail purpose library. It will be used for low-level mail
handling: network protocols (IMAP/NNTP/POP3/SMTP over TCP/IP and
SSL/TCP/IP, already implemented), local storage (mbox/MH/maildir) and
and message / MIME parsing.

%package -n libetpan%{sover}
Summary:        Mail handling library
Provides:       %name = %version-%release
Obsoletes:      %name < %version-%release

%description -n libetpan%{sover}
libEtPan is a mail purpose library. It will be used for low-level mail
handling: network protocols (IMAP/NNTP/POP3/SMTP over TCP/IP and
SSL/TCP/IP, already implemented), local storage (mbox/MH/maildir)
and message / MIME parsing.

%package -n libetpan-devel
Summary:        Development files for libetpan, a mail handling library
Requires:       db-devel
Requires:       libetpan%{sover} = %version-%release
Requires:       pkgconfig(gnutls)
Requires:       pkgconfig(gpg-error)
Requires:       pkgconfig(libgcrypt)
Requires:       pkgconfig(libsasl2)
Requires:       pkgconfig(zlib)

%description -n libetpan-devel
libEtPan is a mail purpose library. It will be used for low-level mail
handling: network protocols (IMAP/NNTP/POP3/SMTP over TCP/IP and
SSL/TCP/IP, already implemented), local storage (mbox/MH/maildir)
and message / MIME parsing.

%prep
%autosetup -p1

%build
touch README INSTALL COPYING
env NOCONFIGURE=1 ./autogen.sh
CFLAGS='%optflags -Wno-unused-function -Wno-unused-parameter -std=gnu11'
%if %{with libetpan_fsanitize}
CFLAGS="$CFLAGS -fsanitize=address,undefined"
sed -i~ 's|^Cflags:|Cflags: -fsanitize=address,undefined|' libetpan.pc.in
diff -u "$_"~ "$_" && exit 123
%endif
%configure \
	--without-curl \
	--without-expat \
	--with-gnutls \
	--enable-ipv6 \
	--without-openssl \
	--with-poll \
	--with-sasl \
	--disable-static \
	--with-zlib \
	%nil
%make_build

%install
%make_install
# remove unneeded *.la files
rm %{buildroot}%{_libdir}/libetpan.la

%ldconfig_scriptlets -n libetpan%{sover}

%files -n libetpan%{sover}
%license COPYRIGHT
%{_libdir}/libetpan.so.%{sover}*

%files -n libetpan-devel
%{_includedir}/libetpan/
%{_includedir}/libetpan.h
%{_libdir}/libetpan.so
%{_libdir}/pkgconfig/libetpan.pc

%changelog
