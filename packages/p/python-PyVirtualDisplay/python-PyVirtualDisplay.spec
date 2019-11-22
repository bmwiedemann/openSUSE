#
# spec file for package python-PyVirtualDisplay
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
%bcond_without test
Name:           python-PyVirtualDisplay
Version:        0.2.1
Release:        0
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc
License:        BSD-2-Clause
URL:            https://github.com/ponty/PyVirtualDisplay
Source:         https://files.pythonhosted.org/packages/source/P/PyVirtualDisplay/PyVirtualDisplay-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-EasyProcess
Requires:       xorg-x11-Xvfb
Recommends:     xorg-x11-Xvnc
Suggests:       xorg-x11-server-extra
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module EasyProcess}
BuildRequires:  %{python_module nose}
%endif
%python_subpackages

%description
PyVirtualDisplay is a python wrapper for Xvfb, Xephyr and Xvnc

%prep
%setup -q -n PyVirtualDisplay-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
mkdir tester
pushd tester
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B -m nose pyvirtualdisplay
}
popd
%endif

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
