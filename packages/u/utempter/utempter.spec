#
# spec file for package utempter
#
# Copyright (c) 2020 SUSE LLC
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


%define lname	libutempter0
%define utmpGroup utmp
Name:           utempter
Version:        1.2.0
Release:        0
Summary:        A privileged helper for utmp and wtmp updates
License:        LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://github.com/altlinux/libutempter/
Source:         ftp://ftp.altlinux.org/pub/people/ldv/utempter/lib%{name}-%{version}.tar.gz
Source1:        ftp://ftp.altlinux.org/pub/people/ldv/utempter/lib%{name}-%{version}.tar.gz.asc
Source2:        baselibs.conf
Source3:        %{name}.keyring
Patch0:         utempter.eal3.diff
Patch1:         utempter-no-staticlib.patch

%description
Utempter is a utility that allows non-privileged applications such as
terminal emulators to modify the utmp database without having to be
setuid root.

%package devel
Summary:        Development files for utempter
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Utempter is a privileged helper for utmp and wtmp updates.  This
package contains the development files needed.

%package -n %{lname}
Summary:        Shared library of utempter
Group:          Development/Libraries/C and C++
Requires(post): permissions
Requires(pre):  group(%{utmpGroup})
Provides:       %{name} = %{version}
Obsoletes:      %{name} < 0.5.6

%description -n %{lname}
Utempter is a privileged helper for utmp and wtmp updates.  This
package contains the library used by applications.

%prep
%setup -q -n lib%{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags} -fPIC" CC="gcc" libexecdir=%{_libexecdir}

%install
make libdir=%{_libdir} libexecdir=%{_libexecdir} DESTDIR=%{buildroot} install

%verifyscript -n %{lname}
%verify_permissions -e %{_libexecdir}/utempter/utempter

%post -n %{lname}
%set_permissions %{_libexecdir}/utempter/utempter
/sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%dir %{_libexecdir}/utempter
%attr(02755, root, %{utmpGroup}) %{_libexecdir}/utempter/utempter
%attr(755,root,root) %{_libdir}/libutempter.so.*
%attr(644,root,root) %doc %{_mandir}/man8/*

%files devel
%license COPYING
%attr(755,root,root) %{_libdir}/libutempter.so
%attr(644,root,root) %{_includedir}/utempter.h
%attr(644,root,root) %doc %{_mandir}/man3/*

%changelog
