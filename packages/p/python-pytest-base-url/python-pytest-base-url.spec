#
# spec file for package python-pytest-base-url
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


Name:           python-pytest-base-url
Version:        2.0.0
Release:        0
Summary:        Pytest plugin for URL based testing
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-base-url
Source:         https://files.pythonhosted.org/packages/source/p/pytest-base-url/pytest-base-url-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.0.0
Requires:       python-requests >= 2.9
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module requests >= 2.9}
# /SECTION
%python_subpackages

%description
pytest plugin for URL based testing.

%prep
%setup -q -n pytest-base-url-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_url_fails'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_base_url
%{python_sitelib}/pytest_base_url-%{version}.dist-info

%changelog
