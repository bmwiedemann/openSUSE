#
# spec file for package python-jmespath
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


Name:           python-jmespath
Version:        1.0.1
Release:        0
Summary:        Python module for declarative JSON document element extraction
License:        MIT
URL:            https://github.com/jmespath/jmespath.py
Source:         https://github.com/jmespath/jmespath.py/archive/refs/tags/%{version}.tar.gz#/jmespath-%{version}.tar.gz
# Testing
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply >= 3.4
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
JMESPath (pronounced "jaymz path") allows you to declaratively specify how
to extract elements from a JSON document.

For example, given this document:

{"foo": {"bar": "baz"}}

The jmespath expression foo.bar will return "baz".

JMESPath also supports:

Referencing elements in a list. Given the data:

{"foo": {"bar": ["one", "two"]}}

The expression: foo.bar[0] will return "one". You can also reference all
the items in a list using the * syntax:

{"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}

The expression: foo.bar[*].name will return ["one", "two"]. Negative
indexing is also supported (-1 refers to the last element in the list).
Given the data above, the expression foo.bar[-1].name will return ["two"].

The * can also be used for hash types:

{"foo": {"bar": {"name": "one"}, "baz": {"name": "two"}}}

The expression: foo.*.name will return ["one", "two"].

%prep
%autosetup -p1 -n jmespath.py-%{version}

%build
%python_build

%install
%python_install
mv %{buildroot}%{_bindir}/jp.py %{buildroot}%{_bindir}/jp
%python_clone -a %{buildroot}%{_bindir}/jp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# hangs on python 3.8 with pytest
%pyunittest discover -v

%post
%python_install_alternative jp

%postun
%python_uninstall_alternative jp

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/jmespath
%{python_sitelib}/jmespath-%{version}*-info
%python_alternative %{_bindir}/jp

%changelog
