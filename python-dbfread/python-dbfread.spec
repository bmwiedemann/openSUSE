#
# spec file for package python-dbfread
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
# Test directories messed up by python_expand
%bcond_without  test
Name:           python-dbfread
Version:        2.0.7
Release:        0
Summary:        DBF file reader for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/olemb/dbfread
Source:         https://files.pythonhosted.org/packages/source/d/dbfread/dbfread-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch

%python_subpackages

%description
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

%prep
%setup -q -n dbfread-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
rm -rf build
rm -rf _build.*
%{python_expand rm -rf build
py.test-%{$python_bin_suffix}
}
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
