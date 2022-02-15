#
# spec file for package dasher
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


Name:           dasher
Version:        5.0.0
Release:        0
Summary:        Zooming Predictive Text Entry System
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://dasher.acecentre.net/
Source:         %{name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM dasher-5.0.0-sys-stat.patch
Patch:          dasher-5.0.0-sys-stat.patch
# PATCH-FIX-UPSTREAM gnome-doc-utils-depr.patch
Patch2:         gnome-doc-utils-depr.patch
# PATCH-FIX-UPSTREAM 0001-Remove-extern-C-warpper-around-atspi-glib-headers-in.patch
Patch3:         0001-Remove-extern-C-warpper-around-atspi-glib-headers-in.patch

BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atspi-2) >= 2.11
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.6
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xtst)

Obsoletes:      %{name}-data-recommended < 0.5.0
Provides:       %{name}-data-recommended = %{version}
Obsoletes:      %{name}-data-extras < 0.5.0
Provides:       %{name}-data-extras = %{version}

%description
Dasher is a zooming predictive text entry system, designed for
situations where keyboard input is impractical (for instance:
accessibility or PDAs). It is usable with greatly limited amounts of
physical input while still allowing high rates of text entry.

%lang_package

%prep
%autosetup -p1
echo "5.0.0" > .tarball-version
rm  m4/glib-gettext.m4
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--with-pic \
	%{nil}
%make_build

%install
%make_install
%suse_update_desktop_file -G "Text Entry Tool" %{name} GNOME
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%files
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/help/C/%{name}
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/*%{ext_man}

%files lang -f %{name}.lang

%changelog
