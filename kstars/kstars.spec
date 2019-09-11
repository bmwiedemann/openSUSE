#
# spec file for package kstars
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


%bcond_without lang
Name:           kstars
Version:        3.3.6
Release:        0
Summary:        Desktop Planetarium
# Note for legal: the Apache licensed files in the tarball are for the
# Android version - they're neither built nor installed
# Likewise, the non-commercial files in  kstars-17.04.2/README.images are not
# used nor installed
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://edu.kde.org/kstars/
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  cfitsio-devel
BuildRequires:  eigen3-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gsl-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifications-devel
BuildRequires:  kplotting-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libindi-devel
BuildRequires:  libnova-devel
BuildRequires:  libraw-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wcslib-devel
BuildRequires:  xplanet
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DataVisualization)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Xml)
Recommends:     libindi
Recommends:     xplanet
Recommends:     %{name}-lang

%description
KStars is astronomy software. It provides an accurate graphical
simulation of the night sky, for any time and location on Earth.

%lang_package

%prep
%setup -q

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %kf5_find_htmldocs
%endif

# Remove static library
rm -f %{buildroot}%{_kf5_libdir}/libhtmesh.a

%fdupes -s %{buildroot}

%files
%license COPYING COPYING.DOC
%doc AUTHORS ChangeLog README README.customize README.ephemerides README.images
%dir %{_kf5_appstreamdir}
%dir %{_kf5_configkcfgdir}
%doc %{_kf5_htmldir}/en/kstars/
%{_datadir}/sounds/*.ogg
%{_kf5_applicationsdir}/org.kde.kstars.desktop
%{_kf5_appsdir}/kstars/
%{_kf5_appstreamdir}/org.kde.kstars.appdata.xml
%{_kf5_bindir}/kstars
%{_kf5_configkcfgdir}/kstars.kcfg
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_notifydir}/kstars.notifyrc

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING COPYING.DOC
%endif

%changelog
