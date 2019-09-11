#
# spec file for package python-requests_ntlm
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
Name:           python-requests_ntlm
Version:        1.1.0
Release:        0
Summary:        NTLM authentication for the python-requests library
License:        ISC
Group:          Development/Languages/Python
Url:            https://github.com/requests/requests-ntlm
Source:         https://github.com/requests/requests-ntlm/archive/v%{version}.tar.gz#/requests-ntlm-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module cryptography >= 1.3}
BuildRequires:  %{python_module ntlm-auth >= 1.0.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 1.3
Requires:       python-ntlm-auth >= 1.0.2
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#%%python_exec -m tests.test_server &
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_version}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
