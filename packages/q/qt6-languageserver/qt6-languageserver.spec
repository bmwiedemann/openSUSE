#
# spec file for package qt6-languageserver
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


%define real_version 6.8.1
%define short_version 6.8
%define short_name qtlanguageserver
%define tar_name qtlanguageserver-everywhere-src
%define tar_suffix %{nil}
#
Name:           qt6-languageserver
Version:        6.8.1
Release:        0
Summary:        Implementation of the Language Server Protocol
License:        LGPL-3.0-only OR GPL-2.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  qt6-core-private-devel
BuildRequires:  cmake(Qt6Concurrent) = %{real_version}
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}

%description
Qt Language Server implements the Language Server Protocol specification and
the JsonRpc 2.0 protocol.

### Static libraries ###

%package -n qt6-languageserver-devel-static
Summary:        LSP implementation for Qt6
Provides:       qt6-languageserver-private-devel = %{version}
Obsoletes:      qt6-languageserver-private-devel < %{version}
Requires:       cmake(Qt6JsonRpcPrivate) = %{real_version}
Obsoletes:      libQt6LanguageServer6 < 6.8.1

%description -n qt6-languageserver-devel-static
The Qt 6 LanguageServer library implements the Language Server Protocol (LSP)
specification.
This library does not have any ABI or API guarantees.

%package -n qt6-jsonrpc-devel-static
Summary:        JsonRpc 2.0 protocol implementation
Provides:       qt6-jsonrpc-private-devel = %{version}
Obsoletes:      qt6-jsonrpc-private-devel < %{version}
Obsoletes:      libQt6JsonRpc6 < 6.8.1

%description -n qt6-jsonrpc-devel-static
JsonRpc 2.0 protocol implementation for Qt6.
This library does not have any ABI or API guarantees.

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%cmake_qt6 \
  -DQT_GENERATE_SBOM:BOOL=FALSE

%{qt6_build}

%install
%{qt6_install}

%files -n qt6-languageserver-devel-static
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtLanguageServerTestsConfig.cmake
%{_qt6_cmakedir}/Qt6LanguageServerPrivate/
%{_qt6_descriptionsdir}/LanguageServerPrivate.json
%{_qt6_includedir}/QtLanguageServer/
%{_qt6_libdir}/libQt6LanguageServer.a
%{_qt6_libdir}/libQt6LanguageServer.prl
%{_qt6_metatypesdir}/qt6languageserverprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_languageserver_private.pri

%files -n qt6-jsonrpc-devel-static
%license LICENSES/*
%{_qt6_cmakedir}/Qt6JsonRpcPrivate/
%{_qt6_descriptionsdir}/JsonRpcPrivate.json
%{_qt6_includedir}/QtJsonRpc/
%{_qt6_libdir}/libQt6JsonRpc.a
%{_qt6_libdir}/libQt6JsonRpc.prl
%{_qt6_metatypesdir}/qt6jsonrpcprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_jsonrpc_private.pri

%changelog
