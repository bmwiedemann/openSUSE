#
# spec file for package python-zipstream
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without test
Name:           python-zipstream
Version:        1.1.4
Release:        0
Summary:        Zipfile generator
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://github.com/allanlei/python-zipstream
Source:         https://files.pythonhosted.org/packages/source/z/zipstream/zipstream-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module nose}
%endif
BuildArch:      noarch

%python_subpackages

%description
zipstream.py is a ZIP archive generator based on Python 3.3's zipfile.py.
zipstream can create archives on the fly, which is useful for streaming
the archive to e.g. web clients without needing to store the archive on
disk first.

%prep
%setup -q -n zipstream-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
