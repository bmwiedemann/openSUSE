#
# spec file for package libustr
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


Name:           libustr
Version:        1.0.4
Release:        0
Url:            http://www.and.org/ustr/
Summary:        A string library
License:        MIT OR LGPL-2.1-or-later OR BSD-2-Clause
Group:          Development/Languages/C and C++
Source:         http://www.and.org/ustr/%{version}/ustr-%{version}.tar.bz2
Source1:        libustr-rpmlintrc
Source2:        baselibs.conf
Patch0:         %{name}-%{version}-c99-inline.patch
Patch1:         libustr-warning.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config

%description
A string library that uses plain strdup() (on average 44%% overhead for
0-20B strings). A single header file is provided.

%package -n libustr-1_0-1
Summary:        A string library
Group:          System/Libraries

%description -n libustr-1_0-1
A string library that uses plain strdup() (on average 44%% overhead for
0-20B strings). A single header file is provided.

%package devel
Summary:        Development files for libustr
Group:          Development/Languages/C and C++
Requires:       libustr-1_0-1 = %{version}

%description devel
Header files for the Ustr string library, and the .so to link with.
Also includes a %{name}.pc file for pkg-config usage.
It includes the ustr-import tool, for when the code shall be
bundled with projects.

%prep
%setup -q -n ustr-%{version}
%patch0
%patch1 -p1

%build
make all-shared %{?_smp_mflags} HIDE= CFLAGS="%optflags -fPIC" CC="%{__cc} -std=gnu89"

%check
%if !0%{?qemu_user_space_build:1}
# bad interaction with qemu (2011-10-02)
make check %{?_smp_mflags} HIDE= CFLAGS="%optflags -fPIC"
%endif

%install
make install-multilib-linux \
    prefix=%{_prefix} \
    bindir=%{_bindir} \
    mandir=%{_mandir} \
    datadir=%{_datadir} \
    libdir=%{_libdir} \
    includedir=%{_includedir} \
    libexecdir=%{_libexecdir} \
    DESTDIR=%{buildroot} \
    LDCONFIG=/bin/true \
    HIDE=
rm -Rfv %{buildroot}/%{_libdir}/*.a %{buildroot}/%{_libdir}/*debug*.so \
	%{buildroot}/%{_libdir}/*debug* \
	%{buildroot}/%{_libdir}/pkgconfig/*debug* \
	%{buildroot}/%{_datadir}/doc

%post -n libustr-1_0-1 -p /sbin/ldconfig

%postun -n libustr-1_0-1 -p /sbin/ldconfig

%files -n libustr-1_0-1
%defattr(-,root,root,-)
%license LICENSE*
%{_libdir}/libustr-1.0.so.*

%files devel
%defattr(-,root,root,-)
%doc ChangeLog README NEWS
%doc README-DEVELOPERS TODO Documentation/*.html Documentation/*.gnumeric
%{_datadir}/ustr-%{version}
%{_bindir}/ustr-import
%{_libexecdir}/ustr-%{version}
%{_includedir}/ustr.h
%{_includedir}/ustr-*.h
%{_libdir}/pkgconfig/ustr.pc
%{_libdir}/libustr.so
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
