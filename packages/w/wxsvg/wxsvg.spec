#
# spec file for package wxsvg
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.5.23
Release:        0
Summary:        Library to create, manipulate and render SVG files
License:        LGPL-2.1-or-later WITH WxWindows-exception-3.1
URL:            http://wxsvg.sourceforge.net/
Source:         https://prdownloads.sourceforge.net/wxsvg/%{name}-%{version}.tar.bz2
Patch:          ffmpeg5.patch
Patch1:         wxsvg-fix-missing-include.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  wxGTK3-3_2-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(pangocairo)
# WARNING: needs to build with the same ffmpeg libraries as DVDStyler.
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libswscale)

%description
WxSVG is a C++ library to create, manipulate and render SVG files.

%package -n     lib%{name}%{sover}
Summary:        Library to create, manipulate and render SVG files

%description -n lib%{name}%{sover}
Dynamic libraries from %{name}, as required at runtime.

%package -n     lib%{name}-devel
Summary:        Header files for %{name}
Requires:       %{name} = %{version}
Requires:       lib%{name}%{sover} = %{version}
Requires:       wxGTK3-3_2-devel
Requires:       pkgconfig(expat)
Requires:       pkgconfig(libart-2.0)

%description -n lib%{name}-devel
Include files for developing programs based on %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n lib%{name}%{sover}

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
