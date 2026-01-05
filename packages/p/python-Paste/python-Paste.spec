#
# spec file for package python-Paste
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-Paste
Version:        3.10.1
Release:        0
Summary:        Tools for using a Web Server Gateway Interface stack
License:        MIT
URL:            https://github.com/cdent/paste
Source:         https://files.pythonhosted.org/packages/source/p/paste/paste-%{version}.tar.gz
Patch0:         test_modified-fixup.patch
# PATCH-FIX-UPSTREAM paste-pr105-partial-pkg_resources-remove.patch gh#pasteorg/paste#105 gh#pasteorg/paste#107
Patch1:         paste-pr105-partial-pkg_resources-remove.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Suggests:       python-flup
Suggests:       python-python3-openid
BuildArch:      noarch
%python_subpackages

%description
These provide several pieces of "middleware" (or filters) that can be nested
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.

%prep
%autosetup -p1 -n paste-%{version}
# remove test requiring internet access
rm tests/test_proxy.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license docs/license.txt
%doc README.rst
%{python_sitelib}/paste
%{python_sitelib}/[pP]aste-%{version}.dist-info
%{python_sitelib}/Paste-%{version}-py*-nspkg.pth

%changelog
