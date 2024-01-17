#
# spec file for package fclones
#
# Copyright (c) 2023 SUSE LLC
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


Name:           fclones
Version:        0.34.0
Release:        0
Summary:        Finds duplicate, unique, under- or over-replicated files
License:        MIT
URL:            https://github.com/pkolaczk/%{name}
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.45.0

%description
A simple command-line utility program that finds duplicate, unique, under- or over-replicated files.
Contrary to fdupes or rdfind, %{name} processes files in parallel, which makes it very efficient on SSDs.
%{name} communicates through standard Unix streams and it can write reports in human- and machine-friendly formats,
therefore you can easily combine it with other tools.

%prep
%setup -qa1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
