#
# spec file for package python-gpt4all
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


%define llamavers b2245
%define komputevers c339310

%{?sle15_python_module_pythons}

Name:           python-gpt4all
Version:        2.7.3
Release:        0
Summary:        open source llms for all
License:        MIT
URL:            https://github.com/nomic-ai/gpt4all
Source0:        https://github.com/nomic-ai/gpt4all/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        https://github.com/nomic-ai/llama.cpp/archive/refs/tags/%{llamavers}.tar.gz
Source2:        https://github.com/nomic-ai/kompute/archive/c339310.tar.gz
Source3:        gpt4all.rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?sle_version} == 150600
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  python-rpm-macros
BuildRequires:  vulkan-devel
BuildRequires:  vulkan-utility-libraries-devel
BuildRequires:  shaderc
BuildRequires:  shaderc-devel
BuildRequires:  fmt-devel
Requires:       %{python_module requests}
Requires:       %{python_module tqdm}
%python_subpackages

%description
GPT4All is an ecosystem to run powerful and customized large language models
that work locally on consumer grade CPUs and any GPU.

%prep
%setup -n gpt4all-%{version}
cd gpt4all-backend
rmdir llama.cpp-mainline
tar xzf %{S:1}
mv llama.cpp-%{llamavers} llama.cpp-mainline
cd llama.cpp-mainline
rmdir kompute
tar xzf %{S:2}
mv kompute-%{komputevers}* kompute

%build
%if 0%{?sle_version} == 150600
export CXX=g++-12
export CC=gcc-12
%endif
cd gpt4all-backend
%cmake -DLLAMA_KOMPUTE=ON \
       -DLLMODEL_CUDA=OFF \
       -DLLMODEL_VULKAN=ON \
       -DKOMPUTE_OPT_USE_BUILT_IN_VULKAN_HEADER=OFF \
       -DKOMPUTE_OPT_DISABLE_VULKAN_VERSION_CHECK=ON \
       -DKOMPUTE_OPT_USE_BUILT_IN_FMT=OFF \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
cd ../../gpt4all-bindings/python
%python_build

%install
cd gpt4all-bindings/python
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%{python_sitelib}/*

%changelog
