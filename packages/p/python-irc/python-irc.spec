#
# spec file for package python-irc
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


%define modname irc
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-irc
Version:        17.1
Release:        0
Summary:        A set of Python modules for IRC support
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/jaraco/irc
Source:         https://files.pythonhosted.org/packages/source/i/irc/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module jaraco.collections}
BuildRequires:  %{python_module jaraco.functools >= 1.10}
BuildRequires:  %{python_module jaraco.itertools >= 1.8}
BuildRequires:  %{python_module jaraco.logging}
BuildRequires:  %{python_module jaraco.text}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module tempora >= 1.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-jaraco.collections
Requires:       python-jaraco.functools >= 1.20
Requires:       python-jaraco.itertools >= 1.8
Requires:       python-jaraco.logging
Requires:       python-jaraco.stream
Requires:       python-jaraco.text
Requires:       python-more-itertools
Requires:       python-pytz
Requires:       python-tempora >= 1.6
Provides:       python-irclib = %{version}
Obsoletes:      %{name}-doc
Obsoletes:      python-irclib < %{version}
BuildArch:      noarch
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module jaraco.stream}
%endif
%python_subpackages

%description
This library is intended to encapsulate the IRC protocol at a quite
low level. It provides an event-driven IRC client framework. It has
a fairly thorough support for the basic IRC protocol, CTCP and DCC
connections.

%prep
%setup -q -n %{modname}-%{version}
sed -i -e '1s!/env python!/python!' scripts/testbot.py
sed -i 's/--flake8//' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if 0%{?suse_version} > 1500
%check
export PYTHONDONTWRITEBYTECODE=1
%pytest
%endif

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%doc scripts/
%{python_sitelib}/irc*

%changelog
