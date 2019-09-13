#
# spec file for package tpm-tools
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lib_name libtpm_unseal1
Name:           tpm-tools
Version:        1.3.9.1
Release:        0
Summary:        Trusted Platform Module (TPM) administration tools
License:        IPL-1.0
Group:          Productivity/Security
Url:            http://trousers.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/trousers/tpm-tools/%{version}/tpm-tools-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openCryptoki-devel
BuildRequires:  openssl-devel
BuildRequires:  trousers-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# upstream has already got a pull request for this problem but didn't react
# for some months... so this is my own patch to tackle the problem
Patch0:         0001-Fix-build-against-OpenSSL-1.1.0.patch

%description
Trusted Computing is a set of specifications published by the Trusted
Computing Group (TCG). The Trusted Platform Module (TPM) is the
hardware component for Trusted Computing. The tpm-tools package
provides tools for enablement and configuration of the TPM and
associated interfaces. Also look inside the trousers package for more
software for TC.

%package        pkcs11
Summary:        Management tools using PKCS#11 for the TPM hardware
Group:          Applications/System

%description    pkcs11
Trusted Computing is a set of specifications published by the Trusted
Computing Group (TCG). The Trusted Platform Module (TPM) is the
hardware component for Trusted Computing. The tpm-tools package
provides tools for enablement and configuration of the TPM and
associated interfaces. Also look inside the trousers package for more
software for TC.

This package contains group of tools that use the TPM PKCS#11 token. All data
contained in the PKCS#11 data store is protected by the TPM (keys,
certificates, etc.). You can import keys and certificates, list out the
objects in the data store, and protect data.

%package -n %{lib_name}
Summary:        Management tools for the TPM hardware (library)
Group:          System/Libraries

%description -n %{lib_name}
Trusted Computing is a set of specifications published by the Trusted
Computing Group (TCG). The Trusted Platform Module (TPM) is the
hardware component for Trusted Computing. The tpm-tools package
provides tools for enablement and configuration of the TPM and
associated interfaces. Also look inside the trousers package for more
software for TC.

This package contains shared libraries

%package 	devel
Summary:        Files to use the library routines supplied with tpm-tools
Group:          Development/Libraries
Requires:       %{lib_name} = %{version}

%description 	devel
Trusted Computing is a set of specifications published by the Trusted
Computing Group (TCG). The Trusted Platform Module (TPM) is the
hardware component for Trusted Computing. The tpm-tools package
provides tools for enablement and configuration of the TPM and
associated interfaces. Also look inside the trousers package for more
software for TC.

This package contains the libraries and headers necessary for developing 
tpm-tools applications.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1

%build
autoreconf -fiv
# Disable unused-but-set warnings with gcc >= 4.6
%configure \
	--disable-static
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
cp include/*.h %{buildroot}%{_includedir}/tpm_tools

%files
%defattr(-,root,root)
%doc README LICENSE
%{_mandir}/man1/tpm_*
%{_mandir}/man8/tpm_*
%{_sbindir}/tpm_*
%{_bindir}/tpm_*

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/*.so.*

%files pkcs11
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/tpmtoken_*
%{_mandir}/man1/tpmtoken_*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/tpm_tools
%{_mandir}/man3/tpmUnseal*

%changelog
