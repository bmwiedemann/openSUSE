# vim: set sw=4 ts=4 et nu:
#
# spec file for package pamix
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           pamix
Version:        1.6
Release:        0
Summary:        "alsamixer" for pulseaudio
License:        MIT
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://github.com/patroclos/PAmix#pamix---the-pulseaudio-terminal-mixer
Source:         https://github.com/patroclos/PAmix/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
%if 0%{?leap_version} == 420300
BuildRequires:  ncurses-devel
%else
BuildRequires:  pkgconfig(ncursesw)
%endif

%description
ncurses pulseaudio mixer similar to pavucontrol and alsamixer

%prep
%setup -q -n PAmix-%{version}

%build
%cmake

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%config %{_sysconfdir}/%{name}.conf

%changelog
