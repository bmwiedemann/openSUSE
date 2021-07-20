#
# spec file for package radare2
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        5.3.1
Release:        0
Summary:        Reverse Engineering Framework
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Tools/Debuggers
URL:            https://www.radare.org
Source:         https://github.com/radareorg/radare2/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(libewf)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Opensource tools to disassemble, debug, analyze and manipulate binary files.

%package devel
Summary:        Devel files for radare2
License:        LGPL-3.0
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
Requires:       file-devel
Requires:       pkgconfig(capstone)
Requires:       pkgconfig(libxxhash)
Requires:       pkgconfig(libzip)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)

%description devel
Development files for radare2

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS="%{optflags}"
%configure \
  --docdir=%{_docdir}/%{name} \
  --with-syscapstone \
  --with-sysmagic \
  --with-syszip \
  --with-sysxxhash \
  --with-openssl
%make_build

%install
%make_install
# rename r2p as r2pipe, r2p conflicts with polylib
# name must match strstr("r2p"), as it's a multicall binary
mv %{buildroot}/%{_bindir}/{r2p,r2pipe}
%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files devel
%{_libdir}/libr_*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libr

%files
%doc COMMUNITY.md CONTRIBUTING.md DEVELOPERS.md README.md
%license COPYING COPYING.LESSER
%doc %{_docdir}/%{name}/*
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/libr_*.so.*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
