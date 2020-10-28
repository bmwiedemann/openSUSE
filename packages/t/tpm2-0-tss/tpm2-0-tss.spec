#
# spec file for package tpm2-0-tss
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


Name:           tpm2-0-tss
Version:        3.0.1
Release:        0
Summary:        Intel's TCG Software Stack access libraries for TPM 2.0 chips
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://github.com/tpm2-software/tpm2-tss
Source0:        https://github.com/tpm2-software/tpm2-tss/releases/download/%{version}/tpm2-tss-%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libopenssl-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(udev)
# The same user is employed by trousers (and was employed by the old
# resourcemgr shipped with the tpm2-0-tss package):
#
# trousers just needs those accounts for dropping privileges to. The service
# starts as root and uses set*id to drop to tss, after the tpm device has been
# opened.
#
# tpm2-abrmd has no set*id handling and thus requires /dev/tpm to be owned
# by the tss user. Therefore we also need to install a udev rule file.
#
# trousers was here first and created the user like this, also giving it a
# home in /var/lib/tpm. I don't think the home directory is used by either of
# the packages ATM. Trousers is keeping state there, but the directory is
# owned by root and files are opened before dropping privileges. The passwd
# entry seems not to be evaluated.
Requires:       user(tss)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The tpm2-0-tss package provides a TPM 2.0 TSS implementation. This
implementation is developed by INTEL. This package contains the libraries,
see the tpm2.0-abrmd package for the resource manager daemon, tpm2.0-tools for
utilities.

%package devel
Summary:        Development headers for the Intel TSS library for TPM 2.0 chips
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libtss2-esys0 = %{version}
Requires:       libtss2-fapi1 = %{version}
Requires:       libtss2-mu0 = %{version}
Requires:       libtss2-rc0 = %{version}
Requires:       libtss2-sys1 = %{version}
Requires:       libtss2-tcti-cmd0 = %{version}
Requires:       libtss2-tcti-device0 = %{version}
Requires:       libtss2-tcti-mssim0 = %{version}
Requires:       libtss2-tcti-swtpm0 = %{version}
Requires:       libtss2-tctildr0 = %{version}
Requires:       tpm2-0-tss = %{version}

%description devel
This package provides the development files for the tpm2 stack's libraries for
accessing TPM 2.0 chips.

%package -n libtss2-esys0
Summary:        TPM2 Enhanced System API (ESAPI)
Group:          System/Libraries

%description -n libtss2-esys0
This API is a 1-to-1 mapping of the TPM2 commands documented in Part 3 of the
TPM2 specification. Additionally there are asynchronous versions of each
command. In addition to SAPI, the ESAPI performs tracking of meta data for
TPM object and automatic calculation of session based authorization and
encryption values. Both the synchronous and asynchronous API are exposed
through this library.

%package -n libtss2-sys1
Summary:        TPM2 System API (SAPI)
Group:          System/Libraries

%description -n libtss2-sys1
System API (SAPI) as described in the system level API and TPM command
transmission interface specification. This API is a 1-to-1 mapping of the TPM2
commands documented in Part 3 of the TPM2 specification. Additionally there
are asynchronous versions of each command. These asynchronous variants may be
useful for integration into event-driven programming environments. Both the
synchronous and asynchronous API are exposed through this library.

%package -n libtss2-mu0
Summary:        TPM2 marshaling/unmarshaling library
Group:          System/Libraries

%description -n libtss2-mu0
Marshaling/Unmarshaling (MU) as described in the TCG TSS 2.0
Marshaling/Unmarshaling API Specification. This API provides a set of
marshaling and unmarshaling functions for all data types defined by the TPM
library specification.

%package -n libtss2-rc0
Summary:        TPM2 error code translation library
Group:          System/Libraries

%description -n libtss2-rc0
This library can translate TPM error codes into human readable strings.

%package -n libtss2-tctildr0
Summary:        TCTI interface loading library
Group:          System/Libraries

%description -n libtss2-tctildr0
This is a helper library that simplifies loading other tcti libraries. It is
recommended over custom tcti loading code in applications.

%package -n libtss2-tcti-device0
Summary:        TCTI interface library for using a native TPM device node
Group:          System/Libraries

%description -n libtss2-tcti-device0
TPM Command Transmission Interface library for communicating with a
TPM device node. This provides direct access to the TPM through the Linux
kernel driver.

%package -n libtss2-tcti-mssim0
Summary:        TCTI interface library for Microsoft software TPM2 simulator
Group:          System/Libraries

%description -n libtss2-tcti-mssim0
TPM Command Transmission Interface library for communicating using the
protocol exposed by the Microsoft software TPM2 simulator.

%package -n     libtss2-fapi1
Summary:        FAPI interface library
Group:          System/Libraries

%description -n libtss2-fapi1
This is the tpm2 Feature API (FAPI) library. This API is designed to be very
high-level API, intended to make programming with the TPM as simple as
possible.

%package -n     libtss2-tcti-cmd0
Summary:        TCTI cmd interface library
Group:          System/Libraries

