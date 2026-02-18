#
# spec file for package rumdl
#
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


Name:           rumdl
Version:        0.1.22
Release:        0
Summary:        Markdown Linter written in Rust
License:        MIT
URL:            https://github.com/rvben/rumdl
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

# rumdl@0.0.172 requires rustc 1.91.0
BuildRequires:  cargo >= 1.91

# out-of-memory errors
ExcludeArch:    %{ix86} %{arm} ppc64le

%description
rumdl is a high-performance Markdown linter and formatter that helps ensure
consistency and best practices in your Markdown files. Inspired by ruff 's
approach to Python linting, rumdl brings similar speed and developer experience
improvements to the Markdown ecosystem.

It offers:

- Built for speed with Rust - significantly faster than alternatives
- 54 lint rules covering common Markdown issues
- Automatic formatting with --fix for files and stdin/stdout
- Zero dependencies - single binary with no runtime requirements
- Highly configurable with TOML-based config files
- Multiple installation options - Rust, Python, standalone binaries
- Installable via pip for Python users
- Modern CLI with detailed error reporting
- CI/CD friendly with non-zero exit code on errors


%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
