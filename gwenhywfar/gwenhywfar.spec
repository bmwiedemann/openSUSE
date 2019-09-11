#
# spec file for package gwenhywfar
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%bcond_without qt4
%bcond_with configure
%define	libname libgwenhywfar60
%define devversion 4.20
Name:           gwenhywfar
Version:        4.20.1
Release:        0
Summary:        Multiplatform helper library for other libraries
License:        GPL-2.0+ and LGPL-2.1+
Group:          System/Libraries
Url:            http://www.aqbanking.de/
Source:         https://github.com/aqbanking/gwenhywfar/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if !%{with configure}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
# For doc graphs
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  libopenssl-devel
%if %{with qt4}
%if 0%{?suse_version} >= 1500
#!BuildIgnore:  libopenssl-1_0_0-devel
%endif
BuildRequires:  libqt4-devel
%endif
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
%if 0%{?fedora} == 15
BuildRequires:  fox-devel >= 1.6
%else
BuildRequires:  fox16-devel
%endif
BuildRequires:  xorg-x11-fonts
BuildRequires:  pkgconfig(gnutls) >= 2.9.8
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.17.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
Recommends:     %{libname}

%description
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes some
often needed functions (for example, handling and parsing of
configuration files, reading and writingof XML files, and interprocess
communication).

%package tools
Summary:        Multiplatform Helper Library for Other Libraries - Tools
License:        GPL-2.0+ and LGPL-2.1+
Group:          System/Libraries
Requires:       %{libname} = %{version}

%description tools
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

%package -n %{libname}-plugins
Summary:        Multiplatform Helper Library for Other Libraries - Plugins
License:        LGPL-2.1+
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n %{libname}-plugins
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

%package -n %{libname}
Summary:        Multiplatform Helper Library for Other Libraries
License:        LGPL-2.1+
Group:          System/Libraries
Recommends:     %{name}-lang
Recommends:     %{libname}-plugins = %{version}

%description -n %{libname}
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

%package -n libgwengui-cpp0
Summary:        C++ interface for Gwenhywfar
License:        GPL-2.0+ and LGPL-2.1+
Group:          System/Libraries

%description -n libgwengui-cpp0
This package contains the C++ GUI interface for Gwenhywfar.

%package -n libgwengui-gtk2-0
Summary:        Multiplatform Helper Library for Other Libraries -- GTK+ 2 UI Backend
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libgwengui-gtk2-0
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the GTK+ 2 implementation of the generic UI toolkit.

%package -n libgwengui-gtk3-0
Summary:        Multiplatform Helper Library for Other Libraries -- GTK+ 3 UI Backend
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libgwengui-gtk3-0
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the GTK+ 3 implementation of the generic UI toolkit.

%package -n libgwengui-qt4-0
Summary:        Multiplatform Helper Library for Other Libraries -- Qt4 UI Backend
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libgwengui-qt4-0
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the Qt4 implementation of the generic UI toolkit.

%package -n libgwengui-qt5-0
Summary:        Multiplatform Helper Library for Other Libraries -- Qt5 UI Backend
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libgwengui-qt5-0
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the Qt5 implementation of the generic UI toolkit.

%package -n libgwengui-fox16-0
Summary:        FOX interface for Gwenhywfar
License:        GPL-2.0+ and LGPL-2.1+
Group:          System/Libraries

%description -n libgwengui-fox16-0
This package contains the interface to the FOX toolkit
for Gwenhywfar.

%package devel
Summary:        Multi-Platform Helper Library for Other Libraries
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       %{libname} = %{version}
Requires:       libgwengui-fox16-0 = %{version}
Requires:       libgwengui-gtk2-0 = %{version}
Requires:       libgwengui-gtk3-0 = %{version}
%if %{with qt4}
Requires:       libgwengui-qt4-0 = %{version}
%endif
Requires:       libgwengui-qt5-0 = %{version}

%description devel
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (e.g. for handling and parsing of
configuration files, reading/writing of XML files, interprocess
communication etc).

%lang_package
%prep
%setup -q

