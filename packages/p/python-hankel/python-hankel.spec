#
# spec file for package python-hankel
#
# Copyright (c) 2020 SUSE LLC
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
%define modname hankel
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-hankel
Version:        1.1.0
Release:        0
Summary:        Hankel Transformations using method of Ogata 2005
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/steven-murray/hankel
Source:         https://files.pythonhosted.org/packages/source/h/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mpmath >= 1.0.0
Requires:       python-numpy >= 1.9.3
Requires:       python-scipy >= 0.16.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mpmath >= 1.0.0}
BuildRequires:  %{python_module numpy >= 1.9.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.16.1}
# /SECTION
%python_subpackages

%description
Hankel is a Python library to perform simple and accurate Hankel
transformations using the method of Ogata 2005.

%prep
%setup -q -n hankel-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# TESTS TAKE TOO LONG ON i586 LEADING TO OBS WORKER TIMING OUT
%if "%{_lib}" != "lib"
%check
%pytest
%endif

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.rst
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
