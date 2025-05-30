#
# spec file for package python-husl
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


%bcond_with     test
Name:           python-husl
Version:        4.0.3
Release:        0
Summary:        A Python implementation of the "Human-friendly HSL" (HSLuv) color model
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.husl-colors.org
Source:         https://files.pythonhosted.org/packages/source/h/husl/husl-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python implementation of HUSL (revision 3).

%prep
%setup -q -n husl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.md
%{python_sitelib}/husl.py
%{python_sitelib}/husl-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/husl*

%changelog
