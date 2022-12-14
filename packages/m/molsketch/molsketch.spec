#
# spec file for package molsketch
#
# Copyright (c) 2022 SUSE LLC
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
%define soname %{sover}
Name:           molsketch
Version:        0.7.3
Release:        0
Summary:        2D molecular structures editor
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            https://molsketch.sourceforge.net
Source0:        https://downloads.sourceforge.net/molsketch/Molsketch-%{version}-src.tar.gz
# PATCH-FIX-UPSTREAM molsketch-cmake-qt5-add-translation.patch badshah400@gmail.com -- Use qt5_add_translation instead of qt_add_translation with cmake
Patch0:         molsketch-cmake-qt5-add-translation.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
BuildRequires:  (pkgconfig(openbabel-2.0) or pkgconfig(openbabel-3))
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
The purpose of this editor to help drawing molecules.
Features:
 * open, save and import in all formats supported by the OpenBabel library
 * export to Scalable Vector Graphics (SVG) and a number of common used bitmap
   formats
 * print and export your document to PDF

%package 	devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Provides:       lib%{name}%{soname} =  %{version}
Requires:       libqt5-qttools

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
%autosetup -n %{srcname}-%{version} -p1
dos2unix -k -c ascii doc/cs/%{name}.adp

%build
%cmake \
  -DMSK_INSTALL_DOCS="/share/doc/packages/%{name}"

%cmake_build

%install
%cmake_install

for sz in 24 32 48 64 128 256 512
do
  rsvg-convert -o %{name}-${sz}.png -w ${sz} molsketch/images/molsketch.svg
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  install -m0644 %{name}-${sz}.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/%{name}.png
done

%suse_update_desktop_file -c %{name} %{name} "2D molecular structures editor" %{name} Education Chemistry

%fdupes -s %{buildroot}%{_datadir}

%files
%license COPYING
%doc CHANGELOG
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/molsketch.*
%{_datadir}/pixmaps/molsketch.xpm
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/metainfo/net.sourceforge.molsketch.appdata.xml
%{_datadir}/mime/packages/molsketch.xml

%files devel
%{_includedir}/lib%{name}/

%files doc
%{_docdir}/%{name}/
%exclude %{_docdir}/molsketch/CHANGELOG

%changelog
