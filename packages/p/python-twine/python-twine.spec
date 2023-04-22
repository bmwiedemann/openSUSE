#
# spec file for package python-twine
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
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-twine
Version:        3.4.1
Release:        0
Summary:        Collection of utilities for interacting with PyPI
License:        Apache-2.0
URL:            https://github.com/pypa/twine
Source:         https://files.pythonhosted.org/packages/source/t/twine/twine-%{version}.tar.gz
Patch1:         0001-remove-disable-socket-pytest-opt.patch
BuildRequires:  %{python_module colorama >= 0.4.3}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module jaraco.envs}
BuildRequires:  %{python_module keyring >= 15.1}
BuildRequires:  %{python_module munch}
BuildRequires:  %{python_module pkginfo >= 1.4.2}
BuildRequires:  %{python_module portend}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readme_renderer >= 21.0}
BuildRequires:  %{python_module requests >= 2.20}
BuildRequires:  %{python_module requests-toolbelt >= 0.8.0}
BuildRequires:  %{python_module rfc3986 >= 1.4.0}
BuildRequires:  %{python_module setuptools >= 0.7.0}
BuildRequires:  %{python_module setuptools_scm >= 1.15}
BuildRequires:  %{python_module tqdm >= 4.14}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama >= 0.4.3
Requires:       python-importlib-metadata
Requires:       python-keyring >= 15.1
Requires:       python-pkginfo >= 1.4.2
Requires:       python-readme_renderer >= 21.0
Requires:       python-requests >= 2.20
Requires:       python-requests-toolbelt >= 0.8.0
Requires:       python-rfc3986 >= 1.4.0
Requires:       python-setuptools >= 0.7.0
Requires:       python-tqdm >= 4.14
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Twine is a utility for publishing Python packages on PyPI.

Currently it supports registering projects, uploading distributions, and
checking, if descriptions will render correctly.

%prep
%setup -q -n twine-%{version}
%patch1 -p1

sed -i '1s/^#!.*//' twine/__main__.py
sed -i 's/--cov.*$//' pytest.ini

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/twine
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# do not run integration tests
rm tests/test_integration.py
# test_check_status_code_for_wrong_repo_url is online test
%pytest -k 'not test_check_status_code_for_wrong_repo_url'

%post
%python_install_alternative twine

%postun
%python_uninstall_alternative twine

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%dir %{python_sitelib}/twine
%dir %{python_sitelib}/twine-%{version}-py*.egg-info
%{python_sitelib}/twine/*
%{python_sitelib}/twine-%{version}-py*.egg-info/*
%python_alternative %{_bindir}/twine

%changelog
