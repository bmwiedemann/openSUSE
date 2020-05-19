#
# spec file for package python-textX
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-textX
Version:        2.1.0
Release:        0
Summary:        Meta-language for DSL implementation inspired by Xtext
License:        MIT
Group:          Development/Languages/Python
URL:            https://textx.github.io/textX/stable/
Source:         https://github.com/igordejanovic/textX/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Arpeggio >= 1.9.0
Requires:       python-click >= 7.0
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      %{name}-doc
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module Arpeggio}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module memory_profiler}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
textX is a meta-language for building Domain-Specific Languages (DSLs) in Python.
It is inspired by Xtext.

From a single language description (grammar), textX will build a
parser and a meta-model (a.k.a. abstract syntax) for textual
languages. Own languages can be invented or support for already
existing textual language or file format be built.

textX follows the syntax and semantics of Xtext, but differs in some places
and is implemented in Python using the Arpeggio PEG parser - no grammar
ambiguities, unlimited lookahead, interpreter style of work.

%prep
%setup -q -n textX-%{version}
sed -i '0,/#!\/usr\/bin\/env/ d' examples/hello_world/hello.py
# do not hardcode deps
sed -i -e 's:click==:click>=:g' setup.py

%build
%python_build
pushd tests/functional/subcommands/example_project
%python_build
popd
pushd tests/functional/registration/projects/types_dsl
%python_build
popd
pushd tests/functional/registration/projects/data_dsl
%python_build
popd
pushd tests/functional/registration/projects/flow_dsl
%python_build
popd
pushd tests/functional/registration/projects/flow_codegen
%python_build
popd

%install
%python_install
pushd tests/functional/subcommands/example_project
%python_install
popd
pushd tests/functional/registration/projects/types_dsl
%python_install
popd
pushd tests/functional/registration/projects/data_dsl
%python_install
popd
pushd tests/functional/registration/projects/flow_dsl
%python_install
popd
pushd tests/functional/registration/projects/flow_codegen
%python_install
popd
%python_clone -a %{buildroot}%{_bindir}/textx
%python_expand %fdupes %{buildroot}%{$python_sitelib}/textx

%check
export PYTHONDONTWRITEBYTECODE=1
export LC_ALL=C.UTF-8
# textx executable is update-alternative'd
%pytest -k 'not test_subcommand'
%python_expand rm -r %{buildroot}%{$python_sitelib}/data_dsl*
%python_expand rm -r %{buildroot}%{$python_sitelib}/flow_codegen*
%python_expand rm -r %{buildroot}%{$python_sitelib}/flow_dsl*
%python_expand rm -r %{buildroot}%{$python_sitelib}/types_dsl*
%python_expand rm -r %{buildroot}%{$python_sitelib}/textX_subcommand_test*
%python_expand rm -r %{buildroot}%{$python_sitelib}/textx_subcommand_test*

%post
%python_install_alternative textx

%postun
%python_uninstall_alternative textx

%files %{python_files}
%{python_sitelib}/*
%python_alternative %{_bindir}/textx
%license LICENSE.txt
%doc AUTHORS.md CHANGELOG.md README.md

%changelog
