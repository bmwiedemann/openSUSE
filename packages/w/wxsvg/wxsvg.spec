#
# spec file for package wxsvg
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2019 Mariusz Fik <fisiu@opensuse.org>
# Copyright (c) 2012 Stefan Seyfried <seife+obs@b1-systems.com>
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


%define sover   3
Name:           wxsvg
Version:        1.5.20
Release:        0
Summary:        Library to create, manipulate and render SVG files
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://wxsvg.sourceforge.net/
Source:         https://prdownloads.sourceforge.net/wxsvg/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libart-2.0)
# WARNING: needs to build with the same ffmpeg libraries as DVDStyler.
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libswscale)

%description
WxSVG is a C++ library to create, manipulate and render SVG files.

%package -n     lib%{name}%{sover}
Summary:        Library to create, manipulate and render SVG files
Group:          System/Libraries

%description -n lib%{name}%{sover}
Dynamic libraries from %{name}, as required at runtime.

%package -n     lib%{name}-devel
Summary:        Header files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       lib%{name}%{sover} = %{version}
Requires:       wxWidgets-devel >= 3
Requires:       pkgconfig(expat)
Requires:       pkgconfig(libart-2.0)

%description -n lib%{name}-devel
Include files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog TODO
%{_bindir}/svgview
%license COPYING

%files -n lib%{name}%{sover}
%{_libdir}/libwxsvg.so.%{sover}
%{_libdir}/libwxsvg.so.%{sover}.*

%files -n lib%{name}-devel
%{_includedir}/wxSVG
%{_includedir}/wxSVGXML
%{_libdir}/libwxsvg.so
%{_libdir}/pkgconfig/libwxsvg.pc

%changelog
