#
# spec file for package erlang-sd_notify
#
# Copyright (c) 2020 SUSE LLC
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


%define app_name sd_notify

Name:           erlang-%{app_name}
Version:        1.1
Release:        0
%define app_ver {%version}
Summary:        Erlang interface to systemd notify subsystem
License:        MIT
URL:            https://github.com/systemd/erlang-sd_notify
Source0:        erlang-%{app_name}-%{version}.tar.xz
BuildRequires:  erlang-rebar
Requires:       erlang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Erlang module for native access to the systemd-notify facilities.

%prep
%setup -q

%build
%rebar compile

%install
mkdir -p %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/ebin
install -m 644 -p ebin/%{app_name}.app %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/ebin
install -m 644 -p ebin/%{app_name}.beam %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/ebin

%files
%defattr(-,root,root,-)
%doc LICENSE
%dir %{erlang_libdir}/%{app_name}-%{app_ver}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/ebin
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/%{app_name}.app
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/*.beam

%changelog
