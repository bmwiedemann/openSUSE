#
# spec file for package gtkspell3
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gtkspell3
Version:        3.0.10
Release:        0
Summary:        GTK3 Spell Checker Interface Library
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            http://gtkspell.sf.net/
Source:         https://sourceforge.net/projects/gtkspell/files/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pango) >= 1.3.5
BuildRequires:  pkgconfig(vapigen)

%description
GtkSpell provides MSWord-style and MacOSX-style highlighting of
misspelled words in a GtkTextView widget. Right-clicking a misspelled
word opens a menu of suggested replacements.

%package -n libgtkspell3-3-0
Summary:        GTK3 Spell Checker Interface Library
Group:          System/Libraries
Recommends:     %{name}-lang
# Needed to make lang package installable
Provides:       gtkspell3 = %{version}

%description -n libgtkspell3-3-0
GtkSpell provides MSWord-style and MacOSX-style highlighting of
misspelled words in a GtkTextView widget. Right-clicking a misspelled
word opens a menu of suggested replacements.

%package -n typelib-1_0-GtkSpell-3_0
Summary:        GTK3 Spell Checker Interface Library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GtkSpell-3_0
GtkSpell provides MSWord-style and MacOSX-style highlighting of
misspelled words in a GtkTextView widget. Right-clicking a misspelled
word opens a menu of suggested replacements.

%package devel
Summary:        GTK3 Spell Checker Interface Library -- Development Files
Group:          Development/Libraries/X11
Requires:       libgtkspell3-3-0 = %{version}
Requires:       typelib-1_0-GtkSpell-3_0 = %{version}

%description devel
GtkSpell provides MSWord-style and MacOSX-style highlighting of
misspelled words in a GtkTextView widget. Right-clicking a misspelled
word opens a menu of suggested replacements.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure \
	--disable-static \
	--enable-vala
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%post -n libgtkspell3-3-0 -p /sbin/ldconfig
%postun -n libgtkspell3-3-0 -p /sbin/ldconfig

%files -n libgtkspell3-3-0
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libgtkspell3-3.so.*

%files -n typelib-1_0-GtkSpell-3_0
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib

%files devel
%{_datadir}/gir-1.0/GtkSpell-3.0.gir
%{_includedir}/gtkspell-3.0/
%{_libdir}/libgtkspell3-3.so
%{_libdir}/pkgconfig/gtkspell3-3.0.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtkspell3-3.0.deps
%{_datadir}/vala/vapi/gtkspell3-3.0.vapi
%doc %{_datadir}/gtk-doc/html/gtkspell3/

%files lang -f %{name}.lang

%changelog
