#
# spec file for package devhelp
#
# Copyright (c) 2023 SUSE LLC
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
%define vim_plugin_dir %{_datadir}/vim/vimfiles/plugin/

Name:           devhelp
Version:        43.0
Release:        0
Summary:        Developer's Help Program for GNOME
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Devhelp
Source0:        https://download.gnome.org/sources/devhelp/43/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 1.30.0
BuildRequires:  itstool
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.64
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(webkit2gtk-4.1)

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
%autosetup -p1

%build
%meson \
	-Dflatpak_build=false \
	-Dgtk_doc=true \
	-Dplugin_gedit=true \
	-Dplugin_vim=true \
	-Dplugin_emacs=true \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -G "Developer Help" org.gnome.Devhelp* Documentation
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

# glibmm2 needs this
mkdir -p %{buildroot}%{_datadir}/devhelp/books

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES
%doc NEWS
%{_bindir}/devhelp
%{_datadir}/applications/org.gnome.Devhelp*.desktop
%{_datadir}/dbus-1/services/org.gnome.Devhelp*.service
%{_datadir}/devhelp
%{_datadir}/glib-2.0/schemas/org.gnome.devhelp.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.libdevhelp-3.gschema.xml
%doc %{_datadir}/help/C/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.gnome.Devhelp*.appdata.xml
%{_libdir}/*.so.*
%{_mandir}/man1/devhelp.1%{?ext_man}

%files -n typelib-1_0-Devhelp-3_0
%{_libdir}/girepository-1.0/Devhelp-3.0.typelib

%files devel
%doc %{_datadir}/doc/devhelp-3/
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
%dir %{_datadir}/vim/vimfiles
%dir %{vim_plugin_dir}
%{vim_plugin_dir}/devhelp.vim

%files lang -f %{name}.lang

%changelog
