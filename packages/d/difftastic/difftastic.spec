#
# spec file for package difftastic
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 munix9@googlemail.com
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


Name:           difftastic
Version:        0.52.0
Release:        0
Summary:        A structural diff that understands syntax
License:        MIT AND Apache-2.0
URL:            https://difftastic.wilfred.me.uk/
Source0:        https://github.com/Wilfred/difftastic/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  c++_compiler
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  jq
BuildRequires:  mdbook
BuildRequires:  shared-mime-info
Requires:       shared-mime-info
Suggests:       %{name}-doc
ExclusiveArch:  %{rust_tier1_arches}

%description
Difftastic is a structural diff tool that compares files based on their syntax.

%package doc
Summary:        Documentation for difftastic
BuildArch:      noarch

%description doc
This package contains the documentation for difftastic.

%prep
%autosetup -a1 -p1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

cd manual
mdbook build

%install
#%%{cargo_install}
install -D -m 0755 -t %{buildroot}%{_bindir} target/release/difft

rm -v manual/book/.nojekyll
%fdupes -s manual/book

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/difft

%files doc
%license LICENSE
%doc manual/book

%changelog
