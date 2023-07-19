#
# spec file for package python-jsonschema-spec
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
Name:           python-jsonschema-spec
Version:        0.2.3
Release:        0
Summary:        JSONSchema Spec with object-oriented paths
License:        Apache-2.0
URL:            https://github.com/p1c2u/jsonschema-spec
Source:         https://github.com/p1c2u/jsonschema-spec/archive/refs/tags/%{version}.tar.gz#/jsonschema-spec-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module pathable >= 0.4.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module referencing >= 0.28.0}
BuildRequires:  %{python_module responses >= 0.23.0}
BuildRequires:  %{python_module requests >= 2.31.0}
# /SECTION
Requires:       python-PyYAML >= 5.1
Requires:       python-pathable >= 0.4.1
Requires:       python-referencing >= 0.28.0
Suggests:       python-requests >= 2.31.0
Provides:       python-jsonschema_spec = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
JSONSchema Spec with object-oriented paths.

%prep
%setup -q -n jsonschema-spec-%{version}
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
%{python_sitelib}/jsonschema_spec
%{python_sitelib}/jsonschema_spec-%{version}.dist-info

%changelog
