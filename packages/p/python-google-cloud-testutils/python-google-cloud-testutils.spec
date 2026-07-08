#
# spec file for package python-google-cloud-testutils
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


%{?sle15_python_module_pythons}
Name:           python-google-cloud-testutils
Version:        1.9.1
Release:        0
Summary:        Common tools used to test Python client libraries for Google APIs
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-testutils
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-testutils/google_cloud_testutils-%{version}.tar.gz
BuildRequires:  %{python_module click >= 7.0.0}
BuildRequires:  %{python_module google-auth >= 2.1.0}
BuildRequires:  %{python_module packaging >= 22.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  update-alternatives
Requires:       python-click >= 7.0.0
Requires:       python-google-auth >= 2.1.0
Requires:       python-packaging >= 22.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is a collection of common tools used in system tests of Python client
libraries for Google APIs. It provides utilities for prefixing test resources,
managing test cleanup, and other common testing tasks.

%prep
%autosetup -n google_cloud_testutils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lower-bound-checker
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative lower-bound-checker

%postun
%python_uninstall_alternative lower-bound-checker

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/lower-bound-checker
%{python_sitelib}/test_utils
%{python_sitelib}/google_cloud_testutils-%{version}.dist-info

%changelog
