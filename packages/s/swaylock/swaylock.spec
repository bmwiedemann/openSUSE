#
# spec file for package swaylock
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


Name:           swaylock
Version:        1.7
Release:        0
Summary:        Screen locker for Wayland
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.48.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
Suggests:       %{name}-bash-completion
Suggests:       %{name}-fish-completion
Suggests:       %{name}-zsh-completion
Conflicts:      sway < 1.0

%description
swaylock is a screen locking utility for Wayland compositors.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch
Conflicts:      sway < 1.0

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -I/usr/include/wayland"
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/swaylock
%config %{_sysconfdir}/pam.d/swaylock
%{_mandir}/man1/swaylock.1%{?ext_man}

%files bash-completion
%dir %{_datadir}/bash-completion/
%{_datadir}/bash-completion/completions

%files fish-completion
%dir %{_datadir}/fish/
%{_datadir}/fish/vendor_completions.d/

%files zsh-completion
%dir %{_datadir}/zsh/
%{_datadir}/zsh/site-functions

%changelog
