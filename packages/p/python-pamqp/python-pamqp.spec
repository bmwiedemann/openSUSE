#
# spec file for package python-pamqp
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
Name:           python-pamqp
Version:        2.3.0
Release:        0
Summary:        A pure-python AMQP 0-9-1 frame encoder and decoder
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/gmr/pamqp
Source:         https://github.com/gmr/pamqp/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-unittest2
%endif
%python_subpackages

%description
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder.

pamqp is not a end-user client library for talking to RabbitMQ but
rather is used by client libraries for marshaling and unmarshaling
AMQP frames.

AMQP class/method command class mappings can be found in the
pamqp.specification module while actual frame encoding and
encoding should be run through the pamqp.frame module.

%prep
%setup -q -n pamqp-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/pamqp*

%check
# for python 2.7 has to 'always' be there, for python 3.7 'default' is enough
export PYTHONWARNINGS=always
%pytest tests/*

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
