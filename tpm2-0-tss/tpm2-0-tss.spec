#
# spec file for package tpm2-0-tss
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tpm2-0-tss
Version:        2.2.1
Release:        0
Summary:        Intel's TCG Software Stack access libraries for TPM 2.0 chips
License:        BSD-2-Clause
Group:          Productivity/Security
Url:            https://github.com/tpm2-software/tpm2-tss
Source0:        https://github.com/tpm2-software/tpm2-tss/releases/download/%{version}/tpm2-tss-%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  libopenssl-devel
BuildRequires:  pkg-config
BuildRequires:  udev
Requires(pre):  shadow
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
Requires:       libtss2-mu0 = %{version}
Requires:       libtss2-sys0 = %{version}
Requires:       libtss2-tcti-device0 = %{version}
Requires:       libtss2-tcti-mssim0 = %{version}
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

%package -n libtss2-sys0
Summary:        TPM2 System API (SAPI)
Group:          System/Libraries

%description -n libtss2-sys0
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

%prep
%setup -q -n tpm2-tss-%{version}

%pre
# the same user is employed by trousers (and was employed by the old
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
# home in /var/lib/tpm. I don't think the home directory is used by any of
# both packages ATM. Trousers is keeping state there, but the directory is
# owned by root and files are opened before dropping privileges. The passwd
# entry seems not to be evaluated.
#
# so I guess we can share the account between the two packages for now.
%_bindir/getent group tss >/dev/null || %{_sbindir}/groupadd -g 98 tss
%_bindir/getent passwd tss >/dev/null || \
	%{_sbindir}/useradd -u 98 -o -g tss -s /bin/false -c "TSS daemon" \
	-d %{_localstatedir}/lib/tpm tss

%build
%configure --disable-static --with-udevrulesdir=%{_udevrulesdir}
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
%post -n libtss2-sys0 -p /sbin/ldconfig
%postun -n libtss2-sys0 -p /sbin/ldconfig
%post -n libtss2-tcti-device0 -p /sbin/ldconfig
%postun -n libtss2-tcti-device0 -p /sbin/ldconfig
%post -n libtss2-tcti-mssim0 -p /sbin/ldconfig
%postun -n libtss2-tcti-mssim0 -p /sbin/ldconfig
%post -n libtss2-mu0 -p /sbin/ldconfig
%postun -n libtss2-mu0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc *.md LICENSE
%{_mandir}/man3/*
%{_mandir}/man7/tss2-*
%{_udevrulesdir}/%{udev_rule_file}

%files devel
%defattr(-,root,root)
%{_includedir}/tss2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n libtss2-esys0
%defattr(-,root,root)
%{_libdir}/libtss2-esys.so.*

%files -n libtss2-sys0
%defattr(-,root,root)
%{_libdir}/libtss2-sys.so.*

%files -n libtss2-mu0
%defattr(-,root,root)
%{_libdir}/libtss2-mu.so.*

%files -n libtss2-tcti-device0
%defattr(-,root,root)
%{_libdir}/libtss2-tcti-device.so.*

%files -n libtss2-tcti-mssim0
%defattr(-,root,root)
%{_libdir}/libtss2-tcti-mssim.so.*

%changelog
