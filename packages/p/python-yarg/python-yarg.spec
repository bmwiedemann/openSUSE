#
# spec file for package python-yarg
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-yarg
Version:        0.1.9
Release:        0
Summary:        A PyPI client
License:        MIT
Group:          Development/Languages/Python
URL:            https://yarg.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/y/yarg/yarg-%{version}.tar.gz
Source1:        test-data-cf67924.tgz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
A PyPI client.

%prep
%setup -q -n yarg-%{version}
tar -xzf %{SOURCE1}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests

%check
# https://github.com/kura/yarg/issues/8
sed -i 's:from mock:from unittest.mock:' tests/test_*.py
%pyunittest discover -v

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE LICENSE-REQUESTS
%{python_sitelib}/*

%changelog
