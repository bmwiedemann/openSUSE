#
# spec file for package plasma6-openSUSE
#
# Copyright (c) 2024 SUSE LLC
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


%define wallpaper_branding_version     %(rpm -q --queryformat '%%{VERSION}' wallpaper-branding-openSUSE)

# Plasma 6 pulls in Qt 5 as well, tell qml-autoreqprov what to use
%global __qml_requires_opts --qtver 6
%global plasma_version 6.1.2
Name:           plasma6-openSUSE
Version:        84.87~git20240313T170730~9c664b7
Release:        0
Summary:        openSUSE Plasma 6 Branding Packages
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/openSUSE/plasma-openSUSE
# We use diffs to be as close to upstream as possible and get
# fixes directly. For files that diverge too much from upstream,
# the .tar is the right place.
Source:         plasma-opensuse-%{version}.tar.xz
# Diff between /usr/share/sddm/themes/breeze-openSUSE
# and /usr/share/sddm/themes/breeze
Source3:        sddmtheme.diff
# Diff between /usr/share/plasma/layout-templates/org.kde.plasma.desktop.defaultPanel/contents/layout.js
# and /usr/share/plasma/layout-templates/org.opensuse.desktop.defaultPanel/contents/layout.js
Source4:        panel.diff
# Diff between /usr/share/plasma/shells/org.kde.plasma.desktop/contents/layout.js
# and /usr/share/plasma/look-and-feel/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
Source5:        layout.diff
BuildRequires:  fdupes
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-filesystem
BuildRequires:  plasma6-desktop >= %{plasma_version}
#!BuildIgnore: kio-extras
#!BuildIgnore: kwin6
BuildRequires:  plasma6-workspace >= %{plasma_version}
BuildRequires:  rsync
BuildRequires:  wallpaper-branding-openSUSE
BuildArch:      noarch

%description

%package -n plasma6-branding-openSUSE
Summary:        openSUSE settings for KDE Plasma 6
Group:          System/GUI/KDE
Requires:       distribution-logos-openSUSE-icons
Requires:       plasma6-theme-openSUSE
Provides:       plasma5-defaults-openSUSE = %{version}
Obsoletes:      plasma5-defaults-openSUSE < %{version}
Obsoletes:      plasma5-workspace-branding-openSUSE < %{version}
Requires:       (plasma6-sddm-theme-openSUSE if sddm)
Supplements:    (plasma6-workspace and branding-openSUSE)

%description -n plasma6-branding-openSUSE
This package changes the default settings of Plasma 6.

%package -n plasma6-theme-openSUSE
Summary:        Plasma 6 theme for openSUSE
Group:          System/GUI/KDE
Requires:       plasma6-desktop >= %{plasma_version}
Requires:       plasma6-workspace >= %{plasma_version}
Requires:       wallpaper-branding-openSUSE
Obsoletes:      plasma5-theme-openSUSE < %{version}

%description -n plasma6-theme-openSUSE
This package contains the Plasma 6 Look-and-feel package for openSUSE.

%package -n plasma6-sddm-theme-openSUSE
Summary:        SDDM theme for openSUSE
Group:          System/GUI/KDE
Requires:       wallpaper-branding-openSUSE = %{wallpaper_branding_version}
Provides:       sddm-theme-openSUSE = %{version}
Obsoletes:      sddm-theme-openSUSE < %{version}

%description -n plasma6-sddm-theme-openSUSE
This package contains a version of the Breeze SDDM theme customized
for openSUSE and enables it by default.

%prep
%setup -q -n plasma-opensuse-%{version}

%build

%install
# Defaults
cp -a config-files/* %{buildroot}
%fdupes %{buildroot}/%{_kf6_plasmadir}/desktoptheme

# Look-and-feel package (copy over everything that is not already in the .tar, then apply patch if there is one)
rsync -av --ignore-existing %{_kf6_plasmadir}/look-and-feel/org.kde.breeze.desktop/ %{buildroot}%{_kf6_plasmadir}/look-and-feel/org.openSUSE.desktop/

# Same for the SDDM theme
rsync -av --ignore-existing %{_datadir}/sddm/themes/breeze/ %{buildroot}%{_datadir}/sddm/themes/breeze-openSUSE/
pushd %{buildroot}%{_datadir}/sddm/themes/breeze-openSUSE
patch -p2 -i %{SOURCE3}
popd

# Same for the default panel
rsync -av --ignore-existing %{_kf6_plasmadir}/layout-templates/org.kde.plasma.desktop.defaultPanel/ %{buildroot}%{_kf6_plasmadir}/layout-templates/org.opensuse.desktop.defaultPanel/
patch -o %{buildroot}%{_kf6_plasmadir}/layout-templates/org.opensuse.desktop.defaultPanel/contents/layout.js -i %{SOURCE4} %{_kf6_plasmadir}/layout-templates/org.kde.plasma.desktop.defaultPanel/contents/layout.js

# And the desktop layout
mkdir -p %{buildroot}%{_kf6_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/layouts/
patch -o %{buildroot}%{_kf6_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js -i %{SOURCE5} %{_kf6_plasmadir}/shells/org.kde.plasma.desktop/contents/main.js
chmod 644 %{buildroot}%{_kf6_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js

%files -n plasma6-branding-openSUSE
%license COPYING
# TODO: Move to /usr/etc/xdg, once confirmed this works everywhere
%config %{_kf6_configdir}/*rc
%config %{_kf6_configdir}/kdeglobals

%files -n plasma6-theme-openSUSE
%license COPYING
%{_kf6_plasmadir}/
%{_kf6_sharedir}/color-schemes/
%{_kf6_sharedir}/icons/*

%files -n plasma6-sddm-theme-openSUSE
%license COPYING
%dir %{_kf6_sharedir}/sddm/
%dir %{_kf6_sharedir}/sddm/themes/
%{_kf6_sharedir}/sddm/themes/breeze-openSUSE/
%dir %{_prefix}/lib/sddm/
%dir %{_prefix}/lib/sddm/sddm.conf.d/
# This overrides 10-plasma.conf from sddm-qt6-branding-openSUSE
%{_prefix}/lib/sddm/sddm.conf.d/20-breeze-openSUSE.conf

%changelog
