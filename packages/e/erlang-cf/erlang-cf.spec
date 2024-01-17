#
# spec file for package erlang-cf
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


%define app_name cf
%define app_ver %(echo "%{version}" | cut -d "+" -f1)
Name:           erlang-%{app_name}
Version:        0.3.1
Release:        0
Summary:        A helper library for termial colour printing for Erlang
License:        BSD-3-Clause
Group:          Development/Libraries/Other
URL:            https://github.com/project-fifo/cf
Source:         %{app_name}-%{version}.tar.xz
BuildRequires:  erlang
BuildRequires:  erlang-rebar
Requires:       erlang

%description
A helper library for termial colour printing extending the io:format syntax to add colours.

%prep
%setup -q -n %{app_name}-%{version}

%build
%rebar_set_vsn_cache %{app_ver}
%rebar compile

%install
for dir in ebin ; do
	mkdir -p %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}
	cp -r ${dir}/* %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}/
done

%files
%license LICENSE
%doc README.md
%dir %{erlang_libdir}/%{app_name}-%{app_ver}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/ebin
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/%{app_name}.app
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/*.beam

%changelog
