#
# spec file for package python-spandrel
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


%{?sle15_python_module_pythons}
Name:           python-spandrel
Version:        0.4.2
Release:        0
Summary:        Load and run pre-trained PyTorch image models
License:        MIT
URL:            https://github.com/chaiNNer-org/spandrel
Source0:        https://files.pythonhosted.org/packages/source/s/spandrel/spandrel-%{version}.tar.gz
# The PyPI sdist omits LICENSE; take it from the matching GitHub tag.
Source1:        https://raw.githubusercontent.com/chaiNNer-org/spandrel/v%{version}/LICENSE
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module einops}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module safetensors}
BuildRequires:  %{python_module setuptools >= 46.4.0}
BuildRequires:  %{python_module torchvision}
BuildRequires:  %{python_module torch}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# The auto Python dep generator does not pick up Requires-Dist from this
# setuptools wheel; declare them by hand.
Requires:       python-einops
Requires:       python-numpy
Requires:       python-safetensors
Requires:       python-torch
Requires:       python-torchvision
Requires:       python-typing_extensions
BuildArch:      noarch
# Match Factory python-torch / python-torchvision (ExcludeArch: %%ix86 %%{arm})
ExcludeArch:    %{ix86} %{arm}
%python_subpackages

%description
Spandrel loads pre-trained PyTorch image models from .pth / safetensors
files, auto-detects the architecture and hyperparameters, and exposes a
unified inference interface. Used by ComfyUI for architecture support.

%prep
%autosetup -p1 -n spandrel-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
# imported modules, not scripts (rpmlint non-executable-script)
find %{buildroot} -name '*.py' ! -perm /111 -exec sed -i '1{/^#!/d}' {} +
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/spandrel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Full suite needs model weights and is not in the sdist.
# Import from a directory without the in-tree spandrel/ package.
cd %{_tmppath}
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import spandrel; assert spandrel.__version__ == '%{version}', spandrel.__version__"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/spandrel
%{python_sitelib}/spandrel-%{version}.dist-info

%changelog
