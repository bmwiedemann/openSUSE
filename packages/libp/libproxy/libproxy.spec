#
# spec file for package libproxy
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


%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == ""
%define build_core_not_modules 1
%else
%define name_suffix %{flavor}
%define dash -
%define build_core_not_modules 0
%endif
%define         build_mozjs 0
%if 0%{?suse_version}
%bcond_without mono
%else
%bcond_with mono
%endif
%define _name   libproxy
%if 0%{?build_snapshot}
%define _sourcename %{_name}
%else
%define _sourcename %{_name}-%{version}
%endif
%bcond_without python2
%{!?_assemblies_dir: %global _assemblies_dir %(pkg-config cecil --variable=assemblies_dir)}
Name:           libproxy%{?dash}%{?name_suffix}
Version:        0.4.15
Release:        0
Summary:        Automatic proxy configuration management for applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libproxy.github.io/libproxy/
Source:         https://github.com/libproxy/%{_name}/archive/%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM libproxy-python3.7.patch dimstar@opensuse.org -- Add support for python 3.7 and 3.8, taken from upstream
Patch0:         libproxy-python3.7.patch
# PATCH-FIX-UPSTREAM libproxy-pxgsettings.patch dimstar@opensuse.org -- pxgsettings: use the correct syntax to connect to the changed signal
Patch1:         libproxy-pxgsettings.patch
# PATCH-FIX-UPSTREAM libproxy-CVE-2020-25219.patch boo#1176410 mgorse@suse.com -- Rewrite url::recvline to be nonrecursive.
Patch2:         libproxy-CVE-2020-25219.patch
# PATCH-FIX-UPSTREAM libproxy-fix-pac-buffer-overflow.patch boo#1177143 mgorse@suse.com -- fix buffer overflow when PAC is enabled.
Patch3:         libproxy-fix-pac-buffer-overflow.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libmodman-devel
# netcfg is needed for the test suite.
BuildRequires:  netcfg
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if !%{build_core_not_modules}
%if ! 0%{?windows}
BuildRequires:  NetworkManager-devel
BuildRequires:  dbus-1-devel
BuildRequires:  gconf2-devel
# For directory ownership, but also because we want to rebuild the modules if
# the library changed
BuildRequires:  libproxy1 = %{version}
BuildRequires:  perl
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
%if %{with python2}
BuildRequires:  python-devel
%endif
BuildRequires:  pkgconfig(gio-2.0) >= 2.26
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(javascriptcoregtk-4.0)
%if 0%{?sle_version} > 150200 || 0%{?is_opensuse}
BuildRequires:  libKF5ConfigCore5
%endif
%if %{build_mozjs}
BuildRequires:  pkgconfig(mozjs-38)
%endif
%if %{with mono}
BuildRequires:  mono-devel
%endif
%endif
%endif

%description
libproxy is a library that provides automatic proxy configuration
management.

%if %build_core_not_modules
%package tools
Summary:        An example application using libproxy
Group:          System/Libraries
Requires:       libproxy1 = %{version}

%description tools
An example application that will use libproxy to give the results that can
be expected from other applications. It can be used to debug what would
happen in various cases.

%package devel
Summary:        Development files for libproxy, a library to do PAC/WPAD
Group:          Development/Libraries/C and C++
Requires:       libproxy1 = %{version}

%description devel
libproxy is a library that provides automatic proxy configuration
management.

This subpackage contains header files for developing applications
that want to make use of libproxy.

%package -n libproxy1
Summary:        Automatic proxy configuration management for applications
Group:          System/Libraries
%if !%{build_mozjs}
Obsoletes:      libproxy1-pacrunner-mozjs <= %{version}
%endif

%description -n libproxy1
libproxy is a library that provides automatic proxy configuration
management.

Proxy autoconfiguration (PAC) requires JavaScript (which most
applications do not have), and determing the PAC script location
requires a WPAD protocol implementation, which complicate proxy
support. libproxy exists to abstract this issue and provides
an answer how to reach a certain network resource.

%else
%package -n libproxy1-config-gnome3
Summary:        Libproxy module for GNOME3 configuration
Group:          System/Libraries
Requires:       libproxy1 = %{version}
Provides:       libproxy-gnome = %{version}
Obsoletes:      libproxy-gnome < %{version}
%if 0%{?suse_version}
Recommends:     libproxy1-pacrunner = %{version}
Supplements:    packageand(libproxy1:gnome-session-core)
%else
Requires:       libproxy1-pacrunner = %{version}
%endif

%description -n libproxy1-config-gnome3

A module to extend libproxy with capabilities to query GNOME about
proxy settings.

