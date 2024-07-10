#
# spec file for package envoy-build-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           envoy-build-tools
Version:        20191023
Release:        0
Summary:        Bazel toolchains for Envoy and UDPA build ecosystem
License:        Apache-2.0
Url:            https://github.com/envoyproxy/envoy-build-tools
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildArch:      noarch

%description
envoy-build-tools is the project which contains custom Bazel toolchains which
define the compiler flags for Envoy.

%prep
%setup -q
rm -rf .git
find . \( -name "BUILD" -o -name "*.bzl" -o -name "builtin_include_directory_paths" \) -exec chmod -x {} \;

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r * %{buildroot}%{_datadir}/%{name}
%fdupes %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
%{_datadir}/envoy-build-tools

%changelog

