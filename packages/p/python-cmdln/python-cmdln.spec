#
# spec file for package python-cmdln
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
Name:           python-cmdln
Version:        2.0.0
Release:        0
Summary:        An improved cmd.py for Writing Multi-command Scripts and Shells
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/trentm/cmdln
Source:         https://files.pythonhosted.org/packages/source/c/cmdln/cmdln-%{version}.zip
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  tcl
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
`cmdln.py` is an extension of Python's default `cmd.py` module that
provides "a simple framework for writing line-oriented command
interpreters".	The idea (with both cmd.py and cmdln.py) is to be able
to quickly build multi-sub-command tools (think cvs or svn) and/or
simple interactive shells (think gdb or pdb).  Cmdln's extensions make
it more natural to write sub-commands, integrate optparse for simple
option processing, and make having good command documentation easier.

%prep
%setup -q -n cmdln-%{version}
# remove unwanted shebang
sed -i '/^#!/d' lib/cmdln.py
# remove executable bit in documentation
chmod -x examples/*

%build
%python_build

%install
%python_install

%check

%files %{python_files}
%doc LICENSE.txt docs/ examples/
%{python_sitelib}/cmdln*
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
