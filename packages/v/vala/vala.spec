#
# spec file for package vala
#
# Copyright (c) 2025 SUSE LLC
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


# graphviz is needed only for valadoc
%bcond_without  graphviz

%define         vala_version 0.56
%define         vala_libversion 0_56
# The priority defines which version of vala, in case of multiple ones are installed
# is to be used by default. The rule-of-thumb for vala is to use MAJORMINOR without
# decimal separator, hoping they will not get to the idea to create a 0.100 release.
%define         vala_priority 56
Name:           vala
Version:        0.56.18
Release:        0
Summary:        Programming language for GNOME
License:        LGPL-2.1-or-later
Group:          Development/Languages/Other
URL:            https://wiki.gnome.org/Projects/Vala
Source0:        https://download.gnome.org/sources/vala/0.56/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  glib2-devel >= 2.48.0
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if %{with graphviz}
BuildRequires:  pkgconfig(libgvc) >= 2.16
%endif
# Vala is a compiler, so it's also a devel package
Provides:       vala-devel = %{version}
Obsoletes:      vala-devel < %{version}
# provide generic pkgconfig(vapigen) instead of -version one; not auto-detected due to %%{_datadir}/pkgconfig/vapigen.pc being %%ghost
Provides:       pkgconfig(vapigen) = %{version}

%description
Vala is an object-oriented programming language with a self-hosting
compiler that generates C code and uses the GObject system.

%package -n libvala-%{vala_libversion}-0
Summary:        Vala programming language runtime
Group:          System/Libraries

%description -n libvala-%{vala_libversion}-0
Runtime library for the Vala programming language.

%package -n libvala-%{vala_libversion}-devel
Summary:        Programming language for GNOME
Group:          Development/Libraries/Other
Requires:       libvala-%{vala_libversion}-0 = %{version}
# Stable name for consumers that support multiple API versions
Provides:       libvala-devel = %{version}

%description -n libvala-%{vala_libversion}-devel
Development files for the Vala runtime library.

%if %{with graphviz}
%package -n valadoc
Summary:        Generator for API documentation from Vala source
Group:          Development/Tools/Building

%description -n valadoc
Valadoc is a documentation generator for generating API documentation
from Vala source code.

%package -n valadoc-doclet-devhelp
Summary:        Devhelp plugin for the valadoc generator
Group:          Development/Tools/Building

%description -n valadoc-doclet-devhelp
Valadoc is a documentation generator for generating API documentation
from Vala source code.

%package -n valadoc-doclet-gtkdoc
Summary:        Gtkdoc plugin for valadoc
Group:          Development/Tools/Building

%description -n valadoc-doclet-gtkdoc
Valadoc is a documentation generator for generating API documentation
from Vala source code.

%package -n valadoc-doclet-html
Summary:        HTML plugin for valadoc
Group:          Development/Tools/Building

%description -n valadoc-doclet-html
Valadoc is a documentation generator for generating API documentation
from Vala source code.

%package -n libvaladoc-%{vala_libversion}-0
Summary:        Valadoc runtime
Group:          System/Libraries

%description -n libvaladoc-%{vala_libversion}-0
Valadoc is a documentation generator for generating API documentation
from Vala source code.

%package -n libvaladoc-%{vala_libversion}-devel
Summary:        Development files for the valadoc runtime
Group:          Development/Libraries/Other
Requires:       libvaladoc-%{vala_libversion}-0 = %{version}
# Stable name for consumers that support multiple API versions
Provides:       libvaladoc-devel = %{version}

%description -n libvaladoc-%{vala_libversion}-devel
Valadoc is a documentation generator for generating API documentation
from Vala source code.

This package contains the libvaladoc development files.
%endif

%prep
%autosetup -p1

%build
%configure \
%if %{without graphviz}
	--disable-valadoc \
%endif
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}

%ldconfig_scriptlets -n libvala-%{vala_libversion}-0
%if %{with graphviz}
%ldconfig_scriptlets -n libvaladoc-%{vala_libversion}-0
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.pre-0-4 ChangeLog.pre-0-5-7 NEWS README THANKS
%{_bindir}/vala
%{_bindir}/valac
%{_bindir}/vala-gen-introspect
%{_bindir}/vapigen
%{_mandir}/man1/valac.1%{?ext_man}
%{_mandir}/man1/vala-gen-introspect.1%{?ext_man}
%{_mandir}/man1/vapigen.1%{?ext_man}
%{_libdir}/pkgconfig/vapigen.pc
%{_bindir}/vala-%{vala_version}
%{_bindir}/valac-%{vala_version}
%{_bindir}/vala-gen-introspect-%{vala_version}
%{_bindir}/vapigen-%{vala_version}
%{_mandir}/man1/valac-%{vala_version}.1%{?ext_man}
%{_mandir}/man1/vala-gen-introspect-%{vala_version}.1%{?ext_man}
%{_mandir}/man1/vapigen-%{vala_version}.1%{?ext_man}
%{_datadir}/aclocal/vala.m4
%{_datadir}/aclocal/vapigen.m4
%{_libdir}/pkgconfig/vapigen-%{vala_version}.pc
%dir %{_datadir}/vala
%{_datadir}/vala/Makefile.vapigen
%{_datadir}/vala-%{vala_version}/
%{_libdir}/vala-%{vala_version}/

%if %{with graphviz}
%files -n valadoc
%{_bindir}/valadoc
%{_bindir}/valadoc-%{vala_version}
%{_mandir}/man1/valadoc*.1%{?ext_man}

%files -n valadoc-doclet-devhelp
%dir %{_libdir}/valadoc-%{vala_version}
%dir %{_libdir}/valadoc-%{vala_version}/doclets
%{_libdir}/valadoc-%{vala_version}/doclets/devhelp/

%files -n valadoc-doclet-gtkdoc
%dir %{_libdir}/valadoc-%{vala_version}
%dir %{_libdir}/valadoc-%{vala_version}/doclets
%{_libdir}/valadoc-%{vala_version}/doclets/gtkdoc/

%files -n valadoc-doclet-html
%dir %{_libdir}/valadoc-%{vala_version}
%dir %{_libdir}/valadoc-%{vala_version}/doclets
%{_libdir}/valadoc-%{vala_version}/doclets/html/
%endif

%files -n libvala-%{vala_libversion}-0
%{_libdir}/libvala-%{vala_version}.so.*

%if %{with graphviz}
%files -n libvaladoc-%{vala_libversion}-0
%{_libdir}/libvaladoc-%{vala_version}.so.*
%endif

%files -n libvala-%{vala_libversion}-devel
%{_includedir}/vala-%{vala_version}/
%{_libdir}/libvala-%{vala_version}.so
%{_libdir}/pkgconfig/libvala-%{vala_version}.pc
%dir %{_datadir}/devhelp/
%dir %{_datadir}/devhelp/books/
%{_datadir}/devhelp/books/%{name}-%{vala_version}/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libvala-%{vala_version}.vapi

%files -n libvaladoc-%{vala_libversion}-devel
%{_includedir}/valadoc-%{vala_version}/
%{_libdir}/libvaladoc-%{vala_version}.so
%{_datadir}/valadoc-%{vala_version}/
%{_libdir}/pkgconfig/valadoc-%{vala_version}.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/valadoc-%{vala_version}.*

%changelog
