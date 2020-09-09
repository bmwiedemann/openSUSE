#
# spec file for package lokalize
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           lokalize
Version:        20.08.1
Release:        0
Summary:        KDE Translation Editor
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hunspell-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
This package contains lokalize, an editor for translations

%lang_package

%prep
%setup -q

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
  %cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    # Remove bogus folder
    rm -rf %{buildroot}%{_datadir}/locale/sr/docs/
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.lokalize      Development Translation
  %fdupes -s %{buildroot}%{_kf5_sharedir}/lokalize

%files
%license COPYING*
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/lokalize/
%{_kf5_applicationsdir}/org.kde.lokalize.desktop
%{_kf5_appstreamdir}/org.kde.lokalize.appdata.xml
%{_kf5_bindir}/lokalize
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/lokalize.*
%{_kf5_kxmlguidir}/
%{_kf5_notifydir}/lokalize.notifyrc
%{_kf5_sharedir}/lokalize/
%{_kf5_debugdir}/lokalize.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
