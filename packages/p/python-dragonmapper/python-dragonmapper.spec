#
# spec file for package python-dragonmapper
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-dragonmapper
Version:        0.3.0
Release:        0
Summary:        Identification and conversion functions for Chinese text processing
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tsroten/dragonmapper
Source:         https://github.com/tsroten/dragonmapper/archive/v%{version}.tar.gz#/dragonmapper-%{version}.tar.gz
BuildRequires:  %{python_module base > 3.8}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hanzidentifier >= 1.2.0
Requires:       python-zhon >= 2.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hanzidentifier >= 1.2.0}
BuildRequires:  %{python_module zhon >= 2.0.0}
# /SECTION
%python_subpackages

%description
Identification and conversion functions for Chinese text processing.

%prep
%autosetup -p1 -n dragonmapper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/dragonmapper
%{python_sitelib}/dragonmapper-%{version}.dist-info

%changelog
