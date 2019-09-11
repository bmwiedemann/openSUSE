#
# spec file for package python-feedgenerator
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
Name:           python-feedgenerator
Version:        1.9
Release:        0
Summary:        Standalone version of django.utilsfeedgenerator, compatible with Py3k
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/getpelican/feedgenerator
Source:         https://files.pythonhosted.org/packages/source/f/feedgenerator/feedgenerator-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/getpelican/feedgenerator/master/LICENSE
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz
Requires:       python-six
BuildArch:      noarch

%description
Feedgenerator-py3k is a standalone version of Django's feedgenerator.
It is based on the current Django Version 1.5.dev20120824122350.

%python_subpackages

%prep
%setup -q -n feedgenerator-%{version}
# add the missing licence
cp %{SOURCE1} LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.utf8
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/feedgenerator-%{version}-py%{python_version}.egg-info
%{python_sitelib}/feedgenerator

%changelog
