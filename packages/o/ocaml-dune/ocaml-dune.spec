#
# spec file for package ocaml-dune
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ocaml-dune
Version:        1.10.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        A composable build system for OCaml
License:        MIT
Group:          Development/Languages/OCaml
Url:            https://dune.build/
Conflicts:      ocaml-jbuilder
Conflicts:      ocaml-jbuilder-debuginfo
Conflicts:      ocaml-jbuilder-debugsource
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A composable build system for OCaml

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
cp -av _boot/default/bin/main/main_dune.exe %{buildroot}%{_bindir}/dune
ln -sfvbn dune %{buildroot}%{_bindir}/jbuilder
cp -av _boot/default/doc/*.1 %{buildroot}%{_mandir}/man1/
cp -av _boot/default/doc/*.5 %{buildroot}%{_mandir}/man5/

%files
%defattr(-,root,root)
%doc CHANGES.md README.md
%license LICENSE.md
%{_bindir}/*
%{_mandir}/*/*

%changelog
