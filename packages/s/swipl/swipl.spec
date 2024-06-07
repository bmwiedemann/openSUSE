#
# spec file for package swipl
#
# Copyright (c) 2023 SUSE LLC
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


Name:           swipl
Version:        9.3.7
Release:        0
Summary:        Prolog Compiler
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.swi-prolog.org
Source0:        https://www.swi-prolog.org/download/devel/src/swipl-%{version}.tar.gz
Source98:       swipl-rpmlintrc
# For SOURCE_DATE_EPOCH variable- reproducible builds
Source99:       %{name}.changes
BuildRequires:  cmake
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperftools-devel
BuildRequires:  java-devel >= 1.8.0
# For %%check
BuildRequires:  junit
BuildRequires:  libarchive-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libunwind-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw6)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(yaml-0.1)
Provides:       swi-prolog = %{version}
Provides:       swi_pl = %{version}
Obsoletes:      swi-prolog < %{version}
Obsoletes:      swi_pl < %{version}
# Builds on i586 don't seem to work (gh#SWI-Prolog/swipl-devel#1139)
ExcludeArch:    %ix86

#  jpackage-utils

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage collector, stack expandor, C interface, GNU readline and GNU
Emacs interface, a very fast compiler,and an X11 interface using XPCE.

%prep
%autosetup -p1

sed -i -e "s|#!%{_bindir}/env swipl|#!%{_bindir}/swipl|" \
    packages/protobufs/bootstrap/protoc-gen-swipl

%build
export SOURCE_DATE_EPOCH="$(sed -n '/^----/n;s/ - .*$//;p;q' %{SOURCE99} | date -u -f - +%%s)"
%define __builder ninja
%cmake
%cmake_build

%install
%cmake_install

# # Fix script
# chmod +x %%{buildroot}%%{_libdir}/swipl-%%{version}/library/dialect/sicstus/swipl-lfr.pl
# sed -i "s@%%{_bindir}/../swipl.sh@%%{_bindir}/swipl@" %%{buildroot}%%{_docdir}/%%{name}-%%{version}/packages/examples/pldoc/man_server.pl

# Create common symlink for "pl"
ln -s swipl %{buildroot}%{_bindir}/pl

# Move *.pc file to correct location
install -D -m 0644 %{buildroot}%{_datadir}/pkgconfig/swipl.pc \
    %{buildroot}%{_libdir}/pkgconfig/swipl.pc
rm -v %{buildroot}%{_datadir}/pkgconfig/swipl.pc
rmdir -v %{buildroot}%{_datadir}/pkgconfig

%fdupes %{buildroot}/%{_libdir}/%{name}*
%fdupes %{buildroot}/%{_prefix}/lib/%{name}*
%fdupes %{buildroot}/%{_docdir}/%{name}-%{version}

%check
export LANG="C.utf8"
CTEST_OPT_ARGS=""
# gh#SWI-Prolog/swipl-devel#1139
%ifarch %ix86
CTEST_OPT_ARGS+=" --exclude-regex 'swipl:transaction'"
%endif
%ctest --verbose $CTEST_OPT_ARGS

%files
%license LICENSE README.md
%{_bindir}/pl
%{_bindir}/swipl
%{_bindir}/swipl-ld
# %%{_bindir}/swipl-rc
%{_prefix}/lib/swipl
%dir %{_prefix}/lib/cmake
%{_prefix}/lib/cmake/swipl
# %%{_bindir}/xpce-client
# %%{_libdir}/%%{name}-%%{version}
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/swipl-ld.1%{?ext_man}
# %%{_mandir}/man1/swipl-rc.1%%{?ext_man}
%{_mandir}/man1/swipl.1%{?ext_man}
# %%{_mandir}/man1/xpce-client.1%%{?ext_man}

%changelog
