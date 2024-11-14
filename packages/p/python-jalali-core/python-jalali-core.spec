#
# spec file for package python-jalali-core
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


Name:           python-jalali-core
Version:        1.0.0
Release:        0
Summary:        a Gregorian to Jalali and inverse date convertor
License:        LGPL-2.1-or-later
URL:            https://github.com/slashmili/jalali-core
Source:         https://files.pythonhosted.org/packages/source/j/jalali-core/jalali_core-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
a Gregorian to Jalali and inverse date convertor

%prep
%autosetup -p1 -n jalali_core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/jalali_core
%{python_sitelib}/jalali_core-%{version}.dist-info

%changelog
