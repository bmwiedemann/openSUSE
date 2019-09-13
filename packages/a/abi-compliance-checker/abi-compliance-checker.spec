#
# spec file for package abi-compliance-checker
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


Name:           abi-compliance-checker
Version:        2.3
Release:        0
Summary:        A Compliance Checker For library ABIs
License:        LGPL-2.1-only
Group:          Development/Tools/Other
Url:            https://lvc.github.io/abi-compliance-checker
Source0:        https://github.com/lvc/abi-compliance-checker/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
Requires:       abi-dumper >= 1.1
Requires:       binutils
Requires:       coreutils
Requires:       cpio
Requires:       ctags
Requires:       diffutils
Requires:       file
Requires:       gcc-c++
Requires:       gzip
Requires:       perl-base
Requires:       rpm
Requires:       tar
BuildArch:      noarch

%description
ABI Compliance Checker (ACC) is an easy-to-use tool for checking
backward binary compatibility (BC) of a shared C/C++ library.
It checks header files along with shared libraries of old and new
versions and analyzes changes in Application Binary Interface (ABI)
that may cause compatibility problems: changes in calling stack,
v-table changes, removed symbols, etc. Breakage of the binary
compatibility may result in crashing or incorrect behavior of
applications built with an old version of the library if they run on
a new one. The tool is intended for library developers and operating
system maintainers who are interested in ensuring binary
compatibility, i.e. allow old applications to run with newer library
versions without the need to recompile.

%prep
%setup -q

%build
chmod 0755 %{name}.pl

%install
mkdir -vp %{buildroot}%{_prefix}
perl Makefile.pl --install --prefix=%{_prefix} --destdir=%{buildroot}
# Generate man page with help2man
mkdir -p %{buildroot}%{_mandir}/man1
ln -s %{name}.pl %{name}
help2man -h "--info" -N -o %{name}.1 ./%{name}
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1
%fdupes %{buildroot}

%check
# aarch64 needs -fPIC option and noarch package cannot use %%ifarch
./%{name} \
  -gcc-options -fPIC \
  -test

%files
%doc README.md doc
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*

%changelog
