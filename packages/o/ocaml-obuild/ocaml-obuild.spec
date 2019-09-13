#
# spec file for package ocaml-obuild
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-obuild
Version:        0.1.10
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Package build system for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml

URL:            https://github.com/ocaml-obuild/obuild
Source0:        https://github.com/ocaml-obuild/obuild/archive/obuild-v%{version}/%{name}-%{version}.tar.gz

# Enable reproducible builds. Already applied upstream.
Patch0:         https://github.com/ocaml-obuild/obuild/commit/b40c69380f724933c462ede4b926e3c4f4182d09.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros

%description
A parallel, incremental and declarative build system for OCaml.
Obuild acts as a building black box: users only declare what they want to
build and with which sources; the build system will consistently build it.
The design is based on Haskell's Cabal and borrows most of the layout and
way of working, adapting parts where necessary to fully support OCaml.


%prep
%setup -q -n obuild-obuild-v%{version}
%patch0 -p1

%build
./bootstrap

%install
mkdir -p %{buildroot}/%{_bindir}
cp "dist/build/obuild/obuild" "dist/build/obuild-simple/obuild-simple" "%{buildroot}/%{_bindir}"
# generate manpages
mkdir -p %{buildroot}/%{_mandir}/man1
help2man \
    --output "%{buildroot}/%{_mandir}/man1/obuild.1" \
    --name "parallel, incremental and declarative build system for OCaml" \
    --help-option "" \
    --no-discard-stderr \
    --no-info \
    dist/build/obuild/obuild
help2man \
    --output "%{buildroot}/%{_mandir}/man1/obuild-simple.1" \
    --name "simple package build system for OCaml" \
    --version-string " " \
    --no-discard-stderr \
    --no-info \
    dist/build/obuild-simple/obuild-simple

%files
%defattr(-,root,root,-)
%doc README.md OBUILD_SPEC.md DESIGN.md
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
