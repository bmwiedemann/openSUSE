#
# spec file for package python-hankel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-hankel
Version:        0.3.8
Release:        0
Summary:        Hankel Transformations using method of Ogata 2005
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/steven-murray/hankel
Source:         https://github.com/steven-murray/hankel/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mpmath >= 0.18
Requires:       python-numpy >= 1.6.1
Requires:       python-scipy >= 0.12.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mpmath >= 0.18}
BuildRequires:  %{python_module numpy >= 1.6.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.12.0}
BuildRequires:  python-future
# /SECTION
%ifpython2
Requires:       python-future
%endif
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

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
