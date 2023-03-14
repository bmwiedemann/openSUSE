#
# spec file for package virt-top
#
# Copyright (c) 2023 SUSE LLC
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


Name:           virt-top
Version:        1.1.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Utility like top(1) for displaying virtualization stats
License:        GPL-2.0+
Group:          System/Management
Url:            http://people.redhat.com/~rjones/virt-top/
Source0:        %name-%version.tar.xz
Patch0:         %name.patch
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(calendar)
BuildRequires:  ocamlfind(curses)
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(gettext)
BuildRequires:  ocamlfind(gettext-stub)
BuildRequires:  ocamlfind(libvirt)
BuildRequires:  ocamlfind(str)
BuildRequires:  pkgconfig(libxml-2.0)

%description
virt-top is a 'top(1)'-like utility for showing stats of virtualized
domains.  Many keys and command line options are the same as for
ordinary 'top'.

It uses libvirt so it is capable of showing stats across a variety of
different virtualization systems.

%prep
%autosetup -p1

%build
dune_release_pkgs='virt-top'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list
tee -a %name.files < %name.files.devel

%files -f %name.files
%_bindir/*
%_mandir/man1/*

%changelog
