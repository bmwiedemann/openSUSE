#
# spec file for package python-pyproject-hooks
#
# Copyright (c) 2022 SUSE LLC
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

%define fname pyproject_hooks
Name:           python-pyproject-hooks
Version:        1.0.0
Release:        0
Summary:        Wrappers to call pyproject.toml-based build backend hooks
License:        MIT
URL:            https://github.com/pypa/pyproject-hooks
Source:         https://files.pythonhosted.org/packages/source/p/pyproject_hooks/%{fname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  fdupes
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
BuildArch:      noarch
%python_subpackages

%description
This is a low-level library for calling build-backends in ``pyproject.toml``-based project.
It provides the basic functionality to help write tooling that generates distribution files from Python projects.

If you want a tool that builds Python packages, you'll want to use https://github.com/pypa/build instead.
This is an underlying piece for `pip`, `build` and other "build frontends" use to call "build backends" within them.

Note: The ``pep517`` project has been replaced by this project (low level) and the ``build`` project (high level).

%prep
%setup -q -n %{fname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/pyproject_hooks
%{python_sitelib}/pyproject_hooks-%{version}.dist-info

%changelog
