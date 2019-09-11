#
# spec file for package pangox-compat
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           pangox-compat
Version:        0.0.2
Release:        0
Summary:        PangoX compatibility library - deprecated
License:        LGPL-2.0+
Group:          Development/Libraries/GNOME
Url:            http://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/
Source:         http://download.gnome.org/sources/pangox-compat/0.0/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pango)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.

%package -n libpangox-1_0-0
Summary:        PangoX compatibility library - deprecated
Group:          System/Libraries
# the main package only contains a config file which we assume remains compatible.
Requires:       %{name} >= %{version}

%description -n libpangox-1_0-0
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.

%package -n pangox-devel
Summary:        PangoX compatibility library - deprecated -- development files
Group:          Development/Libraries/GNOME
Requires:       libpangox-1_0-0 = %{version}

%description -n pangox-devel
Pango is a library for layout and rendering of text, with an emphasis
on internationalization. It can be used anywhere that text layout
is needed.

Pango forms the core of text and font handling for GTK+.

This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.

This package contains the files needed to develop against pangox.

%prep
%setup -q

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print

%clean
%{?buildroot:rm -rf %{buildroot}}

%post -n libpangox-1_0-0 -p /sbin/ldconfig

%postun -n libpangox-1_0-0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/pango
%config %{_sysconfdir}/pango/pangox.aliases

%files -n libpangox-1_0-0
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_libdir}/libpangox-1.0.so.*

%files -n pangox-devel
%defattr(-,root,root)
%{_includedir}/pango-1.0/pango/pangox.h
%{_libdir}/libpangox-1.0.so
%{_libdir}/pkgconfig/pangox.pc

%changelog
