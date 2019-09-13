#
# spec file for package elektra
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


Version:        0.8.20
Release:        0
%define tempdocdir %{_prefix}/elektra
%define __libtoolize    /bin/true
%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

Name:           elektra
Source:         http://www.libelektra.org/ftp/elektra/releases/%{name}-%{version}.tar.gz
Url:            http://www.libelektra.org
%define api     4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source1:        elektra-rpmlintrc
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig(dbus-1)
#BuildRequires:  java-1.8.0-devel

# g-ir-compiler fails to build
# BuildRequires:  gobject-introspection-devel
%define use_aug 1
%define use_glib 0
%define use_swig 0
BuildRequires:  augeas-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
%define use_qt5 1
BuildRequires:  discount
BuildRequires:  libQt5DBus-devel
BuildRequires:  libQt5Test-devel
BuildRequires:  libgit2-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libyajl-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-logger
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1320 || 0%{?suse_version} == 1315
BuildRequires:  fish
%endif
#BuildRequires:  lua-devel
#BuildRequires:  python
#BuildRequires:  python-devel
#BuildRequires:  swig
Patch:          patch-fix-augeas-config.patch
# PATCH-FIX-UPSTREAM Qt-GUI-Do-not-use-deprecated-qt_use_modules.patch -- fix build with Qt 5.11
Patch1:         Qt-GUI-Do-not-use-deprecated-qt_use_modules.patch

Summary:        A key/value pair database to store software configurations
License:        BSD-3-Clause
Group:          System/Libraries

%package -n lib%{name}%{api}
Summary:        Hierarchical key-value pair tree configuration library
Group:          System/Libraries
Requires(post):       %{name}

%package -n %{name}-qt-gui
Summary:        Hierarchical key-value pair tree configuration gui
Group:          System/X11/Utilities

%package -n lib%{name}-augeas
Summary:        Augeas support for Elektra
Group:          System/Libraries
Requires:       lib%{name}%{api} = %{version}-%{release}

%package -n libg%{name}-%{api}.0
Summary:        Glib support for Elektra
Group:          System/Libraries

%package -n lib%{name}-lua
Summary:        Lua support for Elektra
Group:          System/Libraries
Requires:       lib%{name}%{api} = %{version}-%{release}

%package -n python-%{name}
Summary:        Python support for Elektra
Group:          Development/Languages/Python
Requires:       lib%{name}%{api} = %{version}-%{release}

%package -n lib%{name}-devel
Summary:        Include files and libraries to build elektrified programs
Group:          Development/Libraries/C and C++
Requires:       pkgconfig lib%{name}%{api} = %{version}-%{release}

%package -n lib%{name}-devel-doc
Summary:        Development documentation for Elektra
Group:          Documentation/Man
Requires:       lib%{name}-devel = %{version}-%{release}

%description
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair mechanism, instead of each
program using its own text configuration files. This allows any program
to read and save its configuration with a consistent API, and allows
them to be aware of other applications' configurations, permitting
easy application integration. While architecturally similar to other OS
registries, Elektra does not have most of the problems found in those
implementations.

%description -n lib%{name}%{api}
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

%description -n %{name}-qt-gui
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

The Qt Gui.

%description -n lib%{name}-augeas
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

The augeas backend for elektra.

%description -n libg%{name}-%{api}.0
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

The glib binding for elektra.

%description -n lib%{name}-lua
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

The lua binding for elektra.

%description -n python-%{name}
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

The python binding for elektra.

%description -n lib%{name}-devel
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

This package contains development specific things as include files and
static libraries to create elektrified programs.

%description -n lib%{name}-devel-doc
Elektra provides a universal and secure framework to store configuration
parameters in a hierarchical key-value pair tree.

This package contains development specific documentation.


%prep
%setup -q
%patch -p1
%patch1 -p1

