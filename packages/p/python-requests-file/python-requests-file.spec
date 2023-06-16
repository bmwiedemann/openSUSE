#
# spec file for package python-requests-file
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-requests-file
Version:        1.5.1
Release:        0
Summary:        File transport adapter for Requests
License:        Apache-2.0
URL:            https://github.com/dashea/requests-file
Source:         https://files.pythonhosted.org/packages/source/r/requests-file/requests-file-%{version}.tar.gz
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Requests-File is a transport adapter for use with the Requests Python
library to allow local filesystem access via file:// URLs.

%prep
%setup -q -n requests-file-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/requests_file.py
%pycache_only %{python_sitelib}/__pycache__/requests_file.*.py*
%{python_sitelib}/requests_file-%{version}*info

%changelog
