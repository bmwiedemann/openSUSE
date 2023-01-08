#
# spec file for package python-traittypes
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


%define skip_python2 1
Name:           python-traittypes
Version:        0.2.1
Release:        0
Summary:        Scipy trait types
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/traittypes
Source:         https://files.pythonhosted.org/packages/source/t/traittypes/traittypes-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM gh#jupyter-widgets/traittypes#43
Patch0:         python-traittypes-remove-nose.patch
# PATCH-FIX-UPSTREAM h#jupyter-widgets/traittypes#32
Patch1:         python-fix-nptypes.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-traitlets >= 4.2.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module traitlets >= 4.2.2}
BuildRequires:  %{python_module xarray}
# /SECTION
%python_subpackages

%description
Custom trait types for scientific computing.

%prep
%autosetup -p1 -n traittypes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest traittypes

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/traittypes
%{python_sitelib}/traittypes-%{version}.dist-info

%changelog
