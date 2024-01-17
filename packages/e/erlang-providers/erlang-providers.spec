#
# spec file for package erlang-providers
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


%define app_name providers
%define app_ver %(echo "%{version}" | cut -d "+" -f1)
Name:           erlang-%{app_name}
Version:        1.8.1
Release:        0
Summary:        An Erlang providers library
License:        Apache-2.0
Group:          Development/Libraries/Other
URL:            https://github.com/tsloughter/providers
Source:         %{app_name}-%{version}.tar.xz
Patch0:         0001-Relax-getopt-version-requirement.patch
BuildRequires:  erlang
BuildRequires:  erlang-getopt
BuildRequires:  erlang-rebar
Requires:       erlang
Requires:       erlang-getopt

%description
An Erlang providers library.

%prep
%setup -q -n %{app_name}-%{version}
%patch0 -p1

%build
%rebar compile

%install
for dir in ebin include ; do
	mkdir -p %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}
	cp -r ${dir}/* %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}/
done

%check
%rebar eunit

%files
%license LICENSE
%doc README.md
%dir %{erlang_libdir}/%{app_name}-%{app_ver}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/ebin
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/%{app_name}.app
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/*.beam
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/include
%{erlang_libdir}/%{app_name}-%{app_ver}/include/*.hrl

%changelog
