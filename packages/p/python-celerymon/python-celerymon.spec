#
# spec file for package python-celerymon
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
Name:           python-celerymon
Version:        1.0.3
Release:        0
Summary:        Real-time monitoring of Celery workers
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ask/celerymon/
Source:         https://files.pythonhosted.org/packages/source/c/celerymon/celerymon-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-celery
Requires:       python-tornado
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
celerymon - Real-time monitoring of Celery workers

%prep
%setup -q -n celerymon-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/celerymon

%post
%python_install_alternative celerymon

%postun
%python_uninstall_alternative celerymon

%files %{python_files}
%license LICENSE
%doc AUTHORS README
%python_alternative %{_bindir}/celerymon
%{python_sitelib}/*

%changelog
