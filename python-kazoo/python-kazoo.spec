#
# spec file for package python-kazoo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-kazoo
Version:        2.6.1
Release:        0
Summary:        Higher Level Zookeeper Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python-zk/kazoo
Source:         https://files.pythonhosted.org/packages/source/k/kazoo/kazoo-%{version}.tar.gz
BuildRequires:  %{python_module eventlet >= 0.17.1}
BuildRequires:  %{python_module gevent >= 1.2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-eventlet >= 0.17.1
Requires:       python-gevent >= 1.2
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Implements a higher level API to Apache Zookeeper for Python clients.

%prep
%setup -q -n kazoo-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# kazoo needs running zookeeper server
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_version} -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
