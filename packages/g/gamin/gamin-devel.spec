#
# spec file for package gamin-devel
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


%define sonum   0
%define vernum  1
%define packnum %{vernum}-%{sonum}
%define famnum  0
Name:           gamin-devel
Version:        0.1.10
Release:        0
Summary:        Libraries and includes to build against gamin
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://www.gnome.org/~veillard/gamin/
Source:         http://www.gnome.org/~veillard/gamin/sources/gamin-%{version}.tar.gz
Source2:        gamin-rpmlintrc
Patch0:         gamin-return.patch
Patch1:         gamin-fam_abi_compatibility_FamErrlist.patch
Patch2:         gamin-fix_python_main.patch
Patch3:         gamin-obsol-glib.diff
# PATCH-FIX-UPSTREAM gamin-0.1.11-double-lock.patch (bgo#669292)
Patch4:         gamin-0.1.11-double-lock.patch
# PATCH-FIX-UPSTREAM 0001-Poll-files-on-nfs4.patch (bgo#693006)
Patch5:         0001-Poll-files-on-nfs4.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
Requires:       libfam%{famnum}-gamin = %{version}
Requires:       libgamin-%{packnum} = %{version}
# Both have libfam.so
Conflicts:      fam-devel
Provides:       %{name}-static = %{version}
# No glib* requires here to avoid build cycles

%description
Libraries, includes, etc. to use and build against gamin.

%package -n libgamin-%{packnum}
Summary:        Library providing the FAM File Alteration Monitor API
Group:          System/Libraries
Requires:       gamin-server >= %{version}
Provides:       libgamin = %{version}
Obsoletes:      libgamin < %{version}

%description -n libgamin-%{packnum}
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM, but not dependent on a system wide
daemon.

%package -n libfam%{famnum}-gamin
Summary:        Library providing the FAM File Alteration Monitor API
Group:          System/Libraries
Requires:       gamin-server >= %{version}
Conflicts:      libfam0

%description -n libfam%{famnum}-gamin
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM, but not dependent on a system wide
daemon.

%prep
%setup -q -n gamin-%version
%patch0 -p0
%patch1
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure --disable-static --disable-server
make %{?_smp_mflags}

%install
%make_install
rm "%{buildroot}%{_libdir}"/*.la

%post   -n libgamin-%{packnum}   -p /sbin/ldconfig
%postun -n libgamin-%{packnum}   -p /sbin/ldconfig

%post   -n libfam%{famnum}-gamin -p /sbin/ldconfig
%postun -n libfam%{famnum}-gamin -p /sbin/ldconfig

%files -n libgamin-%{packnum}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%{_libdir}/libgamin-%{vernum}.so.%{sonum}
%{_libdir}/libgamin-%{vernum}.so.%{sonum}.*

%files -n libfam%{famnum}-gamin
%defattr(-,root,root)
%{_libdir}/libfam.so.%{famnum}
%{_libdir}/libfam.so.%{famnum}.*

%files -n gamin-devel
%defattr(-,root,root)
%{_includedir}/fam.h
%{_libdir}/libfam.so
%{_libdir}/libgamin-%{vernum}.so
%{_libdir}/libgamin_shared.a
%{_libdir}/pkgconfig/gamin.pc

%changelog
