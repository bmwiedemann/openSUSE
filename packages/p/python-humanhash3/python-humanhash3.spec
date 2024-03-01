#
# spec file for package python-humanhash3
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-humanhash3
Version:        0.0.6
Release:        0
Summary:        Human-readable representations of digests
License:        Unlicense
URL:            https://github.com/blag/humanhash
Source:         https://files.pythonhosted.org/packages/source/h/humanhash3/humanhash3-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/blag/humanhash/master/UNLICENSE
Patch0:         convert-to-ascii.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
humanhash provides human-readable representations of digests.

%prep
%autosetup -p1 -n humanhash3-%{version}
cp %{SOURCE99} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license UNLICENSE
%{python_sitelib}/humanhash.py
%pycache_only %{python_sitelib}/__pycache__/humanhash.*.py*
%{python_sitelib}/humanhash3-%{version}.dist-info

%changelog