%package -n libproxy1-config-kde
Summary:        Libproxy module for KDE configuration
# We don't really need the library, but this package brings kreadconfig5
Group:          System/Libraries
Requires:       libKF5ConfigCore5
Requires:       libproxy1 = %{version}
Provides:       libproxy-kde = %{version}
Obsoletes:      libproxy-kde < %{version}
# A generic KDE config loader was introduced in 0.4.12
Obsoletes:      libproxy1-config-kde4 < 0.4.12
# The kde plugin requires 'qtpaths', which is part of libqt5-qtpaths in TW / libqt5-qttools in older releases
%if %{?suse_version} > 1320
Requires:       libqt5-qtpaths
%else
Requires:       libqt5-qttools
%endif
%if 0%{?suse_version}
Recommends:     libproxy1-pacrunner = %{version}
Supplements:    packageand(libproxy1:libkde4)
Supplements:    packageand(libproxy1:plasma5-session)
%else
Requires:       libproxy1-pacrunner = %{version}
%endif

%description -n libproxy1-config-kde
A module to extend libproxy with capabilities to query KDE4 about proxy
settings.

%package -n libproxy1-pacrunner-mozjs
Summary:        Libproxy module to support WPAD/PAC parsing via the Mozilla JavaScript Engine
Group:          System/Libraries
Requires:       libproxy1 = %{version}
# A virtual symbol to identify that this is a pacrunner.
Provides:       libproxy1-pacrunner = %{version}
%if 0%{?suse_version}
Supplements:    packageand(libproxy1:libmozjs185-1_0)
%endif

%description -n libproxy1-pacrunner-mozjs
A module to extend libproxy with capabilities to pass addresses to a
WPAD/PAC script and have it find the correct proxy.

%package -n libproxy1-pacrunner-webkit
Summary:        Libproxy module to support WPAD/PAC parsing via the WebKit JavaScript Engine
Group:          System/Libraries
Requires:       libproxy1 = %{version}
# A virtual symbol to identify that this is a pacrunner.
Provides:       libproxy1-pacrunner = %{version}
%if 0%{?suse_version}
Supplements:    packageand(libproxy1:libjavascriptcoregtk-3_0-0)
%endif

%description -n libproxy1-pacrunner-webkit
A module to extend libproxy with capabilities to pass addresses to a
WPAD/PAC script and have it find the correct proxy.

%package -n libproxy1-networkmanager
Summary:        Libproxy module for NetworkManager configuration
Group:          System/Libraries
Requires:       libproxy1 = %{version}
%if 0%{?suse_version}
Supplements:    packageand(libproxy1:NetworkManager)
%endif

%description -n libproxy1-networkmanager
A module to extend libproxy with capabilities to query NetworkManager
about network configuration changes.

%package -n python3-libproxy
Summary:        Python3 bindings for libproxy
Group:          Development/Languages/Python
Requires:       libproxy1 = %{version}
BuildArch:      noarch

%description -n python3-libproxy
libproxy is a library that provides automatic proxy configuration
management.

This package contains the Python 3 bindings for libproxy.

%package -n python-libproxy
Summary:        Python bindings for libproxy
Group:          Development/Languages/Python
Requires:       libproxy1 = %{version}
BuildArch:      noarch

%description -n python-libproxy
libproxy is a library that provides automatic proxy configuration
management.

This package contains the Python 2 bindings for libproxy.

%package -n perl-Net-Libproxy
Summary:        Perl bindings for libproxy
Group:          Development/Languages/Perl
Requires:       libproxy1 = %{version}
%if 0%{?perl_requires:1}
%{perl_requires}
%else
# For Fedora at least perl = perl_version does not work.
Requires:       perl >= %{perl_version}
%endif

%description -n perl-Net-Libproxy
libproxy is a library that provides automatic proxy configuration
management.

This package contains the Perl for libproxy.

%package -n libproxy-sharp
Summary:        .Net bindings for libproxy
Group:          Development/Languages/Mono
Requires:       libproxy1 = %{version}

%description -n libproxy-sharp
libproxy is a library that provides automatic proxy configuration
management.

This package contains the Mono/.NET for libproxy.

%endif # build_core_not_modules

%prep
%setup -q -n %{_sourcename}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
mkdir build

%build
cd build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"
%if 0%{?windows}
export CXXFLAGS="%{optflags} -fno-stack-protector -static-libgcc"
%endif
cmake \
%if 0%{?windows}
  -DCMAKE_TOOLCHAIN_FILE=../cmake/mingw32.cmake \
  -DBUILD_TESTING=False \
  -DWITH_DOTNET=OFF \
%else
  -DWITH_VALA=yes \
%if %{with mono}
  -DWITH_DOTNET=1 \
%endif
  -DFORCE_SYSTEM_LIBMODMAN=ON \
%endif
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DBIN_INSTALL_DIR=%{_bindir} \
  -DLIB_INSTALL_DIR=%{_libdir} \
  -DMODULE_INSTALL_DIR=%{_libdir}/libproxy-%{version}/modules \
  -DLIBEXEC_INSTALL_DIR=%{_libexecdir}/libproxy-%{version} \
  -DPYTHON_SITEPKG_DIR=%{python_sitelib} \
  -DSHARE_INSTALL_PREFIX=%{_datadir} \
  -DINCLUDE_INSTALL_DIR=%{_includedir} \
  -DPERL_VENDORINSTALL=yes \
  -DBIPR=0 \
