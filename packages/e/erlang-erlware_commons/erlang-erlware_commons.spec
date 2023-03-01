#
# spec file for package erlang-erlware_commons
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


%define app_name erlware_commons
%define app_ver %(echo "%{version}" | cut -d "+" -f1)
Name:           erlang-%{app_name}
Version:        1.6.0
Release:        0
Summary:        A project focused on all aspects of reusable Erlang components
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/erlware/erlware_commons
Source:         %{app_name}-%{version}.tar.xz
BuildRequires:  erlang
BuildRequires:  erlang-cf
BuildRequires:  erlang-rebar
# make the tests happy
BuildRequires:  git
Requires:       erlang
Requires:       erlang-cf

%description
Erlware Commons is an Erlware project focused on all aspects of reusable Erlang components.

%prep
%setup -q -n %{app_name}-%{version}

%build
%rebar compile

%install
for dir in ebin include priv ; do
	mkdir -p %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}
	cp -r ${dir}/* %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/${dir}/
done

%check
# ec_cmd_log:color_test is expecting that erlang-cf package considers the TERMinal
# as color-capable one.
export TERM=ansi
%rebar eunit

%files
%license COPYING
%doc doc
%dir %{erlang_libdir}/%{app_name}-%{app_ver}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/ebin
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/%{app_name}.app
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/*.beam
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/include
%{erlang_libdir}/%{app_name}-%{app_ver}/include/*.hrl
%{erlang_libdir}/%{app_name}-%{app_ver}/priv

%changelog
