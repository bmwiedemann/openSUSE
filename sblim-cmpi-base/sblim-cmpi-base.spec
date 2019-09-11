#
# spec file for package sblim-cmpi-base
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


Name:           sblim-cmpi-base
Version:        1.6.4
Release:        0
Summary:        SBLIM Base Instrumentation
License:        EPL-1.0
Group:          System/Management
Url:            http://sblim.wiki.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Source1:        sblim-cmpi-base-rpmlintrc
# PATCH-FEATURE-OPENSUSE sblim-cmpi-base-%{version}-methods-enable.patch [ bnc#470670 ] mhrusecky@suse.cz -- Enables methods by default
Patch0:         sblim-cmpi-base-1.6.2-methods-enable.patch
Patch2:         sblim-cmpi-base-1.6.4-fix-bashisms.patch
Patch3:         0001-make-lib-dependencies-explicit-in-Makefile.am.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  sblim-cmpi-devel
BuildRequires:  sblim-indication_helper-devel
BuildRequires:  sblim-sfcb
BuildRequires:  sblim-testsuite
Requires:       cim-schema
Requires:       cim-server
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Standards Based Linux Instrumentation Base Providers

%package devel
Summary:        SBLIM Base Instrumentation Header Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
SBLIM Base Provider Development Package

%package testsuite
Summary:        SBLIM Base Instrumentation (test suite)
Group:          System/Management
Requires:       %{name} = %{version}
Requires:       sblim-testsuite

%description testsuite
Test suite for the Standards Based Linux Instrumentation Base Providers

%prep
%setup -q -T -b 0
%patch0
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
%configure TESTSUITEDIR=%{_datadir}/sblim-testsuite --disable-static
# build without parallelism because of broken build system deps
make

%install
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
make DESTDIR=%{buildroot} install
%else
make DESTDIR=%{buildroot} install docdir=%{_docdir}/%{name}
%endif
# don't delete .la's until we sort out if sfcb/openwbem/pegasus use ltdlopen()
# %{__rm} %{buildroot}%{_libdir}/{libcmpiOSBase_Common,libdmiinfo}.la
# remove unused libtool files
rm -f %{buildroot}/%{_libdir}/*.a
rm -f %{buildroot}/%{_libdir}/cmpi/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/cmpi/*.la

# install indication samples into %docdir
install -m0644 ./test/indication/SFCB*.xml %{buildroot}/%{_docdir}/%{name}*

%pre
# definition of schema and registration files

%define SCHEMA %{_datadir}/%{name}/Linux_Base.mof %{_datadir}/%{name}/Linux_BaseIndication.mof
%define REGISTRATION %{_datadir}/%{name}/Linux_BaseIndication.registration
# If upgrading, deregister old version
if [ $1 -gt 1 ]
then
  %{_datadir}/%{name}/provider-register.sh -d \
	-r %{REGISTRATION} -m %{SCHEMA} > /dev/null ||:
fi

%post
# Register Schema and Provider - this is higly provider specific
# tog-pegasus needs some schemes registered first
if [ -x %{_bindir}/peg-loadmof.sh ]; then
	peg-loadmof.sh -n root/cimv2 %(for i in Card UnixProcess Processor OperatingSystem ComputerSystem ComputerSystemPackage RunningOS OSProcess SystemDevice ProcessIndication ElementStatisticalData; echo -n "%{_datadir}/mof/cim-current/*/CIM_$i.mof ")
	rctog-pegasus try-restart
fi
# and then following script can handle registration for various providers
%{_datadir}/%{name}/provider-register.sh \
	-r %{REGISTRATION} -m %{SCHEMA} > /dev/null ||:
/sbin/ldconfig

%preun
# Deregister only if not upgrading
if [ $1 -eq 0 ]
then
  %{_datadir}/%{name}/provider-register.sh -d \
	-r %{REGISTRATION} -m %{SCHEMA} > /dev/null ||:
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
%docdir %{_datadir}/doc/%{name}-%{version}
%doc %{_datadir}/doc/%{name}-%{version}
%else
%doc %{_docdir}/%{name}
%endif
%dir %{_libdir}/cmpi/
%{_libdir}/cmpi/libcmpiOSBase*.so
%{_libdir}/libcmpiOSBase_Common.so.*
%{_libdir}/libdmiinfo.so.*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/provider-register.sh
%{_datadir}/%{name}/Linux_Base*
#possibly needed atm, as per above comment... leaving for now
%{_libdir}/libcmpiOSBase_Common.la
%{_libdir}/libdmiinfo.la

%files devel
%defattr(-,root,root)
%dir %{_includedir}/sblim
%{_includedir}/sblim/*
%{_libdir}/libcmpiOSBase_Common.so
%{_libdir}/libdmiinfo.so

%files testsuite
%defattr(-,root,root)
%dir %{_datadir}/sblim-testsuite
%dir %{_datadir}/sblim-testsuite/cim
%dir %{_datadir}/sblim-testsuite/system
%dir %{_datadir}/sblim-testsuite/system/linux
%{_datadir}/sblim-testsuite/test-cmpi-base.sh
%{_datadir}/sblim-testsuite/cim/Linux*.cim
%{_datadir}/sblim-testsuite/system/linux/*.pl
%{_datadir}/sblim-testsuite/system/linux/*.system
%{_datadir}/sblim-testsuite/system/linux/Linux_OperatingSystem.version.sh
%{_datadir}/sblim-testsuite/system/linux/createKeyFiles.sh

%changelog
