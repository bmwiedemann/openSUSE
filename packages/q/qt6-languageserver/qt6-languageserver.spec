#
# spec file for package qt6-languageserver
#
# Copyright (c) 2022 SUSE LLC
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


%define real_version 6.4.1
%define short_version 6.4
%define short_name qtlanguageserver
%define tar_name qtlanguageserver-everywhere-src
%define tar_suffix %{nil}
#
Name:           qt6-languageserver
Version:        6.4.1
Release:        0
Summary:        Implementation of the Language Server Protocol
License:        LGPL-3.0-only OR GPL-2.0-or-later
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)

%description
Qt Language Server implements the Language Server Protocol specification and
the JsonRpc 2.0 protocol.

### Private only library ###

%package -n libQt6LanguageServer6
Summary:        LSP implementation for Qt6

%description -n libQt6LanguageServer6
The Qt 6 LanguageServer library implements the Language Server Protocol (LSP)
specification.

%package private-devel
Summary:        Qt 6 LanguageServer library - Development files
Requires:       libQt6LanguageServer6 = %{version}
Requires:       qt6-core-private-devel = %{version}
Requires:       qt6-jsonrpc-private-devel = %{version}

%description private-devel
Development files for the Qt 6 LanguageServer private library.
This library does not have any ABI or API guarantees.

%package -n libQt6JsonRpc6
Summary:        JsonRpc 2.0 protocol implementation

%description -n libQt6JsonRpc6
JsonRpc 2.0 protocol implementation for Qt6.

%package -n qt6-jsonrpc-private-devel
Summary:        Qt 6 JsonRpc library - Development files
Requires:       libQt6JsonRpc6 = %{version}
Requires:       cmake(Qt6Core)

%description -n qt6-jsonrpc-private-devel
Development files for the Qt 6 JsonRpc library.
This library does not have any ABI or API guarantees.

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%post -n libQt6JsonRpc6 -p /sbin/ldconfig
%post -n libQt6LanguageServer6 -p /sbin/ldconfig
%postun -n libQt6JsonRpc6 -p /sbin/ldconfig
%postun -n libQt6LanguageServer6 -p /sbin/ldconfig

%files -n libQt6LanguageServer6
%{_qt6_libdir}/libQt6LanguageServer.so.*

%files private-devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtLanguageServerTestsConfig.cmake
%{_qt6_cmakedir}/Qt6LanguageServerPrivate/
%{_qt6_descriptionsdir}/LanguageServerPrivate.json
%{_qt6_includedir}/QtLanguageServer/
%{_qt6_libdir}/libQt6LanguageServer.prl
%{_qt6_libdir}/libQt6LanguageServer.so
%{_qt6_metatypesdir}/qt6languageserverprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_languageserver_private.pri

%files -n libQt6JsonRpc6
%license LICENSES/*
%{_qt6_libdir}/libQt6JsonRpc.so.*

%files -n qt6-jsonrpc-private-devel
%{_qt6_cmakedir}/Qt6JsonRpcPrivate/
%{_qt6_descriptionsdir}/JsonRpcPrivate.json
%{_qt6_includedir}/QtJsonRpc/
%{_qt6_libdir}/libQt6JsonRpc.prl
%{_qt6_libdir}/libQt6JsonRpc.so
%{_qt6_metatypesdir}/qt6jsonrpcprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_jsonrpc_private.pri

%changelog
