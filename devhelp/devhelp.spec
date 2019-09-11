#
# spec file for package devhelp
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


%define emacs_plugin_dir %{_datadir}/emacs/site-lisp
%define vim_plugin_dir %{_datadir}/vim/site/plugin

Name:           devhelp
Version:        3.32.0
Release:        0
Summary:        Developer's Help Program for GNOME
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Devhelp
Source0:        https://download.gnome.org/sources/devhelp/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 1.30.0
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(amtk-5) >= 5.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.56
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.20

Recommends:     %{name}-lang
Suggests:       emacs-plugin-devhelp
Suggests:       gedit-plugin-devhelp
Suggests:       vim-plugin-devhelp

%description
Devhelp is an API documentation browser for GTK+ and GNOME.

%package -n typelib-1_0-Devhelp-3_0
Summary:        Introspection bindings for the GNOME Developer Help program
Group:          System/Libraries

%description -n typelib-1_0-Devhelp-3_0
Devhelp is an API documentation browser for GTK+ and GNOME.

This package contains the gobject introspection based typelib library.

%package devel
Summary:        Development files for the GNOME Developer Help program
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       typelib-1_0-Devhelp-3_0 = %{version}

%description devel
Devhelp is an API documentation browser for GTK+ and GNOME.

This package contains the development files for Devhelp.

%package -n emacs-plugin-devhelp
Summary:        Devhelp plugin for Emacs
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       emacs

%description -n emacs-plugin-devhelp
Devhelp is an API documentation browser for GTK+ and GNOME.

This package contains the Devhelp plugin for Emacs.

%package -n gedit-plugin-devhelp
Summary:        Devhelp plugin for Gedit
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       gedit

%description -n gedit-plugin-devhelp
Devhelp is an API documentation browser for GTK+ and GNOME.

This package contains the Devhelp plugin for gedit.

%package -n vim-plugin-devhelp
Summary:        Devhelp plugin for Vim
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       vim

%description -n vim-plugin-devhelp
Devhelp is an API documentation browser for GTK+ and GNOME.

This package contains the Devhelp plugin for Vim.

%lang_package

%prep
%autosetup
translation-update-upstream po %{name}

%build
%meson \
	-Dflatpak_build=false \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -G "Developer Help" org.gnome.Devhelp Documentation
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

# glibmm2 needs this
mkdir -p %{buildroot}%{_datadir}/devhelp/books

# Install emacs plugin
mkdir -p %{buildroot}%{emacs_plugin_dir}
cp -a plugins/devhelp.el %{buildroot}%{emacs_plugin_dir}

# Install vim plugin
mkdir -p %{buildroot}%{vim_plugin_dir}
cp -a plugins/devhelp.vim %{buildroot}%{vim_plugin_dir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS HACKING NEWS README
%{_bindir}/devhelp
%dir %{_datadir}/metainfo
%{_datadir}/applications/org.gnome.Devhelp.desktop
%{_datadir}/dbus-1/services/org.gnome.Devhelp.service
%{_datadir}/devhelp
%{_datadir}/glib-2.0/schemas/org.gnome.devhelp.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.libdevhelp-3.gschema.xml
%doc %{_datadir}/help/C/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.gnome.Devhelp.appdata.xml
%{_libdir}/*.so.*
%{_mandir}/man1/devhelp.1%{?ext_man}

%files -n typelib-1_0-Devhelp-3_0
%{_libdir}/girepository-1.0/Devhelp-3.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}-3
%{_datadir}/gir-1.0/Devhelp-3.0.gir
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n emacs-plugin-devhelp
#Own these directories to not depend on additional requirements
%dir %{_datadir}/emacs
%dir %{emacs_plugin_dir}
%{emacs_plugin_dir}/devhelp.el

%files -n gedit-plugin-devhelp
#Own these directories to not depend on additional requirements
%dir %{_libdir}/gedit
%dir %{_libdir}/gedit/plugins
%{_libdir}/gedit/plugins/*

%files -n vim-plugin-devhelp
#Own these directories to not depend on additional requirements
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{vim_plugin_dir}
%{vim_plugin_dir}/devhelp.vim

%files lang -f %{name}.lang

%changelog
