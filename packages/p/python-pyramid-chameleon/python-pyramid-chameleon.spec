#
# spec file for package python-pyramid-chameleon
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 LISA GmbH, Bingen, Germany.
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
Name:           python-pyramid-chameleon
Version:        0.3
Release:        0
Summary:        Pyramid Chameleon integration
License:        BSD-3-Clause AND ZPL-2.1 AND MIT
URL:            https://github.com/Pylons/pyramid_chameleon
Source:         https://files.pythonhosted.org/packages/source/p/pyramid_chameleon/pyramid_chameleon-%{version}.tar.gz
Patch0:         fix-test___call__spec_alreadyregistered.patch
BuildRequires:  %{python_module Chameleon}
BuildRequires:  %{python_module hupper}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module plaster-pastedeploy}
BuildRequires:  %{python_module plaster}
BuildRequires:  %{python_module pyramid} >= 1.4
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Chameleon
Requires:       python-pyramid
BuildArch:      noarch
%python_subpackages

%description
These are bindings for the `Chameleon templating system
<http://pagetemplates.org/>`_ for the Pyramid_ web framework.

%prep
%setup -q -n pyramid_chameleon-%{version}
# Remove CC-SA-NC licensed stuff
rm -rf docs/
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt COPYRIGHT.txt CONTRIBUTORS.txt
%{python_sitelib}/*

%changelog
