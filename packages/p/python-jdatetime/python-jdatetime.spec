#
# spec file for package python-jdatetime
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


%{?sle15_python_module_pythons}
Name:           python-jdatetime
Version:        5.1.0
Release:        0
Summary:        Jalali datetime binding for python
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/slashmili/python-jalali
Source:         https://github.com/slashmili/python-jalali/archive/v%{version}.tar.gz
BuildRequires:  %{python_module jalali-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytzdata}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  glibc-locale
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-jalali-core
%python_subpackages

%description
jdatetime is the Jalali implementation of Python's datetime module.

%prep
%autosetup -p1 -n python-jalali-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover tests -v

%files %{python_files}
%doc README.rst CHANGELOG.md
%license LICENSE
%{python_sitelib}/jdatetime
%{python_sitelib}/jdatetime-%{version}.dist-info

%changelog
