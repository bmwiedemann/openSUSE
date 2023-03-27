#
# spec file for package python-bindep
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


Name:           python-bindep
Version:        2.11.0
Release:        0
Summary:        Binary dependency utility
License:        Apache-2.0
URL:            https://docs.opendev.org/opendev/bindep
Source:         https://files.pythonhosted.org/packages/source/b/bindep/bindep-%{version}.tar.gz
Patch0:         remove-mock.patch
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module distro >= 1.7.0}
BuildRequires:  %{python_module Parsley}
BuildRequires:  %{python_module coverage >= 3.6}
BuildRequires:  %{python_module fixtures >= 0.3.12}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pbr >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module testrepository >= 0.0.13}
BuildRequires:  %{python_module testtools >= 0.9.27}
BuildRequires:  %{python_module wheel}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  openSUSE-release
Requires:       python-Parsley
Requires:       python-distro >= 1.7.0
Requires:       python-packaging
Requires:       python-pbr >= 2.0.0
Suggests:       python-distro < 1.7.0
Suggests:       python-packaging < 21.0
BuildArch:      noarch
%python_subpackages

%description
Bindep is a tool for checking the presence of binary packages needed to
use an application / library. It started life as a way to make it easier to set
up a development environment for OpenStack projects. While OpenStack depends
heavily on `pip` for installation of Python dependencies, some dependencies are
not Python based, and particularly for testing, some dependencies have to be
installed before `pip` can be used - such as `virtualenv` and `pip` itself.

%prep
%autosetup -p1 -n bindep-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bindep
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -s -k 'not (test_arch_implies_pacman or test_manjaro_implies_pacman)'

%post
%python_install_alternative bindep

%postun
%python_uninstall_alternative bindep

%files %{python_files}
%doc AUTHORS ChangeLog NEWS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/bindep
%{python_sitelib}/bindep
%{python_sitelib}/bindep-%{version}*info

%changelog
