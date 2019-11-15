#
# spec file for package msitools
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


Name:           msitools
Version:        0.100
Release:        0
Summary:        Tools to inspect and build Windows Installer (.MSI) files
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/msitools
Source:         https://download.gnome.org/sources/msitools/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.14
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.4
BuildRequires:  pkgconfig(libgcab-1.0) >= 0.1.10
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7
BuildRequires:  pkgconfig(uuid) >= 1.41.3
BuildRequires:  pkgconfig(vapigen) >= 0.16
Recommends:     %{name}-lang

%description
msitools is a set of programs to inspect and build Windows Installer
(.MSI) files.  It is based on libmsi, a portable library to read and
write .MSI files.

msitools plans to be a solution for packaging and deployment of
cross-compiled Windows applications.

%package -n libmsi0
Summary:        Library to inspect and build Windows Installer (.MSI) files
License:        LGPL-2.1-or-later

%description -n libmsi0
libmsi is a port of (and a subset of) Wine's implementation of the Windows
Installer.

%package -n typelib-1_0-Libmsi-1_0
Summary:        Introspection bindings for libmsi, a library to inspect and build .msi files
License:        LGPL-2.1-or-later

%description -n typelib-1_0-Libmsi-1_0
libmsi is a port of (and a subset of) Wine's implementation of the Windows
Installer.

%package devel
Summary:        Development files for libmsi, a library to inspect and build .msi files
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}
Requires:       libmsi0 = %{version}
Requires:       typelib-1_0-Libmsi-1_0 = %{version}

%description devel
msitools is a set of programs to inspect and build Windows Installer
(.MSI) files.  It is based on libmsi, a portable library to read and
write .MSI files.  libmsi in turn is a port of (and a subset of) Wine's
implementation of the Windows Installer.

msitools can be used for packaging and deployment of
cross-compiled Windows applications.

%lang_package

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libmsi0 -p /sbin/ldconfig
%postun -n libmsi0 -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS
%{_bindir}/msibuild
%{_bindir}/msidiff
%{_bindir}/msidump
%{_bindir}/msiextract
%{_bindir}/msiinfo
%{_bindir}/wixl
%{_bindir}/wixl-heat
%{_datadir}/bash-completion/completions/msitools
%{_datadir}/wixl-%{version}/

%files lang -f %{name}.lang

%files -n libmsi0
%{_libdir}/libmsi.so.0*

%files -n typelib-1_0-Libmsi-1_0
%{_libdir}/girepository-1.0/Libmsi-1.0.typelib

%files devel
%{_includedir}/libmsi-1.0/
%{_libdir}/libmsi.so
%{_libdir}/pkgconfig/libmsi-1.0.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/

%changelog
