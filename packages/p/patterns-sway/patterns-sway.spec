#
# spec file for package patterns-sway
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


%bcond_with betatest
Name:           patterns-sway
Version:        20261030
Release:        0
Summary:        Patterns for Installation (Sway)
License:        MIT
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the sway patterns.

################################################################################

%package sway
%pattern_graphicalenvironments
Summary:        Sway Tiling Wayland Compositor and related tools
Provides:       pattern() = sway
Provides:       pattern-icon() = pattern-sway
Provides:       pattern-order() = 1470
Provides:       pattern-visible()
# SECTION core compositor
Requires:       Mesa
Requires:       alacritty
Requires:       fontawesome-fonts
Requires:       grim
Requires:       slurp
Requires:       sway
Requires:       swaybg
Requires:       swayidle
Requires:       swaylock
Requires:       waybar
Requires:       wofi
# /SECTION
# SECTION output management
Recommends:     kanshi
# /SECTION
# SECTION clipboard
Recommends:     wl-clipboard
# /SECTION
# SECTION audio
Recommends:     pipewire-pulseaudio
Recommends:     pulseaudio-utils
# /SECTION
# SECTION desktop integration
Recommends:     desktop-data-openSUSE
Recommends:     system-config-printer
# /SECTION
#upstream brandings for clean Sway experience
# SECTION upstream branding
Recommends:     sway-branding-upstream
Recommends:     waybar-branding-upstream
# /SECTION

%description sway
Sway Tiling Wayland Compositor and related tools.

%files sway
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/sway.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern sway to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/sway.txt

%changelog
