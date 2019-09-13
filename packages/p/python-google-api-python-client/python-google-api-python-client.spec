#
# spec file for package python-google-api-python-client
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
Name:           python-google-api-python-client
Version:        1.7.8
Release:        0
Summary:        Google APIs Python Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/google/google-api-python-client
Source:         https://files.pythonhosted.org/packages/source/g/google-api-python-client/google-api-python-client-%{version}.tar.gz
BuildRequires:  %{python_module google-auth >= 1.4.1}
BuildRequires:  %{python_module google-auth-httplib2 >= 0.0.3}
BuildRequires:  %{python_module httplib2 >= 0.9.2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  %{python_module unittest2}
BuildRequires:  %{python_module uritemplate  >= 3.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 1.4.1
Requires:       python-google-auth-httplib2 >= 0.0.3
Requires:       python-httplib2 >= 0.9.2
Requires:       python-six >= 1.6.1
Requires:       python-uritemplate >= 3.0.0
# Package renamed in SLE 12, do not remove Provides, Obsolete directives
# until after SLE 12 EOL
Provides:       google-api-python-client = %{version}
Obsoletes:      google-api-python-client < %{version}
BuildArch:      noarch
%python_subpackages

%description
Google APIs Client Library for Python

%prep
%setup -q -n google-api-python-client-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG
%license LICENSE
%{python_sitelib}/*

%changelog
