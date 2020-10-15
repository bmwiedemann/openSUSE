#
# spec file for package python-google-api-core
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
Name:           python-google-api-core
Version:        1.22.4
Release:        0
Summary:        Google API client core library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googleapis/python-api-core
Source:         https://files.pythonhosted.org/packages/source/g/google-api-core/google-api-core-%{version}.tar.gz
BuildRequires:  %{python_module google-auth >= 1.21.1}
BuildRequires:  %{python_module googleapis-common-protos >= 1.6.0}
BuildRequires:  %{python_module grpcio >= 1.29.0}
BuildRequires:  %{python_module grpcio-gcp >= 0.2.2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module protobuf >= 3.12.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.18.0}
BuildRequires:  %{python_module setuptools >= 34.0.0}
BuildRequires:  %{python_module six >= 1.13.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-google-auth >= 1.21.1
Requires:       python-googleapis-common-protos >= 1.6.0
Requires:       python-grpcio >= 1.29.0
Requires:       python-protobuf >= 3.12.0
Requires:       python-pytz
Requires:       python-requests >= 2.18.0
Requires:       python-setuptools >= 34.0.0
Requires:       python-six >= 1.13.0
Suggests:       python-grpcio-gcp >= 0.2.2
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-enum34
BuildRequires:  python2-futures >= 3.2.0
%endif
%ifpython2
Requires:       python-enum34
Requires:       python-futures >= 3.2.0
%endif
%python_subpackages

%description
Core Library for Google Client Libraries.

%prep
%setup -q -n google-api-core-%{version}

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
