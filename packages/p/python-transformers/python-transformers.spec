#
# spec file for package python-transformers
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-transformers
Version:        5.14.1
Release:        0
Summary:        State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
License:        Apache-2.0
URL:            https://github.com/huggingface/transformers
Source:         https://files.pythonhosted.org/packages/source/t/transformers/transformers-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-huggingface-hub >= 1.5.0
Requires:       python-numpy >= 1.17
Requires:       python-packaging >= 20.0
Requires:       python-regex >= 2025.10.22
Requires:       python-safetensors >= 0.8.0
Requires:       python-tokenizers >= 0.22.0
Requires:       python-tqdm >= 4.60
Requires:       python-typer
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION runtime dependencies (also needed for the %%check import test)
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module huggingface-hub >= 1.5.0}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module regex >= 2025.10.22}
BuildRequires:  %{python_module safetensors >= 0.8.0}
BuildRequires:  %{python_module tokenizers >= 0.22.0}
BuildRequires:  %{python_module tqdm >= 4.60}
BuildRequires:  %{python_module typer}
# /SECTION
%python_subpackages

%description
Transformers provides thousands of pretrained models to perform tasks on
different modalities such as text, vision, and audio.

These models can be applied on text, for tasks like text classification,
information extraction, question answering, summarization, translation
and text generation; on images, for tasks like image classification,
object detection and segmentation; and on audio, for tasks like speech
recognition and audio classification.

The library is designed with two strong goals in mind: be as easy and
fast to use as possible, and provide state-of-the-art models with a
unified API.

%prep
%autosetup -p1 -n transformers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/transformers
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The full test suite requires torch plus network access to download
# models from the Hugging Face Hub, so it cannot run in the build.
# Fall back to an import smoke test of the top-level package.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import transformers; print(transformers.__version__)"

%post
%python_install_alternative transformers

%postun
%python_uninstall_alternative transformers

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/transformers
%{python_sitelib}/transformers
%{python_sitelib}/transformers-%{version}.dist-info

%changelog
