#
# spec file for package gtkspell
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


Name:           gtkspell
Version:        2.0.16
Release:        0
# FIXME: Replace Obsoletes <= version with Obsoletes < version in libgtkspell0 subpackage on update (after 2.0.16)
Summary:        GTK2 Spell Checker Interface Library
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            http://gtkspell.sf.net/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  intltool
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(enchant) >= 0.4.0
BuildRequires:  pkgconfig(gtk+-2.0)

%description
GtkSpell provides MSWord-style and MacOSX-style highlighting of
misspelled words in a GtkTextView widget. Right-clicking a misspelled
word opens a menu of suggested replacements.

%package -n libgtkspell0
Summary:        GTK2 Spell Checker Interface Library
Group:          System/Libraries
Recommends:     %{name}-lang
# Needed to make lang package installable
Provides:       gtkspell = %{version}
# SLPP applied during development of 12.1. gtkspell last shipped in 11.4
# Change <= to < on update to new version (> 2.0.16)
Obsoletes:      gtkspell <= %{version}

%description -n libgtkspell0
GtkSpell provides MSWord-style and MacOSX-style highlighting of
misspelled words in a GtkTextView widget. Right-clicking a misspelled
word opens a menu of suggested replacements.

%package      devel
Summary:        Static libraries and header files from gtkspell
Group:          Development/Libraries/X11
Requires:       libgtkspell0 = %{version}

%description devel
Static libraries and header files from gtkspell.

%package      doc
Summary:        GTK2 Spell Checker Interface Library
Group:          System/Libraries
Requires:       libgtkspell0 = %{version}

%description doc
GtkSpell provides MSWord-style and MacOSX-style highlighting of
misspelled words in a GtkTextView widget. Right-clicking a misspelled
word opens a menu of suggested replacements.

%lang_package

%prep
%setup -q %{name}-%{version}
translation-update-upstream

%build
%configure\
	--disable-static \
	--enable-gtk-doc=no
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post -n libgtkspell0 -p /sbin/ldconfig
%postun -n libgtkspell0 -p /sbin/ldconfig

%files -n libgtkspell0
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.*

%files lang -f %{name}.lang

%files devel
%{_includedir}/gtkspell-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_datadir}/gtk-doc/html/*

%changelog
