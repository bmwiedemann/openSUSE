#
# spec file for package erlang-getopt
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


%define app_name getopt
%define app_ver %(echo "%{version}" | cut -d "+" -f1)
Name:           erlang-%{app_name}
Version:        1.0.2
Release:        0
Summary:        Command-line parsing module similar to getopt
License:        BSD-3-Clause
Group:          Development/Libraries/Other
URL:            https://github.com/jcomellas/getopt.git
Source:         %{app_name}-%{version}.tar.xz
BuildRequires:  erlang
BuildRequires:  erlang-rebar
Requires:       erlang

%description
Command-line parsing module that uses a syntax similar to that of GNU getopt.

%prep
%setup -q -n %{app_name}-%{version}

%build
%rebar compile

%install
for dir in ebin ; do
	mkdir -p %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}
	cp -r ${dir}/* %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}/
done

%check
%rebar eunit

%files
%license LICENSE.txt
%doc examples README.md
%dir %{erlang_libdir}/%{app_name}-%{app_ver}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/ebin
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/%{app_name}.app
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/*.beam

%changelog
