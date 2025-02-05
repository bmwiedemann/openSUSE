#
# spec file for package openssl-ibmca
#
# Copyright (c) 2025 SUSE LLC
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
%global modulesdir %(pkg-config --variable=modulesdir libcrypto)

%global sslengcnf %{_sysconfdir}/ssl/engines3.d
%global sslengdef %{_sysconfdir}/ssl/engdef3.d

%define         flavor  @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == ""
Name:           openssl-ibmca
%endif

%if "%{flavor}" == "engine"
Name:           openssl-ibmca-engine
%endif

%if "%{flavor}" == "provider"
Name:           openssl-ibmca-provider
%endif

Version:        2.4.1
Release:        0
Summary:        The IBMCA OpenSSL dynamic engine
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/openssl-ibmca
Source:         https://github.com/opencryptoki/openssl-ibmca/archive/v%{version}.tar.gz#/openssl-ibmca-%{version}.tar.gz
Source1:        engine_section.txt
Source2:        _multibuild
###
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
###
BuildRequires:  libica-devel >= 4.0.0
BuildRequires:  libica-tools >= 4.0.0
BuildRequires:  libopenssl-3-devel
BuildRequires:  libopenssl3
Requires:       libica4 >= 4.0.0
Requires:       libopenssl3
###
ExclusiveArch:  s390x

###
Patch10:        openssl-ibmca-01-engine-Enable-external-AES-GCM-IV-when-libica-is-in-FIPS-mode.patch
Patch11:        openssl-ibmca-02-test-provider-Do-not-link-against-libica-use-dlopen-instead.patch
Patch12:        openssl-ibmca-03-test-provider-Explicitly-initialize-OpenSSL-after-setting-env-vars.patch
Patch13:        openssl-ibmca-04-engine-Fix-compile-error.patch
Patch14:        openssl-ibmca-05-provider-Fix-segfault-with-openssl-list-key-managers.patch
Patch15:        openssl-ibmca-06-Provider-Fix-segfault-with-openssl-list-signature-algorithms-verbose.patch
###

%description
This package contains a shared object OpenSSL dynamic engine which interfaces
to libica, a library enabling the IBM s390/x CPACF crypto instructions.

%prep
%autosetup -p1 -n openssl-ibmca-%{version}
 ./bootstrap.sh

%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"

%if "%{flavor}" == ""
%configure \
  --libdir=%{modulesdir}
  mkdir -p %{buildroot}/%{enginesdir}
%endif

%if "%{flavor}" == "engine"
%configure \
  --disable-provider \
  --libdir=%{enginesdir}
%endif

%if "%{flavor}" == "provider"
%configure \
  --disable-engine \
  --libdir=%{modulesdir}
%endif

%make_build

%install
# Update the sample config file so that the dynamic path points
# to the correct version of the engines directory.
%if "%{flavor}" != "provider"
sed -i -e "/^dynamic_path/s, = .*/, = %{enginesdir}/," src/engine/openssl.cnf.sample
%endif

%make_install

%if "%{flavor}" == ""
mkdir -p %{buildroot}/%{enginesdir}
mv %{buildroot}/%{modulesdir}/ibmca.* %{buildroot}/%{enginesdir}/
%endif

rm -f %{buildroot}/%{enginesdir}/ibmca*.la
rm -f %{buildroot}/%{modulesdir}/ibmca*.la

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

mkdir -p %{sslengcnf}
mkdir -p %{sslengdef}
cp -p %{_datadir}/%{name}/openssl-ibmca.sectiondef.txt %{sslengcnf}/openssl-ibmca.cnf
cp -p %{_datadir}/%{name}/openssl-ibmca.enginedef.cnf %{sslengdef}/openssl-ibmca.cnf

%if "%{flavor}" == ""
if [ -f "%{_datadir}/doc/packages/openssl-ibmca/ibmca-engine-opensslconfig" ]; then
   cp -p %{_datadir}/doc/packages/openssl-ibmca/ibmca-engine-opensslconfig %{_datadir}/doc/packages/openssl-ibmca/ibmca-engine-opensslconfig.orig
   sed -e 's/ossl-modules/engines-3/' %{_datadir}/doc/packages/openssl-ibmca/ibmca-engine-opensslconfig.orig > %{_datadir}/doc/packages/openssl-ibmca/ibmca-engine-opensslconfig
   rm %{_datadir}/doc/packages/openssl-ibmca/ibmca-engine-opensslconfig.orig
fi
%endif

%postun
if [ $1 -eq 0 ]; then # last uninstall
  rm -f %{sslengcnf}/openssl-ibmca.cnf
  rm -f %{sslengdef}/openssl-ibmca.cnf
fi

%files
%license LICENSE
%doc ChangeLog
%doc README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/openssl-ibmca.sectiondef.txt
%{_datadir}/%{name}/openssl-ibmca.enginedef.cnf
%if "%{flavor}" == ""
    %doc src/engine/ibmca-engine-opensslconfig
    %doc src/provider/ibmca-provider-opensslconfig
    %doc src/engine/openssl.cnf.sample
    %{enginesdir}/ibmca.*
    %{modulesdir}/ibmca-provider.*
    %{_mandir}/man5/ibmca.5%{?ext_man}
    %{_mandir}/man5/ibmca-provider.5%{?ext_man}
%endif
%if "%{flavor}" == "provider"
    %doc src/provider/ibmca-provider-opensslconfig
    %{modulesdir}/ibmca-provider.*
    %{_mandir}/man5/ibmca-provider.5%{?ext_man}
%endif
%if "%{flavor}" == "engine"
    %doc src/engine/ibmca-engine-opensslconfig
    %doc src/engine/openssl.cnf.sample
    %{enginesdir}/ibmca.*
    %{_mandir}/man5/ibmca.5%{?ext_man}
%endif

%changelog
