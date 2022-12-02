#
# spec file for package gnome-builder
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


# FIXME # Figure out where this comes from and fix it.
%global __requires_exclude typelib\\(Ide\\)
%global __requires_exclude_from %{_libdir}/gnome-builder/plugins

# Update this on every major/minor bump
%define basever 43

Name:           gnome-builder
### FIXME ### Enable docs build again on next versionbump (see meson options)
Version:        43.3
Release:        0
Summary:        A toolsmith for GNOME-based applications
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Builder
Source0:        https://download.gnome.org/sources/gnome-builder/43/%{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc

# PATCH-FIX-OPENSUSE Dirty-quick-hackfix-typelibs.patch -- Nuke away bogus typelibs dependencies
Patch0:         Dirty-quick-hackfix-typelibs.patch

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  llvm-clang-devel >= 3.5
BuildRequires:  meson >= 0.59.1
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-gi-docgen
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(dspy-1)
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(flatpak) >= 0.8.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.61.2
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.71
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.48.0
BuildRequires:  pkgconfig(gtk4) >= 4.7
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.5
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= 3.41.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.37.0
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= 0.25.0
BuildRequires:  pkgconfig(libpanel-1) >= 1.0.alpha1
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.32.0
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.21.0
BuildRequires:  pkgconfig(sysprof-4) >= 3.42.0
BuildRequires:  pkgconfig(sysprof-capture-4) >= 3.42.0
BuildRequires:  pkgconfig(sysprof-ui-5) >= 3.42.0
BuildRequires:  pkgconfig(template-glib-1.0) >= 3.35.0
BuildRequires:  pkgconfig(vapigen) >= 0.30.0.55
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.69.0
BuildRequires:  pkgconfig(webkit2gtk-5.0)
Requires:       autoconf
Requires:       automake
Requires:       libtool
Requires:       python3-gobject-Gdk
Requires:       typelib(Jsonrpc) = 1.0
Recommends:     %{name}-doc
Recommends:     flatpak
Recommends:     flatpak-builder
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
# We need to obsolete the doc sub-package
Obsoletes:      gnome-builder-doc <= %{version}

%description
Builder is an IDE for GNOME and a tool to help writing GNOME-based
applications.




# doc sub-package not built (no files section) for version 43 -- https://gitlab.gnome.org/GNOME/gnome-builder/-/issues/1793

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
### FIXME ### Enable on next versionbump
#	-D docs=true \
%meson \
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
%{_libdir}/pkgconfig/gnome-builder-%{version}.pc
%dir %{python3_sitelib}/gi
%dir %{python3_sitelib}/gi/overrides
%{python3_sitelib}/gi/overrides/*

#%%files doc
#%%doc %%{_datadir}/doc/libide/

%files lang -f %{name}.lang

%changelog
