#
# spec file for package python-gpt4all
#
# Copyright (c) 2025 SUSE LLC
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


%define llamavers 58a55ef
%define komputevers 7c20efa

%{?sle15_python_module_pythons}
Name:           python-gpt4all
Version:        3.4.2
Release:        0
Summary:        open source llms for all
License:        Apache-2.0 AND MIT
URL:            https://github.com/nomic-ai/gpt4all
#MIT
Source0:        https://github.com/nomic-ai/gpt4all/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
#MIT
Source1:        https://github.com/nomic-ai/llama.cpp/archive/%{llamavers}.tar.gz#/llama.cpp-%{llamavers}.tar.gz
# Apache-2.0
Source2:        https://github.com/nomic-ai/kompute/archive/%{komputevers}.tar.gz#/kompute-%{komputevers}.tar.gz
Source3:        %{name}.rpmlintrc
# PATCH-FIX-OPENSUSE vk301.patch gh#KhronosGroup/Vulkan-Samples#1269
Patch1:         vk301.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?sle_version} == 150600
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  fmt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  qt6-base-common-devel
BuildRequires:  qt6-httpserver-devel
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-pdf-devel
BuildRequires:  qt6-quickdialogs2-devel
BuildRequires:  qt6-sql-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  qt6-wayland-devel
BuildRequires:  rapidjson-devel
BuildRequires:  shaderc
BuildRequires:  shaderc-devel
BuildRequires:  update-desktop-files
BuildRequires:  vulkan-devel
BuildRequires:  vulkan-utility-libraries-devel
Requires:       python-importlib-metadata
Requires:       python-jinja2
Requires:       python-requests
Requires:       python-tqdm
Requires:       python-typer
Requires:       python-typing_extensions
%python_subpackages

%description
GPT4All is an ecosystem to run powerful and customized large language models
that work locally on consumer grade CPUs and any GPU.

%package -n gpt4all-chat
Summary:        qt6 gui for gpt4all
Requires:       qt6-qt5compat-imports
Requires:       qt6-sql-sqlite
Requires:       qt6ct

%description -n gpt4all-chat
Qt based GUI for GPT4All versions with GPT-J as the base model.

%package -n libllmodel0
Summary:        gpt4all libllmodel0

%description -n libllmodel0
Libnrairy for aessing the models

%prep
%setup -n gpt4all-%{version}

pushd gpt4all-backend/deps/
rmdir llama.cpp-mainline
tar xzf %{S:1}
mv llama.cpp-%{llamavers}* llama.cpp-mainline
pushd llama.cpp-mainline/ggml/src
rmdir kompute
tar xzf %{S:2}
mv kompute-%{komputevers}* kompute
popd
popd
%patch -P1 -p1

%build
%if 0%{?sle_version} == 150600
export CXX=g++-12
export CC=gcc-12
%endif
cd gpt4all-backend
%cmake -DLLAMA_KOMPUTE=ON \
       -DLLMODEL_CUDA=OFF \
       -DLLMODEL_VULKAN=OFF \
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

%files %{python_files}
%{python_sitelib}/*

%changelog
