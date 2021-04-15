#
# spec file for package grisbi
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


Name:           grisbi
Version:        2.0.3
Release:        0
Summary:        Personal Accounting Application
License:        GPL-2.0-or-later
Group:          Productivity/Office/Finance
URL:            http://www.grisbi.org
Source0:        https://downloads.sourceforge.net/project/grisbi/grisbi%20stable/2.0.x/2.0.3/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sourceforge.net/project/grisbi/grisbi%20stable/2.0.x/2.0.3/%{name}-%{version}.tar.bz2.asc

BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(libcrypto) >= 1.0.0
BuildRequires:  pkgconfig(libgoffice-0.10) >= 0.10.0
BuildRequires:  pkgconfig(libgsf-1) >= 1.14
BuildRequires:  pkgconfig(libofx) >= 0.9
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(zlib)

%description
Grisbi is a personal accounting application, aiming at providing the most
simple and intuitive software for basic use, although it can be very powerful
if you spend a little time on the setup.

One notable feature is that it respects French accounting rules.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--disable-schemas-compile \
	%{nil}
%make_build

%install
%make_install

# Those files are deprecated and not needed anymore
rm %{buildroot}%{_datadir}/mime-info/grisbi.{keys,mime}

%check
%make_build check

%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/grisbi
%{_mandir}/man1/grisbi.1%{?ext_man}
%{_datadir}/applications/grisbi.desktop
%{_datadir}/doc/grisbi/
%{_datadir}/glib-2.0/schemas/org.gtk.grisbi.gschema.xml
%{_datadir}/grisbi/
%{_datadir}/icons/*/*/*/*grisbi.*
%{_datadir}/mime/packages/grisbi.xml
%{_datadir}/pixmaps/grisbi/

%files lang -f %{name}.lang

%changelog
