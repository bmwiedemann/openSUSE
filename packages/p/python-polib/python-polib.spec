#
# spec file for package python-polib
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-polib
Version:        1.2.0
Release:        0
Summary:        A library to manipulate gettext files
License:        MIT
URL:            https://github.com/izimobil/polib/
Source0:        https://files.pythonhosted.org/packages/source/p/polib/polib-%{version}.tar.gz
Patch0:         polib-1.1.0-fix-tests-big-endian.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.8
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
polib allows you to manipulate, create, modify gettext catalogs (.pot, .po and
binary .mo files). You can load existing files, iterate through it's entries,
add, modify entries, comments or metadata, etc... or create new po/pot files
from scratch.

polib provides a simple and pythonic API, exporting only two convenience
functions 'pofile' and 'mofile', and the 4 core classes: POFile, MOFile,
POEntry and MOEntry for creating new files/entries.

%package -n python-polib-doc
Summary:        A library to manipulate gettext files - documentation
Group:          Documentation/Other
Provides:       %{python_module polib-doc = %{version}}

%description -n python-polib-doc
polib allows you to manipulate, create, modify gettext catalogs (.pot, .po and
binary .mo files). You can load existing files, iterate through it's entries,
add, modify entries, comments or metadata, etc... or create new po/pot files
from scratch.

polib provides a simple and pythonic API, exporting only two convenience
functions 'pofile' and 'mofile', and the 4 core classes: POFile, MOFile,
POEntry and MOEntry for creating new files/entries.

This package contains documentation in HTML format.

%prep
%autosetup -p1 -n polib-%{version}

%build
%pyproject_wheel

pushd docs
make %{?_smp_mflags} html
rm _build/html/.buildinfo
popd

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/izimobil/polib/issues/150
%pytest tests/tests.py -k 'not (test_save_as_mofile or test_is_file)'

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.rst
%{python_sitelib}/polib.py
%pycache_only %{python_sitelib}/__pycache__/polib.*pyc
%{python_sitelib}/polib-%{version}.dist-info

%files -n python-polib-doc
%doc docs/_build/html

%changelog
