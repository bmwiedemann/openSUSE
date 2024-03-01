#
# spec file for package thefuck
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


%define pythons python3
Name:           thefuck
Version:        3.32
Release:        0
Summary:        Correcting console command utility
License:        MIT
URL:            https://github.com/nvbn/thefuck/
Source:         https://github.com/nvbn/thefuck/archive/refs/tags/%{version}.tar.gz
Patch0:         drop-six.patch
BuildRequires:  fdupes
BuildRequires:  go
BuildRequires:  python-rpm-macros
BuildRequires:  python3-colorama
BuildRequires:  python3-dbm
BuildRequires:  python3-decorator
BuildRequires:  python3-pexpect
BuildRequires:  python3-pip
BuildRequires:  python3-psutil
BuildRequires:  python3-pyte
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-colorama
Requires:       python3-dbm
Requires:       python3-decorator
Requires:       python3-psutil
Requires:       python3-pyte
BuildArch:      noarch

%description
TheFuck is a tool that corrects errors in previous console commands.

%prep
%autosetup -p1

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
sed -i -e 's/^from mock import/from unittest.mock import/' $(find tests -name '*.py')
%pytest

%files
%{_bindir}/%{name}
%{_bindir}/fuck
%{python3_sitelib}/thefuck
%{python3_sitelib}/thefuck-%{version}*-info

%license LICENSE.md
%doc CONTRIBUTING.md README.md

%changelog
