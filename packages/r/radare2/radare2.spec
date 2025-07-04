#
# spec file for package radare2
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


Name:           radare2
Version:        5.9.8
Release:        0
Summary:        Reverse Engineering Framework
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Tools/Debuggers
URL:            https://www.radare.org
Source:         https://github.com/radareorg/radare2/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         https://github.com/radareorg/radare2/commit/c6c772d2eab692ce7ada5a4227afd50c355ad545.patch#/CVE-2025-1378.patch
Patch2:         https://github.com/radareorg/radare2/commit/e64c606b1342a4c0ab2c35ef5146b69667dcd43a.patch#/CVE-2025-1744.patch
Patch3:         https://github.com/radareorg/radare2/commit/db6decd4bc90bb4a492129e70803136fa184f470.patch#/CVE-2025-1864.patch
# From https://github.com/radareorg/radare2/commit/5705d99cc1f23f36f9a84aab26d1724010b97798.patch but needed a rediff
Patch4:         CVE-2025-5641.patch
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
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
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
%fdupes -s %{buildroot}
mkdir -p %{buildroot}/%{_docdir}/radare2
mv %{buildroot}/%{_datadir}/doc/radare2/* %{buildroot}%{_docdir}/radare2/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
%license COPYING COPYING.LESSER
%{_docdir}/radare2/*
%{_bindir}/*
%{_libdir}/libr_*.so.*
%dir %{_datadir}/radare2
%dir %{_datadir}/radare2/%{version}
%dir %{_datadir}/radare2/%{version}/cons
%dir %{_datadir}/radare2/%{version}/flag
%dir %{_datadir}/radare2/%{version}/hud
%dir %{_datadir}/radare2/%{version}/magic
%dir %{_datadir}/radare2/%{version}/www
%dir %{_datadir}/radare2/%{version}/platform
%dir %{_datadir}/radare2/%{version}/scripts
%{_datadir}/radare2/%{version}/cons/*
%{_datadir}/radare2/%{version}/flag/*
%{_datadir}/radare2/%{version}/hud/*
%{_datadir}/radare2/%{version}/magic/*
%{_datadir}/radare2/%{version}/www/*
%{_datadir}/radare2/%{version}/platform/*
%{_datadir}/radare2/%{version}/scripts/*

%{_mandir}/man1/*
%{_mandir}/man7/*

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*

%changelog