%build
export SUSE_ASNEEDED=0
%cmake -DTARGET_PLUGIN_FOLDER="elektra%{api}" \
  -DPLUGINS="ALL" \
  -DTOOLS="ALL" \
  -DBINDINGS="ALL" \
  -DENABLE_TESTING="OFF" \
  -DBUILD_TESTING="OFF" \
  -DTARGET_DOCUMENTATION_HTML_FOLDER="share/doc/elektra-doc/html" \
  -DBUILD_DOCUMENTATION=ON \
  -DTARGET_CMAKE_FOLDER=%{_lib}/cmake/elektra \
  -DCMAKE_C_FLAGS="-fPIC $CFLAGS" \
  -DCMAKE_CXX_FLAGS="-fPIC $CXXFLAGS"
# get basics done, care abuot bindings later
  #-DPYTHON_INCLUDE_DIR=`python3  -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())"` \
  #-DPYTHON_LIBRARY=/usr/%{_lib}/libpython3.so \
# doxygen appears to have problems with multi level directory creation on elder distros
mkdir -p doc/html doc/man
make %{?_smp_mflags}

%install
%suse_update_desktop_file -r org.libelektra.elektra-qt-editor "Settings;DesktopSettings;"
%make_install -C build
# Remove statically linked kdb
#rm $RPM_BUILD_ROOT%{_bindir}/kdb-static
# not known by any package?
rm -r $RPM_BUILD_ROOT%{_datadir}/zsh/vendor-completions/
# add elektra modules paths
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/
echo "%{_libdir}/elektra%{api}" > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/elektra.conf

%post -n lib%{name}%{api}
/sbin/ldconfig
# activate dbus messages on db changes
%{_bindir}/kdb global-mount dbus || :

%postun -n lib%{name}%{api} -p /sbin/ldconfig
%post -n libg%{name}-%{api}.0 -p /sbin/ldconfig
%postun -n libg%{name}-%{api}.0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/kdb
%{_datadir}/bash-completion/completions/*
%if 0%{?suse_version} <= 1320
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d/
%endif
%{_datadir}/fish/vendor_completions.d/*
%doc doc/AUTHORS LICENSE.md README.md doc/INSTALL.md
%dir %{_libdir}/elektra/tool_exec
%{_libdir}/elektra/tool_exec/[b-p,r-z]*

%files -n lib%{name}%{api}
%defattr(-,root,root,-)
%{_libdir}/*elektr*.so.*
%dir %{_libdir}/elektra%{api}
# skip elektra-augeas
%{_libdir}/elektra%{api}/*elektra-[b-z]*.so
%dir %{_datadir}/doc/elektra
%{_datadir}/doc/elektra/*
%config %{_sysconfdir}/ld.so.conf.d/elektra.conf

%if 0%{?use_qt5} > 0
%files -n %{name}-qt-gui
%defattr(-,root,root,-)
%dir %{_libdir}/elektra%{api}
%{_bindir}/elektra-qt-editor
%{_libdir}/elektra/tool_exec/qt-gui
%{_datadir}/app*
%{_datadir}/icons/*
%endif

%if 0%{?use_aug} > 0
%files -n lib%{name}-augeas
%defattr(-,root,root,-)
%{_libdir}/elektra%{api}/libelektra-augeas.so
%endif

%if 0%{?use_glib} > 0
%files -n libg%{name}-%{api}.0
%defattr(-,root,root,-)
%{_libdir}/libgelektra-%{api}.0.so
%endif

%if 0%{?use_swig} > 0
%files -n lib%{name}-lua
%defattr(-,root,root,-)
%{_libdir}/lua/*

%files -n python-%{name}
%defattr(-,root,root,-)
%{_libdir}/python*
%endif

%files -n lib%{name}-devel
%defattr(-,root,root,-)
%{_includedir}/*
%dir %{_libdir}/elektra
%{_libdir}/libelektra*.so
%{_libdir}/pkgconfig/*
%dir %{_libdir}/cmake/elektra
%{_libdir}/cmake/elektra/*.cmake

%files -n lib%{name}-devel-doc
%defattr(-,root,root,-)
%dir %{_datadir}/doc/elektra-doc
%dir %{_datadir}/doc/elektra-doc/html
%{_datadir}/doc/elektra-doc/html/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
