#
# spec file for package python-typing-inspection
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
Name:           python-typing-inspection
Version:        0.4.2
Release:        0
Summary:        Runtime typing introspection tools
License:        MIT
URL:            https://github.com/pydantic/typing-inspection
Source:         https://files.pythonhosted.org/packages/source/t/typing-inspection/typing_inspection-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module typing-extensions >= 4.12.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing-extensions >= 4.12.0
BuildArch:      noarch
%python_subpackages

%description
typing-inspection provides tools to inspect type annotations at runtime.

The library can be imported from the typing_inspection module.

%prep
%autosetup -p1 -n typing_inspection-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/typing_inspection
%{python_sitelib}/typing_inspection-%{version}.dist-info

%changelog
