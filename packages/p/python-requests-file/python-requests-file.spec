#
# spec file for package python-requests-file
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without tests
Name:           python-requests-file
Version:        1.4.3
Release:        0
Summary:        File transport adapter for Requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/dashea/requests-file
Source:         https://files.pythonhosted.org/packages/source/r/requests-file/requests-file-%{version}.tar.gz
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
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

%if %{with tests}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
