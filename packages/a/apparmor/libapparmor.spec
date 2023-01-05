#
# spec file for package libapparmor
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2011-2022 Christian Boltz
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


Name:           libapparmor
Version:        3.1.2
Release:        0
Summary:        Utility library for AppArmor
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://launchpad.net/apparmor
Source0:        apparmor-%{version}.tar.gz
Source1:        apparmor-%{version}.tar.gz.asc
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  flex
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides the libapparmor library, which contains the
change_hat(2) symbol, used for sub-process confinement by AppArmor, as
well as functions to parse AppArmor log messages.

%package -n libapparmor1
Summary:        Utility library for AppArmor
Group:          System/Libraries
%ifarch ppc64
Obsoletes:      libapparmor-64bit < 2.9
Provides:       libapparmor-64bit = %{version}
%endif
Provides:       libapparmor = %{version}
Obsoletes:      libapparmor < 2.9

%description -n libapparmor1
This package provides the libapparmor library, which contains the
change_hat(2) symbol, used for sub-process confinement by AppArmor, as
well as functions to parse AppArmor log messages.

%package -n libapparmor-devel
Summary:        Development headers and libraries for libapparmor
Group:          Development/Libraries/C and C++
Requires:       libapparmor1 = %{version}
Provides:       libapparmor:/usr/include/sys/apparmor.h

%description -n libapparmor-devel
These libraries are needed for developing software that makes use of the
AppArmor API.

%prep
%setup -q -n apparmor-%{version}

%build
(
  cd ./libraries/libapparmor
  %configure \
  --without-perl \
  --without-python \
  --without-ruby \

  make
)

%check
make check -C libraries/libapparmor

%install
%makeinstall -C libraries/libapparmor
# create symlink for old change_hat(2) manpage
( cd %{buildroot}/%{_mandir}/man2/ && ln -s aa_change_hat.2 change_hat.2 )

# remove *.la and *.a files
rm -fv %{buildroot}%{_libdir}/libapparmor.la
rm -fv %{buildroot}%{_libdir}/libapparmor.a

%post -n libapparmor1 -p /sbin/ldconfig

%postun -n libapparmor1 -p /sbin/ldconfig

%files -n libapparmor1
%defattr(-,root,root)
%{_libdir}/libapparmor.so.*

%files -n libapparmor-devel
%defattr(-,root,root)
%{_libdir}/libapparmor.so
%{_libdir}/pkgconfig/libapparmor.pc
%doc %{_mandir}/man2/aa_change_hat.2.gz
%doc %{_mandir}/man2/aa_change_profile.2.gz
%doc %{_mandir}/man2/aa_stack_profile.2.gz
%doc %{_mandir}/man2/change_hat.2.gz
%doc %{_mandir}/man2/aa_find_mountpoint.2.gz
%doc %{_mandir}/man2/aa_getcon.2.gz
%doc %{_mandir}/man2/aa_query_label.2.gz
%doc %{_mandir}/man3/aa_features.3.gz
%doc %{_mandir}/man3/aa_kernel_interface.3.gz
%doc %{_mandir}/man3/aa_policy_cache.3.gz
%doc %{_mandir}/man3/aa_splitcon.3.gz
%dir %{_includedir}/aalogparse
%{_includedir}/sys/apparmor.h
%{_includedir}/sys/apparmor_private.h
%{_includedir}/aalogparse/*

%changelog
