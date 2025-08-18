#
# spec file for package python-feedgenerator
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


Name:           python-feedgenerator
Version:        2.2.1
Release:        0
Summary:        Standalone version of django.utilsfeedgenerator, compatible with Py3k
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getpelican/feedgenerator
Source:         https://files.pythonhosted.org/packages/source/f/feedgenerator/feedgenerator-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
FeedGenerator is a standalone version of Django’s feedgenerator module.
It has evolved over time and includes numerous enhancements.

%prep
%setup -q -n feedgenerator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.utf8
# skip coverage by using an empty configuration file
%pytest -c /dev/null

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/feedgenerator-%{version}*-info
%{python_sitelib}/feedgenerator

%changelog
