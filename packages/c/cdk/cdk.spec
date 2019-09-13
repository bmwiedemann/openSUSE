#
# spec file for package cdk
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


%define lname lib%{name}5
%define mainver 5.0
%define datever 20190224

Name:           cdk
Url:            http://invisible-island.net/cdk/
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
Version:        %{mainver}.%{datever}
Release:        0
Summary:        The Runtime for the Curses Development Kit
License:        BSD-3-Clause
Group:          System/Libraries
Source:         ftp://ftp.invisible-island.net/cdk/cdk-%{mainver}-%{datever}.tgz
Source1:        ftp://ftp.invisible-island.net/cdk/cdk-%{mainver}-%{datever}.tgz.asc
Source2:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         root        %{_tmppath}/%{name}-%{version}-store

%description
CDK is a widget set developed on top of the basic curses library. It
contains 21 ready to use widgets, some of which are: a text entry
field, a scrolling list, a selection list, an alphalist, a pull-down
menu, a radio list, a viewer widget, and a dialog box.

%package -n %lname
Summary:        The Runtime for the Curses Development Kit - Shared library
Group:          Development/Libraries/C and C++

%description -n %lname
CDK is a widget set developed on top of the basic curses library. It
contains 21 ready to use widgets, some of which are: a text entry
field, a scrolling list, a selection list, an alphalist, a pull-down
menu, a radio list, a viewer widget, and a dialog box.

%package devel
Summary:        Development Part of Curses Development Kit
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       ncurses-devel

%description devel
This package includes the development headers and static libraries for
CDK, the Curses Development Kit.

%prep
%setup -q -n cdk-%{mainver}-%{datever}

%build

%configure --with-ncurses	\
    --enable-const		\
    --with-pkg-config		\
    --disable-rpath-hack	\
    --with-versioned-syms=${PWD}/package/cdk.map \
    --with-shared
make all %{?_smp_mflags}
make install DESTDIR=%{root} INSTALL="install -pD" \
    DOCUMENT_DIR=%{root}%{_defaultdocdir}/%{name}
make clean

%configure --with-ncursesw	\
    --enable-const		\
    --with-pkg-config		\
    --disable-rpath-hack	\
    --with-versioned-syms=${PWD}/package/cdk.map \
    --with-cfgname=cdkw		\
    --with-libname=cdkw		\
    --with-shared
make all %{?_smp_mflags}
make installCDKLibrary DESTDIR=%{root} INSTALL="install -pD" \
    DOCUMENT_DIR=%{root}%{_defaultdocdir}/%{name}
make %{root}%{_libdir}/libcdkw.so.%{mainver} DESTDIR=%{root}

%install
tar -cpf - -C %{root} . | tar -xpf - -C %{buildroot}
%if %{defined license}
rm -vf %{buildroot}%{_defaultdocdir}/%{name}/COPYING
%endif
# fixes rpmlint unstripped-binary-or-object
chmod +x %{buildroot}%{_libdir}/*.so
find %{buildroot} -name '*.a' -delete -print
# Remove installed in wrong directory documentation files
rm -rf %{buildroot}%{_datadir}/doc

%post -n %lname
/sbin/ldconfig

%postun -n %lname
/sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%if %{defined license}
%license COPYING
%doc EXPANDING NOTES TODO README CHANGES VERSION
%else
%doc EXPANDING NOTES TODO README CHANGES VERSION COPYING
%endif
%{_libdir}/libcdk*.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/cdk*5-config
%{_libdir}/libcdk*.so
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man3/*.3%{ext_man}

%changelog
