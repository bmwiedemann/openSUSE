#
# spec file for package ollama
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?sle_version} && 0%{?sle_version} >= 150600
%global force_gcc_version 12
%endif

Name:           ollama
Version:        0.10.1
Release:        0
Summary:        Tool for running AI models on-premise
License:        MIT
URL:            https://ollama.com
Source:         https://github.com/ollama/ollama/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zstd
Source2:        ollama.service
Source3:        %{name}-user.conf
Source4:        sysconfig.ollama
BuildRequires:  cmake >= 3.24
BuildRequires:  git-core
BuildRequires:  ninja
BuildRequires:  sysuser-tools
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.24
Requires(pre):  %fillup_prereq
# 32bit seems not to be supported anymore
ExcludeArch:    %{ix86} %{arm}
%sysusers_requires
%if 0%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  libstdc++6-gcc%{?force_gcc_version}
%else
BuildRequires:  gcc-c++ >= 11.4.0
BuildRequires:  libstdc++6
%endif

%description
Ollama is a tool for running AI models on one's own hardware.
It offers a command-line interface and a RESTful API.
New models can be created or existing ones modified in the
Ollama library using the Modelfile syntax.
Source model weights found on Hugging Face and similar sites
can be imported.

%prep
%autosetup -a1 -p1

%build
%define __builder ninja

%sysusers_generate_pre %{SOURCE3} %{name} %{name}-user.conf

%ifnarch ppc64
export GOFLAGS="-buildmode=pie -mod=vendor"
%endif
%if 0%{?force_gcc_version}
export CXX="g++-%{?force_gcc_version}"
export CC="gcc-%{?force_gcc_version}"
# pie doesn't work with gcc12 on leap
export GOFLAGS="-mod=vendor"
%endif

export GOFLAGS="${GOFLAGS} -v"

%cmake -UOLLAMA_INSTALL_DIR -DOLLAMA_INSTALL_DIR=%{_libdir}/ollama
%cmake_build

cd ..
go build -mod=vendor -buildmode=pie -o %{name} .

%install
%cmake_install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}-user.conf
install -D -m 0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d %{buildroot}%{_localstatedir}/lib/%{name}

mkdir -p "%{buildroot}/%{_docdir}/%{name}"
cp -Ra docs/* "%{buildroot}/%{_docdir}/%{name}"

%check
%if 0%{?force_gcc_version}
export CXX="g++-%{?force_gcc_version}"
export CC="gcc-%{?force_gcc_version}"
# pie doesn't work with gcc12 on leap
export GOFLAGS="-mod=vendor"
%endif
go test -v ./...

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}-user.conf
%{_prefix}/lib/ollama
%{_fillupdir}/sysconfig.%{name}
%attr(-, ollama, ollama) %{_localstatedir}/lib/%{name}

%changelog
