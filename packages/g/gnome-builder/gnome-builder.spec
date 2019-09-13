#
# spec file for package gnome-builder
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


# FIXME # Figure out where this comes from and fix it.
%global __requires_exclude typelib\\(Ide\\)

Name:           gnome-builder
Version:        3.32.4
Release:        0
Summary:        A toolsmith for GNOME-based applications
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND CC-BY-SA-3.0
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Builder
Source0:        https://download.gnome.org/sources/gnome-builder/3.32/%{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  libvala-devel
BuildRequires:  llvm-clang-devel >= 3.5
BuildRequires:  meson >= 0.47.1
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(flatpak) >= 0.8.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.49.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.48.0
BuildRequires:  pkgconfig(gspell-1) >= 1.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= 3.30.1
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.30.2
BuildRequires:  pkgconfig(libdevhelp-3.0) >= 3.25.1
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= 0.25.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.22.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.52.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:  pkgconfig(pangoft2) >= 1.38.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.21.0
BuildRequires:  pkgconfig(sysprof-2) >= 3.30.2
BuildRequires:  pkgconfig(sysprof-ui-2) >= 3.30.2
BuildRequires:  pkgconfig(template-glib-1.0) >= 3.28.0
BuildRequires:  pkgconfig(vapigen) >= 0.30.0.55
BuildRequires:  pkgconfig(vte-2.91) >= 0.40.2
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.12.0
Requires:       autoconf
Requires:       automake
Requires:       libtool
Requires:       python3-gobject-Gdk
Requires:       typelib(Jsonrpc) = 1.0
Recommends:     %{name}-doc
Recommends:     flatpak
Recommends:     flatpak-builder
Recommends:     gnome-builder-plugin-jedi = %{version}
Recommends:     gnome-builder-plugin-jhbuild = %{version}
Recommends:     gnome-builder-plugin-vala-pack = %{version}
Obsoletes:      gnome-builder-plugin-beautifier < 3.27.4
Obsoletes:      gnome-builder-plugin-clang < %{version}
Obsoletes:      gnome-builder-plugin-cmake < %{version}
Obsoletes:      gnome-builder-plugin-ctags < %{version}
Obsoletes:      gnome-builder-plugin-devhelp < %{version}
Obsoletes:      gnome-builder-plugin-fpaste < %{version}
Obsoletes:      gnome-builder-plugin-gettext < %{version}
Obsoletes:      gnome-builder-plugin-gnome-code-assistance < %{version}
Obsoletes:      gnome-builder-plugin-html-completion < %{version}
Obsoletes:      gnome-builder-plugin-mingw < %{version}
Obsoletes:      gnome-builder-plugin-symbol-tree < %{version}
Obsoletes:      gnome-builder-plugin-sysmon < %{version}
Obsoletes:      gnome-builder-plugin-todo < %{version}
Obsoletes:      gnome-builder-plugin-xml-pack < %{version}

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

%package plugin-jedi
Summary:        Jedi plugin for python3 code completion in %{name}
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       python3-jedi
Requires:       python3-lxml
Supplements:    packageand(%{name}:python3-jedi)

%description plugin-jedi
This package provides the jedi plugin for code completion assistance in Python3 inside %{name}'s editor.

%package plugin-jhbuild
Summary:        Jhbuild plugin for %{name}
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
# Disabled, as many users prefer to run jhbuild from a git checkout, no need to install our distro jhbuild.
#Requires:       jhbuild
Supplements:    packageand(%{name}:jhbuild)

%description plugin-jhbuild
This package provides the jhbuild plugin for %{name}.

%package plugin-vala-pack
Summary:        Vala-pack plugin for %{name}
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       vala
Supplements:    packageand(%{name}:vala)

%description plugin-vala-pack
This package provides the vala-pack plugin for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Ddocs=true \
	-Dhelp=true \
	-Dnetwork_tests=false \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}
%find_lang %{name}

# [RPMLINT] REMOVE __pycache__ DIR CONTAINING AN UNNECESSARY PYTHON OBJECT FILE W/O CORRESPONDING SOURCE CODE
rm -fr %{buildroot}%{python3_sitearch}/gi/overrides/__pycache__/Ide.cpython-35.opt-1.pyc
# Drop temp files used in doc creation.
# The /usr/share/doc/gnome-builder/en/.doctrees/environment.pickle
# file varied for every build
rm -fr %{buildroot}%{_datadir}/doc/%{name}/*/.doctrees

%check
#%%meson_test

%files
%license COPYING
%doc AUTHORS CONTRIBUTING.md NEWS README.md
%doc %{_datadir}/doc/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libexecdir}/%{name}-clang
# EXCLUDE THE OPTIONAL PLUGINS FROM THE MAIN PACKAGE
%exclude %{_libdir}/%{name}/plugins/jedi.plugin
%exclude %{_libdir}/%{name}/plugins/jedi_plugin.py
%exclude %{_libdir}/%{name}/plugins/jhbuild.plugin
%exclude %{_libdir}/%{name}/plugins/jhbuild_plugin.py
%exclude %{_libdir}/%{name}/plugins/vala-pack.plugin
%{_datadir}/metainfo/org.gnome.Builder.appdata.xml
%{_datadir}/applications/org.gnome.Builder.desktop
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.gnome-code-assistance.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.editor.language.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.extension-type.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.code-insight.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.color_picker_plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugins.eslint.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project-tree.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.workbench.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.build.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.plugin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.project.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.builder.clang.gschema.xml
%dir %{_datadir}/gtksourceview-3.0
%dir %{_datadir}/gtksourceview-3.0/styles
%{_datadir}/gtksourceview-3.0/styles/builder-dark.style-scheme.xml
%{_datadir}/gtksourceview-3.0/styles/builder.style-scheme.xml
%{_datadir}/gtksourceview-4/styles/builder-dark.style-scheme.xml
%{_datadir}/gtksourceview-4/styles/builder.style-scheme.xml
%{_datadir}/icons/hicolor/
%{_includedir}/%{name}/
%{_includedir}/%{name}-3.32/
%{python3_sitearch}/gi/overrides/*

%files doc
%doc %{_datadir}/gtk-doc/html/libide

%files plugin-jedi
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/jedi.plugin
%{_libdir}/%{name}/plugins/jedi_plugin.py

%files plugin-jhbuild
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/jhbuild.plugin
%{_libdir}/%{name}/plugins/jhbuild_plugin.py

%files plugin-vala-pack
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/vala-pack.plugin

%files lang -f %{name}.lang

%changelog
