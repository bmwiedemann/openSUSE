#
# spec file for package playerctl
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017 Dakota Williams <raineforest@raineforest.me>
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


%global majorver 2
%global minorver 0
%global sover 2
%global libname lib%{name}%{sover}
%global typelibname typelib-1_0-Playerctl-%{majorver}_%{minorver}
Name:           playerctl
Version:        2.4.1
Release:        0
Summary:        MPRIS command-line controller and library for media players
License:        LGPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://github.com/acrisci/playerctl
Source0:        https://github.com/acrisci/playerctl/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.38
BuildRequires:  pkgconfig(gtk-doc)

%description
Playerctl is a command-line utility and library for controlling
media players that implement the MPRIS D-Bus Interface Specification.
Playerctl makes it easy to bind player actions, such as play and pause,
to media keys.

For more advanced users, Playerctl provides an introspectable library
available in your favorite scripting language that allows more detailed
control like the ability to subscribe to media player events or get metadata,
such as artist and title for the playing track.

%package -n %{libname}
Summary:        A library for controlling media players over D-Bus
Group:          System/Libraries

%description -n %{libname}
A library for controlling media players that implement the MPRIS D-Bus
Interface Specification.

%package -n %{typelibname}
Summary:        GObject Introspection interface description for lib%{name}
Group:          System/Libraries
# Obsolete the wrongly named package, Last seen in package version 2.0.1
Obsoletes:      typelib-1_0-Playerctl-2_0_1 < %{version}

%description -n %{typelibname}
This package provides the GObject Introspection bindings lib%{name},
enabling usage in programming languages that support it.

%package devel
Summary:        Development files for lib%{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package provides libraries and headers for developing applications that
use lib%{name}.

%package doc
Summary:        Documentation for lib%{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides HTML documentation for lib%{name}.

%package        bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%package        zsh-completion
Summary:        ZSH completion for %{name}
Group:          System/Shells
Requires:       zsh
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description    zsh-completion
ZSH command line completion support for %{name}.

%prep
%autosetup
# remove shebang
sed -i '/^#!/d' data/playerctl.bash

%build
%meson --default-library=shared -Dbash-completions=true -Dzsh-completions=true
%meson_build

%install
%meson_install
# we only want the shared library
rm -f %{buildroot}%{_libdir}/lib%{name}.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_datadir}/dbus-1/services/org.mpris.MediaPlayer2.playerctld.service
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n %{libname}
%license COPYING
%{_libdir}/lib%{name}.so.%{sover}*

%files -n %{typelibname}
%{_libdir}/girepository-1.0/Playerctl-%{majorver}.%{minorver}.typelib

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Playerctl-%{majorver}.%{minorver}.gir

%files doc
%{_datadir}/gtk-doc/html/%{name}

%files bash-completion
%{_datadir}/bash-completion/

%files zsh-completion
%{_datadir}/zsh/

%changelog
