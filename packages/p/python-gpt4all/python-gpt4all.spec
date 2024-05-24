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


%define llamavers a3f03b7
%define komputevers c339310

%{?sle15_python_module_pythons}

Name:           python-gpt4all
Version:        2.7.3
Release:        0
Summary:        open source llms for all
License:        Apache-2.0 AND MIT
URL:            https://github.com/nomic-ai/gpt4all
#MIT
Source0:        https://github.com/nomic-ai/gpt4all/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
#MIT
Source1:        https://github.com/nomic-ai/llama.cpp/archive/%{llamavers}.tar.gz
# Apache-2.0
Source2:        https://github.com/nomic-ai/kompute/archive/c339310.tar.gz
Source3:        %{name}.rpmlintrc
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
BuildRequires:  qt6-httpserver-devel
BuildRequires:  qt6-pdf-devel
BuildRequires:  qt6-quickdialogs2-devel
BuildRequires:  qt6-sql-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  qt6-wayland-devel
BuildRequires:  shaderc
BuildRequires:  shaderc-devel
BuildRequires:  update-desktop-files
BuildRequires:  vulkan-devel
BuildRequires:  vulkan-utility-libraries-devel
Requires:       %{python_module importlib-metadata}
Requires:       %{python_module requests}
Requires:       %{python_module tqdm}
Requires:       %{python_module typer}
Requires:       %{python_module typing_extensions}
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
cd gpt4all-backend
rmdir llama.cpp-mainline
tar xzf %{S:1}
mv llama.cpp-%{llamavers}* llama.cpp-mainline
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
cd ../../gpt4all-chat
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
install -D -m 0755 ../cli/app.py %{buildroot}/%{_bindir}/gpt4all-app
%{python_expand # fix shebang
sed -i 's|%{_bindir}/env python.*$|%{_bindir}/$python|' %{buildroot}/%{_bindir}/gpt4all-app
}
%python_clone -a %{buildroot}/%{_bindir}/gpt4all-app
cd ../../gpt4all-chat
%cmake_install

%suse_update_desktop_file -c gpt4all-chat chat "Open-source assistant-style large language models that run locally on your CPU" gpt4all-chat gpt4all-chat.svg

mv %{buildroot}%{_bindir}/chat %{buildroot}%{_bindir}/gpt4all-chat
rm -v  %{buildroot}%{_prefix}/lib/*.a
mkdir -p %{buildroot}%{_libdir}
mv -v %{buildroot}%{_prefix}/lib/libllmodel.so* %{buildroot}%{_libdir}

%post
%python_install_alternative gpt4all-app

%postun
%python_uninstall_alternative gpt4all-app

%files %{python_files}
%{python_sitelib}/*
%python_alternative %{_bindir}/gpt4all-app

%files -n gpt4all-chat
%{_bindir}/gpt4all-chat
%{_prefix}/lib/libgptj*
%{_prefix}/lib/libllamamodel*
%{_prefix}/lib/libbert*
%{_datadir}/applications/gpt4all-chat.desktop

%files -n libllmodel0
%{_libdir}/libllmodel.so*

%changelog
