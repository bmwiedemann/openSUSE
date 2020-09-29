#
# spec file for package gtk-sharp3
#
# Copyright (c) 2020 SUSE LLC
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


%define vsuffix git.2020.01.10.9dc89137b
Name:           gtk-sharp3
# package "libmono-profiler-gui-thread-check0-devel" does not allow us to add even a single symbol to version string without invoking rpmlint warning "W: filename-too-long-for-joliet"
Version:        2.99.4
Release:        0
Summary:        C-Sharp Language Bindings for GTK+
License:        GPL-2.0-only
Group:          System/GUI/GNOME
URL:            https:/github.com/mono/gtk-sharp
Source:         gtk-sharp3-%{vsuffix}.tar.xz
Source99:       create-source-archive.sh
Patch1:         profiler-update.patch
BuildRequires:  gtkhtml2-devel
BuildRequires:  libmono-2_0-devel
BuildRequires:  librsvg-devel
BuildRequires:  libtool
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Requires:       mono-core

%description
This package contains C-Sharp bindings for Gtk+, Gdk, Atk, and Pango.
for use with Mono.

%package devel
Summary:        .NET/C-Sharp Bindings for GIO
License:        LGPL-2.1-only
Group:          Development/Languages/Mono
Requires:       gtk-sharp3 = %{version}

%description devel
Files for developing programs using the C-Sharp bindings for Gtk+, Gdk, Atk, and Pango.

%package gapi
Summary:        C Source Parser and C Generator
License:        GPL-2.0-only
Group:          System/GUI/GNOME
Requires:       perl-XML-LibXML
Requires:       perl-XML-LibXML-Common
Requires:       perl-XML-SAX

%description gapi
The gtk-sharp-gapi package includes the parser and code generator used
by the GTK if you want to bind GObject-based libraries, or need to
compile a project that uses it to bind such a library.

%package -n gtk-sharp3-gapi-devel
Summary:        .NET/C-Sharp Bindings for GIO
License:        LGPL-2.1-only
Group:          Development/Languages/Mono
Requires:       gtk-sharp3-gapi = %{version}

%description -n gtk-sharp3-gapi-devel
Files for developing programs that use gapi-sharp3.

%package -n gtk-sharp3-doc
Summary:        Monodoc documentation for gtk-sharp2
License:        LGPL-2.1-only
Group:          System/GUI/GNOME

%description -n gtk-sharp3-doc
This package contains the gtk-sharp2 documentation for monodoc.

%package -n glib-sharp3
Summary:        Mono bindings for glib
License:        LGPL-2.1-only
Group:          System/GUI/GNOME

%description -n glib-sharp3
This package contains Mono bindings for glib.

%package -n gio-sharp3
Summary:        Mono bindings for gio
License:        LGPL-2.1-only
Group:          System/GUI/GNOME

%description -n gio-sharp3
This package contains Mono bindings for gio-sharp.

%package -n gio-sharp3-devel
Summary:        .NET/C-Sharp Bindings for GIO
License:        LGPL-2.1-only
Group:          Development/Languages/Mono
Requires:       gio-sharp3 = %{version}

%description -n gio-sharp3-devel
Files for developing programs that use gio-sharp

%package -n libmono-profiler-gui-thread-check0
Summary:        Profiler for gtk-sharp3
License:        GPL-2.0-only
Group:          Development/Languages/Mono

%description -n libmono-profiler-gui-thread-check0
A profiler called "gui-thread-check" is included as
part of the install for debugging purposes.

%post -n libmono-profiler-gui-thread-check0 -p /sbin/ldconfig
%postun -n libmono-profiler-gui-thread-check0 -p /sbin/ldconfig

%package -n libmono-profiler-gui-thread-check0-devel
Summary:        Profiler for gtk-sharp3
License:        GPL-2.0-only
Group:          Development/Languages/Mono
Requires:       libmono-profiler-gui-thread-check0 = %{version}

%description -n libmono-profiler-gui-thread-check0-devel
A profiler called "gui-thread-check" is included as
part of the install for debugging purposes.

%package -n gtk-sharp3-complete
Summary:        GTK+ and GNOME bindings for Mono (virtual package)
License:        LGPL-2.1-only
Group:          System/GUI/GNOME
Requires:       glib-sharp3 = %{version}
Requires:       gtk-sharp3 = %{version}
Requires:       gtk-sharp3-doc = %{version}
Requires:       gtk-sharp3-gapi = %{version}

%description -n gtk-sharp3-complete
Gtk-Sharp is a library that allows you to build fully native graphical GNOME
applications using Mono. Gtk-Sharp is a binding to GTK+, the cross platform
user interface toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk, libgnome, libgnomeui and libgnomecanvas. This is a virtual
package which depends on all gtk-sharp3 subpackages)

%prep
%setup -q -n gtk-sharp3-%{vsuffix}
%patch1 -p1
NOCONFIGURE=1 ./autogen.sh

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --libexecdir=%{_prefix}/lib/ --enable-debug
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.*a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libatksharpglue-3.so
%{_libdir}/libgtksharpglue-3.so
%{_libdir}/libgiosharpglue-3.so
%{_libdir}/libpangosharpglue-3.so
%{_prefix}/lib/mono/gtk-sharp-3.0/atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/cairo-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/pango-sharp.dll
%{_prefix}/lib/mono/gac/atk-sharp/
%{_prefix}/lib/mono/gac/cairo-sharp/
%{_prefix}/lib/mono/gac/gdk-sharp/
%{_prefix}/lib/mono/gac/gtk-dotnet/
%{_prefix}/lib/mono/gac/gtk-sharp/
%{_prefix}/lib/mono/gac/pango-sharp/

%files devel
%{_libdir}/pkgconfig/gtk-sharp-3.0.pc
%{_libdir}/pkgconfig/gdk-sharp-3.0.pc
%{_libdir}/pkgconfig/gtk-dotnet-3.0.pc
%{_libdir}/pkgconfig/glib-sharp-3.0.pc

%files gapi
%dir %{_prefix}/lib/gapi-3.0
%{_bindir}/gapi3-codegen
%{_bindir}/gapi3-fixup
%{_bindir}/gapi3-parser
%{_datadir}/gapi-3.0
%{_prefix}/lib/gapi-3.0/gapi_codegen.exe
%{_prefix}/lib/gapi-3.0/gapi-fixup.exe
%{_prefix}/lib/gapi-3.0/gapi-parser.exe
%{_prefix}/lib/gapi-3.0/gapi_pp.pl
%{_prefix}/lib/gapi-3.0/gapi2xml.pl

%files -n gtk-sharp3-gapi-devel
%{_libdir}/pkgconfig/gapi-3.0.pc

%files -n gtk-sharp3-doc
%license COPYING
%doc README
%{_prefix}/lib/monodoc

%files -n glib-sharp3
%{_prefix}/lib/mono/gac/glib-sharp/
%{_prefix}/lib/mono/gtk-sharp-3.0/glib-sharp.dll

%files -n gio-sharp3
%{_prefix}/lib/mono/gac/gio-sharp/
%{_prefix}/lib/mono/gtk-sharp-3.0/gio-sharp.dll

%files -n gio-sharp3-devel
%{_libdir}/pkgconfig/gio-sharp-3.0.pc

%files -n libmono-profiler-gui-thread-check0
%{_libdir}/libmono-profiler-gui-thread-check.so.*

%files -n libmono-profiler-gui-thread-check0-devel
%{_libdir}/libmono-profiler-gui-thread-check.so

%files -n gtk-sharp3-complete
%dir %{_prefix}/lib/mono/gtk-sharp-3.0

%changelog
