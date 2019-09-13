#
# spec file for package florence
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


Name:           florence
Version:        0.6.3
Release:        0
Summary:        Extensible scalable on-screen virtual keyboard
License:        GPL-2.0-or-later AND GFDL-1.2-only
Group:          System/X11/Utilities
URL:            http://florence.sourceforge.net
Source0:        http://downloads.sourceforge.net/florence/%{name}-%{version}.tar.bz2
Source99:       florence-rpmlintrc
# PATCH-FIX-OPENSUSE florence-icondir.patch bnc#855529 dap.darkness@gmail.com -- Set correct svg icon directory to not breake the application
Patch0:         florence-icondir.patch
# PATCH-FIX-UPSTREAM florence-implicit-definitions.patch sf#florence#14 dimstar@opensuse.org -- Fix implicit definition of function wait()
Patch1:         florence-implicit-definitions.patch
# PATCH-FIX-UPSTREAM florence-buildfix.patch dimstar@opensuse.org -- Fix build system: link libflorence-1.0.la
Patch2:         florence-buildfix.patch
# PATCH-FIX-UPSTREAM florence-build-without-scrollkeeper.patch -- Fix build without scrollkeeper
Patch3:         florence-build-without-scrollkeeper.patch

BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
Requires(post): desktop-file-utils
Requires(post): glib2-tools
Requires(postun): desktop-file-utils
Requires(postun): glib2-tools
Recommends:     %{name}-lang

%description
Florence is an extensible scalable virtual keyboard for X11.
You need it if you can't use a real hardware keyboard, for
example because you are disabled, your keyboard is broken or
because you use a tablet PC, but you must be able to use a pointing
device (as a mouse, a trackball or a touchscreen).

Florence stays out of your way when you don't need it:
it appears on the screen only when you need it.
A Timer-based auto-click functionality is available
to help disabled people having difficulties to click.

%package -n libflorence-1_0-1
Summary:        Library files for %{name}
Group:          System/X11/Utilities

%description -n libflorence-1_0-1
Extensible scalable on-screen virtual keyboard.
This package contains libraries.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use florence.

%lang_package

%prep
%setup -q
sed -i 's|Icon=@ICONDIR@/%{name}.svg|Icon=%{name}|g' data/%{name}.desktop.in.in
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fiv
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name *.la -delete
%suse_update_desktop_file -r %{name} Utility Accessibility
%find_lang %{name} %{?no_lang_C}

%post
%glib2_gsettings_schema_post
%desktop_database_post

%post -n libflorence-1_0-1 -p /sbin/ldconfig

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun

%postun -n libflorence-1_0-1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog COPYING-DOCS NEWS README
%dir %{_datadir}/gnome/help/%{name}
%doc %{_datadir}/gnome/help/%{name}/C/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}_applet.1%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files -n libflorence-1_0-1
%defattr(-,root,root)
%{_libdir}/libflorence-1.0.so.*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/florence-1.0
%{_includedir}/florence-1.0/florence.h
%{_libdir}/libflorence-1.0.so
%{_libdir}/pkgconfig/florence-1.0.pc

%files lang -f %{name}.lang

%changelog
