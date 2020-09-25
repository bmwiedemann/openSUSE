#
# spec file for package python-paho-mqtt
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
Name:           python-paho-mqtt
Version:        1.5.1
Release:        0
Summary:        MQTT version 3.11 client class
License:        EPL-1.0
Group:          Development/Languages/Python
URL:            http://eclipse.org/paho
Source:         https://files.pythonhosted.org/packages/source/p/paho-mqtt/paho-mqtt-%{version}.tar.gz
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This code provides a client class which enable applications to connect to an
MQTT broker to publish messages, and to subscribe to topics and receive
published messages. It also provides some helper functions to make publishing
one off messages to an MQTT server very straightforward.

The MQTT protocol is a machine-to-machine (M2M)/"Internet of Things"
connectivity protocol. Designed as an extremely lightweight publish/subscribe
messaging transport, it is useful for connections with remote locations where
a small code footprint is required and/or network bandwidth is at a premium.

Paho is an Eclipse Foundation project.

%prep
%setup -q -n paho-mqtt-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
