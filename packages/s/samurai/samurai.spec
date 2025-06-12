#
# spec file for package samurai
#
# Copyright (c) 2025 SUSE LLC
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


%global git_ref  737f702fed670acb25e5e70b4b802690df7a4a8b

Name:           samurai
Version:        1.2+git41.g737f702
Release:        0
Summary:        C99 implementation of the ninja build tool
License:        Apache-2.0
URL:            https://github.com/michaelforney/samurai
Source0:        %{URL}/archive/%{git_ref}/%{name}-%{version}.tar.gz
BuildRequires:  c_compiler
BuildRequires:  make

%description
samurai is a ninja-compatible build tool written in C99.

samurai implements the ninja build language through version 1.9.0
except for MSVC dependency handling. It uses the same format for the
".ninja_log" and ".ninja_deps" files as ninja, currently version 5
and 4, respectively.

%prep
%autosetup -n %{name}-%{git_ref} -p1

%build
export CC=cc
%set_build_flags

make clean
%make_build

%install
%make_install PREFIX="%_prefix"

%files
%license LICENSE
%_bindir/*
%_mandir/man1/*.1*

%changelog
