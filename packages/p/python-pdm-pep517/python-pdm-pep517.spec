#
# spec file for package python-pdm-pep517
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pdm-pep517
Version:        0.10.1
Release:        0
Summary:        Python Development Master
License:        MIT
URL:            https://pdm-pep517.fming.dev://github.com/frostming/pdm-pep517
Source:         https://files.pythonhosted.org/packages/source/p/pdm-pep517/pdm-pep517-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PDM is a modern Python package manager with PEP 582 support. It
installs and manages packages in a similar way to npm that
doesn't need to create a virtualenv at all!

%prep
%autosetup -p1 -n pdm-pep517-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_project_version_use_scm'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pdm*

%changelog
