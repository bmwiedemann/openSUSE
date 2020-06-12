#
# spec file for package bspwm
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 Luke Jones, luke.nukem.jones@gmail.com
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


Name:           bspwm
Version:        0.9.9
Release:        0
Summary:        A tiling window manager based on binary space partitioning
License:        BSD-2-Clause
Group:          System/GUI/Other
URL:            https://github.com/baskerville/bspwm
Source0:        https://github.com/baskerville/bspwm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        bspwm.desktop
BuildRequires:  pkgconfig
BuildRequires:  zsh
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
Recommends:     dmenu
Recommends:     lemonbar
Recommends:     sxhkd

%description
A tiling window manager based on binary space partitioning.
* It only responds to X events, and the messages it receives on a dedicated socket.
* bspc is a program that writes messages on bspwm's socket.
* bspwm doesn't handle any keyboard or pointer inputs: a third party program (e.g.
sxhkd) is needed in order to translate keyboard and pointer events to bspc invocations.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
Bash completion for bspc

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
ZSH completion for bspc

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
Fish completion for bspc

%prep
%setup -q
# fix rpmlint E: env-script-interpreter
sed -i 's,^#! /usr/bin/env ,#!/usr/bin/,' ./examples/receptacles/{extract_canvas,induce_rules}

%build
export CPPFLAGS="%{optflags} -fcommon"
make %{?_smp_mflags} V=1

%install
%make_install PREFIX=%{_prefix} DOCPREFIX=%{_docdir}/%{name}
install -pm 644 %{SOURCE1} contrib/freedesktop/bspwm.desktop
install -D -p -m 644 examples/bspwmrc \
        %{buildroot}%{_sysconfdir}/skel/.config/bspwm/bspwmrc
install -D -p -m 644 LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%{_bindir}/bspwm
%{_bindir}/bspc
%{_docdir}/%{name}
%{_mandir}/man1/bspwm.1%{?ext_man}
%{_mandir}/man1/bspc.1%{?ext_man}
%{_datadir}/xsessions/bspwm.desktop
%{_sysconfdir}/skel/.config/bspwm
%config %{_sysconfdir}/skel/.config/bspwm/bspwmrc

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
