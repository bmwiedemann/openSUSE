#
# spec file for package python-traitlets
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


Name:           python-traitlets
Version:        5.8.0
Release:        0
Summary:        Traitlets Python configuration system
License:        BSD-3-Clause
URL:            https://github.com/ipython/traitlets
Source:         https://files.pythonhosted.org/packages/source/t/traitlets/traitlets-%{version}.tar.gz
Source99:       python-traitlets.rpmlintrc
BuildRequires:  %{python_module argcomplete >= 2.0}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A configuration system for Python applications.

%prep
%autosetup -p1 -n traitlets-%{version}
sed -i 's/--color yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%doc examples/
%license COPYING.md
%{python_sitelib}/traitlets/
%{python_sitelib}/traitlets-%{version}*-info

%changelog
