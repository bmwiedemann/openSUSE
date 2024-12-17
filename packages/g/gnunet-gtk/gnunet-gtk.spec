#
# spec file for package gnunet-gtk
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 4
Name:           gnunet-gtk
Version:        0.23.1
Release:        0
Summary:        GTK interface to GNUnet
License:        GPL-3.0-or-later
URL:            https://www.gnunet.org/
Source0:        https://ftp.gnu.org/pub/gnu/gnunet/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/gnunet/%{name}-%{version}.tar.gz.sig
# https://gnunet.org/~schanzen/3D11063C10F98D14BD24D1470B0998EF86F59B6A
# also https://grothoff.org/christian/
Source2:        https://grothoff.org/christian/grothoff.asc#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gladeui-2.0) >= 3.8
BuildRequires:  pkgconfig(gnunetcore) >= 0.23
BuildRequires:  pkgconfig(gnunetfs)
BuildRequires:  pkgconfig(gnunetstatistics)
BuildRequires:  pkgconfig(gnunetutil) >= 0.9.0
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       gnunet

%description
This package provides a gtk+ based GUI for configuring and using GNUnet.

%package -n libgnunetgtk%{sover}
Summary:        GNUnet GTK shared libraries

%description -n libgnunetgtk%{sover}
This package contains a shared library for the GNUnet GTK interface.

%package devel
Summary:        Development files for gnunet-gtk
Requires:       libgnunetgtk%{sover} = %{version}

%description devel
This package contains files needed to develop with gnunet-gtk.

%prep
%autosetup -p1

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%check
%make_build check

%ldconfig_scriptlets -n libgnunetgtk%{sover}

%files -f %{name}.lang
%license COPYING
%doc ChangeLog README
%{_bindir}/gnunet-fs-gtk
%{_bindir}/gnunet-setup
%{_bindir}/gnunet-statistics-gtk
%{_datadir}/gnunet
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/applications/*.desktop
%{_datadir}/gnunet-gtk
%{_datadir}/icons/hicolor/

%files -n libgnunetgtk%{sover}
%license COPYING
%{_libdir}/libgnunetgtk.so.%{sover}
%{_libdir}/libgnunetgtk.so.%{sover}.*

%files devel
%license COPYING
%{_includedir}/gnunet-gtk
%{_libdir}/libgnunetgtk.so

%changelog
