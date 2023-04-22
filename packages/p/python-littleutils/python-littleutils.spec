#
# spec file for package python-littleutils
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
%{?sle15_python_module_pythons}
Name:           python-littleutils
Version:        0.2.2
Release:        0
Summary:        Small personal collection of python utility functions
License:        MIT
URL:            https://github.com/alexmojaki/littleutils
Source:         https://files.pythonhosted.org/packages/source/l/littleutils/littleutils-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Small personal collection of python utility functions

%prep
%autosetup -p1 -n littleutils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -mlittleutils.__init__ -v

%files %{python_files}
%{python_sitelib}/littleutils*

%changelog
