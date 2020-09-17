#
# spec file for package python-gabbi
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-gabbi
Version:        2.0.4
Release:        0
Summary:        Declarative HTTP testing library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/cdent/gabbi
Source:         https://files.pythonhosted.org/packages/source/g/gabbi/gabbi-%{version}.tar.gz
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module jsonpath-rw-ext >= 1.0.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module urllib3 >= 1.11.0}
BuildRequires:  %{python_module wsgi_intercept >= 1.8.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-certifi
Requires:       python-colorama
Requires:       python-jsonpath-rw-ext >= 1.0.0
Requires:       python-pytest
Requires:       python-six
Requires:       python-urllib3 >= 1.11.0
Requires:       python-wsgi_intercept >= 1.8.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form. See the docs_ for
more details on features and formats.

%prep
%setup -q -n gabbi-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/gabbi-run

%post
%python_install_alternative gabbi-run

%postun
%python_uninstall_alternative gabbi-run

%check
# require network
rm -v gabbi/tests/test_live.py gabbi/tests/test_intercept.py
%python_exec -m stestr.cli run --black-regex 'gabbi.tests.test_runner.RunnerTest.test_custom_response_handler'

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/gabbi-run

%changelog
