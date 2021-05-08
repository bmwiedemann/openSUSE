#
# spec file for package ibus-anthy
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ibus-anthy
BuildRequires:  anthy-devel
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject2-devel
BuildRequires:  swig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(python3)
Requires:       anthy
Version:        1.5.12
Release:        0
Summary:        The Anthy engine for IBus input platform
License:        GPL-2.0-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/ibus/ibus-anthy
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
%make_install

find %{buildroot} -name "*.la" -type f -delete -print

%find_lang %{name}
%fdupes -s %{buildroot}

%suse_update_desktop_file ibus-setup-anthy System Utility settings

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS README
%license COPYING
%{_libexecdir}/ibus-*
%{_datadir}/ibus-anthy
%{_datadir}/ibus
%{_libdir}/girepository-1.0
%{_datadir}/applications/ibus-setup-anthy.desktop
%{_datadir}/icons/hicolor/
%{_libdir}/libanthygobject-*.so.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.anthy.gschema.xml

%files devel
%{_includedir}/ibus-anthy-1.0
%{_datadir}/gir-1.0
%{_libdir}/libanthygobject-*.so

%changelog
