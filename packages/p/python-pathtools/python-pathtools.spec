#
# spec file for package python-pathtools
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
Name:           python-pathtools
Version:        0.1.2
Release:        0
Summary:        File system general utilities
License:        MIT
URL:            https://github.com/gorakhargosh/pathtools
Source:         https://files.pythonhosted.org/packages/source/p/pathtools/pathtools-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildArch:      noarch
%python_subpackages

%description
Pattern matching and various utilities for file systems paths.

%prep
%setup -q -n pathtools-%{version}
sed -i "1d" pathtools/path.py pathtools/patterns.py
sed -i "s/^html_theme.*/#html_theme/" docs/source/conf.py

%build
%python_build
cd docs && make html && rm -r build/html/.buildinfo # Build HTML docs

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc AUTHORS README docs/build/html
%{python_sitelib}/pathtools
%{python_sitelib}/pathtools-%{version}-py%{python_version}.egg-info

%changelog
