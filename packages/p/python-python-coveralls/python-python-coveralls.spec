#
# spec file for package python-python-coveralls
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
Name:           python-python-coveralls
Version:        2.9.3
Release:        0
Summary:        Python interface to coveralls io API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/z4r/python-coveralls
Source:         https://files.pythonhosted.org/packages/source/p/python-coveralls/python-coveralls-%{version}.tar.gz
Source1:        python-coveralls-example.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-coverage >= 4.4
Requires:       python-requests
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      python-coveralls
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module coverage >= 4.4}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Python interface to coveralls.io API
This package provides a module to interface with the https://coveralls.io API.

%prep
%setup -q -n python-coveralls-%{version}
sed -i 's|coverage==4.0.3|coverage>=4.0.3|' setup.py
tar -xvzf %{SOURCE1}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/coveralls
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd python-coveralls-example
%pytest example/tests.py --cov=example
popd

%post
%python_install_alternative coveralls

%postun
%python_uninstall_alternative coveralls

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/coveralls
%{python_sitelib}/*

%changelog
