#
# spec file for package python-django-codemod
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-codemod
Version:        0.13.0
Release:        0
Summary:        Collections of libCST codemodders to upgrade Django
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/browniebroke/django-codemod
Source:         https://files.pythonhosted.org/packages/source/d/django-codemod/django-codemod-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-libcst
Requires:       python-rich
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module libcst}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module rich}
# /SECTION
%python_subpackages

%description
Collections of libCST codemodders to upgrade Django.

%prep
%setup -q -n django-codemod-%{version}
sed -i 's/rich<5/rich/' setup.cfg
sed -i '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/djcodemod
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative djcodemod

%postun
%python_uninstall_alternative djcodemod

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/djcodemod
%{python_sitelib}/*

%changelog
