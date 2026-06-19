#
# spec file for package python-openapi-pydantic
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-openapi-pydantic
Version:        0.5.1
Release:        0
Summary:        OpenAPI (v3) specification schema as Pydantic classes
License:        MIT
URL:            https://github.com/mike-oakley/openapi-pydantic
Source:         https://files.pythonhosted.org/packages/source/o/openapi-pydantic/openapi_pydantic-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pydantic >= 1.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 1.8
BuildArch:      noarch
%python_subpackages

%description
OpenAPI (v3) specification schema expressed as Pydantic classes, for
parsing, validating and generating OpenAPI documents in Python.

%prep
%autosetup -p1 -n openapi_pydantic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/openapi_pydantic
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# -B so the import does not write fresh .pyc into the buildroot (mtime mismatch)
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import openapi_pydantic"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/openapi_pydantic
%{python_sitelib}/openapi_pydantic-%{version}.dist-info

%changelog
