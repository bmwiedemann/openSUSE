#
# spec file for package python-conu
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


%define skip_python2 1
Name:           python-conu
Version:        1.0.0
Release:        0
Summary:        Python container testing library
License:        MIT
URL:            https://github.com/user-cont/conu
Source:         https://files.pythonhosted.org/packages/source/c/conu/conu-%{version}.tar.gz
# https://github.com/user-cont/conu/issues/390
Patch0:         python-conu-no-six.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docker
Requires:       python-flexmock
Requires:       python-kubernetes >= 8
Requires:       python-pytest
Requires:       python-requests
Recommends:     docker
Recommends:     podman
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module flexmock}
BuildRequires:  %{python_module kubernetes >= 8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  acl
BuildRequires:  docker
BuildRequires:  podman
BuildRequires:  user(nobody)
# /SECTION
%python_subpackages

%description
Python container testing library.

%prep
%autosetup -p1 -n conu-%{version}
rm tests/integration/test_k8s.py tests/integration/test_openshift.py tests/release/test_release.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (integration or test_get_port_mappings or selinux or ownership)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/conu
%{python_sitelib}/conu-%{version}*-info

%changelog
