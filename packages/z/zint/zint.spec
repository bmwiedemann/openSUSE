#
# spec file for package zint
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


%define so_ver 2_16
Name:           zint
Version:        2.16.0
Release:        0
Summary:        Barcode generator library
License:        GPL-3.0-or-later
URL:            https://sourceforge.net/projects/zint/
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
Source99:       baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
Zint is a C library for encoding data in several barcode variants. The
bundled command-line utility provides a simple interface to the library.
Features of the library:
- Over 50 symbologies including all ISO/IEC standards, like QR codes.
- Unicode translation for symbologies which support Latin-1 and
  Kanji character sets.
- Full GS1 support including data verification and automated insertion of
  FNC1 characters.
- Support for encoding binary data including NULL (ASCII 0) characters.
- Health Industry Barcode (HIBC) encoding capabilities.
- Output in PNG, EPS and SVG formats with user adjustable sizes and colors.
- Verification stage for SBN, ISBN and ISBN-13 data.

%package qt
Summary:        Zint Barcode Studio

%description qt
Zint Barcode Studio is a Qt-based GUI which allows desktop users to generate
barcodes which can then be embedded in documents or HTML pages.

%package -n libzint%{so_ver}
Summary:        Barcode generator library

%description -n libzint%{so_ver}
Zint is a C library for encoding data in several barcode variants. The
bundled command-line utility provides a simple interface to the library.
Features of the library:
- Over 50 symbologies including all ISO/IEC standards, like QR codes.
- Unicode translation for symbologies which support Latin-1 and
  Kanji character sets.
- Full GS1 support including data verification and automated insertion of
  FNC1 characters.
- Support for encoding binary data including NULL (ASCII 0) characters.
- Health Industry Barcode (HIBC) encoding capabilities.
- Output in PNG, EPS and SVG formats with user adjustable sizes and colors.
- Verification stage for SBN, ISBN and ISBN-13 data.

%package -n libzint-devel
Summary:        Development files for Zint
Requires:       libzint%{so_ver} = %{version}
Requires:       pkgconfig(libpng)

%description -n libzint-devel
C library and header files needed to develop applications that use
the Zint library. The API documentation can be found on the project website:
http://www.zint.org.uk/zintSite/Manual.aspx

%package -n libQZint%{so_ver}
Summary:        Qt version of Zint library

%description -n libQZint%{so_ver}
Qt version of Zint library.

%package -n libQZint-devel
Summary:        Development files for Qt version of Zint library
Requires:       libQZint%{so_ver} = %{version}
Requires:       libzint-devel = %{version}

%description -n libQZint-devel
C library and header files needed to develop applications that use libQZint.

%prep
%autosetup -p1 -n %{name}-%{version}-src

# remove bundled getopt sources (we use the corresponding package instead)
rm -r getopt

# zint 2.10 wrongly creates a static QZint library
sed -i 's#STATIC#SHARED#' backend_qt/CMakeLists.txt

%build
%cmake_qt6 -DDATA_INSTALL_DIR:STRING=%{_datadir} -DZINT_QT6:BOOL=TRUE

%qt6_build

%install
%qt6_install

install -D -p -m 644 zint-qt.png %{buildroot}%{_datadir}/pixmaps/zint-qt.png
install -D -p -m 644 zint-qt.desktop %{buildroot}%{_datadir}/applications/zint-qt.desktop

%check
%ctest --parallel 1 --timeout 60 --verbose --exclude-regex 'qzint'

%ldconfig_scriptlets -n libzint%{so_ver}
%ldconfig_scriptlets -n libQZint%{so_ver}

%files
%doc ChangeLog README
%{_bindir}/zint
%{_mandir}/man1/zint.1%{?ext_man}

%files qt
%{_bindir}/zint-qt
%{_datadir}/applications/zint-qt.desktop
%{_datadir}/pixmaps/zint-qt.png

%files -n libzint%{so_ver}
%license LICENSE
%{_libdir}/libzint.so.*

%files -n libzint-devel
%{_includedir}/zint.h
%{_libdir}/libzint.so
%{_libdir}/cmake/zint/

%files -n libQZint%{so_ver}
%{_libdir}/libQZint.so.*

%files -n libQZint-devel
%{_includedir}/qzint.h
%{_libdir}/libQZint.so

%changelog
