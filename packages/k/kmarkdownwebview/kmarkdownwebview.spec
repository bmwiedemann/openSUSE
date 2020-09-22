#
# spec file for package kmarkdownwebview
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


%define kf5_version 5.25.0
%bcond_without lang
Name:           kmarkdownwebview
Version:        0.5.6
Release:        0
Summary:        KPart for rendering Markdown content
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  kparts-devel >= %{kf5_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.7.0
%else
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.6.0
%endif
Recommends:     %{name}-lang

%description
This package allows KDE applications which use it to obtain a live preview of HTML-rendered Markdown content.

%lang_package

%prep
%setup -q

%build
%if 0%{?suse_version} < 1330
  %cmake_kf5 -d build -- -DUSE_WEBKIT=TRUE
%else
  %cmake_kf5 -d build
%endif
  %make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --all-name
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/LGPL-2.1-or-later.txt
%{_kf5_libdir}/libKMarkdownWebView.so
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_plugindir}/kf5/parts/kmarkdownwebviewpart.so
%if 0%{?suse_version} < 1330
%{_kf5_plugindir}/kmarkdownwebviewthumbnail.so
%{_kf5_servicesdir}/kmarkdownwebviewthumbnail.desktop
%endif
%{_kf5_servicesdir}/kmarkdownwebviewpart.desktop
%{_kf5_appstreamdir}/org.kde.kmarkdownwebviewpart.metainfo.xml

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%endif

%changelog