%if %build_core_not_modules
  -DWITH_DOTNET=OFF \
  -DWITH_PERL=OFF \
  -DWITH_PYTHON2=OFF \
  -DWITH_PYTHON3=OFF \
%endif
%if %build_core_not_modules || (! 0%{?is_opensuse} && 0%{?sle_version} <= 150200)
  -DWITH_KDE=OFF \
%endif
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_CONFIG_NAME=RelWithDebInfo \
  -DWITH_WEBKIT3=ON \
  -DWITH_GNOME3=ON \
..
make VERBOSE=1

%install
cd build
make DESTDIR=%{buildroot} install

# On Windows we also do not want to provide the static libraries.
%if 0%{?windows}
find %{buildroot}%{_libdir} -name '*.dll.a' -delete -print
rm %{buildroot}%{_libdir}/libmodman.dll
%endif

%if %build_core_not_modules
# Build the basic directory structure for the modules so we can
# own the directories in the main library package
install -d %{buildroot}%{_libexecdir}/libproxy-%{version}
install -d %{buildroot}%{_libdir}/%{name}-%{version}/modules
%else
# remove files that are part of the core
rm -f %{buildroot}%{_includedir}/*.h
# Delete all files that exist in the base libproxy package
rm -f %{buildroot}%{_bindir}/proxy%{?windows:.exe}
rm -f %{buildroot}%{_libdir}/libproxy.*
rm -f %{buildroot}%{_libdir}/pkgconfig/libproxy-1.0.pc
rm -f %{buildroot}%{_datadir}/cmake/Modules/Findlibproxy.cmake
rm -f %{buildroot}%{_datadir}/vala/vapi/libproxy-1.0.vapi
%endif

%check
cd build
make test

%if %build_core_not_modules
%post -n libproxy1 -p /sbin/ldconfig

%postun -n libproxy1 -p /sbin/ldconfig

%files tools
%defattr(-, root, root)
%{_bindir}/proxy%{?windows:.exe}

%files -n libproxy1
%defattr(-, root, root)
%license COPYING
%doc README AUTHORS
%if ! 0%{?windows}
%{_libdir}/libproxy.so.*
%else
%{_libdir}/libproxy.dll
%endif
%dir %{_libexecdir}/libproxy-%{version}
%dir %{_libdir}/libproxy-%{version}
%dir %{_libdir}/libproxy-%{version}/modules

%files devel
%defattr(-, root, root)
%{_includedir}/*.h
%if ! 0%{?windows}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libproxy-1.0.pc
%{_datadir}/cmake/Modules/Findlibproxy.cmake
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libproxy-1.0.vapi
%endif

%else
%if ! 0%{?windows}
%if 0%{?sle_version} > 150200 || 0%{?is_opensuse}
%files -n libproxy1-config-kde
%defattr(-, root, root)
%{_libdir}/libproxy-%{version}/modules/config_kde.so
%endif

%files -n libproxy1-config-gnome3
%defattr(-, root, root)
%{_libdir}/libproxy-%{version}/modules/config_gnome3.so
%{_libexecdir}/libproxy-%{version}/pxgsettings

%files -n libproxy1-networkmanager
%defattr(-, root, root)
%{_libdir}/libproxy-%{version}/modules/network_networkmanager.so

%files -n libproxy1-pacrunner-webkit
%defattr(-, root, root)
%{_libdir}/libproxy-%{version}/modules/pacrunner_webkit.so

%if %{build_mozjs}
%files -n libproxy1-pacrunner-mozjs
%defattr(-, root, root)
%{_libdir}/libproxy-%{version}/modules/pacrunner_mozjs.so
%endif

%if %{with python2}
%files -n python-libproxy
%defattr(-, root, root)
%{python_sitelib}/*.py
%endif

%files -n python3-libproxy
%defattr(-, root, root)
%{python3_sitelib}/*.py

%files -n perl-Net-Libproxy
%defattr(-,root,root)
%dir %{perl_vendorarch}/Net
%dir %{perl_vendorarch}/auto/Net
%dir %{perl_vendorarch}/auto/Net/Libproxy
%{perl_vendorarch}/Net/Libproxy.pm
%{perl_vendorarch}/auto/Net/Libproxy/Libproxy.so

%if %{with mono}
%files -n libproxy-sharp
%defattr(-, root, root)
%{_assemblies_dir}/gac/libproxy-sharp
%{_assemblies_dir}/libproxy-sharp
%{_libdir}/pkgconfig/libproxy-sharp-1.0.pc
%endif
%endif
%endif

%changelog
