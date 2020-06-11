#
# spec file for package python-amqp
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
Name:           python-amqp
Version:        2.6.0
Release:        0
Summary:        Low-level AMQP client for Python (fork of amqplib)
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            http://github.com/celery/py-amqp
Source:         https://files.pythonhosted.org/packages/source/a/amqp/amqp-%{version}.tar.gz
BuildRequires:  %{python_module case >= 1.3.1}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vine >= 1.1.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-vine >= 1.1.3
BuildArch:      noarch
%python_subpackages

%description
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.
This library should be API compatible with librabbitmq.

%prep
%setup -q -n amqp-%{version}
# requires internet connection:
rm t/integration/test_rmq.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
