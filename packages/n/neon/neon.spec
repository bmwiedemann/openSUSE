#
# spec file for package neon
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 27
Name:           neon
Version:        0.34.0
Release:        0
Summary:        An HTTP and WebDAV Client Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            https://notroj.github.io/neon/
Source0:        https://notroj.github.io/neon/neon-%{version}.tar.gz
Source3:        baselibs.conf
Patch0:         neon-0.28.4-bloat.patch
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
neon is an HTTP and WebDAV client library with a C interface.

%package -n libneon%{sover}
Summary:        An HTTP and WebDAV Client Library
# Drop the main package. It avoids the lib from being installed in different versions
# and generally only contained coders doc anyhow.
Group:          Development/Libraries/Other
Provides:       neon = %{version}
Obsoletes:      neon < %{version}

%description -n libneon%{sover}
neon is an HTTP and WebDAV client library with a C interface.

%package -n libneon-devel
Summary:        An HTTP and WebDAV Client Library
Group:          Development/Libraries/Other
Requires:       libneon%{sover} = %{version}
# renamed after openSUSE 10.3
Provides:       neon-devel = %{version}
Obsoletes:      neon-devel < %{version}

%description -n libneon-devel
neon is an HTTP and WebDAV client library with a C interface.

%prep
%autosetup -p1

%build
%configure \
    --with-ssl \
    --enable-threadsafe-ssl=posix \
    --with-libproxy \
    --with-expat \
    --disable-nls \
    --enable-shared \
    --disable-static \
    --enable-warnings
%make_build

%install
%make_install \
	docdir=%{_defaultdocdir}/%{name} \
	%{nil}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}/%{_mandir}

%check
export TEST_QUIET=0
%make_build check

%ldconfig_scriptlets -n libneon%{sover}

%files -n libneon%{sover}
%license src/COPYING.LIB
%doc AUTHORS BUGS NEWS THANKS TODO
%{_libdir}/*.so.%{sover}
%{_libdir}/*.so.%{sover}.*

%files -n libneon-devel
%license src/COPYING.LIB
%doc %{_defaultdocdir}/%{name}
%{_bindir}/neon-config
%{_includedir}/neon
%{_mandir}/man*/*%{?ext_man}
%{_libdir}/*.so
%{_libdir}/pkgconfig/neon.pc

%changelog
