#
# spec file for package python-xsge_physics
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-xsge_physics
Version:        0.13.1
Release:        0
Summary:        xSGE Physics Framework
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://xsge.nongnu.org
Source:         https://files.pythonhosted.org/packages/source/x/xsge_physics/xsge_physics-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license xsge_physics/COPYING
%{python_sitelib}/*

%changelog
