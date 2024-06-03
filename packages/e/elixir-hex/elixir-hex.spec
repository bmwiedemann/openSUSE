#
# spec file for package elixir-hex
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


%define app_name hex
%define app_ver %(echo "%{version}" | cut -d "+" -f1)
Name:           elixir-%{app_name}
Version:        2.1.1
Release:        0
Summary:        Package manager for the Erlang VM
License:        Apache-2.0
Group:          Development/Libraries/Other
URL:            https://github.com/hexpm/hex
Source:         %{app_name}-%{version}.tar.xz
BuildRequires:  elixir
Requires:       elixir
BuildArch:      noarch

%description
Hex is package manager for the Erlang VM.

This project currently provides tasks that integrate with Mix, Elixir's build tool.

See http://hex.pm for installation instructions and other documentation.

%prep
%setup -q -n %{app_name}-%{version}

%build
export LANG=en_US.UTF-8
%{mix_compile}

%install
for dir in ebin ; do
	mkdir -p %{buildroot}%{elixir_libdir}/%{app_name}/${dir}
	cp -r _build/prod/lib/%{app_name}/${dir}/* %{buildroot}%{elixir_libdir}/%{app_name}/${dir}/
done

%files
%doc README.md CHANGELOG.md
%dir %{elixir_libdir}/%{app_name}
%dir %{elixir_libdir}/%{app_name}/ebin
%{elixir_libdir}/%{app_name}/ebin/%{app_name}.app
%{elixir_libdir}/%{app_name}/ebin/*.beam

%changelog
