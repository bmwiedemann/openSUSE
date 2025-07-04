#
# spec file for package python-requestsexceptions
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


Name:           python-requestsexceptions
Version:        1.4.0
Release:        0
Summary:        Import exceptions from potentially bundled packages in requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://www.openstack.org/
Source:         https://files.pythonhosted.org/packages/source/r/requestsexceptions/requestsexceptions-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The python requests library bundles the urllib3 library, however, some
software distributions modify requests to remove the bundled library.
This makes some operations, such as supressing the "insecure platform
warning" messages that urllib emits difficult.  This is a simple
library to find the correct path to exceptions in the requests library
regardless of whether they are bundled.

%prep
%setup -q -n requestsexceptions-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
# no tests found

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/requestsexceptions
%{python_sitelib}/requestsexceptions-%{version}*-info

%changelog
