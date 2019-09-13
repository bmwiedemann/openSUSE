#
# spec file for package python-Kajiki
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Kajiki
Version:        0.8.0
Release:        0
Summary:        Compiler for Genshi syntax outputting Python bytecode
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/nandoflorestan/kajiki
Source:         https://files.pythonhosted.org/packages/source/K/Kajiki/Kajiki-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module nine}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-nine
BuildArch:      noarch
%python_subpackages

%description
Kajiki compiles Genshi-like syntax to Python bytecode.

(Genshi is a Python library parsing, generating, and processing HTML, XML or
other textual content for output generation on the web.)

%prep
%setup -q -n Kajiki-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/kajiki/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/*

%changelog
