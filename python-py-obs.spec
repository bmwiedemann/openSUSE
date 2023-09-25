#
# spec file for package python-py-obs
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


%global skip_python39 1
%global skip_python310 1
Name:           python-py-obs
Version:        0.0.1
Release:        0
Summary:        Asynchronous API wrapper for the Open Build Service
License:        GPL-2.0-or-later
URL:            https://openbuildservice.org/
Source:         https://files.pythonhosted.org/packages/source/p/py-obs/py_obs-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
``py-obs`` is a simple asynchronous python API wrapper for the `Open Build
Service <https://openbuildservice.org/>`_.

%prep
%autosetup -p1 -n py_obs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/py_obs
%{python_sitelib}/py_obs-%{version}.dist-info

%changelog
