#
# spec file for package umbrello
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
%bcond_without  lang
Name:           umbrello
Version:        19.08.0
Release:        0
Summary:        UML Modeller
License:        GPL-2.0-only AND GFDL-1.2-only AND GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kauth-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kinit-devel
BuildRequires:  kio-devel
BuildRequires:  kparts-devel
BuildRequires:  kservice-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  subversion-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Recommends:     %{name}-lang
Obsoletes:      umbrello5 < %{version}
Provides:       umbrello5 = %{version}

%description
Umbrello is a UML modelling application.

%lang_package

%prep
%setup -q

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"

  %cmake_kf5 -d build -- -DBUILD_KF5=ON
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
  %suse_update_desktop_file    org.kde.umbrello       Development Design

%files
%license COPYING COPYING.DOC
%doc README
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/umbrello
%{_kf5_applicationsdir}/org.kde.umbrello.desktop
%{_kf5_appstreamdir}/org.kde.umbrello.appdata.xml
%{_kf5_bindir}/po2xmi5
%{_kf5_bindir}/umbrello5
%{_kf5_bindir}/xmi2pot5
%{_kf5_iconsdir}/hicolor/*/*/umbrello*
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-uml.png
%{_kf5_sharedir}/umbrello5/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
