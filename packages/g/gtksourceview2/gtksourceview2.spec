#
# spec file for package gtksourceview2
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


%define _name   gtksourceview
Name:           gtksourceview2
Version:        2.10.5
Release:        0
Summary:        GTK+ Source Editing Widget
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org/
Source:         ftp://ftp.gnome.org/pub/GNOME/sources/gtksourceview/2.10/%{_name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE gtksourceview-2.10.5-rpmspec_highlight.patch bgo#676261 lazy.kent@opensuse.org -- add SUSE-specific highlights for rpm spec
Patch0:         gtksourceview-2.10.5-rpmspec_highlight.patch
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  translation-update-upstream

%description
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package -n libgtksourceview-2_0-0
Summary:        GTK+ Source Editing Widget
Group:          System/GUI/GNOME
Recommends:     %{name}-lang = %{version}
# This is needed to make lang package installable.
Provides:       %{name} = %{version}

%description -n libgtksourceview-2_0-0
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package devel
Summary:        GTK+ Source Editing Widget
Group:          System/GUI/GNOME
Requires:       gtk2-devel
Requires:       libgtksourceview-2_0-0 = %{version}
Requires:       libxml2-devel
Obsoletes:      gtksourceview-doc <= 2.5.4
Provides:       gtksourceview-doc = 2.5.4
Obsoletes:      glade3-catalog-gtksourceview

%description devel
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
%patch0
translation-update-upstream

%build
%configure \
        --disable-gtk-doc \
	--with-pic \
	--disable-static
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{_name}-2.0
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -n libgtksourceview-2_0-0 -p /sbin/ldconfig
%postun -n libgtksourceview-2_0-0 -p /sbin/ldconfig

%files -n libgtksourceview-2_0-0
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_libdir}/libgtksourceview-2.0.so.*
%{_datadir}/gtksourceview-2.0/

%files devel
%{_includedir}/gtksourceview-2.0/
%{_libdir}/libgtksourceview-2.0.so
%{_libdir}/pkgconfig/gtksourceview-2.0.pc
%{_datadir}/gtk-doc/html/gtksourceview-2.0/

%files lang -f %{_name}-2.0.lang

%changelog
