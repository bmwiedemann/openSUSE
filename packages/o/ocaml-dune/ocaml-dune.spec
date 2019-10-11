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
Version:        1.11.4
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
Requires:       ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros >= 20191004
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A composable build system for OCaml

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%make_build

%install
#make_install PREFIX='%{_prefix}' LIBDIR="$(ocamlc -where)"
./_boot/default/bin/main/main_dune.exe install \
	--prefix '%{_prefix}' \
	--destdir '%{buildroot}' \
	--libdir "$(ocamlc -where)" \
	dune --build-dir _boot
find '%{buildroot}' -ls
rm -rfv %{buildroot}%{_prefix}/doc
mkdir -vp %{buildroot}%{_mandir}
mv %{buildroot}%{_prefix}/man %{buildroot}%{_datadir}
%ocaml_create_file_list

%files -f %{name}.files
%doc CHANGES.md README.md
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/emacs

%files devel -f %{name}.files.devel

%changelog
