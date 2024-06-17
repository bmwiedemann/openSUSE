#
# spec file for package nwg-dock-hyprland
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023-2024 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           nwg-dock-hyprland
Version:        0.1.9
Release:        0
Summary:        Hyprland application dock
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-dock-hyprland
Source0:        https://codeload.github.com/nwg-piotr/nwg-dock-hyprland/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  go >= 1.22
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  pkgconfig(gtk-layer-shell-0)

%description
Configurable (w/ command line arguments and css) dock, written in Go, aimed
exclusively at the Hyprland Wayland compositor. It features pinned buttons,
client buttons and the launcher button.

%prep
%autosetup -p1 -a1

%build
## Note build takes around 10 minutes, so be patient as there is no output!
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 config/style.css %{buildroot}%{_datadir}/%{name}/style.css

%files
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/style.css

%changelog
