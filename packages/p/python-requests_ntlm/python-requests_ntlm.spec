#
# spec file for package python-requests_ntlm
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
Name:           python-requests_ntlm
Version:        1.3.0
Release:        0
Summary:        NTLM authentication for the python-requests library
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/requests/requests-ntlm
Source:         https://github.com/requests/requests-ntlm/archive/v%{version}.tar.gz#/requests-ntlm-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module cryptography >= 1.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyspnego}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 1.3
Requires:       python-pyspnego
Requires:       python-requests >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
This package allows for HTTP NTLM authentication using
python-requests. HttpNtlmAuth extends requests' AuthBase, so it can
be dropped directly in place, or used in conjunction with a Session
to make use of connection pooling.

%prep
%setup -q -n requests-ntlm-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m tests.test_server &
%pytest --ignore tests/functional/test_functional.py --ignore tests/test_server.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/requests_ntlm
%{python_sitelib}/requests_ntlm-%{version}*-info

%changelog
