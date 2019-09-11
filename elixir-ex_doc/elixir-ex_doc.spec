#
# spec file for package elixir-ex_doc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define app_name ex_doc
Name:           elixir-%{app_name}
Version:        0.7.2
Release:        0
%define app_ver %(echo "%{version}" | cut -d "+" -f1)
Summary:        ExDoc produces HTML and online documentation for Elixir projects
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Other
Url:            https://github.com/elixir-lang/ex_doc
Source:         %{app_name}-v%{version}.tar.bz2
Requires:       elixir
BuildRequires:  elixir
BuildRequires:  elixir-hex
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ExDoc is a tool to generate documentation for your Elixir projects. In case you are looking for documentation for Elixir itself, check out Elixir's website.

%prep
%setup -q -n %{app_name}-v%{version}

%build
export LANG=en_US.UTF-8
%{mix_compile}

%install
for dir in ebin ; do
	mkdir -p %{buildroot}%{elixir_libdir}/%{app_name}/${dir}
	cp -r _build/prod/lib/%{app_name}/${dir}/* %{buildroot}%{elixir_libdir}/%{app_name}/${dir}/
done
install -D -m 0755 bin/ex_doc %{buildroot}%{_bindir}/ex_doc

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md
%license LICENSE
%attr(0755,root,root) %{_bindir}/ex_doc
%dir %{elixir_libdir}/%{app_name}
%dir %{elixir_libdir}/%{app_name}/ebin
%{elixir_libdir}/%{app_name}/ebin/%{app_name}.app
%{elixir_libdir}/%{app_name}/ebin/*.beam

%changelog
