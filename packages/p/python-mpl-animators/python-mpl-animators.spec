#
# spec file for package python-mpl-animators
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-mpl-animators
Version:        1.0.1
Release:        0
Summary:        An interative animation framework for matplotlib
License:        BSD-3-Clause
URL:            https://github.com/sunpy/mpl-animators
Source:         https://files.pythonhosted.org/packages/source/m/mpl_animators/mpl_animators-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.2.0
Requires:       python-numpy >= 1.17.0
Suggests:       python-astropy >= 4.2.0
Provides:       python-mpl_animators = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astropy >= 4.2.0}
BuildRequires:  %{python_module matplotlib >= 3.2.0}
BuildRequires:  %{python_module numpy >= 1.17.0}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
An interative animation framework for matplotlib

%prep
%setup -q -n mpl_animators-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/mpl_animators
%{python_sitelib}/mpl_animators-%{version}*-info

%changelog
