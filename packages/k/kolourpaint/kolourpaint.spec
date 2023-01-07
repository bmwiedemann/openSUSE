#
# spec file for package kolourpaint
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kolourpaint
Version:        22.12.1
Release:        0
Summary:        Paint Program
# See boo#717722 for license details
# GPL-2.0 is the license of the Bulgarian translation
License:        BSD-2-Clause AND LGPL-2.1-or-later AND GFDL-1.2-or-later AND GPL-2.0-only
URL:            https://apps.kde.org/kolourpaint
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5Sane)
# boo#1055759
Requires:       kdelibs4support
Provides:       kolourpaint5 = %{version}
Obsoletes:      kolourpaint5 < %{version}

%description
Paint program by KDE

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kolourpaint RasterGraphics
%fdupes -s %{buildroot}%{_datadir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README*
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.kolourpaint.desktop
%{_kf5_appstreamdir}/org.kde.kolourpaint.appdata.xml
%{_kf5_bindir}/kolourpaint
%{_kf5_iconsdir}/hicolor/*/apps/kolourpaint.*
%{_kf5_kxmlguidir}/
%{_kf5_libdir}/libkolourpaint_lgpl.so*
%{_kf5_sharedir}/kolourpaint/

%files lang -f %{name}.lang

%changelog
