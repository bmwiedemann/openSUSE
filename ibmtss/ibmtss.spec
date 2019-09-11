#
# spec file for package ibmtss
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


#
%define suite ibmtss
%define libversion 0
%define libversion_full 0.0.1
%define libname libibmtss
%define libpkgname %{libname}%{libversion}

Name:           ibmtss
Version:        1470
Release:        0
Summary:        IBM's TPM 2.0 TSS
License:        BSD-3-Clause
Group:          Productivity/Security
URL:            https://sourceforge.net/projects/ibmtpm20tss
Source:         https://sourceforge.net/projects/ibmtpm20tss/files/ibmtss%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ibmswtpm2
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
Recommends:     %{name}-base = %{version}

%description
This is a user space TCG Software Stack (TSS) for TPM 2.0. It
implements the functionality equivalent to the TCG TSS working
group's planned ESAPI, SAPI, and TCTI APIs.

It comes with over 100 "TPM tools" that can be used for scripted
apps, rapid prototyping, education, and debugging.

%package -n %{libpkgname}
Summary:        Shared library for IBM's TPM 2.0 TSS
Group:          System/Libraries

%description -n %{libpkgname}
Shared library for IBM's TPM 2.0 TSS tools

%package base
Summary:        IBM's TPM 2.0 TSS shared files
Group:          Productivity/Security
BuildArch:      noarch

%description base
Includes IBM's TPM 2.0 TSS certificates and policy files.

%package devel
Summary:        IBM's TPM 2.0 TSS headers
Group:          Development/Libraries/C and C++
Requires:       %{libpkgname} = %{version}
Requires:       %{suite} = %{version}

%description devel
Includes IBM's TPM 2.0 TSS C header files

%prep
%setup -q -c

%build
autoreconf -i
%configure --enable-hwtpm --enable-debug --disable-static
cd utils
%{_libexecdir}/%{suite}/tpm_server & tpm_server="$!"
CCFLAGS="%{optflags}" make LNAFLAGS="-Wl,-rpath,%{_libdir}" %{?_smp_mflags}
testfailed=0
TPM_INTERFACE_TYPE=socsim LD_LIBRARY_PATH=.libs ./reg.sh || testfailed=$?
kill "$tpm_server" || :
[ "$testfailed" -eq 0 ]

%install
cd utils
%make_install

mkdir -p %{buildroot}/%{_datadir}/%{suite}
cp -a policies certificates %{buildroot}/%{_datadir}/%{suite}

rm -f  %{buildroot}/%{_libdir}/*.la
find %{buildroot} -name .cvsignore | xargs rm -v

for i in %{buildroot}/%{_mandir}/man1/tsstss*.1 ; do
	mv -v $i $(echo $i | sed -e s,/tsstss,/tss,)
done

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
%{_datadir}/%{suite}

%files devel
%license LICENSE
%{_includedir}/%{suite}
%{_libdir}/%{libname}*.so

%changelog
