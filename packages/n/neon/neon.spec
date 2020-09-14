#
# spec file for package neon
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


Name:           neon
Version:        0.31.2
Release:        0
Summary:        An HTTP and WebDAV Client Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            https://notroj.github.io/neon/
Source0:        https://notroj.github.io/neon/neon-%{version}.tar.gz
Source2:        %{name}.keyring
Source3:        baselibs.conf
Source10:       replace_manpage_with_links.sh
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/Packaging/Patches
Patch0:         %{name}-0.28.4-bloat.patch
Patch1:         fix_timeout_tests_for_ppc64le.patch
BuildRequires:  krb5-devel
BuildRequires:  libexpat-devel
BuildRequires:  libproxy-devel
BuildRequires:  libtool
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(openssl)

%description
neon is an HTTP and WebDAV client library with a C interface.

%package -n libneon27
Summary:        An HTTP and WebDAV Client Library
# Drop the main package. It avoids the lib from being installed in different versions
# and generally only contained coders doc anyhow.
Group:          Development/Libraries/Other
Provides:       neon = %{version}
Obsoletes:      neon < %{version}
#

%description -n libneon27
neon is an HTTP and WebDAV client library with a C interface.

%package -n libneon-devel
Summary:        An HTTP and WebDAV Client Library
Group:          Development/Libraries/Other
Requires:       glibc-devel
Requires:       libneon27 = %{version}
# renamed after openSUSE 10.3
Provides:       neon-devel = %{version}
Obsoletes:      neon-devel < %{version}

%description -n libneon-devel
neon is an HTTP and WebDAV client library with a C interface.

%prep
%setup -q
%patch0
%ifarch ppc64le ppc64
%patch1
%endif

%build
rm -f aclocal.m4 ltmain.sh
sh autogen.sh
%configure \
    --with-ssl \
    --enable-threadsafe-ssl=posix \
    --with-libproxy \
    --with-expat \
    --disable-nls \
    --enable-shared \
    --disable-static \
    --enable-warnings
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} docdir=%{_defaultdocdir}/%{name} install install-man install-html %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_mandir} -type f -exec bash %{S:10} {} \;

%check
make %{?_smp_mflags} check

%post -n libneon27 -p /sbin/ldconfig
%postun -n libneon27 -p /sbin/ldconfig

%files -n libneon27
%doc AUTHORS BUGS ChangeLog NEWS THANKS TODO
%{_libdir}/*.so.27*
%license src/COPYING.LIB

%files -n libneon-devel
%doc %{_defaultdocdir}/%{name}
%{_bindir}/neon-config
%dir %{_includedir}/neon
%{_includedir}/neon/*.h
%{_mandir}/*/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/neon.pc

%changelog
