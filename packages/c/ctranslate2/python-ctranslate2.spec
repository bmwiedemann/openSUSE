#
# spec file for package python-ctranslate2
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
Name:           python-ctranslate2
Version:        4.5.0
Release:        0
Summary:        Library for efficient inference with Transformer models
License:        MIT
URL:            https://github.com/OpenNMT/CTranslate2
Source:         CTranslate2-%version.tar.xz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  ctranslate2-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  openblas-devel

BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module pybind11}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}

ExcludeArch:    %ix86 %arm

Requires(post): update-alternatives
Requires(postun): update-alternatives

%python_subpackages

%description
CTranslate2 is a C++ and Python library for efficient inference with Transformer models.

NOTE: hardware accelaration is currently disabled in this package for license reasons

%prep
%autosetup -p1 -n CTranslate2-%version

%build
cd python
%pyproject_wheel

%install
cd python
%pyproject_install
for bin in ct2-fairseq-converter ct2-marian-converter ct2-openai-gpt2-converter ct2-opennmt-py-converter ct2-opennmt-tf-converter ct2-opus-mt-converter ct2-transformers-converter; do
%python_clone -a %{buildroot}%{_bindir}/$bin
done

%post
for bin in ct2-fairseq-converter ct2-marian-converter ct2-openai-gpt2-converter ct2-opennmt-py-converter ct2-opennmt-tf-converter ct2-opus-mt-converter ct2-transformers-converter; do
%python_install_alternative $bin
done

%postun
for bin in ct2-fairseq-converter ct2-marian-converter ct2-openai-gpt2-converter ct2-opennmt-py-converter ct2-opennmt-tf-converter ct2-opus-mt-converter ct2-transformers-converter; do
%python_uninstall_alternative $bin
done

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/ct2-fairseq-converter
%python_alternative %{_bindir}/ct2-marian-converter
%python_alternative %{_bindir}/ct2-openai-gpt2-converter
%python_alternative %{_bindir}/ct2-opennmt-py-converter
%python_alternative %{_bindir}/ct2-opennmt-tf-converter
%python_alternative %{_bindir}/ct2-opus-mt-converter
%python_alternative %{_bindir}/ct2-transformers-converter
%{python_sitearch}//ctranslate2*

%changelog
