#
# spec file for package python-fritzconnection
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-fritzconnection
Version:        1.15.1
Release:        0
Summary:        A Python module to talk to a AVM fritzbox
License:        MIT
URL:            https://github.com/kbr/fritzconnection/
Source:         https://github.com/kbr/fritzconnection/archive/%{version}.tar.gz#/fritzconnection-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-requests
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# hopefully temporary, we can make it cleaner as soon as version bumps
Conflicts:      python3-fritzconnection
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
%pyproject_wheel

%install
export LC_ALL=C.utf-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fritzcall
%python_clone -a %{buildroot}%{_bindir}/fritzconnection
%python_clone -a %{buildroot}%{_bindir}/fritzhomeauto
%python_clone -a %{buildroot}%{_bindir}/fritzhosts
%python_clone -a %{buildroot}%{_bindir}/fritzmonitor
%python_clone -a %{buildroot}%{_bindir}/fritzphonebook
%python_clone -a %{buildroot}%{_bindir}/fritzstatus
%python_clone -a %{buildroot}%{_bindir}/fritzwlan
%python_group_libalternatives fritzconnection fritzcall fritzhomeauto fritzhosts fritzmonitor fritzphonebook fritzstatus fritzwlan
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check

# Don't run functional tests that require connections to a physical fritzbox router
rm fritzconnection/tests/test_functional.py
# https://github.com/kbr/fritzconnection/issues/154
%pytest -k 'not (test_terminate_thread_on_failed_reconnection or test_restart_failed_monitor)'

%post
%python_install_alternative fritzconnection fritzcall fritzhomeauto fritzhosts fritzmonitor fritzphonebook fritzstatus fritzwlan

%postun
%python_uninstall_alternative fritzconnection

%pre
%python_libalternatives_reset_alternative fritzconnection

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/fritzcall
%python_alternative %{_bindir}/fritzconnection
%python_alternative %{_bindir}/fritzhomeauto
%python_alternative %{_bindir}/fritzhosts
%python_alternative %{_bindir}/fritzmonitor
%python_alternative %{_bindir}/fritzphonebook
%python_alternative %{_bindir}/fritzstatus
%python_alternative %{_bindir}/fritzwlan
%{python_sitelib}/fritzconnection
%{python_sitelib}/fritzconnection-%{version}.dist-info

%changelog
