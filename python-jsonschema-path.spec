#
# spec file for package python-jsonschema-path
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
Name:           python-jsonschema-path
Version:        0.3.3
Release:        0
Summary:        JSONSchema Spec with object-oriented paths
License:        Apache-2.0
URL:            https://github.com/p1c2u/jsonschema-path
Source:         https://github.com/p1c2u/jsonschema-path/archive/refs/tags/%{version}.tar.gz#/jsonschema-path-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module pathable >= 0.4.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module referencing >= 0.28.0}
BuildRequires:  %{python_module requests >= 2.31.0}
BuildRequires:  %{python_module responses >= 0.23.0}
# /SECTION
Requires:       python-PyYAML >= 5.1
Requires:       python-pathable >= 0.4.1
Requires:       python-referencing >= 0.28.0
Suggests:       python-requests >= 2.31.0
Provides:       python-jsonschema_path = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
JSONSchema Spec with object-oriented paths.

%prep
%setup -q -n jsonschema-path-%{version}
# unpin and hope for the best
sed -i '/referencing/ s/,<0.30.0//' pyproject.toml
# Remove need to pytest-cov
sed -i '/--cov/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/jsonschema_path
%{python_sitelib}/jsonschema_path-%{version}.dist-info

%changelog
