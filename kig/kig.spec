#
# spec file for package kig
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
Name:           kig
Version:        19.08.0
Release:        0
Summary:        Interactive Geometry
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  karchive-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kemoticons-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kparts-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.2.0
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_python-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Kig is an application for Interactive Geometry. It's intended to serve
two purposes: Allow students to interactively explore mathematical
figures and concepts using the computer. Serve as a WYSIWYG tool for
drawing mathematical figures and including them in other documents.

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

%files
%license COPYING*
#{_kf5_sharedir}/katepart/
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.kig.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/kig
%{_kf5_bindir}/pykig.py
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_mandir}/man*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/katepart5/
%{_kf5_sharedir}/kig/
%{_kf5_sharedir}/kxmlgui5/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
