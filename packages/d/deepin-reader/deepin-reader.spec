#
# spec file for package deepin-reader
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Hillwood Yang <hillwood@opensuse.org>
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

%define    sover            1
# Workaround boo#1189991
%define    _lto_cflags      %{nil}
%define    openjpeg_version	%(rpm -q --queryformat '%%{VERSION}' openjpeg2-devel)
%define    openjpeg_min     2.4.0

Name:           deepin-reader
Version:        5.10.23
Release:        0
Summary:        The deepin Document Viewer
License:        GPL-3.0+
Group:          Productivity/Office/Other
URL:            https://github.com/linuxdeepin/deepin-reader
Source0:        https://github.com/linuxdeepin/deepin-reader/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTEAM fix-library-link.patch hillwood@opensuse.org
Patch0:         fix-library-link.patch
# PATCH-FIX-UPSTEAM fix-libdir.patch hillwood@opensuse.org - Fix the hardcode libdir
Patch1:         fix-libdir.patch
# PATCH-FIX-UPSTEAM support-riscv.patch hillwood@opensuse.org
Patch2:         support-riscv.patch
BuildRequires:  fdupes
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(chardet)
# Requires:       libdeepin-pdfium%{sover}
# Qt5WebEngineWidgets is invalid on these arches
ExcludeArch:    ppc ppc64 ppc64le s390 s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
deepin-reader is a small, fast and full-featured tool for viewing documents,
supporting PDF and DJVU formats, multi-window and multi-tab management,thumbnail
viewing, adding bookmarks and notes, magnifying, slide show,searching texts,
rotation, etc.

%lang_package

%package -n libdeepin-pdfium%{sover}
Summary:        The library for deepin-reader
Group:          System/Libraries

%description -n libdeepin-pdfium%{sover}
The package provide pdf library for deepin-reader

%prep
%autosetup -p1
sed -i "s/lrelease/lrelease-qt5/g" translate_generation.sh updateTranslation.sh
sed -i "s/system(lrelease/system(lrelease-qt5/g" reader/reader.pro
sed -i "/#include <map>/a#include <cstdint>" tests/include/gtest/stub.h
%if "%{openjpeg_version}" > "%{openjpeg_min}"
sed -i "/#include/s|<openjpeg.h>|<openjpeg-2.5/openjpeg.h>|g" \
3rdparty/deepin-pdfium/src/3rdparty/pdfium/pdfium/core/fxcodec/jpx/{cjpx_decoder.h,jpx_decode_utils.h}
%endif

%build
%qmake5 DAPP_VERSION=%{version} \
        DEFINES+='VERSION=%{version}' \
        DEFINES+=QT_NO_DEBUG_OUTPUT \
        PREFIX=%{_prefix} \
        LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%qmake5_install
rm -rf %{buildroot}%{_libdir}/libdeepin-pdfium.so

%find_lang %{name} --with-qt

find %{buildroot}%{_datadir}/deepin-manual -name '*.svg' -type f -print -exec chmod -x {} \;
find %{buildroot}%{_datadir}/deepin-manual -name '*.md' -type f -print -exec chmod -x {} \;
find %{buildroot}%{_datadir}/deepin-manual -name '*.txt' -type f -print -exec chmod -x {} \;

%suse_update_desktop_file -r %{name} Office Viewer

%fdupes %{buildroot}%{_datadir}

%post -n libdeepin-pdfium%{sover} -p /sbin/ldconfig
%postun -n libdeepin-pdfium%{sover} -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_prefix}/lib/deepin-reader
%{_prefix}/lib/deepin-reader/htmltopdf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/deepin-manual/manual-assets/application/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files -n libdeepin-pdfium%{sover}
%{_libdir}/libdeepin-pdfium.so.*

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}.qm

%changelog

