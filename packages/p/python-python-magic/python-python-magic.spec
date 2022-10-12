#
# spec file for package python-python-magic
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         oldpython python
Name:           python-python-magic
Version:        0.4.27
Release:        0
Summary:        File type identification using libmagic
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ahupp/python-magic
Source:         https://github.com/ahupp/python-magic/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  file
BuildRequires:  python-rpm-macros
Requires:       file
Provides:       python-magic
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-magic
%endif
%python_subpackages

%description
This module uses ctypes to access the libmagic file type
identification library. It makes use of the local magic database and
supports both textual and MIME-type output.

%prep
%setup -q -n python-magic-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/magic
%{python_sitelib}/python_magic-%{version}*-info

%changelog
