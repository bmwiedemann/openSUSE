#
# spec file for package python-croniter
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-croniter
Version:        0.3.32
Release:        0
Summary:        Python iterators for datetime objects with cron-like format
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/kiorky/croniter
Source:         https://files.pythonhosted.org/packages/source/c/croniter/croniter-%{version}.tar.gz
BuildRequires:  %{python_module natsort}
BuildRequires:  %{python_module pytest >= 3.0.3}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tzlocal}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-natsort
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
croniter provides iterators for datetime object with cron-like format.

%prep
%setup -q -n croniter-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src

%files %{python_files}
%license docs/LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
