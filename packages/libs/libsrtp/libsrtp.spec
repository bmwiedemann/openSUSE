#
# spec file for package libsrtp
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


%define soname	1
Name:           libsrtp
Version:        1.6.0
Release:        0
Summary:        Secure Real-Time Transport Protocol (SRTP) library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/cisco/libsrtp
#Git-Clone:	git://github.com/cisco/libsrtp.git
Source:         https://github.com/cisco/libsrtp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc
BuildRequires:  pkg-config
# srtp was last used in openSUSE 13.1.
Provides:       srtp = %{version}
Obsoletes:      srtp < %{version}

%description
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

%package -n %{name}%{soname}
Summary:        Secure Real-Time Transport Protocol (SRTP) library
Group:          System/Libraries

%description -n %{name}%{soname}
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is
specified in RFC 3711. More information about the SRTP protocol
itself can be found on the Secure RTP page.

%package devel
Summary:        Development files for the Secure Real-Time Transport Protocol (SRTP) library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}
# srtp-devel was last used in openSUSE 13.1.
Provides:       srtp-devel = %{version}
Obsoletes:      srtp-devel < %{version}

%description devel
libsrtp is an implementation of the Secure Real-time Transport
Protocol (SRTP) originally authored by Cisco Systems, Inc.

This subpackage contains the development headers.

%prep
%setup -q

%build
%configure \
  --enable-generic-aesicm \
  --enable-syslog
# Doesn't work with OpenSSL 1.1
#  --enable-openssl
#  --enable-gdoi
# FIXME: Does not work:
#  --enable-kernel-linux

make shared_library %{?_smp_mflags}

%install
%make_install

# Make libsrtp.so a symlink.
ln -sf %{name}.so.%{soname} %{buildroot}%{_libdir}/%{name}.so

# Including of files with generic names and quotes is unsafe and can cause include clashes.
# Do it in install phase, because rewriting of the source code before building would require deeper changes.
# /usr/include is included automatically, so we don't modify .pc file. (bnc#839475#c2)
echo "Rewriting #include \"{foo}.h\" to #include <srtp/{foo}.h>..."
sed -i 's|\( *# *include *\)"\([^"]*\.h\)"|\1 <srtp/\2>|' %{buildroot}%{_includedir}/srtp/*.h

# Rewrite FOO_H just to make things consistent and prevent name clashes.
echo "Rewriting header include check tags from {FOO_H} to SRTP_{FOO_H}..."
sed -i 's|\(# *\(ifdef\|ifndef\|define\|endif */\*\) *\)\([A-Z0-9_]*_H\)\($\| *\*/\)|\1SRTP_\3\4|' %{buildroot}%{_includedir}/srtp/*.h
sed -i 's|\(# *\(ifdef\|ifndef\|define\|endif */\*\) *\)\(CRYPTO_KERNEL\|RAND_SOURCE\)\($\| *\*/\)|\1SRTP_\3_H\4|' %{buildroot}%{_includedir}/srtp/*.h

# And finally, prevent all potential clashes in autoconf based variables in config.h.
for SYMBOL in \
  $(sed -n '
    # Everything below const is a definition of the compiler and hopefully undefined.
    /const/,$d
    # Search and print autoconf generated defines.
    s|\(^# *define\|/\* # *undef\) \([A-Z0-9_]*\).*$|\2|p
    ' < %{buildroot}%{_includedir}/srtp/config.h
  ); do
    echo "Rewriting symbol $SYMBOL to SRTP_$SYMBOL..."
    sed -i 's|\([^A-Z0-9_]\)\('$SYMBOL'\)\([^A-Z0-9_]\|$\)|\1SRTP_\2\3|g' %{buildroot}%{_includedir}/srtp/*.h
done

# remove openssl header files incompatible with OpenSSL 1.1
rm %{buildroot}%{_includedir}/srtp/aes_{g,i}cm_ossl.h

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-,root,root)
%{_libdir}/libsrtp.so.*

%files devel
%defattr(-,root,root)
%doc CHANGES LICENSE README TODO VERSION doc/*.pdf doc/*.txt
%{_includedir}/srtp/
%{_libdir}/libsrtp.so
%{_libdir}/pkgconfig/libsrtp.pc

%changelog
