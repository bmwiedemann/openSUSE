#
# spec file for package genius
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           genius
Version:        1.0.24
Release:        0
Summary:        General purpose calculator and mathematics tool
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.jirka.org/genius.html
Source:         http://download.gnome.org/sources/genius/1.0/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  intltool
BuildRequires:  mpfr-devel >= 2.3.0
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20.0
BuildRequires:  pkgconfig(gtksourceview-2.0) >= 0.3.0
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang

%description
Genius is a general purpose calculator program similar in some aspects
to BC, Matlab, Maple or Mathematica. It is useful both as a simple
calculator and as a research or educational tool. The syntax
mimics how mathematics is usually written.

GEL (Genius Extenseion Language) is the name of its extension language.
Many of the standard genius functions are written in GEL itself.

%package -n gnome-genius
Summary:        GNOME interface for Genius, a general purpose calculator
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}

%description -n gnome-genius
Genius is a general purpose calculator program similar in some aspects
to BC, Matlab, Maple or Mathematica. It is useful both as a simple
calculator and as a research or educational tool. The syntax mimics
how mathematics is usually written.

%package devel
Summary:        Development files for Genius, a general purpose calculator
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}

%description devel
Genius is a general purpose calculator program similar in some aspects
to BC, Matlab, Maple or Mathematica. It is useful both as a simple
calculator and as a research or educational tool. The syntax
mimics how mathematics is usually written.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fstack-protector"
%configure \
        --libexec=%{_libexecdir}/genius \
        --disable-update-mimedb
%make_build

%install
%make_install
# We don't want the test plugin:
rm %{buildroot}%{_libdir}/genius/libtestplugin.*
rm %{buildroot}%{_datadir}/genius/plugins/test.plugin
# Not needed anymore on modern desktops:
rm %{buildroot}%{_datadir}/application-registry/genius.applications
rm %{buildroot}%{_datadir}/mime-info/genius.*
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/genius

%files
%license COPYING
%doc NEWS README
%{_datadir}/genius
%{_bindir}/genius

%files -n gnome-genius
%{_bindir}/gnome-genius
%{_libexecdir}/genius
%{_datadir}/applications/gnome-genius.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/mime/packages/genius.xml

%files devel
%doc AUTHORS ChangeLog TODO
%{_includedir}/genius

%files lang -f %{name}.lang

%changelog
