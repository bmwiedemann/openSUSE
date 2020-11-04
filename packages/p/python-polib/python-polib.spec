#
# spec file for package python-polib
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-polib
Version:        1.1.0
Release:        0
Summary:        A library to manipulate gettext files
License:        MIT
Group:          Development/Languages/Python
URL:            http://bitbucket.org/izi/polib/
Source0:        https://files.pythonhosted.org/packages/source/p/polib/polib-%{version}.tar.gz
Patch0:         polib-1.1.0-fix-tests-big-endian.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.8
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
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
%setup -q -n polib-%{version}
%autopatch -p1

%build
%python_build

pushd docs
make %{?_smp_mflags} html
rm _build/html/.buildinfo
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec tests/tests.py

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.rst
%{python_sitelib}/*

%files -n python-polib-doc
%doc docs/_build/html

%changelog
