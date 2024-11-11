#
# spec file for package python-nitrokey
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


Name:           python-nitrokey
Version:        0.2.3
Release:        0
Summary:        Nitrokey Python SDK
License:        Apache-2.0
URL:            https://github.com/Nitrokey/nitrokey-sdk-py
Source:         https://files.pythonhosted.org/packages/source/n/nitrokey/nitrokey-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The Nitrokey Python SDK can be used to use and configure Nitrokey devices.

%prep
%autosetup -p1 -n nitrokey-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSES LICENSES/Apache-2.0.txt LICENSES/MIT.txt
%{python_sitelib}/nitrokey
%{python_sitelib}/nitrokey-%{version}.dist-info

%changelog
