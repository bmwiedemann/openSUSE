#
# spec file for package scantailor
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


Name:           scantailor
Version:        1.2.1
Release:        0
Summary:        Interactive post-processing tool for scanned pages
License:        GPL-3.0-or-later
URL:            https://github.com/ScanTailor-Advanced/scantailor-advanced
Source0:        https://github.com/ScanTailor-Advanced/scantailor-advanced/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.9.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_test-devel >= 1.65.0
%else
BuildRequires:  boost-devel >= 1.65.0
%endif

%description
Scan Tailor is an interactive post-processing tool for scanned pages.
It performs operations such as page splitting, deskewing,
adding/removing borders and others. It takes raw scans, and outputs
pages ready to be printed or assembled into a PDF or DJVU file.

%prep
%autosetup -p1 -n %{name}-advanced-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

# No %%check: upstream's suite is not headless/Qt6-clean in this release -
# imageproc_tests' Scale suite fuzzy-compares against QImage::scaled
# output from the Qt5 era (fails with Qt6), and qt_tests plus the
# SkewFinder case construct QApplication, which aborts without a display.

%files
%license LICENSE
%{_bindir}/scantailor-advanced
%{_datadir}/applications/scantailor-advanced.desktop
%{_datadir}/icons/hicolor/scalable/apps/scantailor-advanced.svg
%{_datadir}/mime/packages/%{name}-project.xml
%dir %{_datadir}/%{name}-advanced
%dir %{_datadir}/%{name}-advanced/translations
%{_datadir}/%{name}-advanced/translations/scantailor-advanced_*.qm

%changelog
