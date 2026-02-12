#
# spec file for package python-oras
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-oras
Version:        0.2.38
Release:        0
Summary:        OCI Registry as Storage Python SDK
License:        Apache-2.0
URL:            https://github.com/oras-project/oras-py
Source:         https://files.pythonhosted.org/packages/source/o/oras/oras-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
#
# SECTION runtime requirements
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module requests}
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jsonschema
Requires:       python-requests
Requires:       python-boto3 >= 1.33.0
Suggests:       python-docker == 5.0.1
BuildArch:      noarch
%python_subpackages

%description
OCI Registry as Storage Python SDK

%prep
%autosetup -p1 -n oras-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# ignore checks that need network connectivity
IGNORED_CHECKS="test_get_many_tags"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ssl_no_verify"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ssl_verify_fails_if_bad_ca"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_ssl_verify_fails_fast_if_bad_ca"
%pytest -k "not (${IGNORED_CHECKS})"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/oras
%{python_sitelib}/oras-%{version}.dist-info

%changelog
