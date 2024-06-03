#
# spec file for package ydotool
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ydotool
Version:        1.0.4
Release:        0
Summary:        Generic command-line automation tool (no X!)
License:        AGPL-3.0-only
URL:            https://github.com/ReimuNotMoe/ydotool
Source:         https://github.com/ReimuNotMoe/ydotool/archive/v1.0.4.tar.gz#/ydotool-1.0.4.tar.gz
BuildRequires:  cmake >= 3.4
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros

%description
ydotool is not limited to Wayland. You can use it on anything as long as it
accepts keyboard/mouse/whatever input. For example, X11, text console,
"RetroArch OS", fbdev apps (fbterm/mplayer/SDL1/LittleVGL/Qt Embedded), etc.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_userunitdir}/%{name}.service
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man8/%{name}d.8%{?ext_man}

%changelog
