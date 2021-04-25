#
# spec file for package python-curlylint
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-curlylint
Version:        0.12.2
Release:        0
Summary:        HTML templates linting for Jinja, Nunjucks, Django templates, Twig, Liquid
License:        MIT
URL:            https://github.com/thibaudcolas/curlylint
Source:         https://files.pythonhosted.org/packages/source/c/curlylint/curlylint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17.2.0
Requires:       python-click >= 6.5
Requires:       python-parsy >= 1.1.0
Requires:       python-pathspec >= 0.6
Requires:       python-toml >= 0.9.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 17.2.0}
BuildRequires:  %{python_module click >= 6.5}
BuildRequires:  %{python_module parsy >= 1.1.0}
BuildRequires:  %{python_module pathspec >= 0.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml >= 0.9.4}
# /SECTION
%python_subpackages

%description
HTML templates linting for Jinja, Nunjucks, Django templates, Twig, Liquid.

%prep
%setup -q -n curlylint-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/curlylint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative curlylint

%postun
%python_uninstall_alternative curlylint

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/curlylint
%{python_sitelib}/*

%changelog
