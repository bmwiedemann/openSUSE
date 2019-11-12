#
# spec file for package ark
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


%define SOMAJOR 19
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ark
Version:        19.08.3
Release:        0
Summary:        KDE Archiver Tool
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE lower-libarchive-minimum-version.patch
Patch0:         lower-libarchive-minimum-version.patch
BuildRequires:  extra-cmake-modules >= 1.7.0
BuildRequires:  karchive-devel >= %{kf5_version}
BuildRequires:  kconfig-devel >= 5.2.0
BuildRequires:  kdelibs4support-devel >= 5.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  kpty-devel >= 5.2.0
BuildRequires:  libarchive-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(bzip2)
Requires:       shared-mime-info
# Recommend the most used compression programs (bnc#872010)
Recommends:     xz
# unrar is non-free. Avoid installing it automatically.
Suggests:       unrar
Obsoletes:      ark-devel
%if 0%{?suse_version} >= 1330
BuildRequires:  libzip-devel >= 1.2.0
%endif
%if 0%{?suse_version} > 1500
Recommends:     p7zip-full
%else
Recommends:     p7zip
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This is a KDE application to work with compressed archives.

%package -n libkerfuffle%{SOMAJOR}
Summary:        KDE Archiver Tool
Group:          System/Libraries

%description -n libkerfuffle%{SOMAJOR}
This is a KDE application to work with compressed archives.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q
%autopatch -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file org.kde.ark System Archiving

%post
%mime_database_post

%postun
%mime_database_postun

%post -n libkerfuffle%{SOMAJOR} -p /sbin/ldconfig
%postun -n libkerfuffle%{SOMAJOR} -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/ark.categories
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/ark/
%doc %{_kf5_mandir}/man1/ark.*
%{_kf5_applicationsdir}/org.kde.ark.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/ark
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_sharedir}/mime/packages/kerfuffle.xml

%files -n libkerfuffle%{SOMAJOR}
%license COPYING*
%{_kf5_libdir}/libkerfuffle.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
