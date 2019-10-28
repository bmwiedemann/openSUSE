#
# spec file for package kalzium
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kalzium
Version:        19.08.2
Release:        0
Summary:        Periodic Table of Elements
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  avogadrolibs-devel
BuildRequires:  eigen3-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gettext-devel
BuildRequires:  glew-devel
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  khtml-devel
BuildRequires:  ki18n-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kparts-devel
BuildRequires:  kplotting-devel
BuildRequires:  kunitconversion-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libopenbabel-devel
BuildRequires:  oxygen5-icon-theme-large
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  solid-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang
# currently in DOESNOTBUILD (2008-07-03)
%ifnarch ppc ppc64 s390 s390x
BuildRequires:  ocaml
BuildRequires:  ocaml(Facile)
%endif

%description
Kalzium shows a periodic table of the elements.

%package devel
Summary:        Periodic Table of Elements
Group:          Development/Libraries/KDE
Requires:       kalzium = %{version}

%description devel
Kalzium shows a periodic table of the elements.

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
    %{kf5_find_htmldocs}
  %endif
  %fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc %lang(en) %{_kf5_htmldir}/en/kalzium/
%license COPYING*
%dir %{_kf5_appstreamdir}
%{_kf5_applicationsdir}/org.kde.kalzium.desktop
%{_kf5_applicationsdir}/org.kde.kalzium_cml.desktop
%{_kf5_appstreamdir}/org.kde.kalzium.appdata.xml
%{_kf5_bindir}/kalzium
%config %{_kf5_configdir}/kalzium.knsrc
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/kalzium.*
%{_kf5_kxmlguidir}/kalzium/
%{_kf5_libdir}/libcompoundviewer.so.*
%{_kf5_libdir}/libscience.so.*
%{_kf5_sharedir}/kalzium/
%{_kf5_sharedir}/libkdeedu/
%{_kf5_mandir}/man1/kalzium.1%{ext_man}

%files devel
%license COPYING*
%{_includedir}/libkdeedu/
%{_kf5_libdir}/libscience.so
%{_kf5_libdir}/libcompoundviewer.so

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
