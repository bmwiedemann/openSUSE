#
# spec file for package signon
#
# Copyright (c) 2023 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%define _suffix qt6
%define _major_ver 6
%else
%define qt5 1
%define _suffix qt5
%define _major_ver 5
%endif
%define _soname 1
%define rname signond
%define rversion VERSION_8.61
Name:           signon%{?pkg_suffix}
Version:        8.61
Release:        0
Summary:        Single Sign On Framework
License:        LGPL-2.0-only
URL:            https://gitlab.com/accounts-sso/signond
Source:         https://gitlab.com/accounts-sso/%{rname}/-/archive/VERSION_%{version}/%{rname}-%{rversion}.tar.bz2
# PATCH-FIX-UPSTREAM -- https://gitlab.com/accounts-sso/signond/-/merge_requests/36/diffs
Patch0:         0001-Add-Qt6-support.patch
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt%{_major_ver}Core)
BuildRequires:  pkgconfig(Qt%{_major_ver}DBus)
BuildRequires:  pkgconfig(Qt%{_major_ver}Gui)
BuildRequires:  pkgconfig(Qt%{_major_ver}Network)
BuildRequires:  pkgconfig(Qt%{_major_ver}Sql)
BuildRequires:  pkgconfig(Qt%{_major_ver}Test)
BuildRequires:  pkgconfig(Qt%{_major_ver}Xml)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libssl)

%description
The SignOn daemon is a D-Bus service which performs user authentication on
behalf of its clients.

# NOTE Read https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/merge_requests/28#note_1689621252
# Only lisignon-qtX must be flavored
%package -n libsignon-qt%{_major_ver}-%{_soname}
Summary:        Single Sign On Framework for Qt

%description -n libsignon-qt%{_major_ver}-%{_soname}
Framework that provides credential storage and authentication service.

%package -n libsignon-qt%{_major_ver}-devel
Summary:        Development files for libsignon-qt%{_soname}
Requires:       libsignon-qt%{_major_ver}-%{_soname} = %{version}
Requires:       pkgconfig(Qt%{_major_ver}Core)

%description -n libsignon-qt%{_major_ver}-devel
This package contains the development files for the signon-qt library.

%if 0%{?qt6}
%package -n signond
Summary:        Single Sign On Framework
Requires:       signond-libs = %{version}
Requires:       qt6-sql-sqlite

%description -n signond
Framework that provides credential storage and authentication service.

# No need to build docs twice
%package -n signond-docs
Summary:        Single Sign On Framework - Documentation
BuildArch:      noarch

%description -n signond-docs
This package contains the documentation for signond.

%package -n libsignon-qt-docs
Summary:        Documentation for the signon-qt library
BuildArch:      noarch

%description -n libsignon-qt-docs
This package contains the documentation for the signon-qt library.

%package -n signon-plugins-docs
Summary:        Documentation for the Single Sign On Framework's plugins
BuildArch:      noarch

%description -n signon-plugins-docs
This package contains the documentation for the Single Sign On Framework's
plugins.

%package -n signond-libs
Summary:        Single Sign On Framework

%description -n signond-libs
Framework that provides credential storage and authentication service.

%package -n signond-libs-devel
Summary:        Development files for signond-libs
Requires:       signond = %{version}
Requires:       signond-libs = %{version}
Requires:       pkgconfig(Qt6Core)

%description -n signond-libs-devel
This package contains the development files for signond-libs.

%package -n signon-plugins
Summary:        Plugins for the Single Sign On Framework
Requires:       signond = %{version}

%description -n signon-plugins
This package contains the following plugins for the Single Sign On Framework:
  * Password plugin
  * Test plugin

%package -n signon-plugins-devel
Summary:        Development files for the Single Sign On Framework's plugins
Requires:       libsignon-qt6-devel = %{version}
Requires:       signon-plugins = %{version}

%description -n signon-plugins-devel
This package contains the development files necessary for creating plugins for
the Single Sign On Framework.
%endif

