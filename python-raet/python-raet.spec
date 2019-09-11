#
# spec file for package python-raet
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-raet
Version:        0.6.8
Release:        0
Summary:        Reliable Asynchronous Event Transport protocol
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/RaetProtocol/raet
Source0:        https://files.pythonhosted.org/packages/source/r/raet/raet-%{version}.tar.gz
Patch0:         fix_unittest.patch
BuildRequires:  %{python_module ioflo >= 1.2.4}
BuildRequires:  %{python_module libnacl >= 1.4.3}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module setuptools-git >= 1.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-enum34
Requires:       python-ioflo >= 1.2.4
Requires:       python-libnacl >= 1.4.3
Requires:       python-msgpack
Requires:       python-six >= 1.6.1
BuildArch:      noarch
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
Raet is a Python library for raet protocol which stands for
Reliable Asynchronous Event Transport protocol.

%prep
%setup -q -n raet-%{version}
%patch0 -p1
# remove systest testing as it contains invalid py3 syntax
rm -rf systest/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%{python_sitelib}/*
%python3_only %{_bindir}/raetflo

%changelog
