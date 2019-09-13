#
# spec file for package augeas
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname lib%{name}0
Name:           augeas
Version:        1.11.0
Release:        0
Summary:        An utility for changing configuration files
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://augeas.net/
Source0:        http://download.augeas.net/augeas-%{version}.tar.gz
Source1:        http://download.augeas.net/augeas-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch0:         augeas-modprobe-lense.patch
Patch1:         gcc9-disable-broken-test.patch
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
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.

%package        -n %{libname}
Summary:        A library for changing configuration files
Group:          System/Libraries
Recommends:     %{name}-lenses = %{version}

%description    -n %{libname}
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.

%package        lenses
Summary:        Official set of lenses for use by %{libname}
Group:          System/Libraries
Requires:       %{libname} = %{version}

%description    lenses
Augeas parses configuration files described in lenses into a tree
structure, which it exposes through its public API. Lenses are the
building blocks of the file <-> tree transformation. The transformation
is controlled by ``lens'' definitions that describe the file format and
mapping of its contents into a tree. This package includes the official
set of lenses.

%package        lense-tests
Summary:        Set of tests for official Augeas lenses
Group:          Development/Libraries/Other
Requires:       %{name}-lenses = %{version}

%description    lense-tests
Set of tests for official Augeas lenses. These can be used when
modifying the official lenses, or when creating new ones.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--disable-static \
	--disable-silent-rules \
	--disable-rpath
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# move vim files to the right location
mv %{buildroot}/%{_datadir}/vim/vimfiles %{buildroot}/%{_datadir}/vim/site

%check
make check %{?_smp_mflags}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/augmatch
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%{_mandir}/man1/*
%license COPYING
%doc AUTHORS NEWS

%files -n %{libname}
%{_libdir}/*.so.*

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
