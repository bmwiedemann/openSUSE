#
# spec file for package python-stomper
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
Name:           python-stomper
Version:        0.4.3
Release:        0
Summary:        Transport neutral client implementation of the STOMP protocol
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://code.google.com/p/stomper
Source0:        https://files.pythonhosted.org/packages/source/s/stomper/stomper-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
# /SECTION
%python_subpackages

%description
This is a python client implementation of the STOMP protocol.

The client is attempting to be transport layer neutral. This module provides
functions to create and parse STOMP messages in a programatic fashion. The
messages can be easily generated and parsed, however its up to the user to do
the sending and receiving.

%prep
%setup -q -n stomper-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest lib/stomper/tests/*

%files %{python_files}
%doc README.rst lib/stomper/examples
%license LICENSE
%{python_sitelib}/*

%changelog
