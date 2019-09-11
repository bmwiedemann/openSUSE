#
# spec file for package python-python-fileinspector
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-fileinspector
Version:        1.0.2
Release:        0
License:        GPL-3.0-or-later
Summary:        A module to determine file mimetypes
Url:            https://github.com/dschreij/fileinspector
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/python-fileinspector/python-fileinspector-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/dschreij/fileinspector/master/copyright
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Recommends:     python-python-magic
BuildArch:      noarch

%python_subpackages

%description
This module is a layer on top of the standard Python mimetypes module and
python-magic. Python-magic only works with local files to which you need to
have access, while mimetypes only uses the filename to determine its
filetype.

%prep
%setup -q -n python-fileinspector-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install

{ echo '#!%{_bindir}/python3'; cat fileinspector.py; } >fileinspector.py.new
install -D fileinspector.py.new %{buildroot}/%{_bindir}/fileinspector

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license copyright
%python3_only %{_bindir}/fileinspector
%{python_sitelib}/*

%changelog
