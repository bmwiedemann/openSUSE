#
# spec file for package nwg-look
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

Name:           nwg-look
Version:        0.2.7
Release:        0
Summary:        GTK3 settings editor adapted to work in sway/wlroots environment
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-look
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch0:         no-docs.patch
BuildRequires:  golang(API) >= 1.22
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Nwg-look is a GTK3 settings editor, designed to work properly in wlroots-based Wayland environment. The look and feel is strongly influenced by LXAppearance.

%prep
%autosetup -a 1 -p0

%build
go build -o bin/nwg-look -mod=vendor -buildmode=pie

%install
%make_install PREFIX="%{_prefix}"

%files
%doc README.md
%license LICENSE
%{_bindir}/nwg-look
%dir %{_datadir}/nwg-look
%{_datadir}/nwg-look/*
%{_datadir}/applications/nwg-look.desktop
%{_datadir}/pixmaps/nwg-look.svg

%changelog
