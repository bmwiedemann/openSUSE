#
# spec file for package python-pylons-sphinx-themes
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
%define oldpython python
Name:           python-pylons-sphinx-themes
Version:        1.0.10
Release:        0
Summary:        Pylons Sphinx themes for documentation styling
License:        SUSE-Repoze
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/pylons-sphinx-themes
Source:         https://files.pythonhosted.org/packages/source/p/pylons-sphinx-themes/pylons-sphinx-themes-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Obsoletes:      python-pylons_sphinx_theme < %{version}
Provides:       python-pylons_sphinx_theme = %{version}
Obsoletes:      python-pylons_theme_support < %{version}
Provides:       python-pylons_theme_support = %{version}
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-pylons_sphinx_theme < %{version}
Provides:       %{oldpython}-pylons_sphinx_theme = %{version}
Obsoletes:      %{oldpython}-pylons_theme_support < %{version}
Provides:       %{oldpython}-pylons_theme_support = %{version}
%endif
%python_subpackages

%description
This repository is a Python package that contains Sphinx themes for Pylons
related projects. This project is based on Pylons Sphinx Theme (singular),
but uses a package implementation instead of git submodules and
manual steps.

To use a theme in your Sphinx documentation, follow the guide in README.md.

%prep
%setup -q -n pylons-sphinx-themes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt CONTRIBUTORS.txt README.md
%{python_sitelib}/pylons_sphinx_themes
%{python_sitelib}/pylons_sphinx_themes-%{version}-py*.egg-info

%changelog
