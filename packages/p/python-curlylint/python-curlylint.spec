#
# spec file for package python-curlylint
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_without libalternatives
Name:           python-curlylint
Version:        0.13.1
Release:        0
Summary:        HTML templates linting for Jinja, Nunjucks, Django templates, Twig, Liquid
License:        MIT
URL:            https://github.com/thibaudcolas/curlylint
Source:         https://files.pythonhosted.org/packages/source/c/curlylint/curlylint-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#thibaudcolas/curlylint#158
Patch0:         avoid-resourcewarning.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
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
%autosetup -p1 -n curlylint-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/curlylint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative curlylint

# post and postun macro call is not needed with only libalternatives

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/curlylint
%{python_sitelib}/curlylint
%{python_sitelib}/curlylint-%{version}.dist-info

%changelog
