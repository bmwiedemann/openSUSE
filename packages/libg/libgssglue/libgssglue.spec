#
# spec file for package libgssglue
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libgssglue
Url:            http://www.citi.umich.edu/projects/nfsv4/linux
Summary:        Generic GSSAPI Library
License:        BSD-3-Clause and MIT
Group:          Development/Libraries/C and C++
Version:        0.4
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  pkg-config
%define debug_package_requires libgssglue1 = %{version}-%{release}
PreReq:         %fillup_prereq %insserv_prereq
Source:         http://www.citi.umich.edu/projects/nfsv4/linux/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         config-guess-sub-update.patch
Patch1:         secure-getenv.patch

%description
This library exports a gssapi interface, but does not implement any
gssapi mechanisms itself. Instead it calls gssapi routines in other
libraries, depending on the mechanism.

%package -n libgssglue1
Summary:        Generic GSSAPI Library
Group:          Development/Libraries/C and C++

%description -n libgssglue1
This library exports a gssapi interface, but does not implement any
gssapi mechanisms itself. Instead it calls gssapi routines in other
libraries, depending on the mechanism.

%package devel
Summary:        Generic GSSAPI Library
Group:          Development/Libraries/C and C++
# last used 11.0
Provides:       libgssapi = %{version}
Obsoletes:      libgssapi <= 0.11
Requires:       glibc-devel
Requires:       libgssglue1 = %{version}

%description devel
This library exports a gssapi interface, but does not implement any
gssapi mechanisms itself. Instead it calls gssapi routines in other
libraries, depending on the mechanism.

%prep
%setup -q
%patch0
%patch1 -p1

%build
autoconf
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" 
%configure --libdir=/%_lib --disable-static
%{__make} %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
#rm -f $RPM_BUILD_ROOT/usr/local/include/gssglue/gssapi/gssapi.h
install -d $RPM_BUILD_ROOT/etc
sed -e "s@/lib/@/%_lib/@" doc/gssapi_mech.conf > $RPM_BUILD_ROOT/etc/gssapi_mech.conf
%{__mkdir_p} %{buildroot}%{_libdir}
%{__ln_s} -v /%{_lib}/$(readlink %{buildroot}/%{_lib}/%{name}.so) %{buildroot}%{_libdir}/%{name}.so
%{__rm} -v %{buildroot}/%{_lib}/%{name}.{so,la}
%{__mv} -v $RPM_BUILD_ROOT/%{_lib}/pkgconfig $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libgssglue1 -p /sbin/ldconfig

%postun -n libgssglue1 -p /sbin/ldconfig

%files -n libgssglue1
%defattr(-,root,root)
%config /etc/gssapi_mech.conf
/%{_lib}/libgssglue.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libgssglue.so
%{_libdir}/pkgconfig/libgssglue.pc
%dir %{_includedir}/gssglue/
%{_includedir}/gssglue/*

%changelog
