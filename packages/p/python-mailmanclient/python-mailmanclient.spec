#
# spec file for package python-mailmanclient
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
# mailman is built only for primary python3 flavor
%define pythons python3
Name:           python-mailmanclient
Version:        3.3.2
Release:        0
Summary:        Python bindings for the Mailman REST API
License:        LGPL-3.0-only
URL:            https://www.list.org/
Source:         https://files.pythonhosted.org/packages/source/m/mailmanclient/mailmanclient-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module falcon}
BuildRequires:  %{python_module mailman}
BuildRequires:  %{python_module pytest-services}
BuildRequires:  %{python_module pytest-vcr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%if 0%{python3_version_nodots} == 38
# help in replacing any previously installed multiflavor package back to the primary python3 package
Provides:       python38-mailmanclient = %{version}-%{release}
Obsoletes:      python38-mailmanclient < %{version}-%{release}
%endif
%python_subpackages

%description
Python bindings for Mailman REST API.

%prep
%autosetup -n mailmanclient-%{version}

%build
export LC_ALL=C.UTF-8
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# doctest does not work:
# Traceback (most recent call last):
#   File "/usr/lib64/python3.7/logging/handlers.py", line 933, in emit
#     self.socket.send(msg)
# OSError: [Errno 9] Bad file descriptor
export LC_ALL=C.UTF-8
%pytest -k 'not using.rst'

%files %{python_files}
%doc README.rst
%license COPYING.LESSER
%{python_sitelib}/*

%changelog
