#
# spec file for package python-mkdocs-get-deps
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


%{?sle15_python_module_pythons}
Name:           python-mkdocs-get-deps
Version:        0.2.2
Release:        0
Summary:        MkDocs extension that lists all dependencies according to a mkdocsyml file
License:        MIT
URL:            https://github.com/mkdocs/get-deps
Source:         https://files.pythonhosted.org/packages/source/m/mkdocs-get-deps/mkdocs_get_deps-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module mergedeep >= 1.3.4}
BuildRequires:  %{python_module platformdirs >= 2.2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML >= 5.1
Requires:       python-mergedeep >= 1.3.4
Requires:       python-platformdirs >= 2.2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
An extra command for MkDocs that infers required PyPI packages from plugins in mkdocs.yml.

%prep
%autosetup -p1 -n mkdocs_get_deps-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mkdocs-get-deps
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative mkdocs-get-deps

%postun
%python_uninstall_alternative mkdocs-get-deps

%files %{python_files}
%python_alternative %{_bindir}/mkdocs-get-deps
%{python_sitelib}/mkdocs_get_deps
%{python_sitelib}/mkdocs_get_deps-%{version}.dist-info

%changelog
