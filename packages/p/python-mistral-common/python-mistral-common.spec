#
# spec file for package python-mistral-common
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


%{?sle15_python_module_pythons}
Name:           python-mistral-common
Version:        1.11.5
Release:        0
Summary:        Library of common utilities for Mistral AI
License:        Apache-2.0
URL:            https://github.com/mistralai/mistral-common
Source0:        https://files.pythonhosted.org/packages/source/m/mistral_common/mistral_common-%{version}.tar.gz
# Upstream ships no license file in the sdist (the license-files entry in
# pyproject.toml points at LICENSE which is omitted from the tarball); carry
# the Apache-2.0 text from the upstream git tag.
Source1:        LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 10.3.0
Requires:       python-jsonschema >= 4.21.1
Requires:       python-numpy >= 1.25
# mistral_common[image] extra (required by vllm); satisfied by the cv2
# module from the Factory opencv package.
Requires:       python-opencv
Requires:       python-pydantic >= 2.7
Requires:       python-pydantic-extra-types >= 2.10.5
Requires:       python-requests >= 2.0.0
Requires:       python-tiktoken >= 0.7.0
Requires:       python-typing_extensions >= 4.11.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
mistral-common is a library of common utilities for Mistral AI models. It
provides the tokenizers (SentencePiece and Tekken), request/response
protocol data models, and validation helpers used to build prompts and
parse completions for Mistral models. This build enables the image extra
so multimodal image inputs can be processed.

%prep
%autosetup -p1 -n mistral_common-%{version}
# The sdist omits the license file upstream declares; carry it in from Source1.
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mistral_common
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The full pytest suite is not run: several hard runtime dependencies
# (python-pydantic-extra-types) and test-only helpers are not available in
# Factory, and many tests download tokenizer/model assets from the network.
# Restrict to a smoke import of the top-level package, which only reads the
# installed distribution metadata.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import mistral_common; print(mistral_common.__version__)"

%post
%python_install_alternative mistral_common

%postun
%python_uninstall_alternative mistral_common

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/mistral_common
%{python_sitelib}/mistral_common
%{python_sitelib}/mistral_common-%{version}.dist-info

%changelog
