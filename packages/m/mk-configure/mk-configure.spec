#
# spec file for package mk-configure
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mk-configure
Version:        0.37.0
Release:        0
Summary:        A build system on top of bmake
License:        BSD-2-Clause AND MIT AND ISC
Group:          Development/Tools/Building
Url:            https://github.com/cheusov/mk-configure/
Source:         https://sourceforge.net/projects/mk-configure/files/mk-configure/mk-configure-%{version}/%{name}-%{version}.tar.gz
Source1:        mkcmake.macros
Source9:        mk-configure-rpmlintrc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bmake
BuildRequires:  bmkdep
BuildRequires:  clang
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  groff
BuildRequires:  info
BuildRequires:  lua-devel
BuildRequires:  libbsd-devel
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
Requires:       bmake
Requires:       bmkdep
Recommends:     %{name}-doc
Provides:       %{name}-rpm-macros
BuildArch:      noarch

%description
mk-configure is a collection of include files for bmake (portable version of
NetBSD make) and a number of executables. It is intended to aid cross-platform
development and software building.

%package doc
Summary:        Mk-configure documentation
Group:          Documentation/Other
Requires:       %{name}

%description doc
Mk-configure package: examples and presentation.

%prep
%setup -q

%define env \
        unset MAKEFLAGS \
        export USE_NM=/usr/bin/nm \
        export USE_INSTALL=/usr/bin/install \
        export USE_AWK=/usr/bin/awk \
        export USE_ID=/usr/bin/id \
        export USE_CC_COMPILERS='gcc clang' \
        export USE_CXX_COMPILERS='g++ clang++' \
        export PREFIX=%{_prefix} \
        export SYSCONFDIR=%{_sysconfdir} \
        export MANDIR=%{_mandir}

# examples are built and tested either,
# let's keep a pristine copy
cp -al examples doc

%build
%{env}
bmake all

%install
%{env}
bmake install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/%{name}
# E: wrong-script-interpreter (Badness: 533)
chmod -x examples/*/*.in
chmod -x examples/*/*/*.in
# HACK vs. duplicates after %%doc macro.
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -r examples %{buildroot}%{_docdir}/%{name}-doc
%fdupes -s %{buildroot}%{_docdir}/%{name}-doc
# rpm macros
install -m644 %{SOURCE1} -D %{buildroot}%{_sysconfdir}/rpm/macros.mkcmake

%check
unset MAKEFLAGS
env bmake test
bmake -k cleandir-examples
bmake -k cleandir-tests

%files
%defattr(-,root,root)
%doc README.md doc/FAQ doc/NEWS doc/TODO
%license doc/LICENSE
%{_bindir}/mkc*
%{_datadir}/mk-configure/
%{_mandir}/man1/*
%{_mandir}/man7/*
%config %{_sysconfdir}/rpm/macros.mkcmake
%dir %{_prefix}/libexec
%{_prefix}/libexec/mk-configure

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}-doc/examples
%doc presentation/presentation.pdf

%changelog
