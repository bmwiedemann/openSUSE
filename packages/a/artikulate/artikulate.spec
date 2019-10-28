#
# spec file for package artikulate
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           artikulate
Version:        19.08.2
Release:        0
Summary:        Pronunciation Self-Teaching
License:        LGPL-3.0-or-later AND GPL-2.0-only AND BSD-3-Clause
Group:          Amusements/Teaching/Other
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kirigami2-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
# Runtime deps
Requires:       kirigami2
Requires:       knewstuff-imports
Requires:       kqtquickcharts >= %{_kapp_version}
Requires:       libqt5-qtquickcontrols
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Improve your pronunciation by listening to native speakers.

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file org.kde.%{name}       Languages

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_configkcfgdir}
%{_kf5_applicationsdir}/org.kde.artikulate.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/artikulate
%{_kf5_bindir}/artikulate_editor
%config %{_kf5_configdir}/artikulate.knsrc
%{_kf5_configkcfgdir}/artikulate.kcfg
%doc %lang(en) %{_kf5_htmldir}/en/artikulate/
%{_kf5_iconsdir}/hicolor/*/*/artikulate*.*
%{_kf5_iconsdir}/hicolor/*/actions/language-artikulate.*
%{_kf5_libdir}/libartikulatecore.so.*
%{_kf5_libdir}/libartikulatelearnerprofile.so.*
%{_kf5_libdir}/libartikulatesound.so.*
%{_kf5_plugindir}/artikulate/
%{_kf5_sharedir}/artikulate/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
