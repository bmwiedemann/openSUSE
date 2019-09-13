#
# spec file for package python-httpstatus35
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
%if %{python3_version_nodots} > 34
%define skip_python3 1
%endif
Name:           python-httpstatus35
Version:        0.0.1
Release:        0
Summary:        Python 3.5 http.HTTPStatus backported to 3.4 and 27
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Gr1N/httpstatus35
Source:         https://files.pythonhosted.org/packages/source/h/httpstatus35/httpstatus35-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
Python 3.5 http.HTTPStatus backported to 3.4 and 2.7.

%prep
%setup -q -n httpstatus35-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
