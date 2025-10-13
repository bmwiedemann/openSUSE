#
# spec file for package python-bokeh_sampledata
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{?sle15_python_modules_python}
# gh#bokeh/bokeh_sampledata#7
Name:           python-bokeh_sampledata
Version:        2025.0
Release:        0
Summary:        Sample datasets for Bokeh examples
License:        BSD-3-Clause
URL:            https://bokeh.org
# Use github source for unit tests
#Source:         https://files.pythonhosted.org/packages/source/b/bokeh_sampledata/bokeh_sampledata-%%{version}.tar.gz
Source:         https://github.com/bokeh/bokeh_sampledata/archive/refs/tags/%{version}.tar.gz#/bokeh_sampledata-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 69.5.1}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module icalendar}
BuildRequires:  %{python_module pandas >= 1.2}
# /SECTION
BuildRequires:  fdupes
Requires:       python-icalendar
Requires:       python-pandas >= 1.2
Provides:       python-bokeh-sampledata = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
This package contains sample datasets for use with Bokeh examples.

%prep
%autosetup -p1 -n bokeh_sampledata-%{version}
sed -i 's/dynamic = \["version"\]/version = "%{version}"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/bokeh_sampledata
%{python_sitelib}/bokeh_sampledata-%{version}.dist-info

%changelog
