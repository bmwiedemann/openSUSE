#
# spec file for package python-Paste
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
%define oldpython python
Name:           python-Paste
Version:        3.4.6
Release:        0
Summary:        Tools for using a Web Server Gateway Interface stack
License:        MIT
URL:            https://github.com/cdent/paste
Source:         https://files.pythonhosted.org/packages/source/P/Paste/Paste-%{version}.tar.gz
Patch0:         test_modified-fixup.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six > 1.4.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six > 1.4.0
Suggests:       python-flup
BuildArch:      noarch
%ifpython2
Suggests:       python-python-openid
Provides:       %{oldpython}-paste = %{version}
Obsoletes:      %{oldpython}-paste < %{version}
%endif
%ifpython3
Suggests:       python3-python3-openid
%endif
%python_subpackages

%description
These provide several pieces of "middleware" (or filters) that can be nested
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.

%prep
%setup -q -n Paste-%{version}
%patch0 -p1
sed -i '/pytest-runner/d' setup.py
# remove test requiring internet access
rm tests/test_proxy.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license docs/license.txt
%doc README.rst
%{python_sitelib}/*

%changelog
