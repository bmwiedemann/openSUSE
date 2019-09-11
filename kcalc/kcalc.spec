#
# spec file for package kcalc
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
Name:           kcalc
Version:        19.08.0
Release:        0
Summary:        Scientific Calculator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  gmp-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kinit-devel
BuildRequires:  knotifications-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KCalc is the KDE calculator tool.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kcalc-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file org.kde.kcalc       Utility Calculator

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_applicationsdir}/org.kde.kcalc.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/kcalc
%{_kf5_configkcfgdir}/
%doc %lang(en) %{_kf5_htmldir}/en/kcalc/
%{_kf5_kxmlguidir}/
%{_kf5_libdir}/libkdeinit5_kcalc.so
%{_kf5_sharedir}/kcalc/
%{_kf5_sharedir}/kconf_update/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
