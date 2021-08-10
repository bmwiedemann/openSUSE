#
# spec file for package elektra
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


Version:        0.8.26
Release:        0
%define tempdocdir %{_prefix}/elektra
%define __libtoolize    /bin/true
%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

%bcond_without augeas
%bcond_without qt5
%bcond_with glib2
%bcond_with swig
%bcond_with java

Name:           elektra
Source:         http://www.libelektra.org/ftp/elektra/releases/%{name}-%{version}.tar.gz
URL:            http://www.libelektra.org
%define api     4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source1:        elektra-rpmlintrc
# PATCH-FIX-UPSTREAM
Patch0:         0001-kdb-add-missing-limits-include.patch
Patch1:         fix-gtest-linkage.patch
BuildRequires:  boost-devel
BuildRequires:  byacc
BuildRequires:  cmake
BuildRequires:  db-devel
BuildRequires:  discount
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  systemd-logger
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(yajl)
%if %{with augeas}
BuildRequires:  augeas-devel
%endif
%if %{with glib2}
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
%endif
%if %{with qt5}
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
%endif
%if %{with swig}
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(lua5.3)
%endif
%if %{with java}
BuildRequires:  java-1.8.0-devel
%endif

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

%package -n libg%{name}-%{api}_0
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

%description -n libg%{name}-%{api}_0
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
%autosetup -p1

%build
%define _lto_cflags %{nil}
export SUSE_ASNEEDED=0
%cmake -DTARGET_PLUGIN_FOLDER="elektra%{api}" \
  -DPLUGINS="ALL" \
  -DTOOLS="ALL" \
  -DENABLE_TESTING="OFF" \
  -DBUILD_TESTING="ON" \
  -DTARGET_DOCUMENTATION_HTML_FOLDER="share/doc/elektra-doc/html" \
  -DBUILD_DOCUMENTATION=ON \
  -DTARGET_CMAKE_FOLDER=%{_lib}/cmake/elektra \
  -DCMAKE_C_FLAGS="-fPIC $CFLAGS" \
  -DCMAKE_CXX_FLAGS="-fPIC $CXXFLAGS" \
  -DCMAKE_EXE_LINKER_FLAGS="-pie -Wl,--allow-multiple-definition" \
%if %{with swig}
  -DBINDINGS="MAINTAINED;swig_lua;swig_python" \
  -DPYTHON_EXECUTABLE:PATH="%{_bindir}/python3" \
  -DPYTHON_LIBRARY:FILEPATH="%{_libdir}/libpython3.so" \
  -DPYTHON_INCLUDE_DIR:PATH="$(python3  -c 'from distutils.sysconfig import get_python_inc; print(get_python_inc())')" \
%else
  -DBINDINGS="MAINTAINED" \
%endif

# doxygen appears to have problems with multi level directory creation on elder distros
mkdir -p doc/html doc/man
make %{?_smp_mflags}

%install
%suse_update_desktop_file -r org.libelektra.elektra-qt-editor "Settings;DesktopSettings;"
%make_install -C build
# not known by any package?
rm -r %{buildroot}%{_datadir}/zsh/vendor-completions/
# TODO: do we want to package test data?
rm -rf %{buildroot}%{_datadir}/elektra/test_data/
rm -rf %{buildroot}%{_libdir}/elektra/tool_exec/{race,test}*

# add elektra modules paths
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo "%{_libdir}/elektra%{api}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/elektra.conf
%fdupes %{buildroot}/%{_datadir}/doc/elektra-doc/
# cleanup hash bangs
for f in benchmark-createtree check-env-dep configure-firefox convert-hosts elektra-merge \
	 elektra-mount elektra-umount ffconfig/setupConfig ffconfig/setupHomepage ffconfig/setupProxy \
	 install-sh-completion; do
    sed -ri '1 s|/usr/bin/env\ (.*)|/usr/bin/\1|' %{buildroot}/%{_libdir}/elektra/tool_exec/$f
done
sed -ri '1 s|/usr/bin/env python$|/usr/bin/python3|' %{buildroot}/%{_libdir}/elektra/tool_exec/find-tools
sed -i '1d' %{buildroot}%{_datadir}/{bash-completion/completions/kdb,fish/vendor_completions.d/kdb.fish}

%post -n lib%{name}%{api}
/sbin/ldconfig
# activate dbus messages on db changes
%{_bindir}/kdb global-mount dbus || :

%postun -n lib%{name}%{api} -p /sbin/ldconfig

%post -n libg%{name}-%{api}_0 -p /sbin/ldconfig
%postun -n libg%{name}-%{api}_0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/kdb
%{_datadir}/bash-completion/completions/*
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

%if %{with qt5}
%files -n %{name}-qt-gui
%defattr(-,root,root,-)
%dir %{_libdir}/elektra%{api}
%{_bindir}/elektra-qt-editor
%{_libdir}/elektra/tool_exec/qt-gui
%{_datadir}/app*
%{_datadir}/icons/*
%endif

%if %{with augeas}
%files -n lib%{name}-augeas
%defattr(-,root,root,-)
%{_libdir}/elektra%{api}/libelektra-augeas.so
%endif

%if %{with glib2}
%files -n libg%{name}-%{api}_0
%defattr(-,root,root,-)
%{_libdir}/libgelektra-%{api}.0.so
%endif

%if %{with swig}
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
