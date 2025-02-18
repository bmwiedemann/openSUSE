#
# spec file for package python-nine
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
Name:           python-nine
Version:        1.2.0
Release:        0
Summary:        Python 2 / 3 compatibility, like six, but favouring Python 3
License:        SUSE-Public-Domain
Group:          Development/Languages/Python
URL:            https://github.com/nandoflorestan/nine
Source:         https://files.pythonhosted.org/packages/source/n/nine/nine-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
python-nine is python-six "turned around": whereas python-six used
to make python2 idioms work in python3, python-nine makes python3
idioms work in python2.

%prep
%setup -q -n nine-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/nine
%{python_sitelib}/nine-%{version}.dist-info

%changelog
