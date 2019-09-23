#
# spec file for package kcm_sddm
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


%bcond_without lang
Name:           kcm_sddm
Version:        5.16.5
Release:        0
Summary:        A sddm control module for KDE
License:        GPL-2.0-only
Group:          System/GUI/KDE
Url:            https://projects.kde.org/projects/kdereview/sddm-kcm/repository
Source:         https://download.kde.org/stable/plasma/%{version}/sddm-kcm-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/sddm-kcm-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         dont-set-empty-autologin.patch
# PATCH-FIX-OPENSUSE
Patch2:         0002-Support-default.session-symlink.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Replace-autologin-configuration-with-a-note-to-use-Y.patch
# PATCH-FIX-UPSTREAM
Patch4:         remove-wayland-suffix.patch
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5Designer) >= 5.4.0
BuildRequires:  cmake(Qt5Gui) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcursor)
Supplements:    packageand(sddm:plasma5-workspace)
Recommends:     %{name}-lang

%description
SDDM control module for KDE. It provides a graphical frontend for the
sddm.

%lang_package

%prep
%setup -q -n sddm-kcm-%{version}
%autopatch -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build

%if %{with lang}
  %find_lang %{name} %{name}.lang
%endif

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files
%doc README
%license COPYING
%{_kf5_knsrcfilesdir}/sddmtheme.knsrc
%{_bindir}/sddmthemeinstaller
%{_kf5_servicesdir}/
%{_kf5_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_kf5_dbuspolicydir}/org.kde.kcontrol.kcmsddm.conf
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_kf5_libdir}/libexec/
%{_kf5_plugindir}/
%{_kf5_sharedir}/sddm-kcm/

%changelog
