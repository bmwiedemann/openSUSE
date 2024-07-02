#
# spec file for package hyprshot
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


Name:           hyprshot
Version:        1.3.0+2
Release:        0
Summary:        Hyprland screenshot utility
License:        GPL-3.0-only
URL:            https://github.com/Gustash/Hyprshot
Source0:        %{name}-%{version}.tar.xz
Source99:       hyprshot-rpmlintrc
Requires:       ImageMagick
Requires:       grim
Requires:       hyprland
Requires:       jq
Requires:       libnotify-tools
Requires:       slurp
Requires:       wl-clipboard
BuildArch:      noarch

%description
Hyprshot is a utility to take screenshot in Hyprland using the mouse.

It allows taking screenshots of windows, regions and monitors which
are saved to a folder of choice copied to the clipboard.

%prep
%autosetup

#
# Fix shebang issues
#
sed -i -r 's,(/usr/bin/)env (bash),\1\2,' hyprshot

%build
# Just a placeholder

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 hyprshot  %{buildroot}%{_bindir}/hyprshot

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprshot

%changelog
