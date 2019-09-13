#
# spec file for package erlang-sd_notify
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


%define app_name sd_notify

Name:           erlang-%{app_name}
Version:        1.0
Release:        0
%define app_ver {%version}
Summary:        Erlang interface to systemd notify subsystem
License:        MIT
Group:          Development/Libraries/Other
Url:            https://github.com/systemd/erlang-sd_notify
Source0:        erlang-%{app_name}-%{version}.tar.bz2
BuildRequires:  erlang-rebar
BuildRequires:  systemd-devel >= 219
Requires:       erlang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Erlang module for native access to the systemd-notify facilities.

%prep
%setup -q

%build
export LDFLAGS=-lsystemd
%rebar compile

%install
mkdir -p %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/{ebin,priv}
install -m 644 -p ebin/%{app_name}.app %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/ebin
install -m 644 -p ebin/%{app_name}.beam %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/ebin
install -m 755 -p priv/%{app_name}_drv.so %{buildroot}%{erlang_libdir}/%{app_name}-%{app_ver}/priv

%files
%defattr(-,root,root,-)
%doc LICENSE
%dir %{erlang_libdir}/%{app_name}-%{app_ver}
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/ebin
%dir %{erlang_libdir}/%{app_name}-%{app_ver}/priv
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/%{app_name}.app
%{erlang_libdir}/%{app_name}-%{app_ver}/ebin/*.beam
%{erlang_libdir}/%{app_name}-%{app_ver}/priv/%{app_name}_drv.so

%changelog
