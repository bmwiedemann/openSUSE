#
# spec file for package python-cmyt
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.0.2
Release:        0
Summary:        A collection of Matplotlib colormaps from the yt project
License:        BSD-3-Clause
URL:            https://github.com/yt-project/cmyt
Source:         https://github.com/yt-project/cmyt/archive/refs/tags/v%{version}.tar.gz#/cmyt-%{version}-gh.tar.gz
BuildRequires:  %{python_module colorspacious >= 1.1.2}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module matplotlib >= 3.8.0}
BuildRequires:  %{python_module numpy >= 1.26.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.2.4}
BuildRequires:  %{python_module pytest-mpl >= 0.13}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.8.0
Requires:       python-numpy >= 1.26.0
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
%license LICENSE
%doc README.md
%{python_sitelib}/cmyt
%{python_sitelib}/cmyt-%{version}.dist-info

%changelog
