#
# spec file for package gtkhotkey
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gtkhotkey
Version:        0.2.1
Release:        0
Summary:        Platform Independent Hotkey Handling for GTK+ Applications
License:        LGPL-3.0+
Group:          Development/Libraries/X11
Url:            http://launchpad.net/gtkhotkey/
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM gtkhotkey-glib-2.31.patch lp#898334 dimstar@opensuse.org -- Fix build with glib 2.31
Patch0:         gtkhotkey-glib-2.31.patch
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GtkHotkey is simple library offering a platform independent way for GTK+
applications to manage and bind desktop-wide hotkeys.

%package -n libgtkhotkey1
Summary:        Platform Independent Hotkey Handling for GTK+ Applications
Group:          Development/Libraries/X11

%description -n libgtkhotkey1
GtkHotkey is simple library offering a platform independent way for GTK+
applications to manage and bind desktop-wide hotkeys.

%package -n libgtkhotkey-devel
Summary:        Platform Independent Hotkey Handling for GTK+ Applications -- Development Files
Group:          Development/Libraries/X11
Requires:       glib2-devel
Requires:       gtk2-devel
Requires:       libgtkhotkey1 = %{version}

%description -n libgtkhotkey-devel
GtkHotkey is simple library offering a platform independent way for GTK+
applications to manage and bind desktop-wide hotkeys.  This package contains
all necessary include files and libraries needed to develop applications that
require these.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall
%__rm -rf %{buildroot}%{_prefix}/doc
%__rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -n libgtkhotkey1 -p /sbin/ldconfig

%postun -n libgtkhotkey1 -p /sbin/ldconfig

%files -n libgtkhotkey1
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libgtkhotkey.so.1*

%files -n libgtkhotkey-devel
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/gtkhotkey
%{_includedir}/gtkhotkey-1.0/
%{_libdir}/libgtkhotkey.so
%{_libdir}/pkgconfig/*.pc

%changelog
