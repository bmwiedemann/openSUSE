#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-mkdocs-material-extensions%{psuffix}
Version:        1.1.1
Release:        0
Summary:        Extension pack for Python Markdown
License:        MIT
URL:            https://github.com/facelessuser/mkdocs-material-extensions
Source:         https://files.pythonhosted.org/packages/source/m/mkdocs_material_extensions/mkdocs_material_extensions-%{version}.tar.gz
BuildRequires:  %{python_module hatch}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module Markdown}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module mkdocs-material}
BuildRequires:  %{python_module pytest}
# /SECTION
%endif
%python_subpackages

%description
Extension pack for Python Markdown

%prep
%setup -q -n mkdocs_material_extensions-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# skip TestEmoji.test_twemoji that needs internet access
%pytest -k 'not test_twemoji'
%endif

%if %{without test}
%files %{python_files}
%doc README.md changelog.md
%license LICENSE.md
%{python_sitelib}/materialx
%{python_sitelib}/mkdocs_material_extensions-%{version}.dist-info
%endif

%changelog
