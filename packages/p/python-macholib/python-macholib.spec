#
# spec file for package python-macholib
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-macholib
Version:        1.16.3
Release:        0
Summary:        Mach-O header analysis and editing
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ronaldoussoren/macholib/
Source:         https://files.pythonhosted.org/packages/source/m/macholib/macholib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-altgraph >= 0.15
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module altgraph >= 0.15}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
macholib can be used to analyze and edit Mach-O headers, the executable
format used by Mac OS X.

It's typically used as a dependency analysis tool, and also to rewrite dylib
references in Mach-O headers to be @executable_path relative.

Though this tool targets a platform specific file format, it is pure python
code that is platform and endian independent.

%prep
%setup -q -n macholib-%{version}
sed -i -e '/^#!\//, 1d' macholib/macho_dump.py
sed -i -e '/^#!\//, 1d' macholib/macho_find.py
sed -i -e '/^#!\//, 1d' macholib/macho_standalone.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/macho_dump
%python_clone -a %{buildroot}%{_bindir}/macho_standalone
%python_clone -a %{buildroot}%{_bindir}/macho_find
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are too much platform specific (?)
rm macholib_tests/test_{command_line,dyld}.py
%pytest

%pre
%python_libalternatives_reset_alternative macho_dump
%python_libalternatives_reset_alternative macho_standalone
%python_libalternatives_reset_alternative macho_find

%files %{python_files}
%doc README.rst doc/*.rst
%license doc/license.rst
%python_alternative %{_bindir}/macho_find
%python_alternative %{_bindir}/macho_standalone
%python_alternative %{_bindir}/macho_dump
%{python_sitelib}/macholib
%{python_sitelib}/macholib-%{version}*-info

%changelog