%build
export PATH=%{_libqt5_bindir}:$PATH
# quick fix for $CPP being unset and configure failing to handle include dirs properly
CPP=`which cpp`
export CPP
%if !%{with configure}
autoreconf -ifv
%endif
%configure\
	--enable-release\
	--enable-full-doc\
	--with-docpath=%{_docdir}/%{name}/api \
	--disable-static \
%if %{with qt4}
	--with-qt4-libs=%{_libdir} \
	--with-guis="fox16 qt4 qt5 gtk2 gtk3" \
%else
	--with-guis="fox16 qt5 gtk2 gtk3" \
%endif
	--with-plugins-cfgmgr=all \
	--with-pic
%__make %{?smp_mflags}
%__make srcdoc %{?smp_mflags}

%install
%make_install
%make_install install-srcdoc
pushd %{buildroot}%{_docdir}/%{name}/api
    # we don't want another 'gwenhywfar' dir below docpath
    %__mv %{name}/* ./
    rm -rf %{name}
    # remove empty files
    `find -maxdepth 1 -type f -empty -print0 | xargs -0 echo %__rm -f`
popd
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/%{name}/apidoc
%fdupes %{buildroot}%{_libdir}/cmake

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post   -n libgwengui-cpp0 -p /sbin/ldconfig
%postun -n libgwengui-cpp0 -p /sbin/ldconfig

%post   -n libgwengui-gtk2-0 -p /sbin/ldconfig
%postun -n libgwengui-gtk2-0 -p /sbin/ldconfig

%post   -n libgwengui-gtk3-0 -p /sbin/ldconfig
%postun -n libgwengui-gtk3-0 -p /sbin/ldconfig

%if %{with qt4}
%post -n libgwengui-qt4-0 -p /sbin/ldconfig
%postun -n libgwengui-qt4-0 -p /sbin/ldconfig
%endif

%post -n libgwengui-qt5-0 -p /sbin/ldconfig
%postun -n libgwengui-qt5-0 -p /sbin/ldconfig

%post -n libgwengui-fox16-0 -p /sbin/ldconfig
%postun -n libgwengui-fox16-0 -p /sbin/ldconfig

%files
%doc AUTHORS COPYING NEWS README TODO
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/ca-bundle.crt
%{_datadir}/%{name}/dialogs/
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/60
%exclude %{_docdir}/%{name}/api

%files tools
%{_bindir}/gct-tool
%{_bindir}/gsa
%{_bindir}/mklistdoc
%{_bindir}/typemaker
%{_bindir}/typemaker2
%{_bindir}/xmlmerge
%{_datadir}/%{name}/typemaker2/

%files -n %{libname}-plugins
%{_libdir}/%{name}/plugins/60/*

%files -n %{libname}
%{_libdir}/lib%{name}.so.*

%files -n libgwengui-cpp0
%{_libdir}/libgwengui-cpp.so.*

%files -n libgwengui-gtk2-0
%{_libdir}/libgwengui-gtk2.so.*

%files -n libgwengui-gtk3-0
%{_libdir}/libgwengui-gtk3.so.*

%if %{with qt4}
%files -n libgwengui-qt4-0
%{_libdir}/libgwengui-qt4.so.*
%endif

%files -n libgwengui-qt5-0
%{_libdir}/libgwengui-qt5.so.*

%files -n libgwengui-fox16-0
%{_libdir}/libgwengui-fox16.so.*

%files devel
%{_bindir}/%{name}-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/%{name}.m4
%doc %{_docdir}/%{name}/api/
%{_includedir}/%{name}4/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/gwengui-gtk2.pc
%{_libdir}/pkgconfig/gwengui-gtk3.pc
%if %{with qt4}
%{_libdir}/pkgconfig/gwengui-qt4.pc
%{_libdir}/cmake/gwengui-qt4-%{devversion}
%endif
%{_libdir}/pkgconfig/gwengui-qt5.pc
%{_libdir}/pkgconfig/gwengui-fox16.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/%{name}-%{devversion}
%{_libdir}/cmake/gwengui-cpp-%{devversion}
%{_libdir}/cmake/gwengui-qt5-%{devversion}

%files lang -f %{name}.lang

%changelog
