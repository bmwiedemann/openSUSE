#
# spec file for package python-async_timeout
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


%define         skip_python2 1
Name:           python-async_timeout
Version:        4.0.2
Release:        0
Summary:        Timeout context manager for asyncio programs
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/async_timeout/
Source:         https://files.pythonhosted.org/packages/source/a/async-timeout/async-timeout-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5.3}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-async-timeout = %{version}
Obsoletes:      python-async-timeout < %{version}
BuildArch:      noarch
%python_subpackages

%description
This provides an asyncio-compatible timeout context manager.

%prep
%setup -q -n async-timeout-%{version}
# do not bother with coverage
sed -i -e '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/async_timeout
%{python_sitelib}/async_timeout-%{version}*-info

%changelog
