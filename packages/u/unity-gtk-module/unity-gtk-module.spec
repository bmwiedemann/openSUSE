#
# spec file for package unity-gtk-module
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


%define _name_gtk2 unity-gtk2-module
%define _name_gtk3 unity-gtk3-module
%define lname_gtk2 libunity-gtk2-parser0
%define lname_gtk3 libunity-gtk3-parser0
%define _version 0.0.0+18.04.20171202
Name:           unity-gtk-module
Version:        0.0.0+bzr20171202
Release:        0
Summary:        GTK+ module for exporting old-style menus as GMenuModels
License:        LGPL-3.0-or-later
Group:          System/GUI/Other
Url:            https://launchpad.net/unity-gtk-module
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE unity-gtk-module-gsettings.patch ria.freelander@gmail.com -- Use a GSettings key instead of patched Gtk2.
Patch0:         unity-gtk-module-gsettings.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)

%description
Many applications implement menus as GtkMenuShells and GtkMenuItems
and aren't looking to migrate to the newer GMenuModel API.
This GTK+ module watches for these types of menus and exports the
appropriate GMenuModel implementation.

%package -n %{_name_gtk2}
Summary:        GTK+2 module for exporting old-style menus as GMenuModels
Group:          System/GUI/Other
Requires:       %{lname_gtk2} = %{version}
Requires:       %{name}-common = %{version}

%description -n %{_name_gtk2}
Many applications implement menus as GtkMenuShells and GtkMenuItems
and aren't looking to migrate to the newer GMenuModel API.
This GTK+2 module watches for these types of menus and exports the
appropriate GMenuModel implementation.

%package -n %{_name_gtk3}
Summary:        GTK+3 module for exporting old-style menus as GMenuModels
Group:          System/GUI/Other
Requires:       %{lname_gtk3} = %{version}
Requires:       %{name}-common = %{version}

%description -n %{_name_gtk3}
Many applications implement menus as GtkMenuShells and GtkMenuItems
and aren't looking to migrate to the newer GMenuModel API.
This GTK+3 module watches for these types of menus and exports the
appropriate GMenuModel implementation.

%package common
Summary:        GTK+ module for exporting old-style menus as GMenuModels -- Common Files
Group:          System/GUI/Other
Recommends:     %{_name_gtk2} = %{version}
Recommends:     %{_name_gtk3} = %{version}
Suggests:       appmenu-qt
Suggests:       appmenu-qt5

%description common
Many applications implement menus as GtkMenuShells and GtkMenuItems
and aren't looking to migrate to the newer GMenuModel API.
This GTK+ module watches for these types of menus and exports the
appropriate GMenuModel implementation.

This package contains common data that is used by unity-gtk-module
packages.

%package -n %{lname_gtk2}
Summary:        GtkMenuShell to GMenuModel parser
Group:          System/Libraries

%description -n %{lname_gtk2}
This library converts GtkMenuShells into GMenuModels.

%package -n %{lname_gtk3}
Summary:        GtkMenuShell to GMenuModel parser
Group:          System/Libraries

%description -n %{lname_gtk3}
This library converts GtkMenuShells into GMenuModels.

%package -n libunity-gtk-parser-devel
Summary:        Development files of libunity-gtk-parser
Group:          Development/Libraries/C and C++
Requires:       %{lname_gtk2} = %{version}
Requires:       %{lname_gtk3} = %{version}
Requires:       pkgconfig(gtk+-2.0)
Requires:       pkgconfig(gtk+-3.0)

%description -n libunity-gtk-parser-devel
The libunity-gtk-parser development package includes the header
files, libraries, development tools necessary for compiling and
linking application which will use libunity-gtk-parser.

%prep
%setup -q -c
%patch0

cat > %{name}.sh << EOF
if [ -f "%{_libdir}/gtk-2.0/modules/lib%{name}.so" ]; then
    export GTK2_MODULES="\$%{nil}{GTK2_MODULES:+\$%{nil}GTK2_MODULES:}unity-gtk-module"
