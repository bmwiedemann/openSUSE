#
# spec file for package python-mailmanclient
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-mailmanclient
Version:        3.3.4
Release:        0
Summary:        Python bindings for the Mailman REST API
Group:          Productivity/Networking/Email/Mailinglists
License:        LGPL-3.0-only
URL:            https://www.list.org/
Source:         https://files.pythonhosted.org/packages/source/m/mailmanclient/mailmanclient-%{version}.tar.gz
%if 0%{?sle_version} && 0%{?sle_version} <= 150300
Patch0:         mailmanclient-skip-httpx-tests.patch
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  mailman3 >= 3.3.5
BuildRequires:  %{python_module falcon}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  %{python_module httpx}
%endif
%if 0%{?sle_version} <= 150400
BuildRequires:  %{python_module async_generator}
%endif
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-services}
BuildRequires:  %{python_module pytest-vcr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Python bindings for Mailman REST API.

%prep
%autosetup -n mailmanclient-%{version} -p1

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
%if %{pkg_vcmp python3-pytest-asyncio >= 0.19}
asynciomode="--asyncio-mode=auto"
%endif
%pytest -k 'not using.rst' $asynciomode

%files %{python_files}
%doc README.rst
%license COPYING.LESSER
%{python_sitelib}/mailmanclient
%{python_sitelib}/mailmanclient-%{version}*-info

%changelog
