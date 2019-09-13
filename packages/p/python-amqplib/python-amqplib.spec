#
# spec file for package python-amqplib
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
%bcond_with     test
Name:           python-amqplib
Version:        1.0.2
Release:        0
Summary:        AMQP Client Library (Advanced Message Queuing Protocol)
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/barryp/py-amqplib
Source:         https://files.pythonhosted.org/packages/source/a/amqplib/amqplib-%{version}.tgz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
BuildArch:      noarch
%python_subpackages

%description
A python client library for AMQP (Advanced Message Queuing Protocol).

%prep
%setup -q -n amqplib-%{version}

%build
%python_build

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{$python_sitelib}
}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc CHANGES README TODO
%doc docs/*.txt
%{python_sitelib}/amqplib
%{python_sitelib}/amqplib-%{version}-py*.egg-info

%changelog
