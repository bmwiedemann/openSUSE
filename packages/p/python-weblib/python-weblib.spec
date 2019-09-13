#
# spec file for package python-weblib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-weblib
Version:        0.1.30
Release:        0
Summary:        Tools to solve typical tasks in Web scraping
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lorien/weblib
# https://github.com/lorien/weblib/issues/15
Source:         https://github.com/lorien/weblib/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module user_agent}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-pytils
Requires:       python-six
Requires:       python-user_agent
BuildArch:      noarch
%python_subpackages

%description
Weblib provides tools to solve typical tasks in Web scraping.

%prep
%setup -q -n weblib-%{version}

%build
%python_build

%check
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/weblib

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
