#
# spec file for package python-bytecode
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-bytecode
Version:        0.14.0
Release:        0
Summary:        Python module to generate and modify bytecode
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/vstinner/bytecode
Source:         https://files.pythonhosted.org/packages/source/b/bytecode/bytecode-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.10}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-typing-extensions if python-base < 3.10)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python module to generate and modify bytecode

%prep
%setup -q -n bytecode-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/bytecode
%{python_sitelib}/bytecode-%{version}*-info

%changelog
