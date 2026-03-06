#
# spec file for package new
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
Name:           cockpit-client-launcher
Version:        356
Release:        0
Summary:        Flatpak-free launcher for the Cockpit GTK client
License:        LGPL-2.1-or-later
URL:            https://cockpit-project.org/
Source1:        %{name}
Source2:        %{name}.desktop
Source3:        cockpit-icon-y2-colors.svg
BuildRequires:  hicolor-icon-theme
Requires:       cockpit-ws
Requires:       cockpit-system
# Not so sure about this particular one
Requires:       libwebkit2gtk3
Requires:       typelib-1_0-WebKit2-4_1
Requires:       zenity
Recommends:     cockpit-ws-selinux
BuildArch:      noarch

%description
%{name} provides a desktop launcher for the Cockpit GTK client without
requiring Flatpak. It connects to the locally installed cockpit-ws service
and automatically detects the configured listening port from cockpit.socket.

%prep

%build

%install
install -d %{buildroot}%{_bindir}
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

install -d %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE2} \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 %{SOURCE3} \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
