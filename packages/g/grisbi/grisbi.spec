# vim: set sw=4 ts=4 et:
#
# spec file for package grisbi
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


Name:           grisbi
Version:        1.0.4
Release:        0
Summary:        Personal Accounting Application
License:        GPL-2.0-or-later
Group:          Productivity/Office/Finance
URL:            http://www.grisbi.org
Source:         http://downloads.sourceforge.net/project/grisbi/grisbi%20stable/1.0.x/%{name}-%{version}.tar.bz2

BuildRequires:  cunit-devel
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)
# Disabled as we do not want to depend on this old compat version - next major grisbi release will depend on new libgoffice
#BuildRequires:  pkgconfig(libgoffice-0.8)
BuildRequires:  pkgconfig(libofx)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-lang

%description
Grisbi is a personal accounting application, aiming at providing the most
simple and intuitive software for basic use, although it can be very powerful
if you spend a little time on the setup.

One notable feature is that it respects French accounting rules.

%lang_package

%prep
%setup -q

%build
%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install
# Those files are deprecated and not needed anymore
rm %{buildroot}%{_datadir}/mime-info/grisbi.{keys,mime}
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/grisbi
%{_mandir}/man1/grisbi.1%{?ext_man}
%{_datadir}/applications/grisbi.desktop
%{_datadir}/doc/grisbi/
%{_datadir}/grisbi/
%{_datadir}/icons/*/*/apps/grisbi.*
%{_datadir}/mime/packages/grisbi.xml
%{_datadir}/pixmaps/grisbi/

%files lang -f %{name}.lang

%changelog
