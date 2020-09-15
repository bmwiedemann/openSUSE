#
# spec file for package gtkgreet
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gtkgreet
Version:        0.6
Release:        0
Summary:        GTK based greeter for greetd
License:        GPL-3.0
URL:            https://git.sr.ht/~kennylevinsen/gtkgreet
Source:         %{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  cmake
BuildRequires:  libjson-c-devel
BuildRequires:  scdoc
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)
Recommends:     greetd

%description
GTK based greeter for greetd, to be run under cage or similar.

%prep
%setup -q

%build
%meson -Dlayershell=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*

%changelog
