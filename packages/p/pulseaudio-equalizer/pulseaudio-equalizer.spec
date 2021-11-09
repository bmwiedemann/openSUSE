#
# spec file for package pulseaudio-equalizer
#
# Copyright (c) 2021 SUSE LLC
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


%define _name   pulseaudio-equalizer-ladspa
Name:           pulseaudio-equalizer
Version:        3.0.2
Release:        0
Summary:        PulseAudio's LADSPA plugin graphical user interface
License:        GPL-3.0-or-later
URL:            https://github.com/pulseaudio-equalizer-ladspa/equalizer
Source:         https://github.com/pulseaudio-equalizer-ladspa/equalizer/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pulseaudio-equalizer-fix-locale-issues.patch sor.alexei@meowr.ru -- Fix issues on non-Latin systems.
Patch0:         pulseaudio-equalizer-fix-locale-issues.patch
# PATCH-FIX-OPENSUSE pulseaudio-equalizer-use-pactl.patch sor.alexei@meowr.ru -- Use pactl instead of pacmd.
Patch1:         pulseaudio-equalizer-use-pactl.patch
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  update-desktop-files
Requires:       bc
Requires:       ladspa-swh-plugins
Requires:       pulseaudio-daemon
Requires:       pulseaudio-utils
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
GUI for PulseAudio's LADSPA interface using Steve Harris' Multiband EQ
(mbeq_1197) plugin.

%prep
%autosetup -n equalizer-%{version} -p1

%build
%meson -Dpurelib=%{python3_sitelib}
%meson_build

%install
%meson_install
%py3_compile %{buildroot}%{python3_sitelib}/pulseeq/
sed -i '/^#!/s|env python3$|python3|' %{buildroot}%{_bindir}/%{name}-gtk

%suse_update_desktop_file -r com.github.%{_name}.Equalizer AudioVideo Mixer GTK

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-gtk
%{_datadir}/%{_name}/
%{_datadir}/applications/*%{_name}*.desktop
%{python3_sitelib}/pulseeq/

%changelog
