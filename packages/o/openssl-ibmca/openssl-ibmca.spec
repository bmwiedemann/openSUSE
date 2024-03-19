#
# spec file for package openssl-ibmca
#
# Copyright (c) 2024 SUSE LLC
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


%define         flavor  @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == ""
%define openssl3 1
%define provider 0
%endif

%if "%{flavor}" == "openssl1"
%define openssl3 0
%define provider 0
%endif

%if "%{flavor}" == "engine"
%define openssl3 1
%define provider 0
%endif

%if "%{flavor}" == "provider"
%define openssl3 1
%define provider 1
%endif

%global enginesdir %(pkg-config --variable=enginesdir libcrypto)
%global modulesdir %(pkg-config --variable=modulesdir libcrypto)

Name:           openssl-ibmca
Version:        2.4.1
Release:        0
Summary:        The IBMCA OpenSSL dynamic engine
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/openssl-ibmca
Source:         https://github.com/opencryptoki/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        engine_section.txt
Source2:        _multibuild
###
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libica-devel >= 4.0.0
BuildRequires:  libica-tools >= 4.0.0
BuildRequires:  libtool
Requires:       libica4 >= 4
%if %{openssl3}
BuildRequires:  openssl-devel > 3.0.0
Requires:       openssl > 3.0.0
%else
BuildRequires:  openssl-devel
Requires:       openssl
%endif
ExclusiveArch:  s390x

%description
This package contains a shared object OpenSSL dynamic engine which interfaces
to libica, a library enabling the IBM s390/x CPACF crypto instructions.

%prep
%autosetup -p1
 ./bootstrap.sh

%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"

%if %{provider}
  %configure \
  --disable-engine \
  --libdir=%{modulesdir}
%else
  %configure \
  --disable-provider \
  --libdir=%{enginesdir}
%endif

%make_build

%install
%if %{provider}
#
###
#
%else
# Update the sample config file so that the dynamic path points
# to the correct version of the engines directory.
sed -i -e "/^dynamic_path/s, = .*/, = %{enginesdir}/," src/engine/openssl.cnf.sample
%endif

%make_install
%if %{provider}
rm -f %{buildroot}/%{modulesdir}/ibmca-provider.la
%else
rm -f %{buildroot}/%{enginesdir}/ibmca.la
%endif

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
    sed -e 's/^dynamic_path/#dynamic_path/' > %{buildroot}%{_datadir}/%{name}/openssl-ibmca.enginedef.cnf

%post
#Original fix for bsc#942839 was to update on first install
#For bsc#966139 update if openssl_def not found
SSLENGCNF=%{_sysconfdir}/ssl/engines.d
SSLENGDEF=%{_sysconfdir}/ssl/engdef.d

%if %{openssl3}
  mkdir -p ${SSLENGCNF}
  mkdir -p ${SSLENGDEF}
%endif

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
%doc src/engine/ibmca-engine-opensslconfig.in
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/openssl-ibmca.sectiondef.txt
%{_datadir}/%{name}/openssl-ibmca.enginedef.cnf
%if %{openssl3}
  %if %{provider}
    %{modulesdir}/ibmca-provider.*
    %{_mandir}/man5/ibmca-provider.5%{?ext_man}
  %else
    %{enginesdir}/ibmca.*
    %{_mandir}/man5/ibmca.5%{?ext_man}
  %endif
%else
  %{enginesdir}/ibmca.*
  %{_mandir}/man5/ibmca.5%{?ext_man}
%endif

%changelog
