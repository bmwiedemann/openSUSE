#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-pdm-pep517%{psuffix}
Version:        1.0.6
Release:        0
Summary:        Python Development Master
License:        MIT
URL:            https://github.com/pdm-project/pdm-pep517
Source:         https://files.pythonhosted.org/packages/source/p/pdm-pep517/pdm-pep517-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pdm-pep517 = %{version}}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  git-core
%endif
# /SECTION
%python_subpackages

%description
PDM is a modern Python package manager with PEP 582 support. It
installs and manages packages in a similar way to npm that
doesn't need to create a virtualenv at all!

%prep
%autosetup -p1 -n pdm-pep517-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# must be set to the same value as it is set by the python_flavored_alternatives macro used below in pytest
export XDG_CONFIG_HOME=$PWD/build/xdgflavorconfig
%{python_expand # the config home is inside the shuffled build dir
mkdir -p $XDG_CONFIG_HOME/git
touch $XDG_CONFIG_HOME/git/config
git config --global user.name abuild
git config --global user.email abuild@obs
}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/pdm
%{python_sitelib}/pdm/pep517
%{python_sitelib}/pdm_pep517-%{version}.dist-info
%endif

%changelog
