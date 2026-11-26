#
# spec file for package kxstitch
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           kxstitch
Version:        3.0.0
Release:        0
Summary:        Cross stitch pattern and chart creation
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kxstitch/
Source0:        https://download.kde.org/stable/kxstitch/%{version}/kxstitch-%{version}.tar.xz
Source1:        https://download.kde.org/stable/kxstitch/%{version}/kxstitch-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/jpwhiting@key1.asc?ref_type=heads
Source2:        kxstitch.keyring
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(Magick++)

%description
KXStitch is a program that lets you create cross stitch patterns and charts.
Patterns can be created from scratch on a user defined size of grid, which can
be enlarged or reduced in size as your pattern progresses. Alternatively you
can import images from many graphics file formats which will allow you to
reduce the number of colors and to restrict the conversion to full stitches or
optionally use fractional stitches. You may also use images as backgrounds
allowing you to trace over them. These imported images can then be modified
using the supplied tools to produce your final design.

%lang_package

%prep
%autosetup -p1

%build
# Breaks on Leap 16.0 with kf6-kdoctools 6.16 and succeeds on 16.1 with 6.25
%if %{pkg_vcmp kf6-kdoctools < 6.25}
rm -r po/ar/docs
%endif

%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html --with-man

%files
%license COPYING LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kxstitch/
%{_kf6_applicationsdir}/org.kde.kxstitch.desktop
%{_kf6_appstreamdir}/org.kde.kxstitch.appdata.xml
%{_kf6_bindir}/kxstitch
%{_kf6_configkcfgdir}/kxstitch.kcfg
%{_kf6_iconsdir}/hicolor/*/actions/kxs*.png
%{_kf6_iconsdir}/hicolor/*/apps/kxstitch.*
%{_kf6_iconsdir}/hicolor/scalable/mimetypes/application-x-kxs.svgz
%{_kf6_mandir}/man1/kxstitch.1%{?ext_man}
%{_kf6_sharedir}/kxstitch/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kxstitch

%changelog