fi
if [ -f "%{_libdir}/gtk-3.0/modules/lib%{name}.so" ]; then
    export GTK3_MODULES="\$%{nil}{GTK3_MODULES:+\$%{nil}GTK3_MODULES:}unity-gtk-module"
fi
if [ -z "\$%{nil}UBUNTU_MENUPROXY" ]; then
    export UBUNTU_MENUPROXY=1
fi
EOF
cat > %{name}.csh << EOF
if ( -f "%{_libdir}/gtk-2.0/modules/lib%{name}.so" ) then
    if ( ! \$%{nil}?GTK2_MODULES ) set GTK2_MODULES=""
    if ( \$%{nil}?GTK2_MODULES ) setenv GTK2_MODULES "\$%{nil}GTK2_MODULES\:"
    setenv GTK2_MODULES "\$%{nil}{GTK2_MODULES}unity-gtk-module"
endif
if ( -f "%{_libdir}/gtk-3.0/modules/lib%{name}.so" ) then
    if ( ! \$%{nil}?GTK3_MODULES ) set GTK3_MODULES=""
    if ( \$%{nil}?GTK3_MODULES ) setenv GTK3_MODULES "\$%{nil}GTK3_MODULES\:"
    setenv GTK3_MODULES "\$%{nil}{GTK3_MODULES}unity-gtk-module"
endif
if ( ! \$%{nil}?UBUNTU_MENUPROXY ) then
    setenv UBUNTU_MENUPROXY 1
endif
EOF

%build
NOCONFIGURE=1 ./autogen.sh
%global _configure ../configure
export PYTHON=python2
for ver in 2 3; do
    mkdir build-gtk$ver
    pushd build-gtk$ver
    %configure \
      --disable-static \
      --enable-gtk-doc \
      --with-gtk=$ver
    make %{?_smp_mflags} V=1
    popd
done

%install
for ver in 2 3; do
    pushd build-gtk$ver
    %make_install
    popd
done
install -Dpm 0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -Dpm 0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
rm -rf %{buildroot}%{python_sitelib}/unity_gtk_module/ \
  %{buildroot}%{_datadir}/upstart/
%if 0%{?suse_version} < 1500 && 0%{?sle_version} < 120200
rm %{buildroot}%{_libexecdir}/systemd/user/unity-gtk-module.service
%endif
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname_gtk2} -p /sbin/ldconfig

%postun -n %{lname_gtk2} -p /sbin/ldconfig

%post -n %{lname_gtk3} -p /sbin/ldconfig

%postun -n %{lname_gtk3} -p /sbin/ldconfig

%post common
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120200
%systemd_user_post %{name}.service
%endif
%if 0%{?suse_version} < 1500
%glib2_gsettings_schema_post
%endif

%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120200
%preun common
%systemd_user_preun %{name}.service
%endif

%postun common
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120200
%systemd_user_postun %{name}.service
%endif
%if 0%{?suse_version} < 1500
%glib2_gsettings_schema_postun
%endif

%files -n %{_name_gtk2}
%{_libdir}/gtk-2.0/modules/lib%{name}.so

%files -n %{_name_gtk3}
%{_libdir}/gtk-3.0/modules/lib%{name}.so

%files common
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS TODO
%config %{_sysconfdir}/profile.d/%{name}.*
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
%{_userunitdir}/%{name}.service
%endif

%files -n %{lname_gtk2}
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS TODO
%{_libdir}/libunity-gtk2-parser.so.*

%files -n %{lname_gtk3}
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS TODO
%{_libdir}/libunity-gtk3-parser.so.*

%files -n libunity-gtk-parser-devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/unity-gtk-parser/
%{_libdir}/libunity-gtk?-parser.so
%{_libdir}/pkgconfig/unity-gtk?-parser.pc

%changelog
