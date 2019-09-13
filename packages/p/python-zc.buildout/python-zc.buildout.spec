#
# spec file for package python-zc.buildout
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%{!?license: %global license %doc}
Name:           python-zc.buildout
Version:        2.13.2
Release:        0
Url:            http://pypi.python.org/pypi/zc.buildout
Summary:        System for managing development buildouts
License:        ZPL-2.1
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/z/zc.buildout/zc.buildout-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
# disabled because of unprovideable requirements and not shipped test files
#BuildRequires:  %%{python_module bobo}
#BuildRequires:  %%{python_module manuel}
#BuildRequires:  %%{python_module zc.recipe.deployment}
#BuildRequires:  %%{python_module zc.zdaemonrecipe}
#BuildRequires:  %%{python_module zdaemon}
#BuildRequires:  %%{python_module zope.testing}
# /SECTION
BuildArch:      noarch
Provides:       python-zc_buildout = %version
Obsoletes:      python-zc_buildout < %version

%python_subpackages

%description
System for managing development buildouts.

Buildout is a project designed to solve 2 problems:
 * Application-centric assembly and deployment
 * Repeatable assembly of programs from Python software distributions

%prep
%setup -q -n zc.buildout-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/zc/buildout
%python_expand %fdupes %{buildroot}%{$python_sitelib}/zc.buildout-2.9.5-py%{$python_version}.egg-info

#%%check
#%%python_exec setup.py test

%files %{python_files}
%doc README.rst CHANGES.rst COPYRIGHT.txt DEVELOPERS.txt
%license LICENSE.txt
%{python_sitelib}/*
%python3_only %{_bindir}/buildout

%changelog
