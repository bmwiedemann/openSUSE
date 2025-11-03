#
# spec file for package python-google-auth-httplib2
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


%{?sle15_python_module_pythons}
Name:           python-google-auth-httplib2
Version:        0.2.1
Release:        0
Summary:        Google Authentication Library: httplib2 transport
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2
Source:         https://files.pythonhosted.org/packages/source/g/google_auth_httplib2/google_auth_httplib2-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module google-auth > 1.32.0}
BuildRequires:  %{python_module httplib2 >= 0.19.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 1.32.0
Requires:       python-httplib2 >= 0.19.0
BuildArch:      noarch
%python_subpackages

%description
This library provides an `httplib2`_ transport for `google-auth`_.

%prep
%autosetup -p1 -n google_auth_httplib2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/google_auth_httplib2.py
%pycache_only %{python_sitelib}/__pycache__/google_auth_httplib*
%{python_sitelib}/google_auth_httplib2-%{version}.dist-info

%changelog
