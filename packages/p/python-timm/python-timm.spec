#
# spec file for package python-timm
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
Name:           python-timm
Version:        1.0.28
Release:        0
Summary:        PyTorch Image Models
License:        Apache-2.0
URL:            https://github.com/huggingface/pytorch-image-models
Source:         https://files.pythonhosted.org/packages/source/t/timm/timm-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module huggingface-hub}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module safetensors}
BuildRequires:  %{python_module torchvision}
BuildRequires:  %{python_module torch}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-huggingface-hub
Requires:       python-safetensors
Requires:       python-torch
Requires:       python-torchvision
BuildArch:      noarch
%python_subpackages

%description
PyTorch Image Models (timm) is a collection of image models, layers, utilities,
optimizers, schedulers, data-loaders / augmentations, and reference training /
validation scripts that aim to pull together a wide variety of SOTA models with
ability to reproduce ImageNet training results.

%prep
%autosetup -p1 -n timm-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Upstream pytest downloads pretrained weights and needs network.
# Smoke-test import, the model registry and a real forward pass instead.
cat > smoke.py <<'EOF'
import timm, torch
assert timm.__version__ == "%{version}", timm.__version__
assert timm.list_models()
# guard the SigLIP ViT that python-sglang builds via timm.create_model()
assert "vit_so400m_patch14_siglip_384" in timm.list_models()
m = timm.create_model("resnet18", pretrained=False, num_classes=10).eval()
with torch.no_grad():
    assert m(torch.randn(1, 3, 64, 64)).shape == (1, 10)
EOF
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B smoke.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/timm
%{python_sitelib}/timm-%{version}.dist-info

%changelog
