#
# spec file for package python-uritemplate
#
# Copyright (c) 2023 SUSE LLC
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


%global skip_python2 1
%bcond_without tests
Name:           python-uritemplate
Version:        4.1.1
Release:        0
Summary:        URI Template Expansison
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/uritemplate
Source:         https://files.pythonhosted.org/packages/source/u/uritemplate/uritemplate-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a Python implementation of RFC6570, URI Template, and can expand
templates up to and including Level 4 in that specification

%prep
%autosetup -p1 -n uritemplate-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python tests/test_uritemplate.py
}
%endif

%files %{python_files}
%license LICENSE LICENSE.*
%doc AUTHORS.rst HISTORY.rst README.rst
%{python_sitelib}/uritemplate
%{python_sitelib}/uritemplate-%{version}*-info

%changelog
