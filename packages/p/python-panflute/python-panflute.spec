#
# spec file for package python-panflute
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


Name:           python-panflute
Version:        2.3.0
Release:        0
Summary:        Pandoc filters package for Python
License:        BSD-3-Clause
URL:            https://github.com/sergiocorreia/panflute
Source:         https://files.pythonhosted.org/packages/source/p/panflute/panflute-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-click
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python-configparser
BuildRequires:  python-shutilwhich
%endif
# /SECTION
%python_subpackages

%description
Panflute is a Python package for writing Pandoc filters.

%prep
%setup -q -n panflute-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/panfl
%python_clone -a %{buildroot}%{_bindir}/panflute
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative panfl
%python_install_alternative panflute

%postun
%python_uninstall_alternative panfl
%python_uninstall_alternative panflute

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/panflute
%python_alternative %{_bindir}/panfl
%{python_sitelib}/panflute
%{python_sitelib}/panflute-%{version}.dist-info

%changelog
