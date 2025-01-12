#
# spec file for package python-dataclasses-json
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
Name:           python-dataclasses-json
Version:        0.6.7
Release:        0
Summary:        API for encoding and decoding dataclasses to and from JSON
License:        MIT
URL:            https://github.com/lidatong/dataclasses-json
Source:         https://github.com/lidatong/dataclasses-json/archive/refs/tags/v%{version}.tar.gz#/dataclasses-json-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#lidatong/dataclasses-json#553
Patch0:         support-poetry-core-2.patch
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module marshmallow}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module poetry-dynamic-versioning}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-inspect}
BuildRequires:  fdupes
Requires:       python-marshmallow
Requires:       python-typing-inspect
BuildArch:      noarch
%python_subpackages

%description
This library provides a simple API for encoding and decoding dataclasses to and from JSON.

It's very easy to get started.

%prep
%autosetup -n  dataclasses-json-%{version}
sed -i '/\[tool.poetry-dynamic-versioning\]/,+1d' pyproject.toml
sed -i 's/version = "0.0.0"/version = "%{version}"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install --no-build-isolation
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pytest

%files %python_files
%license LICENSE
%doc README.md
%{python_sitelib}/dataclasses_json
%{python_sitelib}/dataclasses_json-%{version}.dist-info

%changelog
