#
# spec file for package python-textX
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

%{?sle15_python_module_pythons}
Name:           python-textX
Version:        4.2.3
Release:        0
Summary:        Meta-language for DSL implementation inspired by Xtext
License:        MIT
URL:            https://textx.github.io/textX/stable/
Source:         https://github.com/igordejanovic/textX/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Arpeggio >= 2.0.0
Recommends:     python-click >= 7.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      %{name}-doc
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module Arpeggio >= 2.0.0}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module installer}
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

%build
%pyproject_wheel
for dir in tests/functional/subcommands/example_project \
tests/functional/registration/projects/types_dsl \
tests/functional/registration/projects/data_dsl \
tests/functional/registration/projects/flow_dsl \
tests/functional/registration/projects/flow_codegen ; do
    pushd $dir
    python3 -m build -wn
    popd
done

%install
%pyproject_install
mkdir tmp-modules
find tests/functional -name '*.whl' -exec python3 -m installer -d tmp-modules {} \;
%python_expand install -m 0644 textx/textx.tx %{buildroot}%{$python_sitelib}/textx/
%python_clone -a %{buildroot}%{_bindir}/textx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=C.UTF-8
export PYTHONPATH=$(ls -1d tmp-modules/usr/lib/python3.*/site-packages)
%pytest tests/functional

%post
%python_install_alternative textx

%postun
%python_uninstall_alternative textx

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.md CHANGELOG.md README.md
%python_alternative %{_bindir}/textx
%{python_sitelib}/textx
%{python_sitelib}/textx-%{version}.dist-info

%changelog
