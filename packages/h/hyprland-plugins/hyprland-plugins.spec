#
# spec file for package hyprland-plugins
#
# Copyright (c) 2025 SUSE LLC
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


Name:           hyprland-plugins
Version:        0.49.0+fix
Release:        0
%global pkg_version 0.49.0-fix
Summary:        Official plugins for Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-plugins
Source0:        https://github.com/hyprwm/hyprland-plugins/archive/refs/tags/v%{pkg_version}.tar.gz#/%{name}-%{pkg_version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(hyprland) >= 0.49.0
BuildRequires:  pkgconfig(pangocairo)
%requires_ge    hyprland

%{lua: plugins = {
	['borders-plus-plus'] = 'This plugin adds one or two additional borders to windows',
	['csgo-vulkan-fix'] = 'This fixes custom resolutions on CS:GO with -vulkan',
	['hyprbars'] = 'This plugin adds title bars to windows',
	['hyprexpo'] = 'This plugin adds an expo-like workspace overview',
	['hyprscrolling'] = 'This plugin adds a scrolling layout to hyprland',
	['hyprtrails'] = 'This plugin adds smooth trails behind moving windows',
	['hyprwinwrap'] = 'This plugin is a clone of xwinwrap, allows you to put any app as a\nwallpaper',
	['xtra-dispatchers'] = 'This plugin adds some new dispatchers',
}}

%define _description %{expand:
Plugins allow users to add extra functionality to Hyprland.
}
%description %{_description}

%{lua:
for plugin,desc in pairs(plugins) do
	print("%package -n hyprland-plugin-"..plugin.."\n")
	print("Summary:\tHyprland plugin: "..plugin.."\n")
	print("\n%description -n hyprland-plugin-"..plugin..rpm.expand("%_description").."\n"..desc.."\n")
	print("\n%files -n hyprland-plugin-"..plugin.."\n")
	print("%license LICENSE\n")
	local hyprdir = rpm.expand("%_libdir").."/hyprland/"
	print("%dir "..hyprdir.."\n")
	print("%dir "..hyprdir.."plugins/\n")
	print(hyprdir.."plugins/"..plugin..".so\n")
end
}

%prep
%autosetup -p1 -n %{name}-%{pkg_version}

%build
%set_build_flags
%{lua:
for plugin,_ in pairs(plugins) do
	print(rpm.expand("%make_build").." -C "..plugin.." all\n")
end
}

%install
install -D -m 0755 -t %{buildroot}%{_libdir}/hyprland/plugins/ */*.so

%changelog
