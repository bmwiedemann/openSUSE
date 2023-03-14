#
# spec file for package openssl-ibmca
#
# Copyright (c) 2023 SUSE LLC
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


%global enginesdir %(pkg-config --variable=enginesdir libcrypto)

Name:           openssl-ibmca
Version:        2.3.1
Release:        0
Summary:        The IBMCA OpenSSL dynamic engine
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/openssl-ibmca
Source:         https://github.com/opencryptoki/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        engine_section.txt

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libica-devel >= 3.1.1
BuildRequires:  libica-tools >= 2.4.0
BuildRequires:  libtool
BuildRequires:  openssl-devel
Requires:       openssl
ExclusiveArch:  s390x

%description
This package contains a shared object OpenSSL dynamic engine which interfaces
to libica, a library enabling the IBM s390/x CPACF crypto instructions.

%prep
%autosetup
./bootstrap.sh

%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
%configure \
  --libdir=%{enginesdir}
%make_build

%install
# Update the sample config file so that the dynamic path points
# to the correct version of the engines directory.
sed -i -e "/^dynamic_path/s, = .*/, = %{enginesdir}/," src/engine/openssl.cnf.sample

%make_install
rm %{buildroot}/%{enginesdir}/ibmca.la

# This file contains the declaration of the ibmca engine section. It
# needs to be on the "real" file system when the postinstall scriptlet
# is run. It will be read by the openssl .include directive that points
# to /etc/ssl/engines.d/
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p %{SOURCE1} %{buildroot}%{_datadir}/%{name}/openssl-ibmca.sectiondef.txt

# This will create the actual engine definition section that will be usable
# by the .include directive of openSSL. That include will be inserted during
# the postinstall phase of the package installation.
grep -v "^#" src/engine/openssl.cnf.sample | \
    sed -n -e '/^\[ibmca_section\]/,$ p' | \
    sed -e '/^$/ {N;N;s/\n\n/\n/g;}' | \
    sed -e 's/^dynamic_path/dynamic_path/' > %{buildroot}%{_datadir}/%{name}/openssl-ibmca.enginedef.cnf

%post
#Original fix for bsc#942839 was to update on first install
#For bsc#966139 update if openssl_def not found
SSLENGCNF=%{_sysconfdir}/ssl/engines.d
SSLENGDEF=%{_sysconfdir}/ssl/engdef.d

mkdir -p ${SSLENGCNF}
mkdir -p ${SSLENGDEF}

cp -p %{_datadir}/%{name}/openssl-ibmca.sectiondef.txt ${SSLENGCNF}/openssl-ibmca.cnf
cp -p %{_datadir}/%{name}/openssl-ibmca.enginedef.cnf ${SSLENGDEF}/openssl-ibmca.cnf

%postun
SSLENGCNF=%{_sysconfdir}/ssl/engines.d
SSLENGDEF=%{_sysconfdir}/ssl/engdef.d
if [ $1 -eq 0 ]; then # last uninstall
  rm -f ${SSLENGCNF}/openssl-ibmca.cnf
  rm -f ${SSLENGDEF}/openssl-ibmca.cnf
fi

%files
%license LICENSE
%doc ChangeLog
%doc README.md
%doc src/engine/openssl.cnf.sample
%doc src/engine/ibmca-engine-opensslconfig
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/openssl-ibmca.sectiondef.txt
%{_datadir}/%{name}/openssl-ibmca.enginedef.cnf
%{enginesdir}/ibmca.*
/usr/lib64/engines-3/ibmca-provider.la
/usr/lib64/engines-3/ibmca-provider.so
%{_mandir}/man5/ibmca.5%{?ext_man}
%{_mandir}/man5/ibmca-provider.5.gz

%changelog
