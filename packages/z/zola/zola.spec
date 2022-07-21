#
# spec file for package zola
#
# Copyright (c) 2022 SUSE LLC
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


Name:           zola
Version:        0.16.0
Release:        0
Summary:        Fast static site generator
License:        MIT
URL:            https://github.com/getzola/zola
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  libgcc_s1
BuildRequires:  pkg-config
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
ExclusiveArch:  %{rust_tier1_arches}

%description
Zola is a static site generator (SSG), similar to Hugo, Pelican, and Jekyll.
It is written in Rust and uses the Tera template engine, which is similar to
Jinja2, Django templates, Liquid, and Twig. Content is written in CommonMark,
a strongly defined, highly compatible specification of Markdown.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/zola
%license LICENSE

%doc README.md

%changelog
