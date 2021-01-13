#
# spec file for package termit
#
# Copyright (c) 2021 SUSE LLC
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


Name:           termit
Version:        3.1
Release:        0
Summary:        Vte-based Terminal Emulator
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/nonstop/termit/wiki
Source:         https://github.com/nonstop/termit/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.6.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libstdc++-devel
BuildRequires:  lua-devel >= 5.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vte-2.91) >= 0.60.0
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
termit is a terminal emulator based on the vte library. It includes tabs,
bookmarks, and the ability to switch encodings.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%cmake -DDEBUG=false -DCMAKE_C_FLAGS="$(pkg-config --cflags-only-I vte-2.91)"
%cmake_build

%install
%cmake_install
rm -rf "%{buildroot}%{_datadir}/doc"
rm -rf "%{buildroot}%{_prefix}/src"
%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} System TerminalEmulator
%endif

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc ChangeLog TODO
%doc doc/README
%doc doc/rc.lua.example
%doc doc/lua_api.txt
%dir %{_sysconfdir}/xdg/%{name}
%{_datadir}/locale/**/LC_MESSAGES/termit.mo
%config %{_sysconfdir}/xdg/%{name}/colormaps.lua
%config %{_sysconfdir}/xdg/%{name}/utils.lua
%config %{_sysconfdir}/xdg/%{name}/rc.lua
%{_bindir}/%{name}
%{_datadir}/metainfo/termit.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
