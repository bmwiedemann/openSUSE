#
# spec file for package python-py-espeak-ng
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
Name:           python-py-espeak-ng
Version:        0.1.8
Release:        0
Summary:        Python interface for eSpeak NG
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/gooofy/py-espeak-ng
Source0:        https://files.pythonhosted.org/packages/source/p/py-espeak-ng/py-espeak-ng-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  espeak-ng
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       espeak-ng
BuildArch:      noarch
%python_subpackages

%description
Python interface for eSpeak NG, a speech synthesis library.

%prep
%setup -q -n py-espeak-ng-%{version}
# fix shebang
sed -i '/^#!\/usr\/bin\/env python/d' espeakng/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Needs properly setup espeak sadly
#%%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
