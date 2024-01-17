#
# spec file for package python-humanhash3
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
Name:           python-humanhash3
Version:        0.0.6
Release:        0
Summary:        Human-readable representations of digests
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://github.com/blag/humanhash
Source:         https://files.pythonhosted.org/packages/source/h/humanhash3/humanhash3-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/blag/humanhash/master/UNLICENSE
Patch0:         convert-to-ascii.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
humanhash provides human-readable representations of digests.

%prep
%setup -q -n humanhash3-%{version}
%patch0 -p1
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license UNLICENSE
%{python_sitelib}/*

%changelog
