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
Version:        0.2.3
Release:        0
Summary:        Markdown grammar for tree-sitter
License:        MIT
URL:            https://github.com/MDeiml/tree-sitter-markdown
Source:         %{name}-%{version}.tar.xz
BuildRequires:  tree-sitter

%description
The parser is designed to read markdown according to the CommonMark Spec, but
some extensions to the spec from different sources such as Github flavored
markdown are also included. These can be toggled on or off at compile time.

%package devel
Summary:       Devel files for %{name}

%description devel
Development files for %{name}.

%prep
%autosetup -p1
cd tree-sitter-markdown
tree-sitter generate --no-bindings src/grammar.json
cd ..
cd tree-sitter-markdown-inline
tree-sitter generate --no-bindings src/grammar.json
cd ..

%build
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
mv %{buildroot}%{_libdir}/libtree-sitter-markdown.so.0.2 %{buildroot}%{_libdir}/libtree-sitter-markdown.so
mv %{buildroot}%{_libdir}/libtree-sitter-markdown-inline.so.0.2 %{buildroot}%{_libdir}/libtree-sitter-markdown-inline.so
#remove unncessary stuff
rm %{buildroot}%{_libdir}/libtree-sitter-markdown{.so.0,-inline.so.0}
rm %{buildroot}%{_libdir}/libtree-sitter-{markdown-inline.a,markdown.a}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libtree-sitter-markdown.so
%{_libdir}/libtree-sitter-markdown-inline.so

%files devel
%{_includedir}/tree_sitter
%{_libdir}/pkgconfig/tree-sitter-markdown*

%changelog
