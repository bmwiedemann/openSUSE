#
# spec file for package augeas
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


Name:           augeas
Version:        1.13.0
Release:        0
Summary:        An utility for changing configuration files
License:        LGPL-2.1-or-later
URL:            https://augeas.net/
Source0:        https://github.com/hercules-team/augeas/releases/download/release-%{version}/%{name}-%{version}.tar.gz
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch0:         augeas-modprobe-lense.patch
# from https://patch-diff.githubusercontent.com/raw/hercules-team/augeas/pull/755.patch
Patch1:         sysctl_parsing.patch
Patch2:         augeas-1.13.0-replace_security_context_t-patch
Patch3:         gcc9-disable-broken-test.patch
BuildRequires:  glibc-locale
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libxml-2.0)

%description
An utility for programmatically editing configuration files. Augeas
parses configuration files into a tree structure.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.

%package        devel
Summary:        A library for changing configuration files
Requires:       libaugeas0 = %{version}
Requires:       libfa1 = %{version}

%description    devel
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.

%package -n libaugeas0
Summary:        A library for changing configuration files
Recommends:     %{name}-lenses = %{version}

%description -n libaugeas0
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.

%package -n libfa1
Summary:        Finite automaton library for Augeas

%description -n libfa1
Component library for the Augeas configuration parser.

%package        lenses
Summary:        Official set of lenses for use by libaugeas
Requires:       libaugeas0 = %{version}

%description    lenses
Augeas parses configuration files described in lenses into a tree
structure, which it exposes through its public API. Lenses are the
building blocks of the file <-> tree transformation. The transformation
is controlled by ``lens'' definitions that describe the file format and
mapping of its contents into a tree. This package includes the official
set of lenses.

%package        lense-tests
Summary:        Set of tests for official Augeas lenses
Requires:       %{name}-lenses = %{version}

%description    lense-tests
Set of tests for official Augeas lenses. These can be used when
modifying the official lenses, or when creating new ones.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--disable-silent-rules \
	--disable-rpath
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# move vim files to the right location
mv %{buildroot}/%{_datadir}/vim/vimfiles %{buildroot}/%{_datadir}/vim/site

%check
# This causes a >20x slowdown otherwise (boo#1201884)
unset MALLOC_PERTURB_
%make_build check

%post   -n libaugeas0 -p /sbin/ldconfig
%postun -n libaugeas0 -p /sbin/ldconfig
%post   -n libfa1 -p /sbin/ldconfig
%postun -n libfa1 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/augmatch
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%{_mandir}/man1/*

%files -n libaugeas0
%{_libdir}/libaugeas.so.*

%files -n libfa1
%{_libdir}/libfa.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc
# vim support files
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{_datadir}/vim/site/ftdetect
%{_datadir}/vim/site/ftdetect/augeas.vim
%dir %{_datadir}/vim/site/syntax
%{_datadir}/vim/site/syntax/augeas.vim

%files lenses
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lenses
%dir %{_datadir}/%{name}/lenses/dist
%{_datadir}/%{name}/lenses/dist/*.aug

%files lense-tests
%dir %{_datadir}/%{name}/lenses/dist/tests
%{_datadir}/%{name}/lenses/dist/tests/*.aug

%changelog
