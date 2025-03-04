#
# spec file for package python-pyeapi
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


%{?sle15_python_module_pythons}
Name:           python-pyeapi
Version:        1.0.4
Release:        0
Summary:        Python Client for eAPI
License:        BSD-3-Clause
URL:            https://github.com/arista-eosplus/pyeapi
Source:         https://files.pythonhosted.org/packages/source/p/pyeapi/pyeapi-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-netaddr
BuildArch:      noarch
%python_subpackages

%description
The Python Client for eAPI (pyeapi) is a native Python library wrapper around
Arista EOS eAPI.  It provides a set of Python language bindings for configuring
Arista EOS nodes.

The Python library can be used to communicate with EOS either locally
(on-box) or remotely (off-box). It uses a standard INI-style configuration file
to specify one or more nodes and connection profiles.

The pyeapi library also provides an API layer for building native Python
objects to interact with the destination nodes. The API layer is a convenient
implementation for working with the EOS configuration and is extensible for
developing custom implementations.

%prep
%autosetup -p1 -n pyeapi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}

%check
%pytest test/unit

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%doc examples
%{python_sitelib}/pyeapi
%{python_sitelib}/pyeapi-%{version}.dist-info

%changelog
