#
# spec file for package python-fritzconnection
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%global pythons python3
Name:           python-fritzconnection
Version:        1.10.3
Release:        0
Summary:        A Python module to talk to a AVM fritzbox
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kbr/fritzconnection/
Source:         https://github.com/kbr/fritzconnection/archive/%{version}.tar.gz#/fritzconnection-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-requests
Requires:       python-setuptools
BuildArch:      noarch
Obsoletes:      python310-fritzconnection < 1.9.0
Obsoletes:      python39-fritzconnection < 1.9.0
%python_subpackages

%description
fritzconnection is a Python library to communicate with the AVM
Fritz!Box by the TR-064 protocol.
This allows to read status-informations from the box and to read
and change configuration settings and state.

%prep
%setup -q -n fritzconnection-%{version}

%build
export LC_ALL=C.utf-8
%python_build

%install
export LC_ALL=C.utf-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check

# Don't run functional tests that require connections to a physical fritzbox router
rm fritzconnection/tests/test_functional.py
# https://github.com/kbr/fritzconnection/issues/154
%pytest -k 'not (test_terminate_thread_on_failed_reconnection or test_restart_failed_monitor)'

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/fritzcall
%{_bindir}/fritzconnection
%{_bindir}/fritzhomeauto
%{_bindir}/fritzhosts
%{_bindir}/fritzmonitor
%{_bindir}/fritzphonebook
%{_bindir}/fritzstatus
%{_bindir}/fritzwlan
%{python_sitelib}/*

%changelog
