#
# spec file for package nwg-dock-hyprland
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2023-2025 Malcolm J Lewis <malcolmlewis@opensuse.org>
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
Version:        0.4.3
Release:        0
Summary:        Hyprland application dock
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-dock-hyprland
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  go >= 1.22
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)

%description
Configurable (w/ command line arguments and css) dock, written in Go, aimed
exclusively at the Hyprland Wayland compositor. It features pinned buttons,
client buttons and the launcher button.

%prep
%autosetup -p1 -a1

%build
## Note build takes around 15 minutes
go build -v \
   -mod=vendor \
   -buildmode=pie

%install
install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/images
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 config/style.css %{buildroot}%{_datadir}/%{name}/style.css
cp -ar images/* %{buildroot}%{_datadir}/%{name}/images/

%files
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/style.css
%{_datadir}/%{name}/images

%changelog
