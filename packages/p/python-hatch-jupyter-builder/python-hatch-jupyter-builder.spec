#
# spec file for package python-hatch-jupyter-builder
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


# This si with alts/libalternatives only and has never been something else
%bcond_without libalternatives
Name:           python-hatch-jupyter-builder
Version:        0.8.2
Release:        0
Summary:        A hatch plugin to help build Jupyter packages
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/hatch-jupyter-builder
Source:         https://files.pythonhosted.org/packages/source/h/hatch_jupyter_builder/hatch_jupyter_builder-%{version}.tar.gz
# PATCH-FIX-OPENSUSE hatch-test-nonisolated.patch code@bnavigator.de
Patch1:         hatch-test-nonisolated.patch
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-hatchling >= 1.5
Provides:       python-hatch_jupyter_builder = %{version}-%{release}
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module hatch}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli}
# /SECTION
%python_subpackages

%description
This provides a build hook plugin for Hatch that
adds a build step for use with Jupyter packages.

%prep
%autosetup -p1 -n hatch_jupyter_builder-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hatch-jupyter-builder
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative hatch-jupyter-builder

%postun
%python_uninstall_alternative hatch-jupyter-builder

%files %{python_files}
%python_alternative %{_bindir}/hatch-jupyter-builder
%{python_sitelib}/hatch_jupyter_builder
%{python_sitelib}/hatch_jupyter_builder-%{version}.dist-info

%changelog
