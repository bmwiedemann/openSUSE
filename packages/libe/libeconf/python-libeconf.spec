#
# spec file for package python-libeconf
#
# Copyright (c) 2024 SUSE LLC
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
%define skip_python39 1
Name:           python-libeconf
Version:        0.7.2
Release:        0
Summary:        Python bindings for libeconf
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/openSUSE/libeconf
Source:         libeconf-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       libeconf0 = %{version}
Suggests:       python-libeconf-doc = %{version}
%python_subpackages

%description
Python bindings for libeconf

%package -n python-libeconf-doc
Summary:        Man page for python-libeconf

%description -n python-libeconf-doc
Man page for python-lineconf

%prep
%autosetup -n libeconf-%{version}/bindings/python3

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}/usr/share/man/man3
cp docs/python-libeconf.3 %{buildroot}%{_mandir}/man3/

%files %python_files
%{python_sitelib}
# The cache is not always present
#pycache_only %{python_sitelib}/__pycache__

%files -n python-libeconf-doc
%defattr(-,root,root)
%{_mandir}/man3/*python-libeconf*

%changelog
