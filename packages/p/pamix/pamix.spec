# vim: set sw=4 ts=4 et nu:
#
# spec file for package pamix
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


Name:           pamix
Version:        2.1
Release:        0
Summary:        "alsamixer" for pulseaudio
License:        MIT
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://github.com/patroclos/PAmix#pamix---the-pulseaudio-terminal-mixer
Source:         https://github.com/patroclos/PAmix/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
%if 0%{?leap_version} == 420300
BuildRequires:  ncurses-devel
%else
BuildRequires:  pkgconfig(ncursesw)
%endif
# PATCH-FIX-OPENSUSE pamix-install-man-to-man1.patch -- install man page
# into man1 subdir (upstream TYPE MAN lands in share/man with the
# compat-capped cmake_minimum, invisible to man and failing %files)
Patch0:         pamix-install-man-to-man1.patch

%description
ncurses pulseaudio mixer similar to pavucontrol and alsamixer

%prep
%autosetup -p1 -n PAmix-%{version}

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%dir %{_sysconfdir}/xdg
%config %{_sysconfdir}/xdg/%{name}.conf

%changelog
