#
# spec file for package python-inflate64
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


Name:           python-inflate64
Version:        0.3.1
Release:        0
Summary:        Deflate64 compression/decompression library
License:        LGPL-2.1-or-later
URL:            https://codeberg.org/miurahr/inflate64
Source:         https://files.pythonhosted.org/packages/source/i/inflate64/inflate64-0.3.1.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module importlib_metadata if %python-base < 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyannotate}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-importlib_metadata if python-base < 3.8)
%python_subpackages

%description
A python package to provide compression and decompression feature with Enhanced Deflate algorithm.

%prep
%setup -q -n inflate64-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitearch}/inflate64
%{python_sitearch}/inflate64-%{version}.dist-info

%changelog
