#
# spec file for package libuser
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


Name:           libuser
%define libname %{name}1

Version:        0.62
Release:        0
Url:            https://pagure.io/libuser
Summary:        A user and group account administration library
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cyrus-sasl-devel
BuildRequires:  glib2-devel
BuildRequires:  libselinux-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  popt-devel
BuildRequires:  python-devel
BuildRequires:  sgmltool

%if 0%{?suse_version}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# redefine pkglibdir to honor SUSE shared lib rules, kkaempf@suse.de
Patch1:         libuser-sharedlib.patch
# fix path to slapd for SUSE, mc@suse.de
Patch2:         suse-ldap.dif
%if 0%{?suse_version} <= 1110
# fix SLE11 build, kkaempf@suse.de
Patch3:         g_malloc0_n.patch
BuildRequires:  xz
%endif
%endif

%description
The libuser library implements a standardized interface for manipulating
and administering user and group accounts.  The library uses pluggable
back-ends to interface to its data sources.

Sample applications modeled after those included with the shadow password
suite are included.

%package -n %libname
Summary:        A user and group account administration library
Group:          System/Libraries

%description -n %libname
The libuser library implements a standardized interface for manipulating
and administering user and group accounts.  The library uses pluggable
back-ends to interface to its data sources.

%lang_package -r %libname

%package devel
Summary:        Files needed for developing applications which use libuser
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glib2-devel

%description devel
The libuser-devel package contains header files and other
files useful for developing applications with libuser.

%package python
Summary:        Python bindings for the libuser library
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description python
The libuser-python package contains the Python bindings for
the libuser library, which provides a Python API for manipulating and
administering user and group accounts.

%prep
%setup -q
%if 0%{?suse_version}
%patch1 -p1
%patch2 -p1
%if 0%{?suse_version} <= 1110
%patch3 -p1
%endif
%endif

%build
%if 0%{?suse_version}
autoreconf -f -i
%endif
%configure --with-selinux --with-ldap --with-html-dir=%{_datadir}/gtk-doc/html
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/%{libname}/*.la %{buildroot}/%{py_sitedir}/*.la

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO docs/*.txt
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n %{libname}
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/libuser.conf
%{_libdir}/*.so.*
%dir %{_libdir}/%{libname}
%{_libdir}/%{libname}/*.so

%files lang -f %{name}.lang

%files python
%defattr(-,root,root)
%doc python/modules.txt
%{py_sitedir}/*.so

%files devel
%defattr(-,root,root)
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/libuser
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
