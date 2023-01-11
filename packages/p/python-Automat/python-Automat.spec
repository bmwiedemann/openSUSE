#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%bcond_without python2
Name:           python-Automat%{psuffix}
Version:        22.10.0
Release:        0
Summary:        Self-service finite-state machines for the programmer on the go
License:        MIT
URL:            https://github.com/glyph/automat
Source:         https://files.pythonhosted.org/packages/source/A/Automat/Automat-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires(post): update-alternatives
Requires(preun):update-alternatives
Suggests:       python-Twisted >= 16.1.1
Suggests:       python-graphviz > 0.5.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Twisted >= 16.1.1}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module graphviz >= 0.5.1}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python2-xml
%endif
%endif
%python_subpackages

%description
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

%prep
%setup -q -n Automat-%{version}
# we don't care about the long_description, avoid unmaintained m2r
sed -i "/'m2r'/d" setup.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/automat-visualize
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest automat/_test
%endif

%if !%{with test}
%post
%python_install_alternative automat-visualize

%postun
%python_uninstall_alternative automat-visualize

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/automat-visualize
%{python_sitelib}/automat
%{python_sitelib}/Automat-%{version}*-info
%endif

%changelog
