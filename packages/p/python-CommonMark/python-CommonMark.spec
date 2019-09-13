#
# spec file for package python-CommonMark
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
%define oldpython python
Name:           python-CommonMark
Version:        0.9.0
Release:        0
Summary:        Python parser for the CommonMark Markdown spec
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rtfd/CommonMark-py
Source:         https://files.pythonhosted.org/packages/source/c/commonmark/commonmark-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-future
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Provides:       python-commonmark = %{version}
Obsoletes:      python-commonmark < %{version}
BuildArch:      noarch
%ifpython2
Requires:       python-future
Obsoletes:      %{oldpython}-commonmark < %{version}
Provides:       %{oldpython}-commonmark = %{version}
%endif
%ifpython3
Conflicts:      cmark
Provides:       cmark-python
Obsoletes:      cmark-python
%endif
%python_subpackages

%description
Pure Python port of jgm's stmd.js, a Markdown parser and renderer for the
CommonMark specification, using only native modules.

%prep
%setup -q -n commonmark-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python commonmark/tests/unit_tests.py
# On python2 we error out on unicode issues
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%python3_only %{_bindir}/cmark

%changelog
