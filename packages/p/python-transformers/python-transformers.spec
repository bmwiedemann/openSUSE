#
# spec file for package python-transformers
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-transformers
Version:        4.44.2
Release:        0
Summary:        State-of-the-art Machine Learning for JAX, PyTorch and TensorFlow
License:        Apache-2.0
URL:            https://github.com/huggingface/transformers
Source:         https://github.com/huggingface/transformers/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       python-transformers.rpmlintrc 
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module huggingface-hub >= 0.23.2}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module packaging >= 20.0}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module safetensors >= 0.4.1}
BuildRequires:  %{python_module tokenizers >= 0.19}
BuildRequires:  %{python_module tqdm >= 4.27}
BuildRequires:  fdupes
Requires:       python-filelock
Requires:       python-huggingface-hub >= 0.23.2
Requires:       python-numpy >= 1.17
Requires:       python-packaging >= 20.0
Requires:       python-PyYAML >= 5.1
Requires:       python-regex
Requires:       python-requests
Requires:       python-safetensors >= 0.4.1
Requires:       python-tokenizers >= 0.19
Requires:       python-tqdm >= 4.27
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-diffusers
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-datasets
Suggests:       python-torch
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-opencv-python
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-tensorflow > 2.9
Suggests:       python-onnxconverter-common
Suggests:       python-tf2onnx
Suggests:       python-tensorflow-text < 2.16
Suggests:       python-keras-nlp >= 0.3.1
Suggests:       python-torch
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-jax >= 0.4.1
Suggests:       python-jaxlib >= 0.4.1
Suggests:       python-flax >= 0.4.1
Suggests:       python-optax >= 0.0.8
Suggests:       python-scipy < 1.13.0
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-protobuf
Suggests:       python-tokenizers >= 0.19
Suggests:       python-torchaudio
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-optuna
Suggests:       python-ray >= 2.7.0
Suggests:       python-sigopt
Suggests:       python-timm <= 0.9.16
Suggests:       python-torchvision
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-codecarbon == 1.2.0
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-decord == 0.6.0
Suggests:       python-av == 9.2.0
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-optimum-benchmark >= 0.2.0
Suggests:       python-codecarbon == 1.2.0
Suggests:       python-deepspeed >= 0.9.3
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-deepspeed >= 0.9.3
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-pytest >= 7.2.0
Suggests:       python-pytest-rich
Suggests:       python-pytest-xdist
Suggests:       python-timeout-decorator
Suggests:       python-parameterized
Suggests:       python-psutil
Suggests:       python-datasets
Suggests:       python-dill < 0.3.5
Suggests:       python-evaluate >= 0.2.0
Suggests:       python-pytest-timeout
Suggests:       python-ruff == 0.4.4
Suggests:       python-sacrebleu >= 1.4.12
Suggests:       python-rouge-score
Suggests:       python-nltk
Suggests:       python-GitPython < 3.1.19
Suggests:       python-sacremoses
Suggests:       python-rjieba
Suggests:       python-beautifulsoup4
Suggests:       python-tensorboard
Suggests:       python-pydantic
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-faiss-cpu
Suggests:       python-datasets
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-optuna
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-protobuf
Suggests:       python-tensorflow > 2.9
Suggests:       python-onnxconverter-common
Suggests:       python-tf2onnx
Suggests:       python-tensorflow-text < 2.16
Suggests:       python-keras-nlp >= 0.3.1
Suggests:       python-torch
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-jax >= 0.4.1
Suggests:       python-jaxlib >= 0.4.1
Suggests:       python-flax >= 0.4.1
Suggests:       python-optax >= 0.0.8
Suggests:       python-scipy < 1.13.0
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-protobuf
Suggests:       python-tokenizers >= 0.19
Suggests:       python-torchaudio
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-optuna
Suggests:       python-ray >= 2.7.0
Suggests:       python-sigopt
Suggests:       python-timm <= 0.9.16
Suggests:       python-torchvision
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-codecarbon == 1.2.0
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-decord == 0.6.0
Suggests:       python-av == 9.2.0
Suggests:       python-pytest >= 7.2.0
Suggests:       python-pytest-rich
Suggests:       python-pytest-xdist
Suggests:       python-timeout-decorator
Suggests:       python-parameterized
Suggests:       python-psutil
Suggests:       python-datasets
Suggests:       python-dill < 0.3.5
Suggests:       python-evaluate >= 0.2.0
Suggests:       python-pytest-timeout
Suggests:       python-ruff == 0.4.4
Suggests:       python-sacrebleu >= 1.4.12
Suggests:       python-rouge-score
Suggests:       python-nltk
Suggests:       python-GitPython < 3.1.19
Suggests:       python-sacremoses
Suggests:       python-rjieba
Suggests:       python-beautifulsoup4
Suggests:       python-tensorboard
Suggests:       python-pydantic
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-faiss-cpu
Suggests:       python-datasets
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-datasets
Suggests:       python-isort >= 5.5.4
Suggests:       python-ruff == 0.4.4
Suggests:       python-GitPython < 3.1.19
Suggests:       python-urllib3 < 2.0.0
Suggests:       python-fugashi >= 1.0
Suggests:       python-ipadic >= 1.0.0
Suggests:       python-unidic_lite >= 1.0.7
Suggests:       python-unidic >= 1.0.2
Suggests:       python-sudachipy >= 0.6.6
Suggests:       python-sudachidict_core >= 20220729
Suggests:       python-rhoknp >= 1.1.0
Suggests:       python-scikit-learn
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-pytest >= 7.2.0
Suggests:       python-pytest-rich
Suggests:       python-pytest-xdist
Suggests:       python-timeout-decorator
Suggests:       python-parameterized
Suggests:       python-psutil
Suggests:       python-datasets
Suggests:       python-dill < 0.3.5
Suggests:       python-evaluate >= 0.2.0
Suggests:       python-pytest-timeout
Suggests:       python-ruff == 0.4.4
Suggests:       python-sacrebleu >= 1.4.12
Suggests:       python-rouge-score
Suggests:       python-nltk
Suggests:       python-GitPython < 3.1.19
Suggests:       python-sacremoses
Suggests:       python-rjieba
Suggests:       python-beautifulsoup4
Suggests:       python-tensorboard
Suggests:       python-pydantic
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-faiss-cpu
Suggests:       python-datasets
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-tensorflow > 2.9
Suggests:       python-onnxconverter-common
Suggests:       python-tf2onnx
Suggests:       python-tensorflow-text < 2.16
Suggests:       python-keras-nlp >= 0.3.1
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-protobuf
Suggests:       python-tokenizers >= 0.19
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-datasets
Suggests:       python-isort >= 5.5.4
Suggests:       python-ruff == 0.4.4
Suggests:       python-GitPython < 3.1.19
Suggests:       python-urllib3 < 2.0.0
Suggests:       python-scikit-learn
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-onnxconverter-common
Suggests:       python-tf2onnx
Suggests:       python-onnxruntime >= 1.4.0
Suggests:       python-onnxruntime-tools >= 1.4.2
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-pytest >= 7.2.0
Suggests:       python-pytest-rich
Suggests:       python-pytest-xdist
Suggests:       python-timeout-decorator
Suggests:       python-parameterized
Suggests:       python-psutil
Suggests:       python-datasets
Suggests:       python-dill < 0.3.5
Suggests:       python-evaluate >= 0.2.0
Suggests:       python-pytest-timeout
Suggests:       python-ruff == 0.4.4
Suggests:       python-sacrebleu >= 1.4.12
Suggests:       python-rouge-score
Suggests:       python-nltk
Suggests:       python-GitPython < 3.1.19
Suggests:       python-sacremoses
Suggests:       python-rjieba
Suggests:       python-beautifulsoup4
Suggests:       python-tensorboard
Suggests:       python-pydantic
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-faiss-cpu
Suggests:       python-datasets
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-torch
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-protobuf
Suggests:       python-tokenizers >= 0.19
Suggests:       python-torchaudio
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-optuna
Suggests:       python-ray >= 2.7.0
Suggests:       python-sigopt
Suggests:       python-timm <= 0.9.16
Suggests:       python-torchvision
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-codecarbon == 1.2.0
Suggests:       python-datasets
Suggests:       python-isort >= 5.5.4
Suggests:       python-ruff == 0.4.4
Suggests:       python-GitPython < 3.1.19
Suggests:       python-urllib3 < 2.0.0
Suggests:       python-fugashi >= 1.0
Suggests:       python-ipadic >= 1.0.0
Suggests:       python-unidic_lite >= 1.0.7
Suggests:       python-unidic >= 1.0.2
Suggests:       python-sudachipy >= 0.6.6
Suggests:       python-sudachidict_core >= 20220729
Suggests:       python-rhoknp >= 1.1.0
Suggests:       python-scikit-learn
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-onnxruntime >= 1.4.0
Suggests:       python-onnxruntime-tools >= 1.4.2
Suggests:       python-jax >= 0.4.1
Suggests:       python-jaxlib >= 0.4.1
Suggests:       python-flax >= 0.4.1
Suggests:       python-optax >= 0.0.8
Suggests:       python-scipy < 1.13.0
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-ftfy
Suggests:       python-optuna
Suggests:       python-ray >= 2.7.0
Suggests:       python-sigopt
Suggests:       python-fugashi >= 1.0
Suggests:       python-ipadic >= 1.0.0
Suggests:       python-unidic_lite >= 1.0.7
Suggests:       python-unidic >= 1.0.2
Suggests:       python-sudachipy >= 0.6.6
Suggests:       python-sudachidict_core >= 20220729
Suggests:       python-rhoknp >= 1.1.0
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-natten >= 0.14.6
Suggests:       python-onnxconverter-common
Suggests:       python-tf2onnx
Suggests:       python-onnxruntime >= 1.4.0
Suggests:       python-onnxruntime-tools >= 1.4.2
Suggests:       python-onnxruntime >= 1.4.0
Suggests:       python-onnxruntime-tools >= 1.4.2
Suggests:       python-optuna
Suggests:       python-datasets
Suggests:       python-isort >= 5.5.4
Suggests:       python-ruff == 0.4.4
Suggests:       python-GitPython < 3.1.19
Suggests:       python-urllib3 < 2.0.0
Suggests:       python-ray >= 2.7.0
Suggests:       python-faiss-cpu
Suggests:       python-datasets
Suggests:       python-ruff == 0.4.4
Suggests:       python-sagemaker >= 2.31.0
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-protobuf
Suggests:       python-pydantic
Suggests:       python-uvicorn
Suggests:       python-fastapi
Suggests:       python-starlette
Suggests:       python-sigopt
Suggests:       python-scikit-learn
Suggests:       python-torchaudio
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-pytest >= 7.2.0
Suggests:       python-pytest-rich
Suggests:       python-pytest-xdist
Suggests:       python-timeout-decorator
Suggests:       python-parameterized
Suggests:       python-psutil
Suggests:       python-datasets
Suggests:       python-dill < 0.3.5
Suggests:       python-evaluate >= 0.2.0
Suggests:       python-pytest-timeout
Suggests:       python-ruff == 0.4.4
Suggests:       python-sacrebleu >= 1.4.12
Suggests:       python-rouge-score
Suggests:       python-nltk
Suggests:       python-GitPython < 3.1.19
Suggests:       python-sacremoses
Suggests:       python-rjieba
Suggests:       python-beautifulsoup4
Suggests:       python-tensorboard
Suggests:       python-pydantic
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-faiss-cpu
Suggests:       python-datasets
Suggests:       python-cookiecutter == 1.7.3
Suggests:       python-tensorflow > 2.9
Suggests:       python-onnxconverter-common
Suggests:       python-tf2onnx
Suggests:       python-tensorflow-text < 2.16
Suggests:       python-keras-nlp >= 0.3.1
Suggests:       python-keras > 2.9
Suggests:       python-tensorflow-cpu > 2.9
Suggests:       python-onnxconverter-common
Suggests:       python-tf2onnx
Suggests:       python-tensorflow-text < 2.16
Suggests:       python-keras-nlp >= 0.3.1
Suggests:       python-tensorflow-probability < 0.24
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-timm <= 0.9.16
Suggests:       python-tokenizers >= 0.19
Suggests:       python-torch
Suggests:       python-accelerate >= 0.21.0
Suggests:       python-torchaudio
Suggests:       python-librosa
Suggests:       python-pyctcdecode >= 0.4.0
Suggests:       python-phonemizer
Suggests:       python-kenlm
Suggests:       python-torchvision
Suggests:       python-Pillow >= 10.0.1
Suggests:       python-filelock
Suggests:       python-huggingface_hub >= 0.23.2
Suggests:       python-importlib_metadata
Suggests:       python-numpy >= 1.17
Suggests:       python-packaging >= 20.0
Suggests:       python-protobuf
Suggests:       python-regex
Suggests:       python-requests
Suggests:       python-sentencepiece >= 0.1.91
Suggests:       python-torch
Suggests:       python-tokenizers >= 0.19
Suggests:       python-tqdm >= 4.27
Suggests:       python-decord == 0.6.0
Suggests:       python-av == 9.2.0
Suggests:       python-Pillow >= 10.0.1
BuildArch:      noarch
%python_subpackages

%description
Transformers provides thousands of pretrained models to perform tasks on
different modalities such as text, vision, and audio.
These models can be applied on:
* Text, for tasks like text classification, information extraction, question
  answering, summarization, translation, and text generation, in over 100
  languages.  
* Images, for tasks like image classification, object detection,
  and segmentation.
* Audio, for tasks like speech recognition and audio
  classification.


%prep
%setup -q -n transformers-%{version}
# fix shebang
find . -name \*.py -type f -exec \
  sed -i "s|^#!\s*%{_bindir}/env python|#!%{_bindir}/python3|" {} \;

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/transformers-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative transformers-cli

%postun
%python_uninstall_alternative transformers-cli

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/transformers-cli
%{python_sitelib}/*

%changelog
