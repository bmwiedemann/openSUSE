#
# spec file for package python-gtksourceview
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name pygtksourceview
Name:           python-gtksourceview
Version:        2.10.1
Release:        0
Summary:        Python bindings for the GTK+ source editing widget
License:        LGPL-2.0-only
Group:          Development/Languages/Python
Url:            http://gtksourceview.sourceforge.net/
Source:         ftp://ftp.gnome.org/pub/GNOME/sources/%{_name}/2.2/%{_name}-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-gobject2-devel >= 2.8.0
BuildRequires:  python-gtk-devel >= 2.8.0
BuildRequires:  pkgconfig(gtksourceview-2.0)
Requires:       python-gtk >= 2.8.0

%description
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

This package contains Python bindings for the library.

%package devel
Summary:        Development files for the GTK+ source editing widget Python bindings
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       pkgconfig(gtksourceview-2.0)

%description devel
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

This package contains Python bindings for the library.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure \
    --disable-docs
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} "(" -name "*.la" -or -name "*.a" ")" -print -delete

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{py_sitedir}/gtksourceview2.so
%{_datadir}/pygtk/2.0/defs/gtksourceview2.defs

%files devel
%{_libdir}/pkgconfig/*.pc

%changelog
