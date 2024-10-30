#
# spec file for package python-multidict
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
Name:           python-multidict
Version:        6.1.0
Release:        0
Summary:        Multidict implementation
License:        Apache-2.0
URL:            https://github.com/aio-libs/multidict
Source:         https://files.pythonhosted.org/packages/source/m/multidict/multidict-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing-extensions
%python_subpackages

%description
Multidicts are useful for working with HTTP headers, URL query
arguments, etc.

The code was extracted from the aiohttp library.

%prep
%autosetup -p1 -n multidict-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# remove the extra pytest opts
rm pytest.ini
# test_circular_imports try to import from the system and the module
# is installed in the buildroot at this point.
%pytest_arch --ignore tests/test_circular_imports.py

%files %{python_files}
%license LICENSE
%doc docs/changes.rst README.rst
%{python_sitearch}/multidict
%{python_sitearch}/multidict-%{version}*-info

%changelog
