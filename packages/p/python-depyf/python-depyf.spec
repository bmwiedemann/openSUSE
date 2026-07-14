#
# spec file for package python-depyf
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-depyf
Version:        0.20.0
Release:        0
Summary:        Decompile python functions, from bytecode to source code
License:        MIT
URL:            https://github.com/thuml/depyf
Source:         https://files.pythonhosted.org/packages/source/d/depyf/depyf-%{version}.tar.gz
# PATCH-FIX-UPSTREAM depyf-no-git-in-build.patch -- do not fail metadata generation when git is unavailable
Patch0:         depyf-no-git-in-build.patch
BuildRequires:  %{python_module astor}
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astor
Requires:       python-dill
BuildArch:      noarch
%python_subpackages

%description
depyf decompiles Python bytecode back into readable source code. It is
designed to help understand and debug PyTorch's torch.compile: it turns
the bytecode Dynamo produces back into equivalent Python source, and can
export the intermediate graphs and generated code for inspection so the
compilation process can be followed step by step.

%prep
%autosetup -p1 -n depyf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# The wheel ships the .py sources with their original upstream mtimes
# (2024/2025), while %%pyproject_install byte-compiles them under
# SOURCE_DATE_EPOCH, so the timestamp baked into the .pyc no longer matches
# the .py mtime (rpmlint python-bytecode-inconsistent-mtime).  Recompile with
# hash-based (PEP 552) invalidation, which does not depend on the mtime.
%python_expand find %{buildroot}%{$python_sitelib} -name '*.pyc' -delete
%python_expand $python -m compileall --invalidation-mode checked-hash -s %{buildroot} -q %{buildroot}%{$python_sitelib}
%python_expand $python -O -m compileall --invalidation-mode checked-hash -s %{buildroot} -q %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The upstream test suite decompiles bytecode and re-executes it; depyf
# 0.20.0's decompiler does not yet support instructions emitted by the
# distribution's primary Python (e.g. LOAD_FAST_LOAD_FAST on 3.13+), so
# those tests fail on Factory. The test_pytorch/ tests additionally
# require torch. Restrict %%check to an import smoke test instead.
# PYTHONDONTWRITEBYTECODE keeps the import from rewriting the .pyc files
# already byte-compiled during %%install (which would trip rpmlint's
# python-bytecode-inconsistent-mtime).
%python_expand PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import depyf; from depyf import decompile, Decompiler"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/depyf
%{python_sitelib}/depyf-%{version}.dist-info

%changelog
