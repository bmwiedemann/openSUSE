#
# spec file for package ruby-build
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


# SLE does not provide "bats", which is required for testing.
%if %{undefined sle_version}
%bcond_without test
%else
%bcond_with test
%endif

Name:           ruby-build
Version:        20240702
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
Requires:       gzip
Requires:       make
Requires:       tar
# Maybe Requires would be better.
Recommends:     %{name}-dependencies-mri

%description
ruby-build provides a simple way to compile and install different versions of Ruby on UNIX-like systems.

%package dependencies-mri
Summary:        Meta package for dependencies to build MRI
Requires:       automake
Requires:       bison
Requires:       gcc
Requires:       gdbm-devel
Requires:       gperf
Requires:       graphviz
Requires:       libffi-devel
Requires:       libjpeg-devel
Requires:       libyaml-devel
Requires:       openssl-devel
Requires:       readline-devel
Requires:       tk-devel

%description dependencies-mri
Meta package for ruby-build dependencies to build MRI.

%package dependencies-jruby
Summary:        Meta package for dependencies to build JRuby
Requires:       gcc-c++

%description dependencies-jruby
Meta package for ruby-build dependencies to build JRuby.

%package dependencies-truffleruby
Summary:        Meta package for dependencies to build TruffleRuby
Requires:       gcc
Requires:       openssl-devel

%description dependencies-truffleruby
Meta package for ruby-build dependencies to build TruffleRuby.

%package dependencies-mruby
Summary:        Meta package for dependencies to build mruby
Requires:       gcc
Requires:       git

%description dependencies-mruby
Meta package for ruby-build dependencies to build mruby.

%package dependencies-picoruby
Summary:        Meta package for dependencies to build PicoRuby
Requires:       gcc
Requires:       git

%description dependencies-picoruby
Meta package for ruby-build dependencies to build PicoRuby.

%prep
%autosetup -p1

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
%{_mandir}/man1/ruby-build*

%files dependencies-mri

%files dependencies-jruby

%files dependencies-truffleruby

%files dependencies-mruby

%files dependencies-picoruby

%changelog
