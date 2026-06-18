#
# spec file for package python-uv-dynamic-versioning
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
Name:           python-uv-dynamic-versioning
Version:        0.14.0
Release:        0
Summary:        Dynamic versioning based on VCS tags for uv/hatch project
License:        MIT
URL:            https://github.com/ninoseki/uv-dynamic-versioning/
Source:         https://files.pythonhosted.org/packages/source/u/uv-dynamic-versioning/uv_dynamic_versioning-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module dunamai >= 1.26}
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module jinja2 >= 3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomlkit >= 0.13}
BuildRequires:  git
# /SECTION
BuildRequires:  fdupes
Requires:       python-dunamai >= 1.26
Requires:       python-hatchling >= 1.26
Requires:       python-jinja2 >= 3.0
Requires:       python-tomlkit >= 0.13
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
[poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning) influenced dynamic versioning tool for [uv](https://github.com/astral-sh/uv)/[hatch](https://github.com/pypa/hatch), powered by [dunamai](https://github.com/mtkennerly/dunamai/).

%prep
%autosetup -p1 -n uv_dynamic_versioning-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/uv-dynamic-versioning
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
git init
git config user.email "nobody@build.opensuse.org"
git add pyproject.toml
git commit -m "need at least one commit"
%pytest

%post
%python_install_alternative uv-dynamic-versioning

%postun
%python_uninstall_alternative uv-dynamic-versioning

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/uv-dynamic-versioning
%{python_sitelib}/uv_dynamic_versioning
%{python_sitelib}/uv_dynamic_versioning-%{version}.dist-info

%changelog
