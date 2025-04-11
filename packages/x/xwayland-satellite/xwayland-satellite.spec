#
# spec file for package xwayland-satellite
#
# Copyright (c) 2025 mantarimay
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


%bcond_without test
Name:           xwayland-satellite
Version:        0.5.1
Release:        0
Summary:        Rootless Xwayland integration for Wayland compositors
License:        MPL-2.0
URL:            https://github.com/Supreeeme/xwayland-satellite
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  pkgconfig(xcb-cursor)
Requires:       xwayland

%description
xwayland-satellite grants rootless Xwayland integration to any Wayland
compositor implementing xdg_wm_base. This useful for compositors that
do not support rootless Xwayland themselves (such as niri & weston 14).

%prep
%autosetup -a1 -p1

sed -i 's|/usr/local|/usr|' resources/%{name}.service

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}
install -Dm644 resources/%{name}.service -t %{buildroot}%{_userunitdir}

%if %{with test}
%check
%{cargo_test} -- \
    --skip=copy_from_wayland \
    --skip=quick_delete \
    --skip=copy_from_x11 \
    --skip=input_focus \
    --skip=close_window \
    --skip=reparent \
    --skip=toplevel_flow \
    --skip=bad_clipboard_data \
    --skip=different_output_position \
    --skip=funny_window_title \
    --skip=fake_selection_targets \
    --skip=primary_output \
    --skip=wayland_then_x11_clipboard_owner
%endif

%files
%license LICEN*
%doc README*
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
