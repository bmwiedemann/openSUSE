#
# spec file for package python-django-codemod
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


Name:           python-django-codemod
Version:        2.4.5
Release:        0
Summary:        Collections of libCST codemodders to upgrade Django
License:        MIT
URL:            https://github.com/browniebroke/django-codemod
Source:         https://files.pythonhosted.org/packages/source/d/django-codemod/django_codemod-%{version}.tar.gz
Source1:        conftest.py
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-libcst
Requires:       python-pathspec
Requires:       python-rich
Requires:       python-rich-click
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module libcst}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pathspec}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich-click}
# /SECTION
%python_subpackages

%description
Collections of libCST codemodders to upgrade Django.

%prep
%autosetup -p1 -n django_codemod-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/django_codemod/
%{python_sitelib}/django_codemod-%{version}.dist-info

%changelog
