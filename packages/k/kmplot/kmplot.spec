#
# spec file for package kmplot
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
Name:           kmplot
Version:        19.08.1
Release:        0
Summary:        Mathematical Function Plotter
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kparts-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang
%if 0%{?suse_version} < 1500
# the default gcc 4.8 is too old
BuildRequires:  gcc7-c++
%endif

%description
Mathematical function plotter by KDE.

%lang_package

%prep
%setup -q

%build
%if 0%{?suse_version} < 1500
# the default gcc 4.8 is too old
export CC=gcc-7
export CXX=g++-7
%endif
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

%files
%license COPYING*
%dir %{_kf5_appstreamdir}
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/kmplot
%{_kf5_applicationsdir}/org.kde.kmplot.desktop
%{_kf5_appstreamdir}/org.kde.kmplot.appdata.xml
%{_kf5_bindir}/kmplot
%{_kf5_configkcfgdir}/kmplot.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kmplot.*.xml
%{_kf5_iconsdir}/hicolor/*/apps/kmplot.*
%{_kf5_kxmlguidir}/kmplot/
%{_kf5_plugindir}/kmplotpart.so
%{_kf5_servicesdir}/kmplot_part.desktop
%{_mandir}/*/kmplot.1%{?ext_man}

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
