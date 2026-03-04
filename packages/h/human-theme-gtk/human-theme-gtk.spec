#
# spec file for package human-theme-gtk
#
# Copyright (c) 2021-2026 SUSE LLC
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


Name:           human-theme-gtk
Version:        3.0.0
Release:        0
Summary:        Human theme for GTK
Summary(fr):    Thème Human pour GTK
License:        GPL-3.0-or-later and LGPL-2.1-or-later and CC-BY-SA-3.0
URL:            https://github.com/luigifab/human-theme
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  aspell-fr
Recommends:     gnome-icon-theme
Recommends:     dmz-icon-theme-cursors
Recommends:     gtk2-engine-murrine
Recommends:     libqt5-qtbase-platformtheme-gtk3
Recommends:     libqt5-qtsvg
Recommends:     qt5-globalqss
Recommends:     qt6-platformtheme-gtk3
Recommends:     qt6-globalqss
Recommends:     qt6-svg

%description %{expand:
This theme is mainly intended for MATE and Xfce desktop environments.

After installation you must restart your session.
After uninstallation be sure to remove the config file:
 /etc/profile.d/human-theme-gtk.sh}

%description -l fr %{expand:
Ce thème est principalement destiné pour les environnements
de bureau MATE et Xfce.

Après l'installation vous devez redémarrer votre session.
Après la désinstallation, veillez à supprimer le fichier de config :
 /etc/profile.d/human-theme-gtk.sh}

%prep
%setup -q -n human-theme-%{version}
sed -i 's/IconTheme=gnome/IconTheme=mate/g' src/*/index.theme

%install
install -dm 755 %{buildroot}%{_datadir}/themes/
cp -a src/Human/           %{buildroot}%{_datadir}/themes/
cp -a src/Human-blue/      %{buildroot}%{_datadir}/themes/
cp -a src/Human-green/     %{buildroot}%{_datadir}/themes/
cp -a src/Human-orange/    %{buildroot}%{_datadir}/themes/
install -Dpm 644 data/profile.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

%files
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%license LICENSE
%doc README.md
# the entire source code is GPL-3.0-or-later, except */metacity-1/* which is LGPL-2.1-or-later,
# and */gtk-2.0/* which is CC-BY-SA-3.0-or-later
%{_datadir}/themes/Human/
%{_datadir}/themes/Human-blue/
%{_datadir}/themes/Human-green/
%{_datadir}/themes/Human-orange/

%changelog
