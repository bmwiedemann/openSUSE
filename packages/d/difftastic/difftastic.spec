#
# spec file for package difftastic
#
# Copyright (c) 2025 SUSE LLC
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
Version:        0.63.0
Release:        0
Summary:        A structural diff that understands syntax
License:        Apache-2.0 AND MIT
URL:            https://difftastic.wilfred.me.uk/
Source0:        https://github.com/Wilfred/difftastic/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  jq
BuildRequires:  libstdc++6-devel-gcc13
BuildRequires:  rust >= 1.74.1
BuildRequires:  shared-mime-info
Requires:       shared-mime-info
%if 0%{?suse_version} >= 1600
Suggests:       %{name}-doc
%endif
ExclusiveArch:  %{rust_tier1_arches}

%description
Difftastic is a structural diff tool that compares files based on their syntax.

%if 0%{?suse_version} >= 1600
%package doc
Summary:        Documentation for difftastic
BuildRequires:  mdbook
BuildArch:      noarch

%description doc
This package contains the documentation for difftastic.
%endif

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%if 0%{?suse_version} >= 1600
cd manual
mdbook build
%endif

%install
install -D -m 0755 -t %{buildroot}%{_bindir} target/release/difft

%if 0%{?suse_version} >= 1600
rm -v manual/book/.nojekyll
%fdupes -s manual/book
%endif

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/difft

%if 0%{?suse_version} >= 1600
%files doc
%license LICENSE
%doc manual/book
%endif

%changelog
