#
# spec file for package python-irc
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


%{?sle15_python_module_pythons}
Name:           python-irc
Version:        20.5.0
Release:        0
Summary:        A set of Python modules for IRC support
License:        LGPL-2.1-or-later
URL:            https://github.com/jaraco/irc
Source:         https://files.pythonhosted.org/packages/source/i/irc/irc-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.10}
BuildRequires:  %{python_module importlib-resources if %python-base < 3.12}
BuildRequires:  %{python_module jaraco.collections}
BuildRequires:  %{python_module jaraco.functools >= 1.20}
BuildRequires:  %{python_module jaraco.logging}
BuildRequires:  %{python_module jaraco.stream}
BuildRequires:  %{python_module jaraco.text >= 3.14}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module tempora >= 1.6}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib-metadata
%endif
%if 0%{?python_version_nodots} < 312
Requires:       python-importlib-resources
%endif
Requires:       python-jaraco.collections
Requires:       python-jaraco.functools >= 1.20
Requires:       python-jaraco.logging
Requires:       python-jaraco.stream
Requires:       python-jaraco.text >= 3.14
Requires:       python-more-itertools
Requires:       python-pytz
Requires:       python-tempora >= 1.6
Provides:       python-irclib = %{version}
Obsoletes:      %{name}-doc
Obsoletes:      python-irclib < %{version}
BuildArch:      noarch
%python_subpackages

%description
This library is intended to encapsulate the IRC protocol at a quite
low level. It provides an event-driven IRC client framework. It has
a fairly thorough support for the basic IRC protocol, CTCP and DCC
connections.

%prep
%setup -q -n irc-%{version}
sed -i -e '1s!/env python!/python!' scripts/testbot.py
rm pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
# test_privmsg_sends_msg https://github.com/jaraco/irc/issues/165
%pytest -k 'not test_privmsg_sends_msg'

%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst
%doc scripts/
%{python_sitelib}/irc
%{python_sitelib}/irc-%{version}.dist-info

%changelog
