#
# spec file for package python-uniseg
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-uniseg
Version:        0.7.2
Release:        0
Summary:        Python module for determining Unicode text segmentations
License:        MIT
URL:            https://bitbucket.org/emptypage/uniseg-py
Source:         https://files.pythonhosted.org/packages/source/u/uniseg/uniseg-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
A pure Python module to determine Unicode text segmentations.

%prep
%setup -q -n uniseg-%{version}
sed -i -e '/^#!\//, 1d' uniseg/*test.py uniseg/samples/*.py

%build
%python_build

%install
%python_install
%python_expand rm -Rv %{buildroot}%{$python_sitelib}/uniseg/samples
%python_expand rm -Rv %{buildroot}%{$python_sitelib}/uniseg/docs
%python_expand %fdupes %{buildroot}%{$python_sitelib}/uniseg/__pycache__

%check
%pyunittest -v uniseg/*test.py

%files %{python_files}
%license LICENSE
%doc README.rst
%doc uniseg/docs/uniseg.ja.html
%{python_sitelib}/uniseg-*
%{python_sitelib}/uniseg/*.py
%dir %{python_sitelib}/uniseg
%pycache_only %{python_sitelib}/uniseg/__pycache__

%changelog
