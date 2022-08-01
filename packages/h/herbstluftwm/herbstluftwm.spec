#
# spec file for package herbstluftwm
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


Name:           herbstluftwm
Version:        0.9.5
Release:        0
Summary:        A manual tiling window manager
License:        BSD-2-Clause
Group:          System/GUI/Other
URL:            https://herbstluftwm.org
Source0:        https://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz
Source1:        https://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.desktop
BuildRequires:  asciidoc
BuildRequires:  cmake >= 3.1
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  ncurses-utils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
Bash completion for herbstclient

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish completion for herbstclient

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH completion for herbstclient

%package examples
Summary:        Example scripts for %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Requires:       bash
BuildArch:      noarch

%description examples
Sample bash scripts for herbstluftwm and herbstclient, which give the user
an idea of what is possible.

%prep
%setup -q
# fix errors about improper shebangs due to /usr/bin/env
find . -type f -exec sed -i "s/#!\/usr\/bin\/env bash/#!\/usr\/bin\/bash/" {} +

%build
export CPPFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
%cmake
%make_build

%install
%cmake_install

install -D -m0644  %{SOURCE2} %{buildroot}%{_datadir}/xsessions/%{name}.desktop

# We use the normal doc convention for this instead.
# INSTALL is not shipped.
rm -f %{buildroot}%{_datadir}/doc/%{name}/{INSTALL,NEWS,LICENSE}

%files
%license LICENSE
%doc NEWS
%dir %{_datadir}/doc/%{name}/
%{_datadir}/doc/%{name}/html/
%dir %{_sysconfdir}/xdg/%{name}
%{_sysconfdir}/xdg/%{name}/autostart
%{_sysconfdir}/xdg/%{name}/panel.sh
%{_sysconfdir}/xdg/%{name}/restartpanels.sh
%{_sysconfdir}/xdg/%{name}/dmenu_run_hlwm
%{_bindir}/herbstclient
%{_bindir}/%{name}
%{_mandir}/man1/herbstclient.1%{?ext_man}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man7/%{name}-tutorial.7%{?ext_man}
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/doc/herbstluftwm/hlwm-doc.json

%files examples
%{_datadir}/doc/%{name}/examples/

%files zsh-completion
%{_datadir}/zsh/site-functions/_herbstclient

%files bash-completion
%{_datadir}/bash-completion/completions/herbstclient

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/herbstclient.fish

%changelog
