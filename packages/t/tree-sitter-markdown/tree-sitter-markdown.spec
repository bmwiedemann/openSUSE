#
# spec file for package tree-sitter-markdown
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


%define         _name markdown
Name:           tree-sitter-%{_name}
Version:        0.3.2
Release:        0
Summary:        Markdown grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter-grammars/tree-sitter-markdown
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  tree-sitter

%description
The parser is designed to read markdown according to the CommonMark Spec, but
some extensions to the spec from different sources such as Github flavored
markdown are also included. These can be toggled on or off at compile time.

%package devel
Summary:        Devel files for %{name}

%description devel
Development files for %{name}.

%prep
%autosetup -p1
pushd %{name}
tree-sitter generate --no-bindings src/grammar.json
popd
pushd %{name}-inline
tree-sitter generate --no-bindings src/grammar.json
popd

%build
%make_build PREFIX=%{_prefix} INCLUDEDIR=%{_includedir} LIBDIR=%{_libdir} PCLIBDIR=%{_libdir}/pkgconfig

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir} PCLIBDIR=%{_libdir}/pkgconfig
#remove unncessary stuff
rm %{buildroot}%{_libdir}/libtree-sitter-{markdown-inline.a,markdown.a}

#neovim stuff
install -d %{buildroot}%{_libdir}/tree_sitter
ln -s %{_libdir}/lib%{name}.so.0.14 %{buildroot}%{_libdir}/tree_sitter/%{_name}.so
ln -s %{_libdir}/lib%{name}-inline.so.0.14 %{buildroot}%{_libdir}/tree_sitter/%{_name}-inline.so

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}-inline.so.*
%{_libdir}/tree_sitter/%{_name}.so
%{_libdir}/tree_sitter/%{_name}-inline.so
%if 0%{?suse_version} < 1600
%dir %{_libdir}/tree_sitter
%endif

%files devel
%{_includedir}/tree_sitter
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-inline.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-inline.pc

%changelog
