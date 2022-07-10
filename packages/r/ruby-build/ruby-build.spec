#
# spec file for package ruby-build
#
# Copyright (c) 2022 SUSE LLC
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


# SLE does not provide "bats", which is required for testing.
%if %{undefined sle_version}
%bcond_without test
%else
%bcond_with test
%endif

Name:           ruby-build
Version:        20220710
Release:        0
BuildArch:      noarch
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/rbenv/ruby-build
Summary:        Compile and install Ruby
Source0:        https://github.com/rbenv/ruby-build/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-test-requiring-git-repository.patch
%if %{with test}
BuildRequires:  bats
%endif
Requires:       bash
Requires:       curl
Requires:       gcc
# ruby MRI BuildRequires
Requires:       bison
Requires:       automake
Requires:       gdbm-devel
Requires:       gperf
Requires:       graphviz
Requires:       libffi-devel
Requires:       libjpeg-devel
Requires:       openssl-devel
Requires:       readline-devel
Requires:       tk-devel

%description
ruby-build provides a simple way to compile and install different versions of Ruby on UNIX-like systems.

%prep
%setup -q

%patch0 -p1

%build

%install
PREFIX="%{buildroot}%{_prefix}" ./install.sh

sed -i 's|#!/usr/bin/env bash|#!/bin/bash|g' %{buildroot}%{_bindir}/*

%check
%if %{with test}
bats test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%dir %{_datadir}/ruby-build
%{_datadir}/ruby-build/*

%changelog
