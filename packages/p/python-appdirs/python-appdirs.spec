#
# spec file for package python-appdirs
#
# Copyright (c) 2025 SUSE LLC
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


# in order to avoid rewriting for subpackage generator
%define mypython python
%{?sle15_python_module_pythons}
Name:           python-appdirs
Version:        1.4.4
Release:        0
Summary:        A small Python module for determining platform-specific dirs
License:        MIT
URL:            https://github.com/ActiveState/appdirs
Source:         https://files.pythonhosted.org/packages/source/a/appdirs/appdirs-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# work around boo#1186870
Provides:       %{mypython}%{python_version}dist(appdirs) = %{version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       %{mypython}3dist(appdirs) = %{version}
%endif
%python_subpackages

%description
``appdirs`` will
help you choose an appropriate:

- user data dir (``user_data_dir``)
- user cache dir (``user_cache_dir``)
- site data dir (``site_data_dir``)
- user log dir (``user_log_dir``)

%prep
%setup -q -n appdirs-%{version}

# strip shebang
sed -r -i '1s/^#!.*$//' appdirs.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/appdirs.py*
%{python_sitelib}/appdirs-%{version}.dist-info

%changelog
