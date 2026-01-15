#
# spec file for package python-datamodel-code-generator
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%define upname datamodel_code_generator
Name:           python-datamodel-code-generator
Version:        0.42.2
Release:        0
Summary:        Datamodel Code Generator
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/koxudaxi/datamodel-code-generator/
Source0:        https://files.pythonhosted.org/packages/source/d/%{upname}/%{upname}-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module graphql-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PySnooper >= 0.4.1
Requires:       python-argcomplete >= 1.11.1
Requires:       python-black >= 19.10b0
Requires:       python-genson >= 1.2.1
Requires:       python-graphql-core
Requires:       python-inflect >= 4.1.0
Requires:       python-isort >= 4.3.21
Requires:       python-jinja2 >= 2.11.2
Requires:       python-openapi-spec-validator >= 0.2.8
Requires:       python-prance >= 0.18.2
Requires:       python-pydantic >= 1.5.1
Requires:       python-toml >= 0.10.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-httpx
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PySnooper >= 0.4.1}
BuildRequires:  %{python_module argcomplete >= 1.11.1}
BuildRequires:  %{python_module black >= 19.10b0}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module genson >= 1.2.1}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module inflect >= 4.1.0}
BuildRequires:  %{python_module inline-snapshot >= 0.31.1}
BuildRequires:  %{python_module isort >= 4.3.21}
BuildRequires:  %{python_module jinja2 >= 2.11.2}
BuildRequires:  %{python_module openapi-spec-validator >= 0.2.8}
BuildRequires:  %{python_module prance >= 0.18.2}
BuildRequires:  %{python_module pydantic >= 1.5.1}
BuildRequires:  %{python_module pydantic-core}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module time-machine >= 3.1}
BuildRequires:  %{python_module toml >= 0.10.1}
# /SECTION
%python_subpackages

%description
Python Datamodel Code Generator.

%prep
%setup -q -n %{upname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/datamodel-codegen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_openapi_parser_parse_remote_ref'

%post
%python_install_alternative datamodel-codegen

%postun
%python_uninstall_alternative datamodel-codegen

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/datamodel-codegen
%{python_sitelib}/datamodel[_-]code[_-]generator*/

%changelog
