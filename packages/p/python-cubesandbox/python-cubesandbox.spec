#
# spec file for package python-cubesandbox
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-cubesandbox
Version:        0.5.0
Release:        0
Summary:        Python SDK for CubeSandbox
License:        Apache-2.0
URL:            https://github.com/TencentCloud/CubeSandbox
Source0:        https://files.pythonhosted.org/packages/source/c/cubesandbox/cubesandbox-%{version}.tar.gz
# LICENSE file is not shipped in the PyPI sdist; taken from the upstream repository
Source1:        LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpx >= 0.27
Requires:       python-requests >= 2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module httpx >= 0.27}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2}
# /SECTION
%python_subpackages

%description
Python SDK for CubeSandbox, a lightweight microVM sandbox service for AI
agents built on RustVMM and KVM. The SDK talks to a CubeSandbox control-plane
API to create and manage hardware-isolated sandboxes, run commands and stream
their output, manage the sandbox filesystem, build and manage templates, and
apply per-sandbox network policies.

%prep
%autosetup -p1 -n cubesandbox-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# e2e tests need a live CubeSandbox control plane; the rest mock all HTTP
%pytest -m "not e2e"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cubesandbox
%{python_sitelib}/cubesandbox-%{version}.dist-info

%changelog
