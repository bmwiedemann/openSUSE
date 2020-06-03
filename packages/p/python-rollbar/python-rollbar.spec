#
# spec file for package python-rollbar
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
%bcond_without python2
Name:           python-rollbar
Version:        0.15.0
Release:        0
Summary:        Python notifier for reporting exceptions, errors, and log messages to Rollbar
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rollbar/pyrollbar
Source:         https://github.com/rollbar/pyrollbar/archive/v%{version}.tar.gz
# https://github.com/rollbar/pyrollbar/pull/340
Patch0:         python-rollbar-no-unittest2.patch
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 0.12.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 0.12.1
Requires:       python-setuptools
Requires:       python-six >= 1.9.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-enum34
BuildRequires:  python2-mock
BuildRequires:  python2-unittest2
%endif
%python_subpackages

%description
Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.

%prep
%setup -q -n pyrollbar-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rollbar
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative rollbar

%postun
%python_uninstall_alternative rollbar

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/rollbar
%{python_sitelib}/*

%changelog
