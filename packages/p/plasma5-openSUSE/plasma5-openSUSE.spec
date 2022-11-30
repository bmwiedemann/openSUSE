#
# spec file for package plasma5-openSUSE
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


%define plasma_version 5.26.4
Name:           plasma5-openSUSE
Version:        84.87~git20220602T134713~22403ba
Release:        0
Summary:        openSUSE KDE Extension
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/openSUSE/plasma-openSUSE
# We use diffs to be as close to upstream as possible and get
# fixes directly. For files that diverge too much from upstream,
# the .tar is the right place.
Source:         plasma-opensuse-%{version}.tar.xz
# Diff between /usr/share/plasma/look-and-feel/org.kde.breeze.desktop
# and /usr/share/plasma/look-and-feel/org.openSUSE.desktop
Source2:        lookandfeel.diff
# Diff between /usr/share/sddm/themes/breeze-openSUSE
# and /usr/share/sddm/themes/breeze
Source3:        sddmtheme.diff
# Diff between /usr/share/plasma/shells/org.kde.plasma.desktop/contents/layout.js
# and /usr/share/plasma/look-and-feel/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js
Source5:        layout.diff
BuildRequires:  breeze5-icons
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  oxygen5-icon-theme
BuildRequires:  plasma5-desktop >= %{plasma_version}
BuildRequires:  plasma5-desktop-branding-upstream >= %{plasma_version}
#!BuildIgnore: kwin5
BuildRequires:  plasma5-workspace >= %{plasma_version}
BuildRequires:  plasma5-workspace-branding-upstream >= %{plasma_version}
BuildRequires:  rsync
BuildRequires:  wallpaper-branding-openSUSE
BuildArch:      noarch

%description
This package contains the standard openSUSE desktop and extensions.

%package -n plasma5-workspace-branding-openSUSE
Summary:        openSUSE branded KDE settings
Group:          System/GUI/KDE
Requires:       plasma5-defaults-openSUSE
Requires:       plasma5-workspace >= %{plasma_version}
Requires:       wallpaper-branding-openSUSE
Supplements:    packageand(plasma5-workspace:branding-openSUSE)
Provides:       plasma5-workspace-branding = %{plasma_version}
%if 0%{?suse_version} >= 1315 && 0%{?suse_version} != 1320
Provides:       kdebase4-openSUSE = 43
Provides:       kdebase4-openSUSE-lang = 43
Provides:       kdebase4-runtime-branding-openSUSE = 43
Provides:       kdebase4-workspace-branding-openSUSE = 43
Obsoletes:      kdebase4-openSUSE < 43
Obsoletes:      kdebase4-openSUSE-lang < 43
Obsoletes:      kdebase4-runtime-branding-openSUSE < 43
Obsoletes:      kdebase4-workspace-branding-openSUSE < 43
%else
Conflicts:      kdebase4-openSUSE
Conflicts:      kdebase4-workspace-branding-openSUSE
%endif

%description -n plasma5-workspace-branding-openSUSE
This package does not contain anything by itself, but pulls in
default settings and extensions for the standard openSUSE
desktop.

%package -n plasma5-defaults-openSUSE
Summary:        Default settings for KDE Plasma 5
Group:          System/GUI/KDE
Requires:       plasma5-theme-openSUSE

%description -n plasma5-defaults-openSUSE
This package changes the default settings of Plasma 5.

%package -n plasma5-theme-openSUSE
Summary:        Plasma 5 theme for openSUSE
Group:          System/GUI/KDE
Requires:       wallpaper-branding-openSUSE
Requires(pre):  coreutils
Conflicts:      kdebase4-openSUSE < 43
Conflicts:      kdebase4-workspace-branding-openSUSE < 43
Provides:       plasma5-desktop-branding-openSUSE = 43
Obsoletes:      plasma5-desktop-branding-openSUSE < 43

%description -n plasma5-theme-openSUSE
This package contains the Plasma 5 Look-and-feel package for openSUSE.

%package -n sddm-theme-openSUSE
Summary:        SDDM theme for openSUSE
Group:          System/GUI/KDE
Requires:       libqt5-qtquickcontrols
Requires:       plasma-framework-components
Requires:       plasma5-workspace
Requires:       wallpaper-branding-openSUSE

%description -n sddm-theme-openSUSE
This package contains a version of the Breeze SDDM theme customized
for openSUSE.

%prep
%setup -q -n plasma-opensuse-%{version}

%build

%install
# Defaults
cp -a config-files/* %{buildroot}
%fdupes %{buildroot}/%{_kf5_plasmadir}/desktoptheme

# copy kdeglobals to /etc/kde4/share/config/, to make Firefox the default browser for KDE4 as well (boo#997199)
# necessary at least until mozilla-kde4-integration has been ported to KF5, as Firefox currently checks the KDE4 settings whether it is the default browser
mkdir -p %{buildroot}/%{_sysconfdir}/kde4/share/config/
cp %{buildroot}/%{_kf5_configdir}/kdeglobals %{buildroot}/%{_sysconfdir}/kde4/share/config/

# Look-and-feel package (copy over everything that is not already in the .tar, then apply patch)
rsync -av --ignore-existing %{_kf5_plasmadir}/look-and-feel/org.kde.breeze.desktop/ %{buildroot}%{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/
pushd %{buildroot}%{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/
patch -p2 -i %{SOURCE2}
popd

# Same for the SDDM theme
rsync -av --ignore-existing %{_datadir}/sddm/themes/breeze/ %{buildroot}%{_datadir}/sddm/themes/breeze-openSUSE/
pushd %{buildroot}%{_datadir}/sddm/themes/breeze-openSUSE
patch -p2 -i %{SOURCE3}
popd

cp -R %{_kf5_plasmadir}/layout-templates/org.kde.plasma.desktop.defaultPanel/contents %{buildroot}%{_kf5_plasmadir}/layout-templates/org.opensuse.desktop.defaultPanel/contents

# Single file for the layout, so we can use patch -o
mkdir -p %{buildroot}%{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/layouts/
patch -o %{buildroot}%{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js -i %{SOURCE5} %{_kf5_plasmadir}/shells/org.kde.plasma.desktop/contents/layout.js
chmod 644 %{buildroot}%{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/layouts/org.kde.plasma.desktop-layout.js

# components was a symlink before, but this package contains it as a directory.
# RPM does not like that, so we keep it as a symlink but change the target
mv %{buildroot}%{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/{components,components-real}
ln -s components-real %{buildroot}%{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/components

%pre -n plasma5-theme-openSUSE
# RPM does not like to overwrite a directory with a symlink (KUF and 42.2 Beta 3 have the directory)
if [ -d %{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/components ] && \
   ! [ -L %{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/components ]; then
  mv %{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/{components,components-real}
  ln -s components-real %{_kf5_plasmadir}/look-and-feel/org.openSUSE.desktop/contents/components
fi

%files -n plasma5-workspace-branding-openSUSE
%license COPYING

%files -n plasma5-defaults-openSUSE
%license COPYING
%config %{_kf5_configdir}/*rc
%config %{_kf5_configdir}/kdeglobals
%config %{_sysconfdir}/kde4/

%files -n sddm-theme-openSUSE
%license COPYING
%{_kf5_sharedir}/sddm/themes

%files -n plasma5-theme-openSUSE
%license COPYING
%{_kf5_plasmadir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/color-schemes/
%{_kf5_sharedir}/icons/*/*/*/*.*

%changelog
