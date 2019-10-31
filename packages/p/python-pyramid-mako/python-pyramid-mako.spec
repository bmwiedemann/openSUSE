#
# spec file for package python-pyramid-mako
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
Name:           python-pyramid-mako
Version:        1.1.0
Release:        0
Summary:        Mako template bindings for the Pyramid web framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/pyramid_mako
Source:         https://files.pythonhosted.org/packages/source/p/pyramid_mako/pyramid_mako-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Mako >= 1.1.0
Requires:       python-pyramid
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Mako >= 1.1.0}
BuildRequires:  %{python_module WebTest >= 1.3.1}
BuildRequires:  %{python_module pyramid}
# /SECTION
%python_subpackages

%description
Mako template bindings for the Pyramid web framework.

%prep
%setup -q -n pyramid_mako-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt README.rst docs/*.rst
%license COPYRIGHT.txt LICENSE.txt CONTRIBUTORS.txt
%{python_sitelib}/*

%changelog
