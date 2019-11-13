#
# spec file for package grantlee-editor
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


%define kf5_version 5.59.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           grantlee-editor
Version:        19.08.3
Release:        0
Summary:        Messageviewer header theme editor based on Grantlee
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-mime-devel >= %{_kapp_version}
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  grantleetheme-devel
#Only required for the icon
BuildRequires:  kaddressbook
BuildRequires:  karchive-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kimap-devel
BuildRequires:  kmail-application-icons
BuildRequires:  knewstuff-devel
BuildRequires:  kpimtextedit-devel >= %{_kapp_version}
BuildRequires:  ktexteditor-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkleo
BuildRequires:  messagelib-devel >= %{_kapp_version}
BuildRequires:  pimcommon-devel
BuildRequires:  pkgconfig
BuildRequires:  syntax-highlighting-devel
BuildRequires:  cmake(KF5KaddressbookGrantlee)
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.10.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.10.0
Requires:       kaddressbook
Requires:       kmail-application-icons
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
A theme editor for messageviewer based on Grantlee. Once created or modified,
the themes can be used in KMail.

%lang_package

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
rm %{buildroot}%{_kf5_libdir}/*.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB COPYING.DOC
%{_kf5_debugdir}/grantleeditor.categories
%{_kf5_debugdir}/grantleeditor.renamecategories
%{_kf5_bindir}/contactprintthemeeditor
%{_kf5_bindir}/contactthemeeditor
%{_kf5_bindir}/headerthemeeditor
%{_kf5_applicationsdir}/org.kde.contactprintthemeeditor.desktop
%{_kf5_applicationsdir}/org.kde.contactthemeeditor.desktop
%{_kf5_applicationsdir}/org.kde.headerthemeeditor.desktop
%{_kf5_configkcfgdir}/grantleethemeeditor.kcfg
%doc %lang(en) %{_kf5_htmldir}/en/contactthemeeditor/
%doc %lang(en) %{_kf5_htmldir}/en/headerthemeeditor/
%{_kf5_libdir}/libgrantleethemeeditor.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
