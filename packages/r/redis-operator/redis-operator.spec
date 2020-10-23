#
# spec file for package redis-operator
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define goipath github.com/spotahome/redis-operator

Name:           redis-operator
Version:        1.0.0
Release:        0
Summary:        Redis Operator creates/configures/manages redis-failovers atop Kubernetes
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/spotahome/redis-operator
Source0:        %{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-Ignore-terminating-pods-for-sentinel.patch gh#spotahome/redis-operator#281
Patch0:         0001-Ignore-terminating-pods-for-sentinel.patch
# PATCH-FIX-UPSTREAM 0002-Prevent-warning-from-redis-cli.patch gh#spotahome/redis-operator#256
Patch1:         0002-Prevent-warning-from-redis-cli.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.13

%description
Redis Operator creates/configures/manages redis-failovers atop Kubernetes.
Allows to set up Redis in high available mode using redis-sentinel.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild cmd/redisoperator

%install
%goinstall
mv %{buildroot}%{_bindir}/redisoperator %{buildroot}%{_bindir}/redis-operator

%files
%license LICENSE
%doc README.md
%{_bindir}/redis-operator

%changelog
