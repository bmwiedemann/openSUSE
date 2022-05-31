#
# spec file for package sway-launcher-desktop
#
# Copyright (c) 2022 SUSE LLC
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


Name:           sway-launcher-desktop
Version:        1.6.0
Release:        0
Summary:        TUI Application launcher with Desktop Entry support
License:        GPL-3.0-only
BuildArch:      noarch
Group:          System/X11/Utilities
URL:            https://github.com/Biont/sway-launcher-desktop
Source:         https://github.com/Biont/sway-launcher-desktop/archive/v%{version}.tar.gz
Patch0:         reset-shebang.patch
Requires:       fzf

%description
This is a TUI-based launcher menu made with bash and the amazing fzf. Despite its name, it does not depend on the Sway window manager can be used with just about any WM.

%prep
%setup -q -n %{name}-%{version}
%patch0

%build

%install
install -Dm755 sway-launcher-desktop.sh %{buildroot}%{_bindir}/sway-launcher-desktop

%files
%defattr(-, root, root)
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
