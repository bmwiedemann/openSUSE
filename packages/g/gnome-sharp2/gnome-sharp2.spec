#
# spec file for package gnome-sharp2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name gnome-sharp

Name:           gnome-sharp2
Version:        2.24.2
Release:        0
Summary:        Mono bindings for GNOME
License:        LGPL-2.1
Group:          System/GUI/GNOME
Url:            http://www.mono-project.com/GtkSharp
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{_name}/2.24/%{_name}-%{version}.tar.bz2
Patch0:         fix-sample-mono-path.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(glade-sharp-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-vfs-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
BuildRequires:  pkgconfig(libgnomeui-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-cairo)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains Mono bindings for GNOME.

%package -n gnome-sharp2-complete
Summary:        GTK+ and GNOME bindings for Mono (virtual package)
Group:          System/GUI/GNOME
Requires:       art-sharp2 = %{version}
Requires:       gconf-sharp2 = %{version}
Requires:       gnome-sharp2 = %{version}
Requires:       gnome-vfs-sharp2 = %{version}

%description -n gnome-sharp2-complete
Gtk# is a library that allows you to build fully native graphical GNOME
applications using Mono. Gtk# is a binding to GTK+, the cross platform
user interface toolkit used in GNOME. It includes bindings for Gtk,
Atk, Pango, Gdk, libgnome, libgnomeui and libgnomecanvas.  (Virtual
package which depends on all gtk-sharp2 subpackages)

%package -n gnome-vfs-sharp2
Summary:        Mono bindings for gnomevfs
Group:          System/GUI/GNOME

%description -n gnome-vfs-sharp2
This package contains Mono bindings for gnomevfs.

%package -n art-sharp2
Summary:        Mono bindings for libart
Group:          System/GUI/GNOME

%description -n art-sharp2
This package contains Mono bindings for libart.

%package -n gconf-sharp2
Summary:        Mono bindings for gconf
Group:          System/GUI/GNOME

%description -n gconf-sharp2
This package contains Mono bindings for gconf and gconf peditors.

%package -n gconf-sharp-peditors2
Summary:        Mono bindings for gconf property editors
Group:          System/GUI/GNOME

%description -n gconf-sharp-peditors2
This package contains Mono bindings for gconf property editors.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --libexecdir=%{_prefix}/lib \
    --disable-static \
    --enable-debug
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -type f -name '*.la' -delete -print

%post -n gnome-sharp2 -p /sbin/ldconfig

%postun -n gnome-sharp2 -p /sbin/ldconfig

%files -n gnome-sharp2-complete
%defattr(-, root, root)
%dir %{_prefix}/lib/gtk-sharp-2.0
%dir %{_prefix}/lib/mono/gtk-sharp-2.0

%files -n gnome-sharp2
%defattr(-,root,root)
%{_datadir}/gapi-2.0/gnome-api.xml
%{_libdir}/libgnomesharpglue-2.so
%{_libdir}/pkgconfig/gnome-sharp-2.0.pc
%{_prefix}/lib/mono/gac/*gnome-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*gnome-sharp.dll

%files -n gnome-vfs-sharp2
%defattr(-,root,root)
%{_datadir}/gapi-2.0/gnome-vfs-api.xml
%{_libdir}/pkgconfig/gnome-vfs-sharp-2.0.pc
%{_prefix}/lib/mono/gac/*gnome-vfs-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*gnome-vfs-sharp.dll

%files -n art-sharp2
%defattr(-,root,root)
%{_datadir}/gapi-2.0/art-api.xml
%{_libdir}/pkgconfig/art-sharp-2.0.pc
%{_prefix}/lib/mono/gac/*art-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*art-sharp.dll

%files -n gconf-sharp2
%defattr(-, root, root)
%{_bindir}/gconfsharp2-schemagen
%{_libdir}/pkgconfig/gconf-sharp-2.0.pc
%{_prefix}/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%{_prefix}/lib/mono/gac/*gconf-sharp
%{_prefix}/lib/mono/gtk-sharp-2.0/*gconf-sharp.dll

%files -n gconf-sharp-peditors2
%defattr(-, root, root)
%{_libdir}/pkgconfig/gconf-sharp-peditors-2.0.pc
%{_prefix}/lib/mono/gac/*gconf-sharp-peditors
%{_prefix}/lib/mono/gtk-sharp-2.0/*gconf-sharp-peditors.dll

%changelog
