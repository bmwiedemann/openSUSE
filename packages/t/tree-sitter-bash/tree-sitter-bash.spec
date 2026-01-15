#
# spec file for package tree-sitter-bash
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

%define python_subpackage_only 1
%define         _name bash
Name:           tree-sitter-bash
Version:        0.25.1
Release:        0
Summary:        Bash grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-bash
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  tree-sitter

BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
BuildRequires:  tree-sitter-devel
Suggests:       python-tree-sitter >= 0.24
%treesitter_grammars %{_name}
%python_subpackages

%description
%{summary}.

%package -n python-tree-sitter-bash
Summary:        Python bindings for tree-sitter-bash
Requires:       %{name} = %{version}

%description -n python-tree-sitter-bash
Python bindings for tree-sitter-bash.

%prep
%autosetup

%build
%treesitter_configure
%treesitter_build

export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%treesitter_install
%treesitter_devel_install

#neovim stuff
install -d %{buildroot}%{_libdir}/tree_sitter
ln -s %{_libdir}/lib%{name}.so %{buildroot}%{_libdir}/tree_sitter/%{_name}.so

%pyproject_install
%{python_expand rm %{buildroot}%{$python_sitearch}/tree_sitter_bash/binding.c
%fdupes %{buildroot}%{$python_sitearch}
}

%files
%license LICENSE
%treesitter_files
%{_libdir}/tree_sitter/%{_name}.so
%if 0%{?suse_version} < 1600
%dir %{_libdir}/tree_sitter
%endif

%treesitter_devel_package

%files %{python_files tree-sitter-bash}
%license LICENSE
%{python_sitearch}/tree_sitter_bash
%{python_sitearch}/tree_sitter_bash-%{version}.dist-info

%changelog
