#
# spec file for package ollama
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


Name:           ollama
Version:        0.3.3
Release:        0
Summary:        Tool for running AI models on-premise
License:        MIT
URL:            https://ollama.com
Source:         %{name}-%{version}.tar
Source1:        vendor.tar.zstd
Source2:        ollama.service
Source3:        %{name}-user.conf
Patch0:         enable-lto.patch
BuildRequires:  cmake >= 3.24
BuildRequires:  git
BuildRequires:  sysuser-tools
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.22
%sysusers_requires
%if 0%{?sle_version} == 150600
BuildRequires:  gcc12-c++
BuildRequires:  libstdc++6-gcc12
%else
BuildRequires:  gcc-c++ >= 11.4.0
%endif
# 32bit seems not to be supported anymore
ExcludeArch:    %ix86 %arm

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
%sysusers_generate_pre %{SOURCE3} %{name} %{name}-user.conf

%ifnarch ppc64
export GOFLAGS="-buildmode=pie -mod=vendor"
%endif
%if 0%{?sle_version} == 150600
export CXX=g++-12
export CC=gcc-12
# pie doesn't work with gcc12 on leap
export GOFLAGS="-mod=vendor"
%endif

export OLLAMA_SKIP_PATCHING=1

go generate ./...
go build -v .

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}-user.conf
install -d %{buildroot}%{_localstatedir}/lib/%{name}

mkdir -p "%{buildroot}/%{_docdir}/%{name}"
cp -Ra docs/* "%{buildroot}/%{_docdir}/%{name}"

%check
%if 0%{?sle_version} == 150600
export CXX=g++-12
export CC=gcc-12
# pie doesn't work with gcc12 on leap
export GOFLAGS="-mod=vendor"
%endif
go test ./...

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

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
%attr(-, ollama, ollama) %{_localstatedir}/lib/%{name}

%changelog
