#
# spec file for package scidavis
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scidavis
Version:        1.25
Release:        0
Summary:        An application for Scientific Data Analysis and Visualization
License:        GPL-2.0-only AND GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://scidavis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/scidavis/SciDAVis/%{version}/%{name}-%{version}.tar.gz
Source1:        scidavis-rpmlintrc
# PATCH-FIX-OPENSUSE
Patch0:         0001-Adapt-scidavis-for-openSUSE.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  liborigin-devel
BuildRequires:  pkgconfig
BuildRequires:  python2-qt5-devel
BuildRequires:  qwt-devel
BuildRequires:  qwtplot3d-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(muparser)
%if 0%{?suse_version} > 1220
BuildRequires:  glu-devel
%endif
Recommends:     %{name}-lang = %{version}

%description
SciDAVis is an interactive application for data analysis and
publication-quality plotting. It has scriptability and can be extended.

SciDAVis is similar in its field of application to proprietary Windows
applications like Origin and SigmaPlot as well as free applications like
QtiPlot, Labplot and Gnuplot.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%qmake5 CONFIG+=python\
%if "%{_lib}" == "lib64"
  64BITS=1
%endif

%make_jobs

%install
%qmake5_install

mkdir -p %{buildroot}%{_datadir}/%{name}/translations
cp %{name}/translations/%{name}_*.qm %{buildroot}%{_datadir}/%{name}/translations/

%find_lang %{name} --with-qt

# Remove unneeded files.
rm -rf %{buildroot}%{_datadir}/doc/%{name}

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
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application/
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-sciprj.desktop
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_sysconfdir}/scidavis/

%changelog
