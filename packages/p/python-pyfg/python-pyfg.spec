#
# spec file for package python-pyfg
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyfg
Version:        0.50
Release:        0
Summary:        Python API for fortigate
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/spotify/pyfg
Source:         https://github.com/spotify/pyfg/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/spotify/pyfg/pull/29.patch
Patch1:         0001-Fixed-device.commit-with-vdoms.patch
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-paramiko
BuildArch:      noarch
%python_subpackages

%description
This API allows you to interact with a device runnine FortiOS in a sane way.
With this API you can:

 * Connect to the device, retrieve the running config (the entire config or
   some blocks, whatever you want) and build a model
 * Build the same model from a file
 * Do changes in the candidate configuration locally
 * Create a candidate configuration from a file
 * Do a diff between the running config and the local candidate config
 * Generate the necessary commands to go from the running configuration to
   the candidate configuration

%prep
%setup -q -n pyfg-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# disabled since tests need network access to a preconfigured fortinet device
#%%pytest test/unit/TestFortiOS.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
