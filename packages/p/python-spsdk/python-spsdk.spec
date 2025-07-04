#
# spec file for package python-spsdk
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-spsdk
Version:        2.1.1
Release:        0
Summary:        Unified, reliable and easy to use SW library working across NXP MCU portfolio
License:        BSD-3-Clause
URL:            https://github.com/nxp-mcuxpresso/spsdk
Source:         https://files.pythonhosted.org/packages/source/s/spsdk/spsdk-%{version}.tar.gz
# PATCH-FIX-OPENSUSE python-spsdk-remove_pypemicro.patch
Patch0:         python-spsdk-remove_pypemicro.patch
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-asn1crypto
Requires:       python-astunparse
Requires:       python-bincopy
Requires:       python-bitstring
Requires:       python-click
Requires:       python-click-command-tree
Requires:       python-click-option-group
Requires:       python-colorama
Requires:       python-crcmod
Requires:       python-cryptography
Requires:       python-deepmerge
Requires:       python-fastjsonschema
Requires:       python-hexdump
Requires:       python-importlib_metadata
Requires:       python-libusbsio
Requires:       python-oscrypto
Requires:       python-platformdirs
Requires:       python-prettytable
Requires:       python-pylink-square
Requires:       python-pyocd
Requires:       python-pyserial
Requires:       python-requests
Requires:       python-ruamel.yaml
Requires:       python-sly
Requires:       python-typing-extensions
# Removed dependencies
# Requires:       python-pyocd-pemicro
# dependency no longer required due to Patch0
# Requires:       python-pypemicro
BuildArch:      noarch
%python_subpackages

%description
Secure Provisioning SDK (SPSDK) is unified, reliable and easy to use SW library working across NXP MCU portfolio providing strong foundation from quick customer prototyping up to production deployment.

%prep
%autosetup -p1 -n spsdk-%{version}

%build
%pyproject_wheel
find . -type f -name README.md -exec dos2unix {} +

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/blhost
%python_clone -a %{buildroot}%{_bindir}/ifr
%python_clone -a %{buildroot}%{_bindir}/nxpcrypto
%python_clone -a %{buildroot}%{_bindir}/nxpdebugmbox
%python_clone -a %{buildroot}%{_bindir}/nxpdevhsm
%python_clone -a %{buildroot}%{_bindir}/nxpdevscan
%python_clone -a %{buildroot}%{_bindir}/nxpele
%python_clone -a %{buildroot}%{_bindir}/nxpimage
%python_clone -a %{buildroot}%{_bindir}/pfr
%python_clone -a %{buildroot}%{_bindir}/sdphost
%python_clone -a %{buildroot}%{_bindir}/sdpshost
%python_clone -a %{buildroot}%{_bindir}/shadowregs
%python_clone -a %{buildroot}%{_bindir}/spsdk
%python_clone -a %{buildroot}%{_bindir}/tpconfig
%python_clone -a %{buildroot}%{_bindir}/tphost
%python_clone -a %{buildroot}%{_bindir}/dk6prog
%python_clone -a %{buildroot}%{_bindir}/nxpmemcfg
%python_clone -a %{buildroot}%{_bindir}/nxpwpc
# fix line endings
%python_expand find %{buildroot}%{$python_sitelib} -type f -exec dos2unix {} +
# remove shebangs
%python_expand find %{buildroot}%{$python_sitelib} -iname "*.py" -exec sed -i '1{/env python/d;}' {} +
# compile all here to avoid python-bytecode-inconsistent-mtime
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# remove unneccesary *.c and *.bin files
%python_expand rm -vf %{buildroot}%{$python_sitelib}/spsdk/data/cpu_data/*.c %{buildroot}%{$python_sitelib}/spsdk/data/cpu_data/*.bin

%pre
%python_libalternatives_reset_alternative blhost

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/spsdk/
%{python_sitelib}/spsdk-%{version}.dist-info/
%python_alternative %{_bindir}/blhost
%python_alternative %{_bindir}/ifr
%python_alternative %{_bindir}/nxpcrypto
%python_alternative %{_bindir}/nxpdebugmbox
%python_alternative %{_bindir}/nxpdevhsm
%python_alternative %{_bindir}/nxpdevscan
%python_alternative %{_bindir}/nxpele
%python_alternative %{_bindir}/nxpimage
%python_alternative %{_bindir}/pfr
%python_alternative %{_bindir}/sdphost
%python_alternative %{_bindir}/sdpshost
%python_alternative %{_bindir}/shadowregs
%python_alternative %{_bindir}/spsdk
%python_alternative %{_bindir}/tpconfig
%python_alternative %{_bindir}/tphost
%python_alternative %{_bindir}/dk6prog
%python_alternative %{_bindir}/nxpmemcfg
%python_alternative %{_bindir}/nxpwpc

%changelog
