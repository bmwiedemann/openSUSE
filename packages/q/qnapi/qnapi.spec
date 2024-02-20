#
# spec file for package qnapi
#
# Copyright (c) 2024 SUSE LLC
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


Name:           qnapi
Version:        0.2.3
Release:        0
Summary:        A NapiProjekt client
# libmaia and qt-maybe are BSD-2-Clause and BSD-3-Clause respectively
License:        GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause
URL:            https://qnapi.github.io/
Source0:        https://github.com/QNapi/qnapi/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         qnapi-libmaia.patch
# PATCH-FIX-UPSTREAM qnapi-Qt511.patch
Patch1:         qnapi-Qt511.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(maia)
BuildRequires:  pkgconfig(zlib)
Recommends:     ffmpeg
# Remove when p7zip-full is in all products
%if 0%{?suse_version} > 1500
Requires:       p7zip-full
%else
Requires:       p7zip
%endif

%description
QNapi is unofficial clone of NapiProjekt program (http://napiprojekt.pl)
written using Qt5. It's focused to be functional on GNU/Linux and other
Unix-like systems, for which NapiProjekt is not available.

%description -l it
QNapi è un clone non ufficiale del programma NapiProjekt (http://napiprojekt.pl)
scritto usando Qt5. È indirizzato alla funzionalità su GNU/Linux ed altri sistemi
simili a Unix, per cui NapiProjekt non è disponibile.

%description -l pl
QNapi jest nieoficjalnym klonem programu NapiProjekt (http://napiprojekt.pl)
napisanym w bibliotece Qt5 z myślą o użytkownikach Linuksa oraz innych
systemów, pod które oryginalny NapiProjekt nie jest dostępny.

%prep
%autosetup -p1

# Fix paths specific for openSUSE
sed -i 's|doc.path = $${INSTALL_PREFIX}/share/doc/qnapi|doc.path = $${INSTALL_PREFIX}/share/doc/packages/qnapi|' qnapi.pro

%build
# fixes gcc6 problem with stdlib headers
%qmake5 QMAKE_DEFAULT_INCDIRS="" %{name}.pro
%make_build

%install
make INSTALL_ROOT=%{buildroot} install %{?_smp_mflags}
# Add KDE4 service menu
install -m 644 -D doc/qnapi-download.desktop %{buildroot}%{_datadir}/kde4/services/ServiceMenus/qnapi-download.desktop
install -m 644 -D doc/qnapi-scan.desktop %{buildroot}%{_datadir}/kde4/services/ServiceMenus/qnapi-scan.desktop
# Add Plasma 5 service menu
install -m 644 -D doc/qnapi-download.desktop %{buildroot}%{_datadir}/kservices5/ServiceMenus/qnapi-download.desktop
install -m 644 -D doc/qnapi-scan.desktop %{buildroot}%{_datadir}/kservices5/ServiceMenus/qnapi-scan.desktop

# Fix for "wrong-file-end-of-line-encoding" doc/ChangeLog file
sed -i 's/\r//' doc/ChangeLog

# Put license files in the right place
rm %{buildroot}%{_defaultdocdir}/%{name}/LICENSE*

%fdupes %{buildroot}%{_prefix}
%suse_update_desktop_file -i -r -n %{name} AudioVideo AudioVideoEditing

%files
%doc doc/COPYRIGHT doc/ChangeLog doc/qnapi-download.desktop doc/qnapi-download.schemas doc/qnapi-scan.desktop doc/qnapi-scan.schemas
%license doc/LICENSE doc/LICENSE-pl
%{_bindir}/%{name}
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_mandir}/man1/*
%{_mandir}/it/man1/qnapi.1%{?ext_man}
%{_mandir}/pl/man1/qnapi.1%{?ext_man}
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus
%{_datadir}/kde4/services/ServiceMenus/qnapi-download.desktop
%{_datadir}/kde4/services/ServiceMenus/qnapi-scan.desktop
%dir %{_datadir}/kservices5
%dir %{_datadir}/kservices5/ServiceMenus
%{_datadir}/kservices5/ServiceMenus/qnapi-download.desktop
%{_datadir}/kservices5/ServiceMenus/qnapi-scan.desktop

%changelog
