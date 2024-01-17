#
# spec file for package python-pynxos
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2017-2019, Martin Hauke <mardnh@gmx.de>
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


Name:           python-pynxos
Version:        0.0.5
Release:        0
Summary:        A library for managing Cisco NX-OS devices through NX-API
License:        Apache-2.0
URL:            https://github.com/networktocode/pynxos/
Source:         pynxos-%{version}.tar.xz
Patch0:         remove-future-requirement.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       python-scp
BuildArch:      noarch
# SECTION test requirements
#BuildRequires:  %%{python_module pytest}
#BuildRequires:  %%{python_module requests}
#BuildRequires:  %%{python_module scp}
# /SECTION
%python_subpackages

%description
A library for managing Cisco NX-OS devices through NX-API

%prep
%autosetup -p1 -n pynxos-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests are known to be broken - disable for now
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pynxos
%{python_sitelib}/pynxos-%{version}.dist-info

%changelog
