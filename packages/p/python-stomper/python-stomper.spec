#
# spec file for package python-stomper
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


Name:           python-stomper
Version:        0.4.3
Release:        0
Summary:        Transport neutral client implementation of the STOMP protocol
License:        Apache-2.0
URL:            https://code.google.com/p/stomper
Source0:        https://files.pythonhosted.org/packages/source/s/stomper/stomper-%{version}.tar.gz
Patch0:         remove-future-requirement.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is a python client implementation of the STOMP protocol.

The client is attempting to be transport layer neutral. This module provides
functions to create and parse STOMP messages in a programatic fashion. The
messages can be easily generated and parsed, however its up to the user to do
the sending and receiving.

%prep
%autosetup -p1 -n stomper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest lib/stomper/tests/*

%files %{python_files}
%doc README.rst lib/stomper/examples
%license LICENSE
%{python_sitelib}/stomper
%{python_sitelib}/stomper-%{version}.dist-info

%changelog
