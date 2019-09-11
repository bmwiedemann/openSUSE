#
# spec file for package ibus-anthy
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


Name:           ibus-anthy
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject2-devel
BuildRequires:  swig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(anthy)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(python3)
Version:        1.5.10
Release:        0
Summary:        The Anthy engine for IBus input platform
License:        GPL-2.0+
Group:          System/I18n/Japanese
Url:            https://github.com/ibus/ibus-anthy
Source:         https://github.com/ibus/ibus-anthy/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Anthy engine for IBus platform. It provides Japanese input method from
libanthy.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package includes the header files for the %{name} package.


%prep
%setup -q

%build
%configure --disable-static \
           --libexecdir=%{_libexecdir} \
           --with-python=python3

make %{?_smp_mflags}

%install
%makeinstall

find %{buildroot} -name "*.la" -type f -delete -print

%find_lang %{name}
%fdupes -s %{buildroot}

%suse_update_desktop_file ibus-setup-anthy System Utility settings

%post
/sbin/ldconfig
%if 0%{?suse_version} < 1330
%desktop_database_post
%icon_theme_cache_post
%endif

%postun
/sbin/ldconfig
%if 0%{?suse_version} < 1330
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-*
%{_datadir}/ibus-anthy
%{_datadir}/ibus
%{_libdir}/girepository-1.0
%{_datadir}/applications/ibus-setup-anthy.desktop
%{_datadir}/icons/hicolor/
%{_libdir}/libanthygobject-*.so.*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/*
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.anthy.gschema.xml

%files devel
%defattr(-,root,root,-)
%{_includedir}/ibus-anthy-1.0
%{_datadir}/gir-1.0
%{_libdir}/libanthygobject-*.so

%changelog
