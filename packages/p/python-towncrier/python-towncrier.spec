#
# spec file for package python-towncrier
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
Name:           python-towncrier
Version:        24.8.0
Release:        0
Summary:        Building newsfiles for your project
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hawkowl/towncrier
Source:         https://files.pythonhosted.org/packages/source/t/towncrier/towncrier-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module importlib-metadata >= 4.6 if %python-base < 3.10}
BuildRequires:  %{python_module importlib-resources >= 5 if %python-base < 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-Jinja2
Requires:       python-click
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata >= 4.6
Requires:       python-importlib-resources >= 5
%endif
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Building newsfiles for your project.

%prep
%setup -q -n towncrier-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/towncrier
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative towncrier

%postun
%python_uninstall_alternative towncrier

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/towncrier
%{python_sitelib}/towncrier
%{python_sitelib}/towncrier-%{version}.dist-info

%changelog
