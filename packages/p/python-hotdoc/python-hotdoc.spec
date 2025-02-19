#
# spec file for package python-hotdoc
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


%{?sle15_python_module_pythons}
Name:           python-hotdoc
Version:        0.17.4
Release:        0
Summary:        A documentation tool micro-framework
License:        LGPL-2.1-or-later
Group:          Development/Tools/Doc Generators
URL:            https://github.com/hotdoc/hotdoc
Source:         https://files.pythonhosted.org/packages/source/h/hotdoc/hotdoc-%{version}.tar.gz
Patch:          https://github.com/hotdoc/hotdoc/commit/adf8518431fafb78c9b47862a0a9a58824b6a421.patch#/fix-function-prototypes.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libyaml-devel
BuildRequires:  llvm-devel
BuildRequires:  python-rpm-macros
# The c extension needs libclang.so and llvm-config
Requires:       clang-devel
Requires:       llvm-devel
Requires:       python-PyYAML >= 5.4.1
Requires:       python-appdirs
Requires:       python-cchardet
Requires:       python-dbus-deviation >= 0.6.1
Requires:       python-feedgen
Requires:       python-lxml >= 4.9.1
Requires:       python-networkx >= 2.8.8
Requires:       python-pkgconfig >= 1.5.1
Requires:       python-schema
Requires:       python-toposort >= 1.6
Requires:       python-wheezy.template >= 0.1.195
Requires(post): update-alternatives
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
# The hotdoc cli files were provided as separate package between Aug and Nov 2020
Obsoletes:      hotdoc < %{version}-%{release}
Provides:       hotdoc = %{version}-%{release}
%endif
%python_subpackages

%description
Hotdoc is a documentation framework. It provides an interface for extensions
to plug upon, along with some base objects (formatters, ...)

Hotdoc is distributed with a set of extensions that perform various tasks,
such as parsing C and extracting symbols with clang, parsing
gobject-introspection (gir) files, highlighting the syntax of code snippets
with prism, etc.

%prep
%autosetup -p1 -n hotdoc-%{version}
sed -i -e "s/wheezy.template==/wheezy.template>=/" setup.py
sed -i -e "s/pkgconfig==/pkgconfig>=/" setup.py
sed -i -e "s/networkx==/networkx>=/" setup.py

sed -i -e '1s,#! %{_bindir}/env sh,#!%{_bindir}/sh,' ./hotdoc/extensions/gi/transition_scripts/translate_sections.sh

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hotdoc
%python_clone -a %{buildroot}%{_bindir}/hotdoc_dep_printer
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative hotdoc hotdoc_dep_printer

%postun
%python_uninstall_alternative hotdoc

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitearch}/hotdoc
%{python_sitearch}/hotdoc-%{version}*-info
%python_alternative %{_bindir}/hotdoc
%python_alternative %{_bindir}/hotdoc_dep_printer

%changelog
