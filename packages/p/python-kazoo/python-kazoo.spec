#
# spec file for package python-kazoo
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
Name:           python-kazoo
Version:        2.11.0
Release:        0
Summary:        Higher Level Zookeeper Client
License:        Apache-2.0
URL:            https://github.com/python-zk/kazoo
Source:         https://files.pythonhosted.org/packages/source/k/kazoo/kazoo-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 46.4.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-eventlet >= 0.17.1
Suggests:       python-gevent >= 1.2
Suggests:       python-pure-sasl >= 0.5.1
BuildArch:      noarch
%python_subpackages

%description
Implements a higher level API to Apache Zookeeper for Python clients.

%prep
%setup -q -n kazoo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# kazoo needs running zookeeper server

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/kazoo
%{python_sitelib}/kazoo-%{version}.dist-info

%changelog
