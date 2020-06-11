#
# spec file for package python-readthedocs-sphinx-ext
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-readthedocs-sphinx-ext
Version:        1.0.4
Release:        0
Summary:        Sphinx extension for Read the Docs overrides
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rtfd/readthedocs-sphinx-ext
Source:         https://files.pythonhosted.org/packages/source/r/readthedocs-sphinx-ext/readthedocs-sphinx-ext-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
This module adds extensions that make Sphinx easier to use.
Some of them require Read the Docs features,
others are just code that we ship and enable during builds on Read the Docs.

%prep
%setup -q -n readthedocs-sphinx-ext-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/readthedocs_ext
%{python_sitelib}/readthedocs_sphinx_ext-%{version}-py*.egg-info

%changelog
