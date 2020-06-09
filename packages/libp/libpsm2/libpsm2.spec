#
# spec file for package libpsm2
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


%define git_ver %{nil}

%define psm_so 2
Name:           libpsm2
Version:        11.2.86
Release:        0
Summary:        Intel PSM Messaging API libraries
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/01org/opa-psm2/
Source0:        %{name}-%{version}%{git_ver}.tar.bz2
Source1:        libpsm2.changelog
Source2:        libpsm2-rpmlintrc
Patch2:         libpsm2-use_RPM_OPT_FLAGS.patch
Patch3:         libpsm2-use-exported-variable-for-version-and-release.patch
Patch4:         Add-missing-extern-keywords.patch
BuildRequires:  libnuma-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(udev)
Conflicts:      opa-libs
Obsoletes:      hfi-psm
Obsoletes:      hfi-psm-debuginfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Currently *only* builds on x86_64
ExclusiveArch:  x86_64

%description
The PSM Messaging API, or PSM API, is Intel's low-level
user-level communications interface for the Truescale
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%package     -n %{name}-%{psm_so}
Summary:        Intel PSM Messaging API library
Group:          System/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       %{name} = %{version}

%description -n %{name}-%{psm_so}
libpsm2 provides PSM Messaging API, or PSM API, is Intel's low-level
user-level communications interface for the Truescale
family of products. This package contains the runtime library.

%package        devel
Summary:        Development files for the Intel PSM Messaging API
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{psm_so} = %{version}
Requires:       libuuid-devel
Conflicts:      opa-devel

%package        compat
Summary:        Compatibility library providing the old PSM API/ABI
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{psm_so} = %{version}
Conflicts:      libpsm_infinipath1

%description    devel
Development files for the libpsm2 library.

%description    compat
Support for MPIs linked with PSM versions < 2.


%prep
%setup -q -n %{name}-%{version}%{git_ver}
%patch2
%patch3
%patch4

cp %{S:1} ChangeLog

%build
%global optflags %{optflags} -fcommon
export RPM_OPT_FLAGS
export VERSION=${Version} RELEASE=${Release}
make %{?_smp_mflags}

%install
export DESTDIR=%{buildroot}
make %{?_smp_mflags} DESTDIR=%{buildroot} install
install -m0644 %{buildroot}%{_libdir}/psm2-compat/libpsm_infinipath.so.1 %{buildroot}%{_libdir}/libpsm_infinipath.so.1
# removing file to get rid of rpm errors
rm  %{buildroot}%{_libdir}/psm2-compat/libpsm_infinipath.so.1
rm  %{buildroot}/usr/lib/%name/libpsm2-compat.cmds
# remove static library
rm  %{buildroot}%{_libdir}/libpsm2.a

%post -n %{name}-%{psm_so} -p /sbin/ldconfig
%postun -n %{name}-%{psm_so} -p /sbin/ldconfig
%post compat -p /sbin/ldconfig
%postun compat -p /sbin/ldconfig

%files -n %{name}-%{psm_so}
%defattr(-,root,root,-)
%{_libdir}/libpsm2.so.*
%{_udevrulesdir}/40-psm.rules
%doc README ChangeLog
%license COPYING

%files devel
%defattr(-,root,root,-)
%{_libdir}/libpsm2.so
%{_includedir}/psm2.h
%{_includedir}/psm2_mq.h
%{_includedir}/psm2_am.h

# The following files were part of the devel-noship and moved to devel:
%dir %{_includedir}/hfi1diag/
%dir %{_includedir}/hfi1diag/linux-x86_64/
%{_includedir}/hfi1diag/linux-x86_64/bit_ops.h
%{_includedir}/hfi1diag/linux-x86_64/sysdep.h
%_includedir/hfi1diag/hfi1_deprecated.h
%{_includedir}/hfi1diag/opa_udebug.h
%{_includedir}/hfi1diag/opa_debug.h
%{_includedir}/hfi1diag/opa_intf.h
%{_includedir}/hfi1diag/opa_user.h
%{_includedir}/hfi1diag/opa_service.h
%{_includedir}/hfi1diag/opa_common.h
%{_includedir}/hfi1diag/opa_byteorder.h
%{_includedir}/hfi1diag/opa_revision.h
%{_includedir}/hfi1diag/psm2_mock_testing.h
%{_includedir}/hfi1diag/psmi_wrappers.h

%files compat
%defattr(-,root,root,-)
%dir %{_sysconfdir}/modprobe.d

%{_libdir}/libpsm_infinipath.so.*
%{_udevrulesdir}/40-psm-compat.rules
%config %{_sysconfdir}/modprobe.d/libpsm2-compat.conf

%changelog
