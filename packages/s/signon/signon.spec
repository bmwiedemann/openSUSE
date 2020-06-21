#
# spec file for package signon
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


%define _soname 1
%define _tarbasename signond
%define _version VERSION_8.60
Name:           signon
Version:        8.60
Release:        0
Summary:        Single Sign On Framework
License:        LGPL-2.0-only
Group:          System/Libraries
URL:            https://gitlab.com/accounts-sso/signond
Source:         https://gitlab.com/accounts-sso/%{_tarbasename}/-/archive/VERSION_%{version}/%{_tarbasename}-%{_version}.tar.bz2
Source99:       baselibs.conf
Patch0:         0001_Multilib.patch
# PATCH-FIX-UPSTREAM https://gitlab.com/accounts-sso/signond/-/merge_requests/27
Patch1:         0001-Don-t-use-fno-rtti.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libssl)

%description
The SignOn daemon is a D-Bus service which performs user authentication on
behalf of its clients.

%package -n libsignon-qt5-%{_soname}
Summary:        Single Sign On Framework for Qt
Group:          System/Libraries

%description -n libsignon-qt5-%{_soname}
Framework that provides credential storage and authentication service.

%package -n libsignon-qt5-devel
Summary:        Development files for libsignon-qt%{_soname}
Group:          Development/Libraries/C and C++
Requires:       libsignon-qt5-%{_soname} = %{version}
Requires:       pkgconfig(Qt5Core)

%description -n libsignon-qt5-devel
This package contains the development files for the signon-qt library.

%package -n libsignon-qt5-docs
Summary:        Documentation for libsignon-qt%{_soname}
Group:          Documentation/HTML
BuildArch:      noarch

%description -n libsignon-qt5-docs
This package contains the documentation for the signon-qt library.

%package -n signond
Summary:        Single Sign On Framework
Group:          System/Libraries

%description -n signond
Framework that provides credential storage and authentication service.

%package -n signond-libs
Summary:        Single Sign On Framework
Group:          System/Libraries

%description -n signond-libs
Framework that provides credential storage and authentication service.

%package -n signond-libs-devel
Summary:        Development files for signond-libs
Group:          Development/Libraries/C and C++
Requires:       signond = %{version}
Requires:       signond-libs = %{version}
Requires:       pkgconfig(Qt5Core)

%description -n signond-libs-devel
This package contains the development files for signond-libs.

%package -n signond-docs
Summary:        Single Sign On Framework - Documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description -n signond-docs
This package contains the documentation for signond.

%package -n signon-plugins
Summary:        Plugins for the Single Sign On Framework
Group:          System/Libraries
Requires:       signond = %{version}

%description -n signon-plugins
This package contains the following plugins for the Single Sign On Framework:
- Password plugin
- Test plugin

%package -n signon-plugins-devel
Summary:        Development files for the Single Sign On Framework's plugins
Group:          Development/Libraries/C and C++
Requires:       libsignon-qt5-devel = %{version}
Requires:       signon-plugins = %{version}

%description -n signon-plugins-devel
This package contains the development files necessary for creating plugins for
the Single Sign On Framework.

%package -n signon-plugins-docs
Summary:        Documentation for the Single Sign On Framework's plugins
Group:          Documentation/HTML
BuildArch:      noarch

%description -n signon-plugins-docs
This package contains the documentation for the Single Sign On Framework's
plugins.

%prep
%autosetup -p1 -n %{_tarbasename}-%{_version}

sed -i 's|@LIB@|%{_lib}|g' \
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

sed -i 's|qdbusxml2cpp|qdbusxml2cpp-qt5|g' \
  src/signond/signond.pro

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%qmake5 \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%make_jobs

%install
%qmake5_install

# Remove tests
find %{buildroot} -type f -name '*tests*' -delete

%fdupes -s %{buildroot}

%post -n libsignon-qt5-%{_soname} -p /sbin/ldconfig
%postun -n libsignon-qt5-%{_soname} -p /sbin/ldconfig
%post -n signond-libs -p /sbin/ldconfig
%postun -n signond-libs -p /sbin/ldconfig
%post -n signon-plugins -p /sbin/ldconfig
%postun -n signon-plugins -p /sbin/ldconfig

%files -n libsignon-qt5-%{_soname}
%{_libdir}/libsignon-qt5.so.*

%files -n libsignon-qt5-devel
%dir %{_includedir}/signon-qt5/
%dir %{_includedir}/signon-qt5/SignOn/
%{_includedir}/signon-qt5/SignOn/*
%{_libdir}/libsignon-qt5.so
%{_libdir}/libsignon-qt5.a
%{_libdir}/pkgconfig/libsignon-qt5.pc
%{_libdir}/cmake/SignOnQt5/

%files -n libsignon-qt5-docs
%doc %{_docdir}/libsignon-qt/

%files -n signond
%license COPYING
%doc README.md
%{_bindir}/signond
%{_bindir}/signonpluginprocess
%config(noreplace) %{_sysconfdir}/signond.conf
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.SingleSignOn.service
%{_datadir}/dbus-1/services/com.nokia.SingleSignOn.Backup.service

%files -n signond-libs
%{_libdir}/libsignon-extension.so.*
%{_libdir}/libsignon-plugins-common.so.*

%files -n signond-libs-devel
%dir %{_includedir}/signond/
%{_includedir}/signond/*.h
%dir %{_includedir}/signon-extension/
%dir %{_includedir}/signon-extension/SignOn/
%{_includedir}/signon-extension/SignOn/*
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/pkgconfig/signond.pc
%{_libdir}/pkgconfig/SignOnExtension.pc

%files -n signond-docs
%doc %{_docdir}/signon/

%files -n signon-plugins
%{_libdir}/libsignon-plugins.so.*
%dir %{_libdir}/signon/
%{_libdir}/signon/libexampleplugin.so
%{_libdir}/signon/libpasswordplugin.so
%{_libdir}/signon/libssotest2plugin.so
%{_libdir}/signon/libssotestplugin.so

%files -n signon-plugins-devel
%doc %{_docdir}/signon-plugins-dev/
%dir %{_includedir}/signon-plugins/
%dir %{_includedir}/signon-plugins/SignOn/
%{_includedir}/signon-plugins/SignOn/*.h
%{_includedir}/signon-plugins/*
%{_libdir}/libsignon-plugins.so
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc

%files -n signon-plugins-docs
%doc %{_docdir}/signon-plugins/

%changelog
