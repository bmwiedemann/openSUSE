#
# spec file for package python-xsge_physics
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-xsge_physics
Version:        0.13.3
Release:        0
Summary:        xSGE Physics Framework
License:        LGPL-3.0-or-later
URL:            http://xsge.nongnu.org
Source:         https://files.pythonhosted.org/packages/source/x/xsge_physics/xsge_physics-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sge-pygame >= 1.0
BuildArch:      noarch
%python_subpackages

%description
xSGE is a collection of extensions for SGE.
xSGE extensions are not dependent on any particular SGE implementation.
They should work with any implementation that follows the specification.

This extension provides a framework for collision physics.
This can be useful for platformers.

%prep
%setup -q -n xsge_physics-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license xsge_physics/COPYING
%{python_sitelib}/xsge_physics
%{python_sitelib}/xsge_physics-%{version}.dist-info

%changelog
