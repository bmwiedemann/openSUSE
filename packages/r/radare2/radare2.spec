#
# spec file for package radare2
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


%global sdb_rev    2.2.4
%global sdb_soname 2_2_4

%global qjs_rev v0.11.0

%global tests_rev 65539cb70eba0901995e04b471975beca0c42c69

Name:           radare2
Version:        6.0.7
Release:        0
Summary:        Reverse Engineering Framework
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Tools/Debuggers
URL:            https://www.radare.org
Source0:        https://github.com/radareorg/radare2/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/radareorg/sdb/archive/%{sdb_rev}/sdb-%{sdb_rev}.tar.gz
Source2:        https://github.com/quickjs-ng/quickjs/archive/%{qjs_rev}/quickjs-%{qjs_rev}.tar.gz
Source3:        https://github.com/radareorg/radare2-testbins/archive/%{tests_rev}/radare2-testbins-%{tests_rev}.tar.gz
Patch0:         pkgconfig.patch
BuildRequires:  chrpath
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Opensource tools to disassemble, debug, analyze and manipulate binary files.

%package devel
Summary:        Devel files for radare2
License:        LGPL-3.0-only
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
Requires:       file-devel
Requires:       pkgconfig(capstone)
Requires:       pkgconfig(liblz4)
Requires:       pkgconfig(libxxhash)
Requires:       pkgconfig(libzip)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)

%description devel
Development files for radare2

%package zsh-completion
Summary:        ZSH completion for %{name}
License:        GPL-3.0-only AND LGPL-3.0-only
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for %{name}.

%package -n libsdb%{sdb_soname}
Summary:        Simple string key/value database
License:        GPL-3.0-only AND LGPL-3.0-only
Provides:       libsdb-%{sdb_soname}

%description -n libsdb%{sdb_soname}
sdb is a simple string key/value database based on djb's cdb disk
storage and supports JSON and arrays introspection.

%ldconfig_scriptlets -n libsdb%{sdb_soname}
%ldconfig_scriptlets -n %name

%prep
%autosetup -p1 -n %{name}-%{version}

# Extract sdb
mkdir -p subprojects/sdb
tar   -C subprojects/sdb --strip-components=1 -x -f %{SOURCE1}

# Extract quickjs
mkdir -p subprojects/qjs
tar   -C subprojects/qjs --strip-components=1 -x -f %{SOURCE2}

mkdir -p test/bins
tar   -C test/bins --strip-components=1 -x -f %{SOURCE3}

%build
%__meson subprojects packagefiles --apply

%meson \
  -Duse_sys_capstone=true \
  -Duse_sys_magic=true \
  -Duse_sys_zip=true \
  -Duse_sys_zlib=true \
  -Duse_sys_lz4=true \
  -Duse_sys_xxhash=true \
  -Duse_sys_openssl=true \
  -Duse_webui=true \
  %{nil}
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_docdir}/radare2
mv %{buildroot}%{_datadir}/doc/radare2/* %{buildroot}%{_docdir}/radare2/

chrpath -d %{buildroot}%{_bindir}/r2sdb

# Conflict with snobol4 package
mv %{buildroot}%{_mandir}/man1/sdb.1 %{buildroot}%{_mandir}/man1/r2sdb.1

%fdupes -s %{buildroot}

%check
# add radare2 to PATH for tests
export PATH="$PWD/%{_vpath_builddir}/binr/radare2:$PATH"
%meson_test

%files devel
%{_libdir}/libr_*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libr
%dir %{_datadir}/radare2/%{version}/charsets
%dir %{_datadir}/radare2/%{version}/fcnsign
%dir %{_datadir}/radare2/%{version}/format
%dir %{_datadir}/radare2/%{version}/opcodes
%dir %{_datadir}/radare2/%{version}/syscall
%{_datadir}/radare2/%{version}/charsets/*
%{_datadir}/radare2/%{version}/fcnsign/*
%{_datadir}/radare2/%{version}/format/*
%{_datadir}/radare2/%{version}/opcodes/*
%{_datadir}/radare2/%{version}/syscall/*

%files
%doc COMMUNITY.md CONTRIBUTING.md DEVELOPERS.md README.md
%license COPYING.md
%{_docdir}/radare2/*
%{_bindir}/*
%{_libdir}/libr_*.so.*

%dir %{_datadir}/radare2
%dir %{_datadir}/radare2/%{version}
%{_datadir}/radare2/%{version}/cons
%{_datadir}/radare2/%{version}/flag
%{_datadir}/radare2/%{version}/hud
%{_datadir}/radare2/%{version}/magic
%{_datadir}/radare2/%{version}/www
%{_datadir}/radare2/%{version}/platform
%{_datadir}/radare2/%{version}/scripts
%{_datadir}/radare2/%{version}/panels

%{_mandir}/man1/*
%{_mandir}/man3/r_*
%{_mandir}/man7/*

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*

%files -n libsdb%{sdb_soname}
%{_libdir}/libsdb.so.*

%changelog
