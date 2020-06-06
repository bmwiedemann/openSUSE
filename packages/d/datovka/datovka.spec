#
# spec file for package datovka
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


Name:           datovka
Version:        4.15.0
Release:        0
Summary:        Library to access Czech eGov system "Datove schranky"
License:        GPL-3.0-or-later
Group:          Development/Libraries/Python
URL:            https://www.datovka.cz
Source0:        https://secure.nic.cz/files/datove_schranky/%{version}/%{name}-%{version}.tar.xz
Source1:        https://secure.nic.cz/files/datove_schranky/%{version}/%{name}-%{version}.tar.xz.sha256
# PATCH-FIX-UPSTREAM: remove some issues with current .pro file
Patch0:         datovka-fix-pro.patch
Patch1:         0001-Fixed-compilation-using-Qt-5.15.0.patch
Patch2:         0001-avoid-using-deprecated-qs-rand.patch
Patch3:         0001-gui-datovka-annotate-fall-through-cases.patch
BuildRequires:  libqt5-linguist
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.2.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(libisds) >= 0.10.8
Requires:       libqt5_sql_backend
Recommends:     %{name}-lang
# Included inside with different approach
Obsoletes:      python-dslib
%if 0%{?suse_version} < 1330
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
%endif

%description
A library for accessing ISDS (Informační system datovych schranek/
Data Box Information System) SOAP services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%{?lang_package}

%prep
%autosetup -p1
sed -i \
    -e 's:lrelease:lrelease-qt5:g' \
    %{name}.pro

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
lrelease-qt5 datovka.pro
%qmake5 PREFIX=%{_prefix} DISABLE_VERSION_CHECK_BY_DEFAULT=1
%make_jobs

%install
%qmake5_install

# fix desktop file
sed -i \
    -e 's:Office;:Office;Network;Email;:g' \
    %{buildroot}%{_datadir}/applications/datovka.desktop
rm -rf %{buildroot}%{_datadir}/datovka/doc

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/datovka
%{_datadir}/applications/datovka.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/datovka.appdata.xml
%dir %{_datadir}/datovka
%dir %{_datadir}/datovka/localisations/
%{_datadir}/datovka/localisations/datovka_cs.qm
%{_datadir}/datovka/localisations/datovka_en.qm
%{_datadir}/icons/hicolor/*

%changelog
