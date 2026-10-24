#
# spec file for package python-pskc
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
Name:           python-pskc
Version:        1.4
Release:        0
Summary:        Python module for handling PSKC files
License:        LGPL-2.1-or-later
URL:            https://github.com/arthurdejong/python-pskc
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         python-pskc-utc.patch
# UPSTREAM PATCH Commit 6bcd027
Patch1:         test-certificate.patch
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module signxml}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-defusedxml
Requires:       python-lxml
Requires:       python-python-dateutil
Requires:       python-signxml
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
A Python module to handle Portable Symmetric Key Container (PSKC) files
as defined in RFC 6030. PSKC files are used to transport and provision
symmetric keys and key metadata (seed files) to different types of crypto
modules, commonly one-time password systems or other authentication devices.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/csv2pskc
%python_clone -a %{buildroot}%{_bindir}/pskc2csv
%python_clone -a %{buildroot}%{_bindir}/pskc2pskc
%python_group_libalternatives csv2pskc pskc2csv pskc2pskc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%{python_libalternatives_reset_alternative csv2pskc pskc2csv pskc2pskc}

%post
%{python_install_alternative csv2pskc pskc2csv pskc2pskc}

%postun
%{python_uninstall_alternative csv2pskc pskc2csv pskc2pskc}

%files %{python_files}
%doc ChangeLog README
%license COPYING
%python_alternative %{_bindir}/csv2pskc
%python_alternative %{_bindir}/pskc2csv
%python_alternative %{_bindir}/pskc2pskc
%{python_sitelib}/pskc
%{python_sitelib}/python_pskc-%{version}.dist-info

%changelog
