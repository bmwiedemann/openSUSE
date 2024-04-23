#
# spec file for package python-betamax
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


%{?sle15_python_module_pythons}
Name:           python-betamax
Version:        0.9.0
Release:        0
Summary:        A VCR imitation for python-requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/sigmavirus24/betamax
Source:         https://files.pythonhosted.org/packages/source/b/betamax/betamax-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.0
BuildArch:      noarch
%python_subpackages

%description
Betamax is a VCR_ imitation for requests. This will make mocking out requests
much easier.

%prep
%setup -q -n betamax-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/betamax
%{python_sitelib}/betamax-%{version}.dist-info

%changelog
