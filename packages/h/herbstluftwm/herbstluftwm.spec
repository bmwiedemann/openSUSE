#
# spec file for package herbstluftwm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           herbstluftwm
Version:        0.7.2
Release:        0
Summary:        A manual tiling window manager
License:        BSD-2-Clause
Group:          System/GUI/Other
Url:            https://herbstluftwm.org
Source0:        https://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz
Source1:        https://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.desktop
# PATCH-FIX-SUSE Remove executable bits from the documentation
Patch0:         examples-remove-executable-bits.patch
BuildRequires:  asciidoc
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  glib2-devel
BuildRequires:  libxslt-devel
BuildRequires:  ncurses-utils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description bash-completion
Bash completion for herbstclient

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
Fish completion for herbstclient

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zsh)
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
%patch0 -p1
# fix errors about improper shebangs due to /usr/bin/env
find . -type f -exec sed -i "s/#!\/usr\/bin\/env bash/#!\/usr\/bin\/bash/" {} +

%build
export CPPFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
make VERBOSE= COLOR=0 %{?_smp_mflags}

%install
%make_install \
	INSTALL="install -p" \
	PREFIX="%{_prefix}"

install -D -m0644  %{SOURCE2} %{buildroot}%{_datadir}/xsessions/%{name}.desktop

# We use the normal doc convention for this instead.
# INSTALL is not shipped.
rm -f %{buildroot}%{_datadir}/doc/%{name}/{INSTALL,NEWS,LICENSE,BUGS}

%files
%doc BUGS LICENSE NEWS
%dir %{_datadir}/doc/%{name}/
%{_datadir}/doc/%{name}/herbstclient.html
%{_datadir}/doc/%{name}/%{name}-tutorial.html
%{_datadir}/doc/%{name}/%{name}.html
%dir %{_sysconfdir}/xdg/%{name}
%{_sysconfdir}/xdg/%{name}/autostart
%{_sysconfdir}/xdg/%{name}/panel.sh
%{_sysconfdir}/xdg/%{name}/restartpanels.sh
%{_bindir}/herbstclient
%{_bindir}/%{name}
%{_bindir}/dmenu_run_hlwm
%{_mandir}/man1/herbstclient.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man7/%{name}-tutorial.7%{ext_man}
%{_datadir}/xsessions/%{name}.desktop

%files examples
%dir %{_datadir}/doc/%{name}/examples
%{_datadir}/doc/%{name}/examples/README
%{_datadir}/doc/%{name}/examples/dmenu.sh
%{_datadir}/doc/%{name}/examples/dumpbeautify.sh
%{_datadir}/doc/%{name}/examples/exec_on_tag.sh
%{_datadir}/doc/%{name}/examples/execwith.sh
%{_datadir}/doc/%{name}/examples/float-maximize.sh
%{_datadir}/doc/%{name}/examples/floatmon.sh
%{_datadir}/doc/%{name}/examples/herbstcommander.sh
%{_datadir}/doc/%{name}/examples/keychain.sh
%{_datadir}/doc/%{name}/examples/lasttag.sh
%{_datadir}/doc/%{name}/examples/layout.sh
%{_datadir}/doc/%{name}/examples/loadstate.sh
%{_datadir}/doc/%{name}/examples/maximize.sh
%{_datadir}/doc/%{name}/examples/q3terminal.sh
%{_datadir}/doc/%{name}/examples/savestate.sh
%{_datadir}/doc/%{name}/examples/scratchpad.sh
%{_datadir}/doc/%{name}/examples/toggledualhead.sh
%{_datadir}/doc/%{name}/examples/windowmenu.sh
%{_datadir}/doc/%{name}/examples/wselect.sh

%files zsh-completion
%dir %{_datadir}/zsh/functions
%dir %{_datadir}/zsh/functions/Completion
%dir %{_datadir}/zsh/functions/Completion/X
%{_datadir}/zsh/functions/Completion/X/_herbstclient

%files bash-completion
%config %{_sysconfdir}/bash_completion.d/herbstclient-completion

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/herbstclient.fish

%changelog
