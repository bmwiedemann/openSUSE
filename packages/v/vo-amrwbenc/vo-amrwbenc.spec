#
# spec file for package vo-amrwbenc
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

%define so_nr   0

Name:           vo-amrwbenc
Version:        0.1.3+5
Release:        0
Summary:        VisualOn AMR-WB encoder library
License:        Apache-2.0
Group:          System/Libraries
URL:            http://opencore-amr.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  c_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
This library contains an encoder implementation of the Adaptive
Multi Rate Wideband (AMR-WB) audio codec. The library is based
on a codec implementation by VisualOn as part of the Stagefright
framework from the Google Android project.

%package        -n lib%{name}%{so_nr}
Summary:        VisualOn AMR-WB encoder library
Group:          System/Libraries

%description    -n lib%{name}%{so_nr}
This library contains an encoder implementation of the Adaptive
Multi Rate Wideband (AMR-WB) audio codec. The library is based
on a codec implementation by VisualOn as part of the Stagefright
framework from the Google Android project.

%package        -n lib%{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{so_nr} = %{version}

%description    -n lib%{name}-devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-silent-rules \
	--disable-static \
	%{nil}
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n lib%{name}%{so_nr}

%files -n lib%{name}%{so_nr}
%license COPYING
%doc README NOTICE
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