%description -n libtss2-tcti-cmd0
A TCTI for interaction with a subprocess. It abstracts the details of direct
communication with the interface and protocol exposed by a subprocess that can
receive and transmit raw TPM2 command and response buffers.

%package -n     libtss2-tcti-swtpm0
Summary:        TCTI swtpm interface library
Group:          System/Libraries

%description -n libtss2-tcti-swtpm0
A TCTI for interaction with the TPM2 software simulator. It abstracts the
details of direct communication with the interface and protocol exposed by the
daemon hosting the TPM2 reference implementation.

%prep
%setup -q -n tpm2-tss-%{version}

%build
%configure --disable-static \
    --with-udevrulesdir=%{_udevrulesdir} \
    --with-runstatedir=%{_rundir} \
    --with-tmpfilesdir=%{_tmpfilesdir} \
    --with-sysusersdir=%{_sysusersdir}
make %{?_smp_mflags} PTHREAD_LDFLAGS=-pthread

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# rename the rules file to have a numbered prefix as all others have, too
%define udev_rule_file 90-tpm.rules
mv %{buildroot}%{_udevrulesdir}/tpm-udev.rules %{buildroot}%{_udevrulesdir}/%{udev_rule_file}

%post
%_bindir/udevadm trigger -s tpm -s tpmrm || :

%post -n libtss2-esys0 -p /sbin/ldconfig
%postun -n libtss2-esys0 -p /sbin/ldconfig
%post -n libtss2-sys1 -p /sbin/ldconfig
%postun -n libtss2-sys1 -p /sbin/ldconfig
%post -n libtss2-tctildr0 -p /sbin/ldconfig
%postun -n libtss2-tctildr0 -p /sbin/ldconfig
%post -n libtss2-tcti-device0 -p /sbin/ldconfig
%postun -n libtss2-tcti-device0 -p /sbin/ldconfig
%post -n libtss2-tcti-mssim0 -p /sbin/ldconfig
%postun -n libtss2-tcti-mssim0 -p /sbin/ldconfig
%post -n libtss2-mu0 -p /sbin/ldconfig
%postun -n libtss2-mu0 -p /sbin/ldconfig
%post -n libtss2-rc0 -p /sbin/ldconfig
%postun -n libtss2-rc0 -p /sbin/ldconfig
%post -n libtss2-fapi1
/sbin/ldconfig
%tmpfiles_create %_tmpfilesdir/tpm2-tss-fapi.conf
%postun -n libtss2-fapi1 -p /sbin/ldconfig
%post -n libtss2-tcti-cmd0 -p /sbin/ldconfig
%postun -n libtss2-tcti-cmd0 -p /sbin/ldconfig
%post -n libtss2-tcti-swtpm0 -p /sbin/ldconfig
%postun -n libtss2-tcti-swtpm0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc *.md
%license LICENSE
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/tss2-*
%{_udevrulesdir}/%{udev_rule_file}
%{_sysusersdir}/tpm2-tss.conf
%dir /etc/tpm2-tss/
%config /etc/tpm2-tss/fapi-config.json
%dir /etc/tpm2-tss/fapi-profiles
%config /etc/tpm2-tss/fapi-profiles/*.json

%files devel
%defattr(-,root,root)
%{_includedir}/tss2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n libtss2-esys0
%defattr(-,root,root)
%{_libdir}/libtss2-esys.so.*

%files -n libtss2-sys1
%defattr(-,root,root)
%{_libdir}/libtss2-sys.so.*

%files -n libtss2-mu0
%defattr(-,root,root)
%{_libdir}/libtss2-mu.so.*

%files -n libtss2-rc0
%defattr(-,root,root)
%{_libdir}/libtss2-rc.so.*

%files -n libtss2-tctildr0
%defattr(-,root,root)
%{_libdir}/libtss2-tctildr.so.*

%files -n libtss2-tcti-device0
%defattr(-,root,root)
%{_libdir}/libtss2-tcti-device.so.*

%files -n libtss2-tcti-mssim0
%defattr(-,root,root)
%{_libdir}/libtss2-tcti-mssim.so.*

%files -n libtss2-fapi1
%defattr(-,root,root)
%{_libdir}/libtss2-fapi.so.*
%{_tmpfilesdir}/tpm2-tss-fapi.conf
# this would fix "tmpfile-not-in-filelist" warnings but when adding these
# entries then it complains about "directories not owned by a package:" for
# /run/tpm2-0-tss & friends. When adding them as %ghost, too, then Leap15.1
# complains about "found conflict of libtss2-fapi1-3.0.1-lp152.103.1.x86_64
# with libtss2-fapi1-3.0.1-lp152.103.1.x86_64". Thus leave it be for the
# moment, some insane circle of errors is involved here.
#%%ghost %{_sharedstatedir}/%{name}/system/keystore
#%%ghost %{_rundir}/%{name}/eventlog

%files -n libtss2-tcti-cmd0
%defattr(-,root,root)
%{_libdir}/libtss2-tcti-cmd.so.*

%files -n libtss2-tcti-swtpm0
%defattr(-,root,root)
%{_libdir}/libtss2-tcti-swtpm.so.*

%changelog
