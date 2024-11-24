#
# spec file for package python-types-humanfriendly
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
Name:           python-types-humanfriendly
Version:        10.0.1.20241105
Release:        0
Summary:        Typing stubs for humanfriendly
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python/typeshed
Source:         https://files.pythonhosted.org/packages/source/t/types-humanfriendly/types-humanfriendly-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Collection of library stubs for Python, with static types.

%prep
%autosetup -p1 -n types-humanfriendly-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m mypy humanfriendly-stubs

%files %{python_files}
%doc CHANGELOG.md
%{python_sitelib}/humanfriendly-stubs
%{python_sitelib}/types_humanfriendly-%{version}.dist-info

%changelog
