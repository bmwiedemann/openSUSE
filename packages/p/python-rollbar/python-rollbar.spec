#
# spec file for package python-rollbar
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
Name:           python-rollbar
Version:        0.14.7
Release:        0
Summary:        Python notifier for reporting exceptions, errors, and log messages to Rollbar
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/rollbar/pyrollbar
Source:         https://github.com/rollbar/pyrollbar/archive/v%{version}.tar.gz
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests >= 0.12.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module unittest2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
Requires:       python-requests >= 0.12.1
Requires:       python-setuptools
Requires:       python-six >= 1.9.0
BuildArch:      noarch
%python_subpackages

%description
Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.

%prep
%setup -q -n pyrollbar-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/rollbar
%{python_sitelib}/*

%changelog
