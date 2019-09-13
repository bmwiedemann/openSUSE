#
# spec file for package python-macholib
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-macholib
Version:        1.11
Release:        0
Summary:        Mach-O header analysis and editing
License:        MIT
Group:          Development/Languages/Python
Url:            http://bitbucket.org/ronaldoussoren/macholib
Source:         https://files.pythonhosted.org/packages/source/m/macholib/macholib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module altgraph >= 0.13}
# /SECTION
Requires:       python-altgraph >= 0.13
BuildArch:      noarch

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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.txt
%license doc/license.rst
%python3_only %{_bindir}/macho_find
%python3_only %{_bindir}/macho_standalone
%python3_only %{_bindir}/macho_dump
%{python_sitelib}/*

%changelog
