#
# spec file for package libfm
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


Name:           libfm
Version:        1.3.2
Release:        0
Summary:        A glib/gio-based lib used to develop file managers
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.lxde.org/
Source:         https://github.com/lxde/libfm/archive/%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Patch0:         libfm-default-config.patch
# PATCH-FIX-UPSTREAM https://github.com/lxde/libfm/commit/fbcd183335729fa3e8dd6a837c13a23ff3271000
Patch1:         fix-gcc14.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# Optional: HTML developers documentation
BuildRequires:  gtk-doc >= 1.14
BuildRequires:  gtk2-devel >= 2.18.0
BuildRequires:  intltool >= 0.40.0
# Optional: needed to load embbeded thumbnails in jpeg
BuildRequires:  libexif-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
# Optional: needed for custom actions support
BuildRequires:  vala >= 0.13.0
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libmenu-cache) >= 0.3.2
Recommends:     lxshortcut-%{version}
%lang_package

%description
A glib/gio-based library providing some file management utilities and
related-widgets missing in gtk+/glib. This is the core of PCManFM. The
library is desktop independent (not LXDE specific) and has clean API.
It can be used to develop other applications requiring file management
functionality. For example, you can create your own file manager with
facilities provided by libfm.

%package -n libfm4
Summary:        Libfm libraries
# libfm is extensible by modules - which are in the main package
# they are not strictly required, but a very good thing to have present
Group:          System/Libraries
Recommends:     %{name}

%description -n libfm4
libfm main library

%package -n libfm-gtk4
Summary:        GTK libfm libraries
Group:          System/Libraries

%description -n libfm-gtk4
GTK system libraries for libfm

%package -n lxshortcut
Summary:        Create shortcuts for LXDE
Group:          System/GUI/LXDE

%description -n lxshortcut
LXShortcut is a small program used to edit application shortcuts
created with freedesktop.org Desktop Entry spec.

%package devel
Summary:        Devel files for libfm
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libfm4 = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(libfm-extra)

%description devel
A glib/gio-based lib used to develop file managers providing some
file management utilities and related-widgets missing in gtk+/glib.

%package -n libfm-gtk-devel
Summary:        GTK devel files for libfm
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gtk2-devel
Requires:       libfm-gtk4 = %{version}
Requires:       libfm4 = %{version}
Requires:       pkgconfig

%description -n libfm-gtk-devel
GTK libfm libraries for development

%package doc
Summary:        GTK libfm libraries
Group:          Documentation/Other
Requires:       %{name} >= %{version}

%description doc
libfm developers documentation

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
        --enable-gtk-doc \
        --enable-udisks \
        --disable-static
# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# macro for parallel make
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_bindir}/libfm-pref-apps
rm -f %{buildroot}%{_datadir}/applications/libfm-pref-apps.desktop
# using libfm-pref-apps.1.gz fails!
rm -f %{buildroot}%{_mandir}/man1/libfm-pref-apps.1
# we need to remove libfm-extra stuff
rm -rf %{buildroot}%{_includedir}/%{name}
rm -rf %{buildroot}%{_includedir}/%{name}-1.0/fm-extra.h
rm -rf %{buildroot}%{_includedir}/%{name}-1.0/fm-version.h
rm -rf %{buildroot}%{_includedir}/%{name}-1.0/fm-xml-file.h
rm -rf %{buildroot}%{_libdir}/pkgconfig/%{name}-extra.pc
rm -rf %{buildroot}%{_libdir}/%{name}-extra.so*

%find_lang %{name}
%fdupes -s %{buildroot}/%{_datadir}/locale
%suse_update_desktop_file -u -r -G 'Shortcut Editor' lxshortcut Utility DesktopUtility GTK

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   -n libfm4 -p /sbin/ldconfig
%postun -n libfm4 -p /sbin/ldconfig
%post   -n libfm-gtk4 -p /sbin/ldconfig
%postun -n libfm-gtk4 -p /sbin/ldconfig

%files
%dir %{_sysconfdir}/xdg/%{name}
%config %{_sysconfdir}/xdg/%{name}/%{name}.conf
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/gtk-fileprop-x-desktop.so
%{_libdir}/%{name}/modules/gtk-fileprop-x-shortcut.so
%{_libdir}/%{name}/modules/gtk-menu-actions.so
%{_libdir}/%{name}/modules/gtk-menu-trash.so
%{_libdir}/%{name}/modules/vfs-menu.so
%{_libdir}/%{name}/modules/vfs-search.so
%dir %{_datadir}/%{name}/images/
%{_datadir}/%{name}/images/folder.png
%{_datadir}/%{name}/images/unknown.png
%{_datadir}/%{name}/terminals.list
%{_datadir}/mime/packages/%{name}.xml

%files devel
%dir %{_includedir}/%{name}-1.0
%exclude %{_includedir}/%{name}-1.0/fm-gtk*.h
%{_includedir}/%{name}-1.0/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files -n libfm-gtk-devel
%{_includedir}/%{name}-1.0/fm-gtk*.h
%{_libdir}/pkgconfig/%{name}-gtk.pc
%{_libdir}/%{name}-gtk.so

%files doc
%{_datadir}/gtk-doc/html/%{name}

%files lang -f %{name}.lang

%files -n libfm4
%{_libdir}/libfm.so.*

%files -n libfm-gtk4
%{_libdir}/libfm-gtk.so.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/archivers.list
%{_datadir}/%{name}/ui/*.ui

%files -n lxshortcut
%{_bindir}/lxshortcut
%{_datadir}/applications/lxshortcut.desktop
%{_mandir}/man1/lxshortcut.1%{?ext_man}

%changelog
