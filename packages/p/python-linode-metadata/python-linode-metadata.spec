#
# spec file for package python-linode-metadata
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-linode-metadata
Version:        0.3.3
Release:        0
Summary:        A client to interact with the Linode Metadata service in Python
License:        BSD-3-Clause
URL:            https://github.com/linode/py-metadata
Source:         https://files.pythonhosted.org/packages/source/l/linode-metadata/linode_metadata-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
# /SECTION
BuildRequires:  fdupes
Requires:       python-httpx
BuildArch:      noarch
%python_subpackages

%description
A client to interact with the Linode Metadata service in Python.

%prep
%autosetup -p1 -n linode_metadata-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Test suite requires internet

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/linode_metadata
%{python_sitelib}/linode_metadata-%{version}.dist-info

%changelog
