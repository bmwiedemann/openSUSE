#
# spec file for package python-zopfli
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


Name:           python-zopfli
Version:        0.2.2
Release:        0
Summary:        Zopfli module for python
License:        Apache-2.0
URL:            https://github.com/obp/py-zopfli
Source:         https://files.pythonhosted.org/packages/source/z/zopfli/zopfli-%{version}.zip
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libzopfli-devel >= 1.0.3
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%python_subpackages

%description
Zopfli module for python

%prep
%setup -q -n zopfli-%{version}

%build
export USE_SYSTEM_ZOPFLI=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitearch}/zopfli
%{python_sitearch}/zopfli-%{version}*-info

%changelog
