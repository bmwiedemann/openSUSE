#
# spec file for package SwayNotificationCenter
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


%global alt_pkg_name swaync

Name:           SwayNotificationCenter
Version:        0.10.1
Release:        0
Summary:        A simple GTK notification daemon
License:        GPL-3.0-only
URL:            https://github.com/ErikReider/%{name}
Provides:       %{alt_pkg_name} = %{version}-%{release}
Source0:        %{name}-%{version}.tar.gz
Requires:       gvfs
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  meson >= 0.51.0
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  scdoc
BuildRequires:  vala >= 0.56
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.8.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.8.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(systemd)

%description
A simple notification daemon with a GTK gui for notifications and the control center

%package bash-completion
Summary:        Bash completion for %{name}
Provides:       %{alt_pkg_name}-bash-completion = %{version}-%{release}
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}

%package zsh-completion
Summary:        Zsh completion for %{name}
Provides:       %{alt_pkg_name}-zsh-completion = %{version}-%{release}
Supplements:    (%{name} and zsh)
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}

%package fish-completion
Summary:        Fish completion for %{name}
Provides:       %{alt_pkg_name}-fish-completion = %{version}-%{release}
Supplements:    (%{name} and fish)
Requires:       %{name} = %{version}-%{release}
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/xdg/swaync
%config %{_sysconfdir}/xdg/swaync/config.json
%config %{_sysconfdir}/xdg/swaync/configSchema.json
%config %{_sysconfdir}/xdg/swaync/style.css
%{_bindir}/swaync
%{_bindir}/swaync-client
%{_userunitdir}/swaync.service
%{_datadir}/dbus-1/services/org.erikreider.swaync.service
%{_datadir}/glib-2.0/schemas/org.erikreider.swaync.gschema.xml
%{_mandir}/man1/swaync-client.1%{?ext_man}
%{_mandir}/man1/swaync.1%{?ext_man}
%{_mandir}/man5/swaync.5%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/swaync
%{_datadir}/bash-completion/completions/swaync-client

%files zsh-completion
%{_datadir}/zsh/site-functions/_swaync
%{_datadir}/zsh/site-functions/_swaync-client

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/swaync-client.fish
%{_datadir}/fish/vendor_completions.d/swaync.fish

%changelog
