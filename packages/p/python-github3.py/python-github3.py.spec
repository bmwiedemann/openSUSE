#
# spec file for package python-github3.py
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


Name:           python-github3.py
Version:        4.0.1
Release:        0
Summary:        Python wrapper for the GitHub API
License:        BSD-3-Clause
URL:            https://github.com/sigmavirus24/github3.py
Source0:        https://files.pythonhosted.org/packages/source/g/github3.py/github3.py-%{version}.tar.gz
Source20:       https://raw.githubusercontent.com/sigmavirus24/github3.py/%{version}/tests/id_rsa.pub
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 2.3.0
Requires:       python-jwcrypto >= 0.5.0
Requires:       python-python-dateutil >= 2.6.0
Requires:       python-requests >= 2.18
Requires:       python-uritemplate >= 3.0.0
Recommends:     python-ndg-httpsclient
Recommends:     python-pyOpenSSL
Recommends:     python-pyasn1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module betamax >= 0.8.0}
BuildRequires:  %{python_module PyJWT >= 2.3.0}
BuildRequires:  %{python_module betamax-matchers >= 0.1.0}
BuildRequires:  %{python_module jwcrypto >= 0.5.0}
BuildRequires:  %{python_module pytest > 2.3.5}
BuildRequires:  %{python_module python-dateutil >= 2.6.0}
BuildRequires:  %{python_module requests >= 2.18}
BuildRequires:  %{python_module uritemplate >= 3.0.0}
# /SECTION
%python_subpackages

%description
Github3.py is wrapper for v3 of the GitHub API written in python.

%prep
%setup -q -n github3.py-%{version}
cp %{SOURCE20} tests/

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -c /dev/null -k 'not (test_patch or test_diff)'

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/github3
%{python_sitelib}/github3.py-%{version}.dist-info

%changelog
