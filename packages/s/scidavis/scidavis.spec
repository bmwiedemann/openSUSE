#
# spec file for package scidavis
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Quentin Denis <quentin@links2linux.de>
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


%define __builder ninja
Name:           scidavis
Version:        2.9.0
Release:        0
Summary:        An application for Scientific Data Analysis and Visualization
License:        GPL-2.0-only AND GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://scidavis.sourceforge.net/
Source0:        https://github.com/SciDAVis/scidavis/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Adapt-scidavis-for-openSUSE.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Adapt-scidavis-for-Leap.patch
# PATCH-FIX-UPSTREAM gh#SciDAVis/scidavis#30 https://github.com/SciDAVis/scidavis/commit/afca5696c4f477dcae4a0484dad2d7314884f020
Patch2:         scidavis-specify-std-namespace.patch
# PATCH-FIX-UPSTREAM scidavis-grabFrameBuffer.patch badshah400@gmail.com -- Use grabFrameBuffer instead of grabFramebuffer, https://sourceforge.net/p/scidavis/scidavis-bugs/441
Patch3:         scidavis-grabFrameBuffer.patch
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-sip4
BuildRequires:  python3-sip4-devel
BuildRequires:  qwtplot3d-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(liborigin)
BuildRequires:  pkgconfig(muparser)
BuildRequires:  pkgconfig(qwt5-qt5)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    aarch64

%description
SciDAVis is an interactive application for data analysis and
publication-quality plotting. It has scriptability and can be extended.

SciDAVis is similar in its field of application to proprietary Windows
applications like Origin and SigmaPlot as well as free applications like
QtiPlot, Labplot and Gnuplot.

%lang_package

%prep
%setup -q
%patch -P 0 -p1
%if 0%{?suse_version} < 1550
%patch -P 1 -p1
%endif
%patch -P 2 -p1
%patch -P 3 -p1

%build
export PYTHON=%{_bindir}/python%{python3_version}
%cmake \
  -DBUILD_QWTPLOT3D=OFF \
  -DORIGIN_IMPORT=ON \
  -DQWTPLOT3D_LIBRARY=%{_libqt5_libdir}/libqwtplot3d-qt5.so \
  -Wno-dev \
  %{nil}
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-qt

# Remove unneeded files.
rm -rf %{buildroot}%{_docdir}/%{name}

# mimelnk is deprecated in favor of %%{_datadir}/mime/packages/ for a long time
rm -Rf %{buildroot}%{_datadir}/mimelnk

%files lang -f %{name}.lang
%dir %{_datadir}/scidavis
%dir %{_datadir}/scidavis/translations

%files
%license LICENSE
%doc ChangeLog.md README.md
%dir %{_datadir}/icons/locolor
%dir %{_datadir}/icons/locolor/16x16
%dir %{_datadir}/icons/locolor/16x16/apps
%dir %{_datadir}/icons/locolor/22x22
%dir %{_datadir}/icons/locolor/22x22/apps
%dir %{_datadir}/icons/locolor/32x32
%dir %{_datadir}/icons/locolor/32x32/apps
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
