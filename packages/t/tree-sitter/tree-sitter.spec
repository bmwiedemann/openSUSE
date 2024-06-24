#
# spec file for package tree-sitter
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


%define somajor 0
%define libdirname tree_sitter
Name:           tree-sitter
Version:        0.22.6
Release:        0
Summary:        An incremental parsing system for programming tools
License:        GPL-2.0-only AND MIT
URL:            https://tree-sitter.github.io/
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
Source11:       baselibs.conf
Source20:       tree-sitter-target.py
Source21:       macros.in
Source22:       macros.lua
Source23:       functions.lua
Source24:       compile-macros.sh
Source25:       treesitter_grammar.attr
Source26:       treesitter_grammar.req
BuildRequires:  cargo-packaging
BuildRequires:  rust > 1.40
Requires:       lib%{name}%{somajor} = %{version}
Requires:       nodejs
%{?suse_build_hwcaps_libs}

%description
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. Tree-sitter aims to be:

 * General enough to parse any programming language
 * Fast enough to parse on every keystroke in a text editor
 * Robust enough to provide useful results even in the presence
   of syntax errors
 * Dependency-free so that the runtime library (which is written
   in pure C) can be embedded in any application

%package     -n lib%{name}%{somajor}
Summary:        Asychronous I/O support library

%description -n lib%{name}%{somajor}
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. This is the package with the dynamically linked C library.

%package        devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{somajor} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -a1

#remove gitignore file from docs
rm %{_builddir}/%{name}-%{version}/docs/.gitignore

cp %{SOURCE21} .
cp %{SOURCE22} .
cp %{SOURCE23} .

# fix VERSION in Makefile
sed -i -e '/^VERSION/s/:= .*$/:= %{version}/' Makefile

%build
%{cargo_build}
export CFLAGS='%{optflags}'
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}'
%make_build

sh %{SOURCE24}

%install
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}' INCLUDEDIR='%{_includedir}'
%make_install
install -p -m 0755 -D %{_builddir}/%{name}-%{version}/target/release/tree-sitter \
    %{buildroot}%{_bindir}/tree-sitter

find %{buildroot} -type f \( -name "*.la" -o -name "*.a" \) -delete -print

install -Dm644 macros.treesitter %{buildroot}%{_rpmmacrodir}/macros.treesitter
install -Dm755 %{SOURCE20} %{buildroot}%{_rpmconfigdir}/$(basename %{SOURCE20})

install -Dm644 %{SOURCE25} %{buildroot}%{_fileattrsdir}/$(basename %{SOURCE25})
install -Dm755 %{SOURCE26} %{buildroot}%{_rpmconfigdir}/$(basename %{SOURCE26})

%post -n lib%{name}%{somajor} -p /sbin/ldconfig

%postun -n lib%{name}%{somajor} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/tree-sitter
%{_rpmconfigdir}/tree-sitter-target.py
%{_rpmmacrodir}/macros.treesitter
%{_rpmconfigdir}/treesitter_grammar.req
%{_fileattrsdir}/treesitter_grammar.attr

%files -n lib%{name}%{somajor}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc docs/
%dir %{_includedir}/%{libdirname}/
%{_includedir}/%{libdirname}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
