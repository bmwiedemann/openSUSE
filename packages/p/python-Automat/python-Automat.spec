#
# spec file for package python-Automat
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-Automat%{psuffix}
Version:        0.7.0
Release:        0
Summary:        Self-service finite-state machines for the programmer on the go
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/glyph/automat
Source:         https://files.pythonhosted.org/packages/source/A/Automat/Automat-%{version}.tar.gz
BuildRequires:  %{python_module m2r}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 16.1.0
Requires:       python-six
Requires(post): update-alternatives
Requires(preun): update-alternatives
Suggests:       python-Twisted >= 16.1.1
Suggests:       python-graphviz > 0.5.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Twisted >= 16.1.1}
BuildRequires:  %{python_module attrs >= 16.1.0}
BuildRequires:  %{python_module graphviz >= 0.5.1}
%endif
%python_subpackages

%description
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

%prep
%setup -q -n Automat-%{version}

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
%python_exec setup.py test
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
%{python_sitelib}/*
%endif

%changelog
