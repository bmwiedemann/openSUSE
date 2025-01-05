#
# spec file for package rizin
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rizin
Version:        0.7.4
Release:        0
Summary:        UNIX-like reverse engineering framework and command-line tool-set
URL:            https://github.com/rizinorg/rizin/
Source0:        https://github.com/rizinorg/rizin/releases/download/v%{version}/%{name}-src-v%{version}.tar.xz
License:        GPL-3.0-or-later OR LGPL-3.0-or-later
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson >= 0.55.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-PyYAML
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libmspack)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tree-sitter)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-common = %{version}

%description
Rizin is a free and open-source Reverse Engineering framework, providing a
complete binary analysis experience with features like Disassembler,
Hexadecimal editor, Emulation, Binary inspection, Debugger, and more.

Rizin is a fork of radare2 with a focus on usability, working features and code
cleanliness.

%package devel
Summary:        Development files for the rizin package
Requires:       %{name} = %{version}
Requires:       file-devel
Requires:       openssl-devel

%description devel
Development files for the rizin package. See rizin package for more
information.

%package common
Summary:        Arch-independent SDB files for the rizin package
BuildArch:      noarch
Requires:       %{name} = %{version}

%description common
Arch-independent SDB files used by rizin package. See rizin package for more
information

%prep
%setup -q -n %{name}-v%{version}

%build
# Whereever possible use the system-wide libraries instead of bundles
%meson \
    -Duse_sys_magic=enabled \
    -Duse_sys_libzip=enabled \
    -Duse_sys_zlib=enabled \
    -Duse_sys_lz4=enabled \
    -Duse_sys_xxhash=enabled \
    -Duse_sys_openssl=enabled \
    -Duse_sys_capstone=enabled \
    -Duse_sys_tree_sitter=enabled \
    -Duse_sys_lzma=enabled \
    -Duse_sys_libmspack=enabled \
    -Duse_sys_libzstd=enabled \
    -Duse_sys_pcre2=enabled \
%ifarch s390x
    -Ddebugger=false \
%endif
    -Denable_tests=false \
    -Denable_rz_test=false \
    -Dlocal=disabled \
    -Dpackager="openSUSE" \
    -Dpackager_version="%{version}"
%meson_build

%install
%meson_install

# Create directories for plugins and bindings
install -d %{buildroot}%{_libdir}/%{name}/plugins
install -d %{buildroot}%{_libdir}/rizin-bindings

%ldconfig_scriptlets

%check
# Do not run the unit testsuite yet - it pulls another big repository
# https://github.com/rizinorg/rizin-testbins from github

%files
%doc README.md
%license COPYING COPYING.LESSER
%{_bindir}/r*
%{_libdir}/librz_*.so.*
%{_mandir}/man?/*%{ext_man}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/rizin-bindings

%files devel
%{_includedir}/librz
%{_libdir}/librz*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/*
%{_libdir}/cmake/*/*.cmake

%files common
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/asm
%{_datadir}/%{name}/cons
%{_datadir}/%{name}/flag
%{_datadir}/%{name}/format
%{_datadir}/%{name}/fortunes
%{_datadir}/%{name}/hud
%{_datadir}/%{name}/magic
%{_datadir}/%{name}/opcodes
%{_datadir}/%{name}/reg
%{_datadir}/%{name}/syscall
%{_datadir}/%{name}/types

%changelog
