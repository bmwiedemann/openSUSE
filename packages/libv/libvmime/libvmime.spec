#
# spec file for package libvmime
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libvmime
%define lname	libvmime-suse8
Version:        0.9.2+g203
Release:        0
Summary:        Library for working with RFC 5322, MIME messages and IMAP/POP/SMTP
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://vmime.org/

#Source:         https://github.com/kisli/vmime/archive/v%%version.tar.gz
Source:         vmime-%version.tar.xz
Patch1:         libvmime-nodatetime.diff
Patch2:         libvmime-soname.diff
BuildRequires:  cmake >= 2.8.3
BuildRequires:  gcc-c++
%if 0%{?rhel} || 0%{?fedora_version}
BuildRequires:  gnutls-devel
%else
BuildRequires:  libgnutls-devel
%endif
%if !0%{?sle_version}
BuildRequires:  libgsasl-devel
%endif
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  xz
%if 0%{?with_pdf}
BuildRequires:  ImageMagick
BuildRequires:  doxygen
BuildRequires:  inkscape
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-latex
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(fancyheadings.sty)
BuildRequires:  tex(pcrr7t.tfm)
BuildRequires:  tex(ucs.sty)
%endif

%description
VMime is a C++ class library for working with RFC5322 and
MIME-conforming messages (RFC2045–2049), as well as Internet
messaging services like IMAP, POP or SMTP.

VMime can parse, generate and modify messages, and also connect to
store and transport services to receive or send messages over the
Internet. The library offers features to build a mail client.

%package -n %lname
Summary:        Library for working with MIME messages and IMAP/POP/SMTP
Group:          System/Libraries

%description -n %lname
VMime is a C++ class library for working with RFC5322 and
MIME-conforming messages (RFC2045–2049), as well as Internet
messaging services like IMAP, POP or SMTP.

VMime can parse, generate and modify messages, and also connect to
store and transport services to receive or send messages over the
Internet. The library offers features to build a mail client.

%package devel
Summary:        Development files for vmime, an e-mail message library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
VMime is a C++ class library for working with RFC5322 and
MIME-conforming messages (RFC2045–2049), as well as Internet
messaging services like IMAP, POP or SMTP.

This subpackage contains the headers for the library's API.

%prep
%autosetup -p1 -n vmime-%version

%build
%if 0%{?with_pdf}
pushd doc/book/
make book_pdf
popd
%endif

%cmake \
        -DCMAKE_INSTALL_PREFIX:PATH="%_prefix" \
        -DINCLUDE_INSTALL_DIR:PATH="%_includedir" \
        -DSYSCONF_INSTALL_DIR:PATH="%_sysconfdir" \
        -DSHARE_INSTALL_PREFIX:PATH="%_datadir" \
        -DCMAKE_INSTALL_LIBDIR:PATH="%_libdir" \
	-DVMIME_SENDMAIL_PATH:STRING="%_sbindir/sendmail" \
	-DVMIME_BUILD_SAMPLES:BOOL=OFF \
%if 0%{?sle_version}
	-DVMIME_HAVE_SASL_SUPPORT:BOOL=OFF \
%endif
	-DVMIME_HAVE_TLS_SUPPORT:BOOL=ON \
	-DVMIME_BUILD_STATIC_LIBRARY:BOOL=OFF \
	-DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DVMIME_BUILD_DOCUMENTATION:BOOL=OFF
%cmake_build

%install
b="%buildroot"
%if 0%{?with_pdf}
mkdir -p "$b/%_docdir/%name"
cp -a doc/book/book.pdf "$b/%_docdir/%name/"
%endif
%cmake_install
find "$b" -type f -name "*.la" -delete

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING
%_libdir/libvmime-suse.so.*

%files devel
%_includedir/vmime
%_libdir/libvmime.so
%_libdir/libvmime-suse.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/
%if 0%{?with_pdf}
%_docdir/%name
%endif

%changelog
