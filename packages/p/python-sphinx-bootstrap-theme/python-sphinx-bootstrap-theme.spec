#
# spec file for package python-sphinx-bootstrap-theme
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sphinx-bootstrap-theme
Version:        0.8.1
Release:        0
Summary:        Sphinx Bootstrap Theme
License:        Apache-2.0 AND MIT
Group:          Development/Languages/Python
URL:            http://ryan-roemer.github.com/sphinx-bootstrap-theme/README.html
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-bootstrap-theme/sphinx-bootstrap-theme-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.6.1
BuildArch:      noarch

%python_subpackages

%description
This Sphinx theme integrates the Bootstrap CSS / JavaScript framework
with various layout options, hierarchical menu navigation, and
mobile-friendly responsive design. It is configurable, extensible, and
can use any number of different Bootswatch CSS themes.

%prep
%setup -q -n sphinx-bootstrap-theme-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc HISTORY.rst README.rst TODO.rst
%{python_sitelib}/*

%changelog
