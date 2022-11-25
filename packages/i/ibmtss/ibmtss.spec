#
# spec file for package ibmtss
#
# Copyright (c) 2022 SUSE LLC
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


#
%define libversion 1
%define libversion_full 1.6.0
%define libname libibmtss
%define libpkgname %{libname}%{libversion}

Name:           ibmtss
Version:        1.6.0
Release:        0
Summary:        IBM's TPM 2.0 TSS
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://sourceforge.net/projects/ibmtpm20tss
Source:         https://sourceforge.net/projects/ibmtpm20tss/files/ibmtss%{version}.tar.gz
Source1:        90-tpm-ibmtss.rules
Patch1:         ibmtss-configure.ac-Do-not-disable-optimization-for-debug-b.patch
Patch2:         ibmtss-regtests-Update-openssl-key-generation-for-3.0.0.patch
Patch3:         ibmtss-utils-Update-certifyx509-for-Openssl-3.0.0.patch
Patch4:         ibmtss-utils-Remove-unused-variables-from-certifyx509.patch
Patch5:         ibmtss-tss-Port-HMAC-operations-to-openssl-3.0.patch
Patch6:         ibmtss-utils-Port-to-openssl-3.0.0-replaces-RSA-with-EVP_PK.patch
Patch7:         ibmtss-openssl3-deprecation.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ibmswtpm2
BuildRequires:  libopenssl-devel
BuildRequires:  libtool

%description
This is a user space TCG Software Stack (TSS) for TPM 2.0. It
implements the functionality equivalent to the TCG TSS working
group's planned ESAPI, SAPI, and TCTI APIs.

It comes with over 100 "TPM tools" that can be used for scripted
apps, rapid prototyping, education, and debugging.

%package -n %{libpkgname}
Summary:        Shared library for IBM's TPM 2.0 TSS
Group:          System/Libraries
Recommends:     %{name}-base = %{version}

%description -n %{libpkgname}
Shared library for IBM's TPM 2.0 TSS tools

%package base
Summary:        IBM's TPM 2.0 TSS shared files
Group:          Productivity/Security
BuildArch:      noarch
Requires(post): user(tss)

%description base
Includes IBM's TPM 2.0 TSS certificates and policy files.

%package devel
Summary:        IBM's TPM 2.0 TSS headers
Group:          Development/Libraries/C and C++
Requires:       %{libpkgname} = %{version}
Requires:       %{name} = %{version}

%description devel
Includes IBM's TPM 2.0 TSS C header files

%prep
%setup -q -c
%autopatch -p1

%build
autoreconf -i
%configure --enable-hwtpm --enable-debug --disable-static
cd utils
sed -i -e "s|/gsa/yktgsa/home/k/g/kgold/tpm2/utils|$PWD|" certificates/rootcerts.txt
%{_libexecdir}/%{name}/tpm_server & tpm_server="$!"
CCFLAGS="%{optflags}" make LNAFLAGS="-Wl,-rpath,%{_libdir}" %{?_smp_mflags}
testfailed=0
TPM_INTERFACE_TYPE=socsim LD_LIBRARY_PATH=.libs ./reg.sh -a || testfailed=$?
kill "$tpm_server" || :
[ "$testfailed" -eq 0 ]
sed -i -e "s|$PWD|%{_datadir}/%{name}|" certificates/rootcerts.txt

%install
install -m 644 -D -t %{buildroot}%{_prefix}/lib/udev/rules.d/ %{SOURCE1}
cd utils
%make_install

mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a policies certificates %{buildroot}/%{_datadir}/%{name}

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name .cvsignore | xargs rm -v

%post base
%_bindir/udevadm trigger -s tpm -s tpmrm || :
%post   -n %{libpkgname} -p /sbin/ldconfig
%postun -n %{libpkgname} -p /sbin/ldconfig

%files
%license LICENSE
%doc ibmtss.doc
%{_bindir}/tss*
%{_mandir}/man1/tss*.1%{?ext_man}

%files -n %{libpkgname}
%{_libdir}/%{libname}*.so.%{libversion_full}
%{_libdir}/%{libname}*.so.%{libversion}

%files base
%license LICENSE
%{_datadir}/%{name}
%{_prefix}/lib/udev/rules.d/*

%files devel
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/%{libname}*.so

%changelog
