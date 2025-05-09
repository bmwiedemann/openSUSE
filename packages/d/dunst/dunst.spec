#
# spec file for package dunst
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


%{!?_userunitdir:%define _userunitdir %{_prefix}/lib/systemd/user}
Name:           dunst
Version:        1.12.2
Release:        0
Summary:        A customizable notification daemon
License:        BSD-3-Clause
Group:          System/GUI/Other
URL:            https://dunst-project.org
Source:         https://github.com/dunst-project/dunst/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)

# tests:
BuildRequires:  awk
BuildRequires:  dbus-1-daemon
# https://github.com/dunst-project/dunst/issues/1404#issuecomment-2562077336
BuildRequires:  dejavu


%description
Dunst is a customizable replacement for the notification daemons
provided by most desktop environments.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for dunst, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name}
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for dunst, generated during the build.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name}
BuildArch:      noarch

%description fish-completion
The official fish completion script for dunst, generated during the build.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build SYSCONFDIR=%{_sysconfdir} all dunstify wayland-protocols

%install
%set_build_flags
%make_install PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir}

%check
%set_build_flags
%make_build PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} test

%files
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{_sysconfdir}/dunst
%config %{_sysconfdir}/dunst/dunstrc
%{_bindir}/dunst
%{_bindir}/dunstify
%{_bindir}/dunstctl
%{_datadir}/dbus-1/services/org.knopwob.dunst.service
%{_userunitdir}/dunst.service
%{_mandir}/man1/dunst.1%{?ext_man}
%{_mandir}/man1/dunstify.1%{?ext_man}
%{_mandir}/man5/dunst.5%{?ext_man}
%{_mandir}/man1/dunstctl.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
