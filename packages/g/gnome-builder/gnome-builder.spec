#
# spec file for package gnome-builder
#
# Copyright (c) 2024 SUSE LLC
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


# Update this on every major/minor bump
%define basever 47
%define glib_version 2.75

Name:           gnome-builder
Version:        47.2
Release:        0
Summary:        A toolsmith for GNOME-based applications
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Builder
Source0:        %{name}-%{version}.tar.zst
Source99:       %{name}-rpmlintrc

# PATCH-FIX-OPENSUSE Dirty-quick-hackfix-typelibs.patch -- Nuke away bogus typelibs dependencies
Patch0:         Dirty-quick-hackfix-typelibs.patch

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  llvm-clang-devel >= 3.5
BuildRequires:  meson >= 0.60
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-gobject
BuildRequires:  (pkgconfig(webkit2gtk-5.0) or pkgconfig(webkitgtk-6.0))
BuildRequires:  pkgconfig(dspy-1) >= 1.4.0
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(flatpak) >= 1.10.2
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.74
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.8
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= 3.43.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.alpha
BuildRequires:  pkgconfig(libcmark) >= 0.29.0
BuildRequires:  pkgconfig(libdex-1) >= 0.2
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= 1.1.0
BuildRequires:  pkgconfig(libpanel-1) >= 1.5.0
BuildRequires:  pkgconfig(libpeas-2) >= 1.99.0
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:  pkgconfig(sysprof-6)
BuildRequires:  pkgconfig(sysprof-capture-4) >= 45.0
BuildRequires:  pkgconfig(template-glib-1.0) >= 3.36.1
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.70.0
Requires:       autoconf
Requires:       automake
Requires:       libtool
Requires:       python3-gobject-Gdk
Requires:       typelib(Jsonrpc) = 1.0
Recommends:     %{name}-doc
Recommends:     flatpak
Recommends:     flatpak-builder
Suggests:       gjs
Obsoletes:      gnome-builder-plugin-beautifier < 3.27.4
Obsoletes:      gnome-builder-plugin-clang < 43.alpha
Obsoletes:      gnome-builder-plugin-cmake < 43.alpha
Obsoletes:      gnome-builder-plugin-ctags < 43.alpha
Obsoletes:      gnome-builder-plugin-devhelp < 43.alpha
Obsoletes:      gnome-builder-plugin-fpaste < 43.alpha
Obsoletes:      gnome-builder-plugin-gettext < 43.alpha
Obsoletes:      gnome-builder-plugin-gnome-code-assistance < 43.alpha
Obsoletes:      gnome-builder-plugin-html-completion < 43.alpha
Obsoletes:      gnome-builder-plugin-jhbuild < 43.alpha
Obsoletes:      gnome-builder-plugin-mingw < 43.alpha
Obsoletes:      gnome-builder-plugin-symbol-tree < 43.alpha
Obsoletes:      gnome-builder-plugin-sysmon < 43.alpha
Obsoletes:      gnome-builder-plugin-todo < 43.alpha
Obsoletes:      gnome-builder-plugin-vala-pack < 43.alpha
Obsoletes:      gnome-builder-plugin-xml-pack < 43.alpha

%description
Builder is an IDE for GNOME and a tool to help writing GNOME-based
applications.

%package doc
Summary:        Documentation files for the %{name} package
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Builder is an IDE for GNOME and a tool to help writing GNOME-based
applications.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D docs=true \
	-D help=true \
	-D network_tests=false \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}
%find_lang %{name}

# [RPMLINT] REMOVE __pycache__ DIR CONTAINING AN UNNECESSARY
# PYTHON OBJECT FILE W/O CORRESPONDING SOURCE CODE
rm -fr %{buildroot}%{python3_sitearch}/gi/overrides/__pycache__/Ide.cpython-35.opt-1.pyc
# Drop temp files used in doc creation.
# The /usr/share/doc/gnome-builder/en/.doctrees/environment.pickle
# file varied for every build
rm -fr %{buildroot}%{_datadir}/doc/%{name}/*/.doctrees

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Builder.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Builder.desktop

%files
%license COPYING
%doc AUTHORS CONTRIBUTING.md NEWS README.md
%doc %{_datadir}/doc/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libexecdir}/%{name}-clang
%{_libexecdir}/%{name}-flatpak
%{_libexecdir}/%{name}-git
%{_datadir}/metainfo/org.gnome.Builder.appdata.xml
%{_datadir}/applications/org.gnome.Builder.desktop
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.builder*.gschema.xml
%{_datadir}/icons/hicolor/
%{_includedir}/%{name}-%{basever}/
%{_libdir}/pkgconfig/gnome-builder-%{basever}*.pc

%files doc
%doc %{_datadir}/doc/libide/

%files lang -f %{name}.lang

%changelog
