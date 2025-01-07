#
# spec file for package kubediff
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


Name:           kubediff
Version:        0.1.7
Release:        0
Summary:	Cli tool written in Rust that is a wrapper around kubectl diff
License:        MIT
URL:            https://github.com/Ramilito/kubediff
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.82.0
BuildRequires:  cargo-packaging

%description
Used to sanity check and understand what has changed between environments.

This cli tool written in Rust is a wrapper around kubectl diff and is supposed
to diff one or multiple projects instead of single files against any
environment you want, be it docker-desktop, dev, prod.

It takes a glob pattern to one or more projects and beautifies the output so
you can get an understanding on what differences there are.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}

%files
%doc .github/README.md
%license LICENSE
%{_bindir}/kubediff

%changelog
