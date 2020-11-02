#
# spec file for package gwenhywfar
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


%define libversion 79
%define devversion 5
%define devrelease 5.4
# Beta does not mean "before release" but a release that is considered as beta:
%define _version %{version}
%define _name gwenhywfar
%bcond_with configure
Name:           gwenhywfar
Version:        5.4.1
Release:        0
Summary:        Multiplatform helper library for other libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.aquamaniac.de/rdm/projects/gwenhywfar
# The github mirror tarballs are unreliable
Source:         %{_name}-%{_version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
# For doc graphs
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-fonts
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(gnutls) >= 2.9.8
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.17.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
Recommends:     libgwenhywfar%{libversion}
%if !%{with configure}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
%if 0%{?fedora} == 15
BuildRequires:  fox-devel >= 1.6
%else
BuildRequires:  fox16-devel
%endif

%description
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes some
often needed functions (for example, handling and parsing of
configuration files, reading and writingof XML files, and interprocess
communication).

%package tools
Summary:        Tools for the gwenhywfar multi-platform helper library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       libgwenhywfar%{libversion} = %{version}

%description tools
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

%package -n libgwenhywfar%{libversion}-plugins
Summary:        Plugins for the gwenhywfar multi-platform helper library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libgwenhywfar%{libversion}-plugins
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

%package -n libgwenhywfar%{libversion}
Summary:        Multiplatform Helper Library for Other Libraries
License:        LGPL-2.1-or-later
Group:          System/Libraries
Recommends:     %{name}-lang
Recommends:     libgwenhywfar%{libversion}-plugins = %{version}

%description -n libgwenhywfar%{libversion}
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

%package -n libgwengui-cpp%{libversion}
Summary:        C++ interface for Gwenhywfar
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgwengui-cpp%{libversion}
This package contains the C++ GUI interface for Gwenhywfar.

%package -n libgwengui-gtk2-%{libversion}
Summary:        GTK+ 2 UI backend for Gwenhywfar
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgwengui-gtk2-%{libversion}
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the GTK+ 2 implementation of the generic UI toolkit.

%package -n libgwengui-gtk3-%{libversion}
Summary:        GTK+ 3 UI backend for Gwenhywfar
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgwengui-gtk3-%{libversion}
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the GTK+ 3 implementation of the generic UI toolkit.

%package -n libgwengui-qt5-%{libversion}
Summary:        Qt5 UI backend for the gwenhywfar multi-platform helper library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       libgwengui-qt4-0 = %{version}
Obsoletes:      libgwengui-qt4-0 < %{version}

%description -n libgwengui-qt5-%{libversion}
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the Qt5 implementation of the generic UI toolkit.

%package -n libgwengui-fox16-%{libversion}
Summary:        FOX interface for Gwenhywfar
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgwengui-fox16-%{libversion}
This package contains the interface to the FOX toolkit
for Gwenhywfar.

%package devel
Summary:        Header files for the Gwenhywfar multi-platform helper library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libgwengui-fox16-%{libversion} >= %{version}
Requires:       libgwengui-gtk2-%{libversion} >= %{version}
Requires:       libgwengui-gtk3-%{libversion} >= %{version}
Requires:       libgwengui-qt5-%{libversion} >= %{version}
Requires:       libgwenhywfar%{libversion} = %{version}

%description devel
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (e.g. for handling and parsing of
configuration files, reading/writing of XML files, interprocess
communication etc).

%lang_package

%prep
%setup -q -n %{_name}-%{_version}

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
	--with-guis="fox16 qt5 gtk2 gtk3" \
	--with-plugins-cfgmgr=all
%make_jobs
make %{?_smp_mflags} srcdoc

%install
%make_install
%make_install install-srcdoc
pushd %{buildroot}%{_docdir}/%{name}/api
    # we don't want another 'gwenhywfar' dir below docpath
    mv %{_name}/* ./
    rm -rf %{_name}
    # remove empty files
    `find -maxdepth 1 -type f -empty -print0 | xargs -0 echo rm -f`
popd
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}
%fdupes %{buildroot}%{_datadir}/%{_name}/apidoc
%fdupes %{buildroot}%{_libdir}/cmake
%fdupes %{buildroot}%{_docdir}

%post   -n libgwenhywfar%{libversion} -p /sbin/ldconfig
%postun -n libgwenhywfar%{libversion} -p /sbin/ldconfig
%post   -n libgwengui-cpp%{libversion} -p /sbin/ldconfig
%postun -n libgwengui-cpp%{libversion} -p /sbin/ldconfig
%post   -n libgwengui-gtk2-%{libversion} -p /sbin/ldconfig
%postun -n libgwengui-gtk2-%{libversion} -p /sbin/ldconfig
%post   -n libgwengui-gtk3-%{libversion} -p /sbin/ldconfig
%postun -n libgwengui-gtk3-%{libversion} -p /sbin/ldconfig
%post -n libgwengui-qt5-%{libversion} -p /sbin/ldconfig
%postun -n libgwengui-qt5-%{libversion} -p /sbin/ldconfig
%post -n libgwengui-fox16-%{libversion} -p /sbin/ldconfig
%postun -n libgwengui-fox16-%{libversion} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README TODO
%dir %{_datadir}/%{_name}/
%{_datadir}/%{_name}/dialogs/
%dir %{_libdir}/%{_name}
%dir %{_libdir}/%{_name}/plugins
%dir %{_libdir}/%{_name}/plugins/%{libversion}
%exclude %{_docdir}/%{name}/api

%files tools
%{_bindir}/gct-tool
%{_bindir}/gsa
%{_bindir}/mklistdoc
%{_bindir}/typemaker
%{_bindir}/typemaker2
%{_bindir}/xmlmerge
%{_datadir}/%{_name}/typemaker2/

%files -n libgwenhywfar%{libversion}-plugins
%{_libdir}/%{_name}/plugins/%{libversion}/*

%files -n libgwenhywfar%{libversion}
%{_libdir}/lib%{_name}.so.*

%files -n libgwengui-cpp%{libversion}
%{_libdir}/libgwengui-cpp.so.*

%files -n libgwengui-gtk2-%{libversion}
%{_libdir}/libgwengui-gtk2.so.*

%files -n libgwengui-gtk3-%{libversion}
%{_libdir}/libgwengui-gtk3.so.*

%files -n libgwengui-qt5-%{libversion}
%{_libdir}/libgwengui-qt5.so.*

%files -n libgwengui-fox16-%{libversion}
%{_libdir}/libgwengui-fox16.so.*

%files devel
%{_bindir}/%{_name}-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/%{_name}.m4
%doc %{_docdir}/%{name}/api/
%{_includedir}/%{_name}%{devversion}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{_name}.pc
%{_libdir}/pkgconfig/gwengui-gtk2.pc
%{_libdir}/pkgconfig/gwengui-gtk3.pc
%{_libdir}/pkgconfig/gwengui-qt5.pc
%{_libdir}/pkgconfig/gwengui-fox16.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/%{_name}-%{devrelease}
%{_libdir}/cmake/gwengui-cpp-%{devrelease}
%{_libdir}/cmake/gwengui-qt5-%{devrelease}

%files lang -f %{_name}.lang

%changelog
