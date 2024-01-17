#
# Copyright (c) 2021 SUSE LLC
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

Name:           spdx-sbom-generator
Version:        0.0.13
Release:        0
Summary:        SPDX Software Bill of Materials (SBOM) Generator
License:        Apache-2.0 AND CC-BY-4.0
Url:            https://github.com/opensbom-generator/spdx-sbom-generator
Source:         https://github.com/opensbom-generator/spdx-sbom-generator/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.bz2
BuildRequires:  golang(API)
BuildRequires:  golang-packaging
%{go_nostrip}

%description
The spdx-sbom-generator tool helps those in the community that want to
generate SPDX Software Bill of Materials (SBOMs) with current package
managers.

It has a command line Interface (CLI) that lets you generate SBOM
information, including components, licenses, copyrights, and security
references of your software using SPDX v2.2 specification and aligning
with the current known minimum elements from NTIA. It automatically
determines which package managers or build systems are actually being
used by the software.

spdx-sbom-generator is supporting the following (bundling) package managers:

* GoMod (go)
* Cargo (Rust)
* Composer (PHP)
* DotNet (.NET)
* Maven (Java)
* NPM (Node.js)
* Yarn (Node.js)
* PIP (Python)
* Pipenv (Python)
* Gems (Ruby) 
* Swift Package Manager (Swift)

%prep
%autosetup -p1 -a1

%build
export ldflags='-X "main.version=%version"'
GO111MODULE=on GOFLAGS=-mod=vendor GOOS=linux go build -buildmode=pie -ldflags "$ldflags" -o bin/spdx-sbom-generator cmd/generator/generator.go

bin/spdx-sbom-generator

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 bin/spdx-sbom-generator %{buildroot}%{_bindir}/

%files
%license LICENSES/*.txt
%doc *.md
%{_bindir}/spdx-sbom-generator

%changelog
