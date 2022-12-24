#
# spec file for package python-multivolumefile
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-multivolumefile
Version:        0.2.3
Release:        0
Summary:        Multi volume file wrapper library
License:        LGPL-2.1-or-later
URL:            https://codeberg.org/miurahr/multivolume
Source:         https://files.pythonhosted.org/packages/source/m/multivolumefile/multivolumefile-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyannotate}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 42.0}
BuildRequires:  %{python_module setuptools_scm >= 3.5.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A python library to provide a file-object wrapping multiple files as virtually like as
a single file. It inherit io.RawIOBase class and support some of its standard methods.

%prep
%setup -q -n multivolumefile-%{version}
# remove shebang
sed -i '1{/env python/d}' multivolumefile/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc Changelog.rst README.rst
%license LICENSE
%{python_sitelib}/multivolumefile
%{python_sitelib}/multivolumefile-%{version}.dist-info

%changelog
