#
# spec file for package python-amqpstorm
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


Name:           python-amqpstorm
Version:        2.10.7
Release:        0
Summary:        Thread-safe Python RabbitMQ Client & Management library
License:        MIT
URL:            https://github.com/eandersson/amqpstorm
Source:         https://files.pythonhosted.org/packages/source/A/AMQPStorm/AMQPStorm-%{version}.tar.gz
Patch0:         mock.patch
Patch1:         pamqp3.patch
BuildRequires:  %{python_module pamqp >= 3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pamqp >= 3.0
Requires:       python-requests
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  python
%endif
%python_subpackages

%description
Thread-safe Python RabbitMQ Client & Management library.

Supports Python 2.7 and Python 3.3+.
Tested against CPython, PyPy and Pyston.
When using a SSL connection, TLSv1 or higher is required.

%prep
%autosetup -p1 -n AMQPStorm-%{version}

%build
export LANG="en_US.UTF8"
%pyproject_wheel

%install
export LANG="en_US.UTF8"
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/amqpstorm
# remove generic named examples from sitelib
%python_expand rm -rf %{buildroot}%{$python_sitelib}/examples

%check
# test_heartbeat_basic_raise_on_missed_heartbeats randomly fails
%pytest amqpstorm/tests/unit/* -k "not test_heartbeat_basic_raise_on_missed_heartbeats"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/amqpstorm
%{python_sitelib}/amqpstorm-%{version}*-info

%changelog
