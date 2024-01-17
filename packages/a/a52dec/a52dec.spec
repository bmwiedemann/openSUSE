#
# spec file for package a52dec
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


%define lib       liba52
%define libname   %{lib}-0

Name:           a52dec
Version:        0.8.0
Release:        0
Summary:        ATSC A/52 stream decoder library
License:        GPL-2.0-or-later
URL:            https://git.adelielinux.org/community/a52dec/
Source:         https://distfiles.adelielinux.org/source/a52dec/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       %{libname} = %{version}
Provides:       a52 = %{version}
Obsoletes:      a52 < %{version}

%description
liba52 is a library for decoding ATSC A/52 streams.

%package -n %{libname}
Summary:        ATSC A/52 stream decoder library
Provides:       %{lib} = %{version}
Obsoletes:      %{lib} < %{version}
Provides:       liba52dec0 = %{version}
Obsoletes:      liba52dec0 < %{version}

%description -n %{libname}
liba52 is a library for decoding ATSC A/52 streams.
Shared library part of a52dec.

%package -n %{lib}-devel
Summary:        Header files for the a52dec library
Requires:       %{libname} = %{version}
Provides:       a52dec-devel = %{version}
Obsoletes:      a52dec-devel < %{version}
Provides:       liba52dec-devel = %{version}
Obsoletes:      liba52dec-devel < %{version}

%description -n %{lib}-devel
Header files and static library for the a52dec library.
Install this package if you want to compile programs using the library.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
	--disable-static \
	--enable-shared \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libname}

%files
%license COPYING
%doc README ChangeLog AUTHORS HISTORY NEWS TODO
%{_bindir}/%{name}
%{_bindir}/extract_a52
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/extract_a52.1%{?ext_man}

%files -n %{libname}
%{_libdir}/%{lib}.so.*

%files -n %{lib}-devel
%{_includedir}/%{name}/
%{_libdir}/%{lib}.so
%{_libdir}/pkgconfig/%{lib}.pc

%changelog
