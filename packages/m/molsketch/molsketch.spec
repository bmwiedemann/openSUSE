#
# spec file for package molsketch
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define srcname Molsketch
%define sover 1
%define soname -qt5-%{sover}
%define binname %{name}-qt5
Name:           molsketch
Version:        0.5.1
Release:        0
Summary:        2D molecular structures editor
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Chemistry
Url:            https://molsketch.sourceforge.net
Source0:        https://downloads.sourceforge.net/molsketch/Molsketch-%{version}-src.tar.gz
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{suse_version} >= 1550
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(openbabel-2.0)

%description
The purpose of this editor to help drawing molecules.
Features:
 * open, save and import in all formats supported by the OpenBabel library
 * export to Scalable Vector Graphics (SVG) and a number of common used bitmap
   formats
 * print and export your document to PDF

%package -n     lib%{name}%{soname}
Summary:        C++ library for %{name}
Group:          System/Libraries
Provides:       libobabeliface%{soname} = %{version}

%description -n lib%{name}%{soname}
2D molecular structures editor.

This package provides the shared libraries.

%package 	    devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{soname} = %{version}
%if %{with qt4}
Requires:       libqt4-devel-doc
%else
Requires:       libqt5-qttools
%endif

%description 	devel
2D molecular structures editor.

This package contains header files and libraries needed to develop
application that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
2D molecular structures editor.

Help documentation for %{name}.

%prep
%setup -q -n %{srcname}-%{version}

dos2unix -k doc/cs/molsketch.adp

%build
%cmake \
  -DMSK_INSTALL_PREFIX=%{_prefix} \
  -DMSK_INSTALL_DOCS=%{_docdir}/%{name} \
  -DMSK_INSTALL_INCLUDES=%{_includedir}

%make_jobs

%install
%cmake_install

for sz in 24 32 48 64 128 256 512
do
  rsvg-convert -o %{name}-${sz}.png -w ${sz} molsketch/images/molsketch.svg
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  install -m0644 %{name}-${sz}.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/%{name}.png
done

%suse_update_desktop_file -c %{name} %{name} "2D molecular structures editor" %{binname} %{name} Education Chemistry

%fdupes -s %{buildroot}%{_datadir}

%post -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%if 0%{?suse_version} <= 1320
%post
%icon_theme_cache_post
%desktop_database_post
%mime_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%mime_database_postun
%endif

%files
%doc CHANGELOG COPYING
%{_bindir}/%{binname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/molsketch.*
%{_datadir}/pixmaps/molsketch.xpm
%exclude %{_docdir}/%{name}/cs/
%exclude %{_docdir}/%{name}/en/
%exclude %{_docdir}/%{name}/nl/
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-molsketch.svg
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/net.sourceforge.molsketch.appdata.xml
%{_datadir}/mime/packages/molsketch.xml

%files -n lib%{name}%{soname}
%{_libdir}/lib%{name}*so.*
%{_libdir}/libobabeliface*so.*

%files devel
%{_libdir}/lib%{name}*so
%{_libdir}/libobabeliface*so

%files doc
%{_docdir}/%{name}/cs/
%{_docdir}/%{name}/en/
%{_docdir}/%{name}/nl/

%changelog
