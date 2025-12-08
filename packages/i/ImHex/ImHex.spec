#
# spec file for package ImHex
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define sover 1_38_0
Name:           ImHex
Version:        1.38.0
Release:        0
Summary:        A Hex Editor for Reverse Engineers, Programmers
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://imhex.werwolv.net/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/WerWolv/ImHex-Patterns/archive/refs/heads/master.zip#/ImHex-Patterns-master.zip
Source99:       %{name}-rpmlintrc
# Patch to workaround libLLVMDemangle.so() not found which may be a SUSE issue
Patch0:         ImHex-llvm_demangler-linking.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  file-devel >= 5.39
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  llvm-devel
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl) >= 7.76.1
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nlohmann_json) >= 3.10.2
BuildRequires:  pkgconfig(yara)
### bundled stuff
# needs capstone 5.x
Provides:       bundled(capstone) = 5.0.0-rc2
Provides:       bundled(gnulib)
Provides:       bundled(imgui)
Provides:       bundled(intervaltree)
Provides:       bundled(libpl)
Provides:       bundled(libromfs)
Provides:       bundled(microtar)
%if 0%{?suse_version} > 1600
BuildRequires:  fmt-10-devel
%else
BuildRequires:  pkgconfig(fmt)
%endif

%description
A hex editor with a custom C++-like pattern language for parsing and highlighting a file's content,
data import and export, string search, file hashing, disassembler support, bookmarks, data analyzers,
demanglers, color picker, regex replacer, calculator, built-in cheat sheets and eye friendly UI.

%package -n libimhex%{sover}
Summary:        Shared library for ImHex
Group:          System/Libraries

%description -n libimhex%{sover}
libimhex is a C++ library library providing functions needed for ImHex.

%package devel
Summary:        Development files for ImHex
Group:          Development/Libraries/C and C++
Requires:       libimhex%{sover} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that want to make use of ImHex.

%prep
%setup -q
%autopatch -p1
# Clean bundled libs
rm -Rv lib/third_party/{fmt,llvm-demangle,yara}
# ImHex Patterns
unzip %{SOURCE1} && mv ImHex-Patterns-master/ ImHex-Patterns

%build
echo %{version} > VERSION
%cmake \
  -DIMHEX_OFFLINE_BUILD=ON \
  -DUSE_SYSTEM_NLOHMANN_JSON=ON \
  -DUSE_SYSTEM_CURL=ON \
  -DUSE_SYSTEM_FMT=ON \
  -DUSE_SYSTEM_CAPSTONE=OFF \
  -DUSE_SYSTEM_YARA=ON \
  -DUSE_SYSTEM_LLVM=ON
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/imhex

%ldconfig_scriptlets -n libimhex%{sover}

%files
%doc README.md
%license LICENSE
%exclude %{_datadir}/licenses/imhex/LICENSE
%{_bindir}/imhex
%exclude %{_bindir}/imhex-updater
%dir %{_libdir}/imhex
%dir %{_libdir}/imhex/plugins
%{_libdir}/imhex/plugins/builtin.hexplug
%{_libdir}/imhex/plugins/decompress.hexplug
%{_libdir}/imhex/plugins/diffing.hexplug
%{_libdir}/imhex/plugins/disassembler.hexplug
%{_libdir}/imhex/plugins/fonts.hexpluglib
%{_libdir}/imhex/plugins/hashes.hexplug
%{_libdir}/imhex/plugins/remote.hexplug
%{_libdir}/imhex/plugins/script_loader.hexplug
%{_libdir}/imhex/plugins/ui.hexpluglib
%{_libdir}/imhex/plugins/visualizers.hexplug
%{_libdir}/imhex/plugins/yara_rules.hexplug
%{_datadir}/imhex
%exclude %{_datadir}/imhex/sdk
%{_datadir}/metainfo/net.werwolv.ImHex.metainfo.xml
%{_datadir}/mime/packages/imhex.xml
%{_datadir}/pixmaps/imhex.svg
%{_datadir}/applications/imhex.desktop

%files -n libimhex%{sover}
%{_libdir}/libimhex.so.%{version}

%files devel
%{_libdir}/libimhex.so
%dir %{_datadir}/imhex
%{_datadir}/imhex/sdk

%changelog
