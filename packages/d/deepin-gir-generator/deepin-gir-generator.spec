#
# spec file for package deepin-gir-generator
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define _name go-gir-generator

Name:           deepin-gir-generator
Version:        2.0.2
Release:        0
Summary:        Go-gir-generator imeplement static golang bindings for GObject
License:        MIT
Group:          Development/Languages/Golang
Url:            https://github.com/linuxdeepin/go-gir-generator
Source:         https://github.com/linuxdeepin/%{_name}/archive/%{version}/%{_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM support-glib2_36-and-higher.patch hillwood@opensuse.org -- Fix compatibility with glib 2.63+
Patch0:         support-glib2_36-and-higher.patch
%if 0%{?suse_version} > 1500
BuildRequires:  golang(API) = 1.15
%endif
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  fdupes
Provides:       %{_name}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Go-gir-generator imeplement static golang bindings for GObject.

There has many go bindings for GObject/Gtk libraries, but almost all of them 
are written by hand. It's bored and error-prone when the binding C libaray 
changed.

Go-gir-geneator's object is like python-gobject's that binding the newest 
library without need change binding codes.

Currently it only official support Gobject-2.0, Glib-2.0, Gio-2.0. Because 
generate the gdkpixbuf binding hasn't completed, so Gdk/Gtk were also in blocking.


%package -n golang-github-linuxdeepin-go-gir-generator
Summary:        Additional mobile libraries
Group:          Development/Languages/Golang
AutoReqProv:    Off
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(gudev-1.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-2.0)
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(gdk-2.0)
Requires:       pkgconfig(gdk-3.0)
Requires:       pkgconfig(gudev-1.0)
Provides:       golang(pkg.deepin.io/gir/glib-2.0)
Provides:       golang(pkg.deepin.io/gir/gio-2.0)
Provides:       golang(pkg.deepin.io/gir/gobject-2.0)
Provides:       golang(pkg.deepin.io/gir/gudev-1.0)
BuildArch:      noarch

%{go_exclusivearch}

%description -n golang-github-linuxdeepin-go-gir-generator
Go-gir-generator imeplement static golang bindings for GObject.

There has many go bindings for GObject/Gtk libraries, but almost all of them 
are written by hand. It's bored and error-prone when the binding C libaray 
changed.

Go-gir-geneator's object is like python-gobject's that binding the newest 
library without need change binding codes.

Currently it only official support Gobject-2.0, Glib-2.0, Gio-2.0. Because 
generate the gdkpixbuf binding hasn't completed, so Gdk/Gtk were also in blocking.

%prep
%autosetup -p1 -n %{_name}-%{version}

# fix go source path
%if 0%{?suse_version} >= 1330
sed -i 's|gocode|go/%{go_api_ver}/contrib|' Makefile
%else
sed -i 's|gocode|go/contrib|' Makefile
%endif

%build
make %{?_smp_mflags}

%install
%make_install

%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md documentation/WhyWaf.txt documentation/Design.txt
%license LICENSE
%{_bindir}/gir-generator

%files -n golang-github-linuxdeepin-go-gir-generator
%defattr(-,root,root,-)
%{go_contribsrcdir}/*

%changelog
