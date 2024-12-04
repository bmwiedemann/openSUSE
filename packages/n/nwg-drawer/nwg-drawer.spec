#
# spec file for package nwg-drawer
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


Name:           nwg-drawer
Version:        0.6.0
Release:        0
Summary:        Wlroots application drawer
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-drawer
Source:         https://github.com/nwg-piotr/nwg-drawer/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  make
BuildRequires:  golang(API) >= 1.23
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(pango)

%description
Application drawer for wlroots-based Wayland compositors.

%prep
%autosetup -p1 -a1

%build
go build -v -o bin/%{name} -mod=vendor -buildmode=pie

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r desktop-directories %{buildroot}%{_datadir}/%{name}
cp -r img %{buildroot}%{_datadir}/%{name}
install -m644 drawer.css %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
install -m755 bin/%{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
