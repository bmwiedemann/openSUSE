#
# spec file for package pim-sieve-editor
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
Name:           pim-sieve-editor
Version:        20.08.2
Release:        0
Summary:        Sieve scripts editor for KDE PIM
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
# Is only required for the icon
BuildRequires:  kmail-application-icons
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IMAP)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5LibKSieve)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KUserFeedback)
BuildRequires:  cmake(Qt5Network) >= 5.10.0
BuildRequires:  cmake(Qt5Test) >= 5.10.0
BuildRequires:  cmake(Qt5Widgets) >= 5.10.0
Requires:       kmail
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package provides an editor, complete with syntax highlighting and
command completion, to edit Sieve scripts ("server side filtering")
in KDE PIM applications.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file org.kde.sieveeditor    Network   Email

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/sieveeditor.categories
%{_kf5_debugdir}/sieveeditor.renamecategories
%doc %lang(en) %{_kf5_htmldir}/en/sieveeditor/
%{_kf5_applicationsdir}/org.kde.sieveeditor.desktop
%{_kf5_bindir}/sieveeditor
%{_kf5_configkcfgdir}/sieveeditorglobalconfig.kcfg
%{_kf5_libdir}/libsieveeditor.so.*
%{_kf5_sharedir}/kconf_update/
%{_kf5_appstreamdir}/org.kde.sieveeditor.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
