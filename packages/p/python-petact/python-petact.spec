#
# spec file for package python-petact
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


%bcond_without libalternatives
Name:           python-petact
Version:        0.1.2
Release:        0
Summary:        A python package extraction tool
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matthewscholefield/petact
Source:         https://files.pythonhosted.org/packages/source/p/petact/petact-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/MatthewScholefield/petact/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
Petact is a library used for installing and updating compressed tar files.
When install_package is called, it downloads an md5 file and compares it with
the md5 of the locally downloaded tar. If they are different, the old
extracted files are deleted and the new tar is downloaded and extracted to
the same place.

%prep
%setup -q -n petact-%{version}
cp %{SOURCE99} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/petact
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests

%pre
%python_libalternatives_reset_alternative petact

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/petact
%{python_sitelib}/petact
%{python_sitelib}/petact-%{version}*-info

%changelog
