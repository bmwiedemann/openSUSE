#
# spec file for package nwg-bar
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

Name:           nwg-bar
Version:        0.1.6
Release:        0
Summary:        Golang replacement to the nwgbar 
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-bar
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch0:         no-docs.patch
BuildRequires:  golang(API) >= 1.20
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  gtk-layer-shell-devel


%description
Golang replacement to the nwgbar command (a part of nwg-launchers), with some improvements. Originally aimed at sway, works with wlroots-based compositors only.
%prep
%autosetup -a 1 -p0

%build
go build -o bin/nwg-bar -mod=vendor -buildmode=pie

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README.md
%{_bindir}/nwg-bar
%dir %{_datadir}/nwg-bar
%{_datadir}/nwg-bar/*

%changelog
