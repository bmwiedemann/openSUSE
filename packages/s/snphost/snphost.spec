# SPDX-License-Identifier: Apache-2.0
#
# Copyright (C) 2023 VirTEE
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Larry Dewey <larry.dewey@amd.com>

Name:           snphost
Version:        0.1.2~0
Release:        0
Summary:        A Rust command-line tool for interacting with the AMD Secure Processor
License:        Apache-2.0
Group:          Productivity/Security
Url:            https://github.com/virtee/snphost
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:	openssl-devel
%if 0%{?suse_version} > 1600
BuildRequires: 	ruby3.2-rubygem-asciidoctor
%else
BuildRequires: 	ruby2.5-rubygem-asciidoctor
%endif
ExclusiveArch:  x86_64

%description
snphost is a command line utility for interacting with the AMD Secure Encrypted Virtualization - Secure Nested Paging (SEV-SNP) host environment (via the /dev/sev device).

%prep
# The number passed to -a (a stands for "after") should be equivalent to the Source tag number
# of the vendor tarball, 1 in this case (from Source1).
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}
 
%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
