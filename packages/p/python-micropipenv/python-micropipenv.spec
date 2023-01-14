#
# spec file for package python-micropipenv
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


%define modname micropipenv
Name:           python-micropipenv
Version:        1.4.5
Release:        0
Summary:        Convert various requirements-type files to use with pip-tools
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/thoth-station/micropipenv
Source:         https://github.com/thoth-station/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pip
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-toml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flexmock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A simple wrapper around pip to support requirements.txt, Pipenv and Poetry files for containerized applications

%prep
%autosetup -p1 -n %{modname}-%{version}

sed -i '1{\@^#!%{_bindir}/env python@d}' micropipenv.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/micropipenv
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative micropipenv

%postun
%python_uninstall_alternative micropipenv

%files %{python_files}
%doc README.rst
%license CHANGELOG.md LICENSE OWNERS
%python_alternative %{_bindir}/micropipenv
%pycache_only %{python_sitelib}/__pycache__/%{modname}*.pyc
%{python_sitelib}/%{modname}.py
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
