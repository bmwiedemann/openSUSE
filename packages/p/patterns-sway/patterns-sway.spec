#
# spec file for package patterns-sway
#
# Copyright (c) 2020 SUSE LLC
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
Version:        20200619
Release:        0
Summary:        Patterns for Installation (Sway)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
Group:          Metapackages
Provides:       pattern() = sway
Provides:       pattern-icon() = pattern-sway
Provides:       pattern-order() = 1460
Provides:       pattern-visible()

Requires:       Mesa
Requires:       alacritty
Requires:       grim
Requires:       mako
Requires:       slurp
Requires:       sway
Requires:       swaybg
Requires:       swayidle
Requires:       swaylock
Requires:       waybar
Requires:       wofi

Recommends:     kanshi
Recommends:     pulseaudio
Recommends:     pulseaudio-utils

Recommends:     system-config-printer
Recommends:     desktop-data-openSUSE

#upstream brandings for clean Sway experience
Recommends:     sway-branding-upstream
Recommends:     waybar-branding-upstream

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
