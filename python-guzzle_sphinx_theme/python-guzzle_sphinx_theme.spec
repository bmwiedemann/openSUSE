#
# spec file for package python-guzzle_sphinx_theme
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-guzzle_sphinx_theme
Version:        0.7.11
Release:        0
Summary:        Sphinx theme used by Guzzle
License:        MIT AND OFL-1.1
Group:          Development/Languages/Python
URL:            https://github.com/guzzle/guzzle_sphinx_theme
Source:         https://files.pythonhosted.org/packages/source/g/guzzle_sphinx_theme/guzzle_sphinx_theme-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 1.2b1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.2b1
BuildArch:      noarch
%python_subpackages

%description
This package contains the python bindings of the Sphinx theme used by Guzzle.

%prep
%setup -q -n guzzle_sphinx_theme-%{version}
find guzzle_sphinx_theme/guzzle_sphinx_theme/static -type f -exec chmod -x "{}" \;
find . -iname .DS_Store -delete

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
