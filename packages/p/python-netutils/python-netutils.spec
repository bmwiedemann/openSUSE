#
# spec file for package python-netutils
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
%{?sle15_python_module_pythons}
Name:           python-netutils
Version:        1.19.1
Release:        0
Summary:        Common helper functions useful in network automation
License:        Apache-2.0
URL:            https://netutils.readthedocs.io
Source:         https://github.com/networktocode/netutils/archive/refs/tags/v%{version}.tar.gz#/netutils-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Allow building for Python 3.15
Patch0:         support-python-315.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module legacycrypt if %python-base >= 3.13}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-napalm
%if 0%{?python_version_nodots} >= 313
Recommends:     python-legacycrypt
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
A Python library that is a collection of objects for common network automation tasks.

%prep
%autosetup -p1 -n netutils-%{version}
chmod -x netutils/lib_helpers.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/netutils
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_is_fqdn_resolvable, test_fqdn_to_ip, test_tcp_ping: needs internet connection
# test_sphinx_build: needs Sphinx, which is a huge dependency just for the one test
%pytest -k "not (test_is_fqdn_resolvable or test_fqdn_to_ip or test_tcp_ping or test_sphinx_build)"

%pre
%python_libalternatives_reset_alternative netutils

%post
%python_install_alternative netutils

%postun
%python_uninstall_alternative netutils

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/netutils
%{python_sitelib}/netutils
%{python_sitelib}/netutils-%{version}.dist-info

%changelog
