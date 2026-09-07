#
# spec file for package openslide
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


%define soversion 1

Name:           openslide
Version:        4.0.1
Release:        0
Summary:        C library for reading virtual slides
License:        LGPL-2.1-only
URL:            https://openslide.org/
Source0:        https://github.com/openslide/openslide/releases/download/v%{version}/openslide-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdicom)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.

%package -n libopenslide%{soversion}
Summary:        C library for reading virtual slides

%description -n libopenslide%{soversion}
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.

%package -n libopenslide-devel
Summary:        Development files for openslide
Requires:       libopenslide%{soversion} = %{version}
Recommends:     libopenslide-doc = %{version}

%description -n libopenslide-devel
This package contains libraries and header files for
developing applications that use openslide.

%package doc
Summary:        Documentation for openslide
BuildArch:      noarch

%description doc
This package contains documentation for developing with openslide library.

%package tools
Summary:        Command line tools for openslide
Requires:       libopenslide%{soversion} = %{version}

%description tools
This package contains command line tools for working with virtual slides.

%prep
%autosetup -p1

%build
# Note: Building without '-Dtest=disabled' fails without network access. A test is still executed.
%meson -Dtest=disabled

%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n libopenslide%{soversion}

%files -n libopenslide%{soversion}
%license COPYING.LESSER
%doc CHANGELOG.md README.md
%{_libdir}/*.so.%{soversion}*

%files -n libopenslide-devel
%{_includedir}/openslide/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%doc doc/html/

%files tools
%{_bindir}/openslide*
%{_bindir}/slidetool
%{_mandir}/man1/openslide*.1%{?ext_man}
%{_mandir}/man1/slidetool.1%{?ext_man}

%changelog
