#
# spec file for package python-TagStats
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


Name:           python-TagStats
Version:        0.1.2
Release:        0
Summary:        Statistics for each tag's set of key phrases
License:        MIT
URL:            https://github.com/chuanconggao/TagStats
Source:         https://files.pythonhosted.org/packages/source/T/TagStats/TagStats-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/chuanconggao/TagStats/%{version}/LICENSE
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A module to compute the statistics of each tag's set of key phrases
over input lines in Python 3.

%prep
%setup -q -n TagStats-%{version}
cp %{SOURCE10} .
sed -i -e '/^#! \//, 1d' tagstats/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/[Tt]ag[Ss]tats
%{python_sitelib}/[Tt]ag[Ss]tats-%{version}*-info

%changelog
