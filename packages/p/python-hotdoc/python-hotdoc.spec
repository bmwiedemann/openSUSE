#
# spec file for package python-hotdoc
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-hotdoc
Version:        0.12.2
Release:        0
Summary:        A documentation tool micro-framework
License:        LGPL-2.1-or-later
Group:          Development/Tools/Doc Generators
URL:            https://github.com/hotdoc/hotdoc
Source:         https://files.pythonhosted.org/packages/source/h/hotdoc/hotdoc-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module setuptools}
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
# The c extension needs llvm-config
Requires:       llvm-devel
Requires:       python-PyYAML >= 5.1
Requires:       python-appdirs
Requires:       python-cchardet
Requires:       python-dbus-deviation >= 0.4.0
Requires:       python-lxml
Requires:       python-networkx >= 1.11
Requires:       python-pkgconfig >= 1.1.0
Requires:       python-schema
Requires:       python-toposort >= 1.4
Requires:       python-wheezy.template >= 0.1.167
Requires:       python-xdg >= 4.0.0
%python_subpackages

%description
Hotdoc is a documentation framework. It provides an interface for extensions
to plug upon, along with some base objects (formatters, ...)

Hotdoc is distributed with a set of extensions that perform various tasks,
such as parsing C and extracting symbols with clang, parsing
gobject-introspection (gir) files, highlighting the syntax of code snippets
with prism, etc.

%package -n hotdoc
Summary:        A documentation tool micro-framework
Group:          Development/Tools/Doc Generators
Requires:       python3-hotdoc

%description -n hotdoc
Hotdoc is a documentation framework. It provides an interface for extensions
to plug upon, along with some base objects (formatters, ...)

Hotdoc is distributed with a set of extensions that perform various tasks,
such as parsing C and extracting symbols with clang, parsing
gobject-introspection (gir) files, highlighting the syntax of code snippets
with prism, etc.

%prep
%setup -q -n hotdoc-%{version}
sed -i -e "s/wheezy.template==/wheezy.template>=/" setup.py
sed -i -e "s/pkgconfig==/pkgconfig>=/" setup.py
sed -i -e "s/networkx==/networkx>=/" setup.py

sed -i -e '1s,#! /usr/bin/env sh,#!/usr/bin/sh,' ./hotdoc/extensions/gi/transition_scripts/translate_sections.sh


%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}


%files %{python_files}
%license COPYING
%{python_sitearch}/hotdoc*

%files -n hotdoc
%license COPYING
%doc README.md
%python3_only %{_bindir}/hotdoc
%python3_only %{_bindir}/hotdoc_dep_printer

%changelog
