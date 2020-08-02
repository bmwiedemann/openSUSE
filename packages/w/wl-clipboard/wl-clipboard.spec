#
# spec file for package slurp
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

Name:           wl-clipboard
Version:        2.0.0
Release:        0
License:        GPL-3.0-only
Summary:        Wayland Clipboard Utilities
Url:            https://github.com/bugaevc/wl-clipboard
Group:          Productivity/Graphics/Other
Source:         https://github.com/bugaevc/%{name}/archive/v%{version}.tar.gz
BuildRequires:  meson >= 0.43.0
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-server) >= 1.16
Recommends:     xdg-utils
Recommends:     mailcap

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This project implements two command-line Wayland clipboard utilities, wl-copy and wl-paste, that let you easily copy data between the clipboard and Unix pipes, sockets, files and so on.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q

%build
# This is kind of a hack IMHO because the wl-clipboard meson build scripts
# don't call pkg-config when they probably should
export CFLAGS="%{optflags} -I/usr/include/wayland"
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_mandir}/man1/wl-clipboard.1.*
%{_mandir}/man1/wl-copy.1.*
%{_mandir}/man1/wl-paste.1.*

%files zsh-completion
%{_datadir}/zsh/site-functions/_wl-copy
%{_datadir}/zsh/site-functions/_wl-paste

%files bash-completion
%{_datadir}/bash-completion/completions/wl-copy
%{_datadir}/bash-completion/completions/wl-paste

%changelog
