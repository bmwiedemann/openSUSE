#
# spec file for package python-surer
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


Name:           python-surer
Version:        0.0.3
Release:        0
Summary:        Idiomatic assertion toolkit with human-friendly failure messages
License:        GPL-3.0-or-later
URL:            https://github.com/getmoto/surer
Source:         https://files.pythonhosted.org/packages/source/s/surer/surer-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# surer is a fork of sure and uses the same namespace
Conflicts:      python-sure
%python_subpackages

%description
An idiomatic testing library for python with powerful and flexible assertions.
Inspired and modeled after RSpec Expectations and should.js.

%prep
%setup -q -n surer-%{version}
# gh#getmoto/surer#2
sed -i 's/license = Apache License 2.0/license = GPL-3.0-or-later/' setup.cfg
sed -i '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/sure
%{python_sitelib}/surer-%{version}.dist-info

%changelog
