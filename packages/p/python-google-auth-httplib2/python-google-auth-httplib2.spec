#
# spec file for package python-google-auth-httplib2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-google-auth-httplib2
Version:        0.0.3
Release:        0
Summary:        Google Authentication Library: httplib2 transport
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2
Source:         https://files.pythonhosted.org/packages/source/g/google-auth-httplib2/google-auth-httplib2-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module httplib2 >= 0.9.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth
Requires:       python-httplib2 >= 0.9.1
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This library provides an `httplib2`_ transport for `google-auth`_.

%prep
%setup -q -n google-auth-httplib2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
