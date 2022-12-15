#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
%define rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define modname libcst
Name:           python-libcst%{psuffix}
Version:        0.4.9
Release:        0
Summary:        Python 3.5+ concrete syntax tree with AST-like properties
License:        MIT
URL:            https://github.com/Instagram/LibCST
Source0:        https://files.pythonhosted.org/packages/source/l/%{modname}/%{modname}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
# PATCH-FIX-OPENSUSE remove-ufmt-dep.patch python-ufmt package doesn't exists in Tumbleweed
Patch0:         remove-ufmt-dep.patch
# PATCH-FIX-OPENSUSE replace-python-call.patch
# wrong executable call when outside of venv (gh#Instagram/LibCST#468)
Patch1:         replace-python-call.patch
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  rust
Requires:       python-PyYAML >= 5.2
Requires:       python-typing-inspect >= 0.4.0
Requires:       python-typing_extensions >= 3.7.4.2
Requires:       (python-dataclasses if python-base < 3.7)
%if %{with test}
# black and isort needed for tests and the code regeneration
BuildRequires:  %{python_module PyYAML >= 5.2}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module dataclasses if %python-base < 3.7}
BuildRequires:  %{python_module hypothesis >= 4.36.0}
BuildRequires:  %{python_module hypothesmith >= 0.0.4}
BuildRequires:  %{python_module isort >= 5.5.3}
BuildRequires:  %{python_module typing-inspect >= 0.4.0}
BuildRequires:  %{python_module typing_extensions >= 3.7.4.2}
%endif
%python_subpackages

%description
A concrete syntax tree with AST-like properties for Python 3.5+ programs.

%prep
%setup -q -n libcst-%{version}
tar x -C native/ -f %{SOURCE1}
cp -rf native/vendor vendor
mkdir -p .cargo && echo "" >> .cargo/config.toml && cat %{SOURCE2} >>.cargo/config.toml

pushd native
mkdir -p .cargo
cat %{SOURCE2} >>.cargo/config.toml
popd

%autopatch -p1

# Depends on optional pyre
rm \
  libcst/metadata/tests/test_type_inference_provider.py \
  libcst/metadata/tests/test_full_repo_manager.py \
  libcst/tests/test_pyre_integration.py

# gh#Instagram/LibCST#467
sed -i 's/import AbstractBaseMatcherNodeMeta/import Optional, AbstractBaseMatcherNodeMeta/' libcst/codegen/gen_matcher_classes.py

%if !%{with test}
%build
export CARGO_NET_OFFLINE=true PROFILE=release
%python_build
%endif

%install
%if !%{with test}
export CARGO_NET_OFFLINE=true PROFILE=release
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# test_fuzz needs network access because of 'from hypothesmith import from_grammar'
rm libcst/tests/test_fuzz.py

%{python_exec # https://github.com/Instagram/LibCST/issues/331 + 467
$python -m libcst.codegen.generate matchers
$python -m libcst.codegen.generate return_types
$python -m libcst.codegen.generate visitors
$python -m unittest -v
}
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/libcst
%{python_sitearch}/libcst-%{version}-py*.egg-info
%endif

%changelog
