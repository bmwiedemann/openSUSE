#
# spec file for package python-xsge_lighting
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
Name:           python-xsge_lighting
Version:        1.0.1
Release:        0
Summary:        xSGE Lighting Library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://python-sge.github.io/
#Git-Clone:     https://github.com/python-sge/xsge
Source:         https://files.pythonhosted.org/packages/source/x/xsge_lighting/xsge_lighting-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-sge-pygame >= 1.0
Requires:       python-six >= 1.4.0
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
xSGE is a collection of extensions for SGE.
xSGE extensions are not dependent on any particular SGE implementation.
They should work with any implementation that follows the specification.

This extension provides an interface for lighting.

%prep
%setup -q -n xsge_lighting-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license xsge_lighting/COPYING
%{python_sitelib}/*

%changelog
