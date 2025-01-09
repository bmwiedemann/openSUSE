#
# spec file for package meld
#
# Copyright (c) 2025 SUSE LLC
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


Name:           meld
Version:        3.22.3
Release:        0
Summary:        Visual diff and merge tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://meldmerge.org/
Source0:        https://download.gnome.org/sources/meld/3.22/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
# Needed for typelib() Requires
BuildRequires:  gobject-introspection-devel
BuildRequires:  itstool
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.0
BuildRequires:  pkgconfig(py3cairo) >= 1.15.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.30
BuildRequires:  pkgconfig(python3) >= 3.6
# needed for VCS diffs
Requires:       patch
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
# the code obscures a lot of logic, instead of requiring GtkSource 4.0, they require
# GtkSource (any version) and then runtime complain if it's not 4.0 :( (boo#1184842)
Requires:       typelib(GtkSource) = 4
# Suggest various vcs that meld can handle
Suggests:       bzr
Suggests:       cvs
# Not in Factory, but still in OBS
Suggests:       darcs
Suggests:       fossil
Suggests:       git
Suggests:       mercurial
Suggests:       monotone
Suggests:       subversion
Suggests:       tla
#
BuildArch:      noarch

%description
Meld is a visual diff and merge tool. Two or three files can be
compared and be edited in place. (The diffs update dynamically). Two
or three directories can be compared and file comparisons be launched.
The working copy directory from version control systems such as CVS,
Subversion, Bazaar-ng and Mercurial can be browsed and viewed.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Meld.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Meld.desktop

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Meld.appdata.xml
%{_datadir}/applications/org.gnome.Meld.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.meld.gschema.xml
%doc %{_datadir}/help/C/meld/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/org.gnome.Meld.xml
%{_mandir}/man1/meld.1%{?ext_man}
%{python3_sitelib}/meld/

%files lang -f %{name}.lang

%changelog
