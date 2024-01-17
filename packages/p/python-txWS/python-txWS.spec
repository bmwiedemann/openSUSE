#
# spec file for package python-txWS
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-txWS
Version:        0.9.1
Release:        0
Summary:        Twisted WebSockets wrapper
License:        X11
Group:          Development/Languages/Python
URL:            https://github.com/MostAwesomeDude/txWS
Source0:        https://files.pythonhosted.org/packages/source/t/txWS/txWS-%{version}.tar.gz
# https://github.com/MostAwesomeDude/txWS/commit/9e3a2a464b1c908086c82b293c271e58196f83df
Source1:        https://raw.githubusercontent.com/MostAwesomeDude/txWS/master/tests.py
# https://github.com/MostAwesomeDude/txWS/issues/36
Patch0:         python-txWS-no-python2.patch
# https://github.com/MostAwesomeDude/txWS/commit/05aadd036a7d9a0959c0d915a139779706e960d7
Patch1:         python-txWS-tobytes.patch
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pyupgrade
Requires:       python-Twisted
BuildArch:      noarch
%python_subpackages

%description
txWS (Twisted WebSockets) is a library for
adding WebSockets server support to Twisted applications.

%prep
%autosetup -p1 -n txWS-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cp %{SOURCE1} .
# https://github.com/MostAwesomeDude/txWS/issues/36
pyupgrade tests.py || true
sed -i '/import six/d' tests.py
sed -i 's:\(challenge = \)\(.*\):\1b\2:' tests.py
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/tx{WS,ws}*
%{python_sitelib}/__pycache__

%changelog
