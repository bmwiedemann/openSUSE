#
# spec file for package python-jaraco.vcs
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


%{?sle15_python_module_pythons}
Name:           python-jaraco.vcs
Version:        2.0.0
Release:        0
Summary:        Facilities for working with VCS repositories
License:        MIT
URL:            https://github.com/jaraco/jaraco.vcs
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.vcs/jaraco.vcs-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module jaraco.path}
BuildRequires:  %{python_module jaraco.versioning}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest >= 6}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jaraco.classes
Requires:       python-jaraco.versioning
Requires:       python-more-itertools
Requires:       python-packaging
BuildArch:      noarch
%python_subpackages

%description
Facilities for working with VCS repositories

%prep
%autosetup -p1 -n jaraco.vcs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# jaraco/vcs/__init__.py - not a git repo
%pytest --ignore jaraco/vcs/__init__.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/jaraco/vcs
%{python_sitelib}/jaraco.vcs-%{version}.dist-info

%changelog
