#
# spec file for package kontact
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kontact
Version:        19.08.2
Release:        0
Summary:        Personal Information Manager
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-server-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  grantleetheme-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdepim-apps-libs-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kiconthemes-devel
BuildRequires:  kontactinterface-devel
BuildRequires:  kpimtextedit-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  libkdepim-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5DBus) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
Recommends:     kmail
Suggests:       akregator
Suggests:       kaddressbook
Suggests:       knotes
Suggests:       korganizer
Provides:       kontact5 = %{version}
Obsoletes:      kontact5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Kontact combines the individual applications KMail, KAddressBook and
KOrganizer as views in one window.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file org.kde.kontact         Office   Core-Office

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB COPYING.DOC
%{_kf5_debugdir}/kontact.categories
%{_kf5_debugdir}/kontact.renamecategories
%dir %{_kf5_appstreamdir}/
%doc %lang(en) %{_kf5_htmldir}/en/kontact/
%{_datadir}/kconf_update/
%{_datadir}/messageviewer/
%{_kf5_applicationsdir}/org.kde.kontact.desktop
%{_kf5_appstreamdir}/org.kde.kontact.appdata.xml
%{_kf5_bindir}/kontact
%{_kf5_configkcfgdir}/kontact.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/kontact.png
%{_kf5_iconsdir}/hicolor/scalable/apps/kontact.svg
%{_kf5_plugindir}/kcm_kontact.so
%{_kf5_servicesdir}/kontactconfig.desktop
%{_libdir}/libkontactprivate.so.*
%dir %{_kf5_sharedir}/dbus-1/services/
%{_kf5_sharedir}/dbus-1/services/org.kde.kontact.service

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
