#
# spec file for package python-zipstream
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


Name:           python-zipstream
Version:        1.1.4
Release:        0
Summary:        Zipfile generator
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/allanlei/python-zipstream
Source:         https://github.com/allanlei/python-zipstream/archive/v%{version}.tar.gz#/zipstream-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
BuildRequires:  %{python_module pytest}
%python_subpackages

%description
zipstream.py is a ZIP archive generator based on Python 3.3's zipfile.py.
zipstream can create archives on the fly, which is useful for streaming
the archive to e.g. web clients without needing to store the archive on
disk first.

%prep
%setup -q -n python-zipstream-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.markdown
%license LICENSE
%{python_sitelib}/zipstream
%{python_sitelib}/zipstream-%{version}.dist-info

%changelog
