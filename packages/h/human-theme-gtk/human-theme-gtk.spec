#
# spec file for package human-theme-gtk
#
# Copyright (c) 2021-2025 SUSE LLC
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
Version:        2.4.0
Release:        0
Summary:        Human theme for GTK
Summary(fr):    Thème Human pour GTK
License:        GPL-3.0-or-later AND LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:            https://github.com/luigifab/human-theme
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  aspell-fr
Recommends:     dmz-icon-theme-cursors
Recommends:     gnome-icon-theme
Recommends:     gtk2-engine-murrine
Suggests:       libqt5-qtbase-platformtheme-gtk3
Suggests:       libqt5-qtstyleplugins-platformtheme-gtk2
Suggests:       qt6-platformtheme-gtk3
# https://software.opensuse.org/search?baseproject=openSUSE%3AFactory&q=qt+theme+gtk
BuildArch:      noarch

%description %{expand:
This theme works with GTK 2.24 (with gtk2-engine-murrine),
3.24, and 4.12. Better rendering with Pango 1.42- or 1.51+.

It is mainly intended for MATE and Xfce desktop environments.
After installation you must restart your session.}

%description -l fr %{expand:
Ce thème fonctionne avec : GTK 2.24 (avec gtk2-engine-murrine),
3.24, et 4.12. Meilleur rendu avec Pango 1.42- ou 1.51+.

Il est principalement destiné pour les environnements de bureau MATE et Xfce.
Après l'installation vous devez redémarrer votre session.}

%prep
%setup -q -n human-theme-%{version}
sed -i 's/IconTheme=gnome/IconTheme=mate/g' src/*/index.theme

%install
install -dm 755 %{buildroot}%{_datadir}/themes/
cp -a src/human-theme/           %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-blue/      %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-green/     %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-orange/    %{buildroot}%{_datadir}/themes/
install -Dpm 644 data/profile.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

%files
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%license LICENSE
%doc README.md
# the entire source code is GPL-3.0-or-later, except */metacity-1/* which is LGPL-2.1-or-later,
# and */gtk-2.0/* which is CC-BY-SA-3.0-or-later
%{_datadir}/themes/human-theme/
%{_datadir}/themes/human-theme-blue/
%{_datadir}/themes/human-theme-green/
%{_datadir}/themes/human-theme-orange/

%changelog
