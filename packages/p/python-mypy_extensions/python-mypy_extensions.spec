#
# spec file for package python-mypy_extensions
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
Name:           python-mypy_extensions
Version:        1.0.0
Release:        0
Summary:        Experimental type system extensions for programs checked with mypy typechecker
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.mypy-lang.org/
Source:         https://files.pythonhosted.org/packages/source/m/mypy_extensions/mypy_extensions-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
The "mypy_extensions" module defines experimental extensions to the
standard "typing" module that are supported by the mypy typechecker.

%prep
%setup -q -n mypy_extensions-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
