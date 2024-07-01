#
# spec file for package python-twine
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
Name:           python-twine
Version:        5.1.0
Release:        0
Summary:        Collection of utilities for interacting with PyPI
License:        Apache-2.0
URL:            https://github.com/pypa/twine
Source:         https://files.pythonhosted.org/packages/source/t/twine/twine-%{version}.tar.gz
Patch0:         0001-remove-disable-socket-pytest-opt.patch
# PATCH-FIX-UPSTREAM skip-unsupported-Metadata-Version-test.patch gh#pypa/twine#1071 mcepl@suse.com
# Skip failing test case
Patch1:         skip-unsupported-Metadata-Version-test.patch
BuildRequires:  %{python_module importlib-metadata >= 3.6}
BuildRequires:  %{python_module jaraco.envs}
BuildRequires:  %{python_module jaraco.packaging >= 9}
BuildRequires:  %{python_module keyring >= 15.1}
BuildRequires:  %{python_module munch}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkginfo >= 1.8.1}
BuildRequires:  %{python_module portend}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readme_renderer >= 35.0}
BuildRequires:  %{python_module requests >= 2.20}
BuildRequires:  %{python_module requests-toolbelt >= 0.8.0}
BuildRequires:  %{python_module rfc3986 >= 1.4.0}
BuildRequires:  %{python_module rich >= 12.0.0}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.0}
BuildRequires:  %{python_module urllib3 >= 1.26.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata >= 3.6
Requires:       python-keyring >= 15.1
Requires:       python-pkginfo >= 1.8.1
Requires:       python-readme_renderer >= 35.0
Requires:       python-requests >= 2.20
Requires:       python-requests-toolbelt >= 0.8.0
Requires:       python-rfc3986 >= 1.4.0
Requires:       python-rich >= 12.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Twine is a utility for publishing Python packages on PyPI.

Currently it supports registering projects, uploading distributions, and
checking, if descriptions will render correctly.

%prep
%autosetup -p1 -n twine-%{version}

sed -i '1s/^#!.*//' twine/__main__.py

%build
%pyproject_wheel

%install
%pyproject_install
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
%python_alternative %{_bindir}/twine
%{python_sitelib}/twine
%{python_sitelib}/twine-%{version}*-info

%changelog
