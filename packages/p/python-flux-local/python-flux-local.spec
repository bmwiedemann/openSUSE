#
# spec file for package python-flux-local
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
Name:           python-flux-local
Version:        7.0.0
Release:        0
Summary:        Set of tools for managing a flux gitops repository
License:        Apache-2.0
URL:            https://github.com/allenporter/flux-local
Source:         https://files.pythonhosted.org/packages/source/f/flux-local/flux_local-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
#
BuildRequires:  %{python_module aiofiles >= 24.1.0}
BuildRequires:  %{python_module GitPython >= 3.1.43}
BuildRequires:  %{python_module mashumaro >= 3.15}
BuildRequires:  %{python_module nest-asyncio >= 1.6.0}
BuildRequires:  %{python_module PyYAML >= 6.0.2}
BuildRequires:  %{python_module python-slugify >= 8.0.4}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.3.3}
BuildRequires:  %{python_module pytest-asyncio >= 0.25.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-aiofiles >= 24.1.0
Requires:       python-GitPython >= 3.1.43
Requires:       python-mashumaro >= 3.15
Requires:       python-nest-asyncio >= 1.6.0
Requires:       python-python-slugify >= 8.0.4
Requires:       python-PyYAML >= 6.0.2
# Note: flux-local provides repo testing using pytest
Requires:       python-pytest >= 8.3.3
Requires:       python-pytest-asyncio >= 0.25.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
flux-local is a python library and set of tools for managing a flux gitops
repository, with validation steps to help improve quality of commits, PRs, and
general local testing.

%prep
%autosetup -p1 -n flux_local-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/flux-local
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative flux-local

%postun
%python_uninstall_alternative flux-local

%files %{python_files}
%python_alternative %{_bindir}/flux-local
%{python_sitelib}/flux_local
%pycache_only %{python_sitelib}/flux_local/__pycache__/
%{python_sitelib}/flux_local-%{version}.dist-info

%changelog
