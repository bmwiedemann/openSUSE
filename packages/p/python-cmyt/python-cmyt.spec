#
# spec file for package python-cmyt
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


Name:           python-cmyt
Version:        2.0.0
Release:        0
Summary:        A collection of Matplotlib colormaps from the yt project
License:        BSD-3-Clause
URL:            https://github.com/yt-project/cmyt
Source:         https://files.pythonhosted.org/packages/source/c/cmyt/cmyt-%{version}.tar.gz
BuildRequires:  %{python_module colorspacious}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib
Requires:       python-numpy
BuildArch:      noarch
%python_subpackages

%description
Matplotlib colormaps from the yt project !

%prep
%autosetup -p1 -n cmyt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -rf "%{buildroot}%{$python_sitelib}/tests"
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# fails on 32bit platform with a float error
%pytest -k "not test_overview_to_fig"

%files %{python_files}
%{python_sitelib}/cmyt
%{python_sitelib}/cmyt-%{version}.dist-info

%changelog
