#
# spec file for package python-matrix-client
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


Name:           python-matrix-client
Version:        0.4.0
Release:        0
Summary:        Client-Server SDK for Matrix
License:        Apache-2.0
URL:            https://github.com/matrix-org/matrix-python-sdk
Source:         https://files.pythonhosted.org/packages/source/m/matrix_client/matrix_client-%{version}.tar.gz
# PATCH-FIX-OPENSUSE update-setup.py-to-avoid-installing-of-test-pkg.patch
Patch0:         update-setup.py-to-avoid-installing-of-test-pkg.patch
# PATCH-FIX-OPENSUSE dont-require-pytest-runner.patch
Patch1:         dont-require-pytest-runner.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 < 2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       python-urllib3 < 2
BuildArch:      noarch
%python_subpackages

%description
Client-Server SDK for Matrix

%prep
%autosetup -p1 -n matrix_client-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/matrix_client*

%changelog
