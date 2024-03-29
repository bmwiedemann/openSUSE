#
# spec file for package python-mailmanclient
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-mailmanclient
Version:        3.3.5
Release:        0
Summary:        Python bindings for the Mailman REST API
License:        LGPL-3.0-only
Group:          Productivity/Networking/Email/Mailinglists
URL:            https://www.list.org/
Source:         https://files.pythonhosted.org/packages/source/m/mailmanclient/mailmanclient-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
%if 0%{?sle_version} && 0%{?sle_version} <= 150300
Patch0:         mailmanclient-skip-httpx-tests.patch
%endif
# SECTION test requirements
BuildRequires:  %{python_module falcon}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-services}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  mailman3 >= 3.3.5
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  %{python_module httpx}
%endif
%if 0%{?sle_version} && 0%{?sle_version} <= 150400
BuildRequires:  %{python_module async_generator}
%endif
# /SECTION
%python_subpackages

%description
Python bindings for Mailman REST API.

%prep
%autosetup -n mailmanclient-%{version} -p1
# get rid of six
sed -i 's/six.moves.urllib_error/urllib.error/' src/mailmanclient/tests/test_domain.py src/mailmanclient/tests/test_unicode.py

%build
export LC_ALL=C.UTF-8
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# doctest does not work:
# Traceback (most recent call last):
#   File "/usr/lib64/python3.7/logging/handlers.py", line 933, in emit
#     self.socket.send(msg)
# OSError: [Errno 9] Bad file descriptor
export LC_ALL=C.UTF-8
%pytest -k 'not using.rst' --asyncio-mode=auto

%files %{python_files}
%doc README.rst
%license COPYING.LESSER
%{python_sitelib}/mailmanclient
%{python_sitelib}/mailmanclient-%{version}.dist-info

%changelog
