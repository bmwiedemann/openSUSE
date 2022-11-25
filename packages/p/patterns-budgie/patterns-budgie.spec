#
# spec file for package patterns-budgie
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Callum Farmer <gmbr3@opensuse.org>
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


%bcond_with betatest
Name:           patterns-budgie
Version:        20220527
Release:        0
Summary:        Patterns for Installation (Budgie)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Budgie pattern.

################################################################################

%package budgie
%pattern_graphicalenvironments
Summary:        Budgie Desktop Environment
Group:          Metapackages
Provides:       pattern() = budgie
Provides:       pattern-icon() = pattern-budgie
Provides:       pattern-order() = 1660
Provides:       pattern-visible()
Requires:       pattern() = x11
Requires:       pattern() = x11_yast
Requires:       budgie-desktop
Requires:       lightdm
Recommends:     gnome-terminal
Recommends:     budgie-backgrounds
Recommends:     gnome-software
Suggests:       gnome-backgrounds
Suggests:       cheese
Suggests:       dconf-editor
Suggests:       evince
Suggests:       evolution
Suggests:       evolution-ews
Suggests:       gnome-bluetooth
Suggests:       gnome-calculator
Suggests:       gnome-characters
Suggests:       gnome-clocks
Suggests:       gnome-contacts
Suggests:       gnome-control-center-color
Suggests:       gnome-control-center-goa
Suggests:       gnome-dictionary
Suggests:       gnome-disk-utility
Suggests:       gnome-documents
Suggests:       gnome-logs
Suggests:       gnome-maps
Suggests:       gnome-screenshot
Suggests:       gnome-system-monitor

%description budgie
The Budgie Desktop is a feature-rich, modern desktop designed to keep out the way of the user.

%files budgie
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/budgie.txt

%package budgie_applets
%pattern_budgiedesktop
Summary:        Applets for Budgie Desktop Environment
Group:          Metapackages
Provides:       pattern() = budgie_applets
Provides:       pattern-icon() = pattern-budgie
Provides:       pattern-order() = 2370
Provides:       pattern-visible()
Requires:       pattern() = budgie
## Other applets ##
Recommends:     budgie-calendar-applet
Recommends:     budgie-screenshot-applet
Recommends:     budgie-haste-applet
## BUDGIE EXTRAS ##
Recommends:     budgie-app-launcher-applet
Recommends:     budgie-applications-menu-applet
Recommends:     budgie-brightness-controller-applet
Recommends:     budgie-clockworks-applet
Recommends:     budgie-countdown-applet
Recommends:     budgie-dropby-applet
Recommends:     budgie-fuzzyclock-applet
Recommends:     budgie-hotcorners-applet
Recommends:     budgie-kangaroo-applet
Recommends:     budgie-keyboard-autoswitch-applet
Recommends:     budgie-network-manager-applet
Recommends:     budgie-previews
Recommends:     budgie-quickchar
Recommends:     budgie-quicknote-applet
Recommends:     budgie-recentlyused-applet
Recommends:     budgie-rotation-lock-applet
Recommends:     budgie-showtime-applet
Recommends:     budgie-takeabreak-applet
Recommends:     budgie-trash-applet
Recommends:     budgie-visualspace-applet
Recommends:     budgie-wallstreet
Recommends:     budgie-weathershow-applet
Recommends:     budgie-window-shuffler
Recommends:     budgie-workspace-stopwatch-applet
Recommends:     budgie-workspace-wallpaper-applet
#

%description budgie_applets
Applets for Budgie Desktop Environment

%files budgie_applets
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/budgie_applets.txt


%prep

%build

%install
mkdir -p %{buildroot}%{_defaultdocdir}/patterns
echo 'This file marks the pattern budgie to be installed.' >%{buildroot}%{_defaultdocdir}/patterns/budgie.txt
echo 'This file marks the pattern budgie_applets to be installed.' >%{buildroot}%{_defaultdocdir}/patterns/budgie_applets.txt

%changelog
