#
# spec file for package python-brewer2mpl
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
Name:           python-brewer2mpl
Version:        1.4.1
Release:        0
Summary:        colorbrewer2org color maps for Python and matplotlib
License:        Apache-2.0 AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/jiffyclub/brewer2mpl/wiki
Source:         https://files.pythonhosted.org/packages/source/b/brewer2mpl/brewer2mpl-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/jiffyclub/palettable/v%{version}/license.txt
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-matplotlib
BuildArch:      noarch
%python_subpackages

%description
brewer2mpl is a pure Python package for accessing colorbrewer2.org
color maps from Python. With brewer2mpl, the raw RGB colors of all 165
colorbrewer2.org color maps can be retrieved. The color map data ships with
brewer2mpl, so that no network connection is required.

For more information and to view some of the color maps, see the wiki at
https://github.com/jiffyclub/brewer2mpl/wiki.

%prep
%setup -q -n brewer2mpl-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license license.txt
%{python_sitelib}/*

%changelog
