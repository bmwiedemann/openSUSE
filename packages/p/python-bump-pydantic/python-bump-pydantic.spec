#
# spec file for package python-bump-pydantic
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


Name:           python-bump-pydantic
Version:        0.8.0
Release:        0
Summary:        Convert Pydantic from V1 to V2
License:        MIT
URL:            https://github.com/pydantic/bump-pydantic
Source:         https://files.pythonhosted.org/packages/source/b/bump-pydantic/bump_pydantic-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module libcst >= 0.4.2}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module typer >= 0.7.0}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-libcst >= 0.4.2
Requires:       python-rich
Requires:       python-typer >= 0.7.0
Requires:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
Bump Pydantic is a tool to help you migrate your code from Pydantic V1 to V2.

%prep
%autosetup -p1 -n bump_pydantic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bump-pydantic
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative bump-pydantic

%postun
%python_uninstall_alternative bump-pydantic

%files %{python_files}
%python_alternative %{_bindir}/bump-pydantic
%{python_sitelib}/bump_pydantic
%{python_sitelib}/bump_pydantic-%{version}.dist-info

%changelog
