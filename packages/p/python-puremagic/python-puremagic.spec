#
# spec file for package python-puremagic
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
Name:           python-puremagic
Version:        1.28
Release:        0
Summary:        Pure python implementation of magic file detection
License:        MIT
URL:            https://github.com/cdgriffith/puremagic
Source:         https://files.pythonhosted.org/packages/source/p/puremagic/puremagic-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pure python implementation of magic file detection

%prep
%autosetup -p1 -n puremagic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/puremagic
%{python_sitelib}/puremagic-%{version}.dist-info

%changelog
