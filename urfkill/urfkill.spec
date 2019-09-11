#
# spec file for package urfkill
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           urfkill
Version:        0.5.0
Release:        0
Url:            http://github.com/lcp/urfkill
Summary:        A daemon to control radio killswitches
License:        GPL-2.0+
Group:          System/Daemons
Source:         https://github.com/lcp/urfkill/archive/%{name}-%{version}.tar.gz
Patch0:         urfkill-change-default-user.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.30.1
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libexpat-devel
BuildRequires:  libgudev-1_0-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  polkit-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
Requires:       polkit

%description
Urfkill is a daemon to control radio killswitches through /dev/rfkill
and supports PolicyKit authorization mechanism.

%package -n liburfkill-glib0
Summary:        The glib binding library for urfkill
Group:          System/Daemons

%description -n liburfkill-glib0
Urfkill add-on library to integrate the standard urfkill library with
the GLib thread abstraction and main loop.

%if !0%{?_crossbuild}

%package -n typelib-1_0-Urfkill-0_0
Summary:        The urfkill glib library-- Introspection bindings
Group:          System/Daemons

%description -n typelib-1_0-Urfkill-0_0
Urfkill add-on library to integrate the standard urfkill library with
the GLib thread abstraction and main loop.

This package provides the GObject Introspection bindings for urfkill.

%endif

%package -n liburfkill-glib-devel
Summary:        The glib binding library for urfkill
Group:          Development/Libraries/Other
Requires:       glib2-devel
Requires:       liburfkill-glib0 = %{version}-%{release}
Requires:       typelib-1_0-Urfkill-0_0 = %{version}-%{release}
Provides:       %{name}-devel = %{version}

%description -n liburfkill-glib-devel
Urfkill add-on library to integrate the standard urfkill library with
the GLib thread abstraction and main loop.
http://freedesktop.org/wiki/Software/urfkill

%prep
%setup -n %{name}-%{name}-%{version} -q
%patch0 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure\
  --disable-static \
  --libexecdir=%{_libexecdir}/urfkill \
%if 0%{?_crossbuild}
  --disable-introspection \
%endif
  --with-session-tracking=systemd \
  --enable-gtk-doc
make %{?jobs:-j%jobs}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la

%pre
getent group urfkill >/dev/null || groupadd -r urfkill
getent passwd urfkill >/dev/null || useradd -r -g urfkill -d /var/lib/urfkill -s /bin/false -c "killswitch control daemon" urfkill

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n liburfkill-glib0 -p /sbin/ldconfig

%postun -n liburfkill-glib0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%dir %{_libexecdir}/urfkill
%{_libexecdir}/urfkill/urfkilld
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/polkit-1/actions/org.freedesktop.*.policy
%doc %{_mandir}/man?/*.*
%config %{_sysconfdir}/dbus-1/system.d/*.conf
%config %{_sysconfdir}/urfkill

%files -n liburfkill-glib0
%defattr(-,root,root)
%{_libdir}/liburfkill-glib.so.*

%if !0%{?_crossbuild}

%files -n typelib-1_0-Urfkill-0_0
%defattr(-, root, root)
%{_libdir}/girepository-1.0/*.typelib
%endif

%files -n liburfkill-glib-devel
%defattr(-,root,root)
%if !0%{?_crossbuild}
%{_datadir}/gir-1.0/Urfkill-*.gir
%endif
%doc %{_datadir}/gtk-doc/html/urfkill
%{_includedir}/liburfkill-glib
%{_libdir}/liburfkill-glib.so
%{_libdir}/pkgconfig/urfkill-glib.pc

%changelog