%prep
%autosetup -p1 -n %{rname}-%{rversion}

sed -i 's|/usr/lib|%{_libdir}|g' \
  lib/plugins/signon-plugins.pc.in \
  lib/plugins/signon-plugins-common/signon-plugins-common.pc.in \
  src/signond/signondaemon.h \
  src/remotepluginprocess/remotepluginprocess.h \
  src/plugins/example/exampleplugin.pro

# Fix documentation directory
sed -i -e '/^documentation.path/ s|share/doc|share/doc/packages|g' \
  doc/doc.pri \
  lib/plugins/doc/doc.pri \
  lib/SignOn/doc/doc.pri

sed -i -e '/^example.path/ s|share/doc|share/doc/packages|g' \
  src/plugins/example/example.pro

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%if 0%{?qt6}
%qmake6 \
%else
%qmake5 \
%endif
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%make_jobs

%install
%if 0%{?qt6}
%qmake6_install
%else
%qmake5_install

# Only needed once
rm %{buildroot}%{_bindir}/*
rm %{buildroot}%{_libdir}/libsignon-{extension,plugins}*
rm %{buildroot}%{_libdir}/pkgconfig/{SignOnExtension,signond,signon-plugins}*
rm %{buildroot}%{_sysconfdir}/signond.conf
rm -r %{buildroot}%{_datadir}/dbus-1
rm -r %{buildroot}%{_docdir}
rm -r %{buildroot}%{_includedir}/signon-{extension,plugins}
rm -r %{buildroot}%{_includedir}/signond
rm -r %{buildroot}%{_libdir}/signon

%endif

# Remove tests
find %{buildroot} -type f -name '*tests*' -print -delete

%ldconfig_scriptlets -n libsignon-qt%{_major_ver}-%{_soname}
%if 0%{?qt6}
%ldconfig_scriptlets -n signond-libs
%ldconfig_scriptlets -n signon-plugins
%endif

%files -n libsignon-qt%{_major_ver}-%{_soname}
%license COPYING
%{_libdir}/libsignon-qt%{_major_ver}.so.*

%files -n libsignon-qt%{_major_ver}-devel
%{_includedir}/signon-qt%{_major_ver}/
%{_libdir}/libsignon-qt%{_major_ver}.so
%{_libdir}/libsignon-qt%{_major_ver}.a
%{_libdir}/pkgconfig/libsignon-qt%{_major_ver}.pc
%{_libdir}/cmake/SignOnQt%{_major_ver}/

%if 0%{?qt6}
%files -n signond
%doc README.md
%config(noreplace) %{_sysconfdir}/signond.conf
%{_bindir}/signond
%{_bindir}/signonpluginprocess
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.SingleSignOn.service
%{_datadir}/dbus-1/services/com.nokia.SingleSignOn.Backup.service

%files -n signond-libs
%{_libdir}/libsignon-extension.so.*
%{_libdir}/libsignon-plugins-common.so.*

%files -n signond-libs-devel
%{_includedir}/signond/
%{_includedir}/signon-extension/
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/pkgconfig/signond.pc
%{_libdir}/pkgconfig/SignOnExtension.pc

%files -n signon-plugins
%{_libdir}/libsignon-plugins.so.*
%dir %{_libdir}/signon/
%{_libdir}/signon/libexampleplugin.so
%{_libdir}/signon/libpasswordplugin.so
%{_libdir}/signon/libssotest2plugin.so
%{_libdir}/signon/libssotestplugin.so

%files -n signon-plugins-devel
%doc %{_docdir}/signon-plugins-dev/
%{_includedir}/signon-plugins/
%{_libdir}/libsignon-plugins.so
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc

%files -n signond-docs
%doc %{_docdir}/signon/

%files -n libsignon-qt-docs
%doc %{_docdir}/libsignon-qt/

%files -n signon-plugins-docs
%doc %{_docdir}/signon-plugins/
%endif

%changelog
