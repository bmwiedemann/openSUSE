#
# spec file for package kate
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


%define _appstreamkpackage 0%(cat %{_kf5_cmakedir}/KF5Package/KF5PackageMacros.cmake | grep -q 'appstream-metainfo' && echo 1)
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kate
Version:        19.08.0
Release:        0
Summary:        Advanced Text Editor
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Defuse-root-block.patch
BuildRequires:  kactivities5-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kparts-devel
BuildRequires:  kservice-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwallet-framework-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libgit2-devel
BuildRequires:  pkgconfig
BuildRequires:  plasma-framework-devel
BuildRequires:  threadweaver-devel
BuildRequires:  pkgconfig(Qt5Core) >= 5.4.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Script) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Sql) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
Requires:       %{name}-plugins = %{version}
Recommends:     %{name}-lang
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Kate is an advanced text editor for KDE.

%package -n kwrite
Summary:        KDE Text Editor
Group:          Productivity/Text/Editors
Requires:       %{name}-plugins = %{version}
Obsoletes:      kwrite5 < %{version}

%description -n kwrite
KWrite is the default text editor of the K desktop environment.

%package plugins
Summary:        KDE Text Editor plugins
Group:          Productivity/Text/Editors
Obsoletes:      kate5-plugins < %{version}
Provides:       ktexteditorpreviewplugin = %{version}
Obsoletes:      ktexteditorpreviewplugin < %{version}

%description plugins
Kate is an advanced text editor for KDE. This package contains
plugins and data files for Kate and KWrite editors.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%files
%license COPYING*
%doc README*
%dir %{_kf5_appstreamdir}
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/kate/
%doc %lang(en) %{_kf5_htmldir}/en/katepart/
%doc %{_kf5_mandir}/man1/kate.*
%{_kf5_applicationsdir}/org.kde.kate.desktop
%{_kf5_appstreamdir}/org.kde.kate.appdata.xml
%{_kf5_bindir}/kate
%{_kf5_iconsdir}/hicolor/*/apps/kate.*

%files -n kwrite
%license COPYING*
%doc README*
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/kwrite/
%{_kf5_applicationsdir}/org.kde.kwrite.desktop
%{_kf5_appstreamdir}/org.kde.kwrite.appdata.xml
%{_kf5_bindir}/kwrite
%{_kf5_iconsdir}/hicolor/*/apps/kwrite.*

%files plugins
%license COPYING*
%doc README*
%if 0%{?_appstreamkpackage}
%{_kf5_appstreamdir}/org.kde.plasma.katesessions.appdata.xml
%endif
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/kateproject/
%{_kf5_sharedir}/katexmltools/
%{_kf5_sharedir}/plasma/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
