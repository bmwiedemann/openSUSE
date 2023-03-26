#
# spec file for package python-CommonMark
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


%define oldpython python
%bcond_without python2
Name:           python-CommonMark
Version:        0.9.1
Release:        0
Summary:        Python parser for the CommonMark Markdown spec
License:        BSD-3-Clause
URL:            https://github.com/rtfd/CommonMark-py
Source:         https://files.pythonhosted.org/packages/source/c/commonmark/commonmark-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-commonmark = %{version}
Obsoletes:      python-commonmark < %{version}
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-future >= 0.14.0
%endif
%ifpython2
Requires:       python-future >= 0.14.0
Obsoletes:      %{oldpython}-commonmark < %{version}
Provides:       %{oldpython}-commonmark = %{version}
%endif
Conflicts:      cmark
Provides:       cmark-python
Obsoletes:      cmark-python
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
%python_clone -a %{buildroot}%{_bindir}/cmark
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%if "%{python_flavor}" == "python3"
%pyunittest commonmark/tests/*.py
# On python2 we error out on unicode issues
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 commonmark/tests/run_spec_tests.py
%endif

%post
%python_install_alternative cmark

%postun
%python_uninstall_alternative cmark

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/commonmark
%{python_sitelib}/commonmark-%{version}*-info
%python_alternative %{_bindir}/cmark

%changelog
