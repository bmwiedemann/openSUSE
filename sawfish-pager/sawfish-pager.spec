#
# spec file for package sawfish-pager
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sawfish-pager
Version:        0.90.4
Release:        0
Summary:        Pager for Sawfish window manager
License:        GPL-2.0
%if 0%{?suse_version} > 1230
Group:          System/X11/Utilities
%else
Group:          System/GUI/Other
%endif
Source0:        http://download.tuxfamily.org/sawfishpager/%{name}_%{version}.tar.xz
# PATCH-FIX-UPSTREAM sawfish-pager-makefilefix --toganm@opensuse.org
Patch0:         Makefile-Overrides.patch
Url:            http://sawfish.wikia.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bc
BuildRequires:  gmp-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires:  pkgconfig(librep)
BuildRequires:  pkgconfig(rep-gtk)
BuildRequires:  pkgconfig(sawfish) >= 1.9.1
#BuildRequires:  sawfish-lisp >= 1.9.1

%if 0%{?suse_version} == 1210
BuildRequires:  xz
%endif
Requires:       sawfish >= 1.9.1

%description

Sawfish specific configurable pager map of your desktop with a
viewport support. It can be configured to follow where you are, or
optionally show all workspaces at once.

A pager is a map of your desktop. As maps go, it shows not only the visible
part (your current viewport), but if you are so configured, also the parts
that extend beyond the sides of your screen. Also, if you have more than
one workspace, the pager will follow you to where you are, or optionally
show all workspaces at once. Of course you can select viewports and
windows, and also move or raise/lower the latter.

Check README from this package documentation how to activate.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
#autoreconf -fi
%configure
make %{?_smp_mflags} 

%install
%make_install

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README TODO
%_libdir/sawfish/sawfishpager
%_datadir/sawfish/lisp/sawfish/wm/ext/*

%changelog
