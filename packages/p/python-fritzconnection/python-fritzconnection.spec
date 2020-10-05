#
# spec file for package python-fritzconnection
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
%define skip_python2 1
Name:           python-fritzconnection
Version:        1.3.4
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
for i in fritzcall fritzconnection fritzhomeauto fritzhosts fritzphonebook fritzstatus fritzwlan ; do
   %python_clone -a %{buildroot}%{_bindir}/${i}
done

%post
%{python_install_alternative fritzcall fritzconnection fritzhomeauto fritzhosts fritzphonebook fritzstatus fritzwlan}

%preun
%{python_uninstall_alternative fritzcall fritzconnection fritzhomeauto fritzhosts fritzphonebook fritzstatus fritzwlan}

%check
# Don't run functional tests that require connections to a physical fritzbox router
rm fritzconnection/tests/test_functional.py
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/fritzcall
%python_alternative %{_bindir}/fritzconnection
%python_alternative %{_bindir}/fritzhomeauto
%python_alternative %{_bindir}/fritzhosts
%python_alternative %{_bindir}/fritzphonebook
%python_alternative %{_bindir}/fritzstatus
%python_alternative %{_bindir}/fritzwlan
%{python_sitelib}/*

%changelog
