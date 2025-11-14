#
# spec file for package python-colorful
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-colorful
Version:        0.5.8
Release:        0
Summary:        Terminal string styling done right, in Python
License:        MIT
URL:            https://github.com/timofurrer/colorful
Source:         https://github.com/timofurrer/colorful/archive/refs/tags/v%{version}.tar.gz#/colorful-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
colorful gives you control over terminal string styling in Python
with an easy to use API.

%prep
%autosetup -p1 -n colorful-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/colorful
%{python_sitelib}/colorful-%{version}*-info

%changelog
