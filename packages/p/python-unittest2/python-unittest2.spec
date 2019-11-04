#
# spec file for package python-unittest2
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-unittest2
Version:        1.1.0
Release:        0
Summary:        The new features in unittest for Python 2.7 backported to Python 2.3+
License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/unittest2
Source:         https://files.pythonhosted.org/packages/source/u/unittest2/unittest2-%{version}.tar.gz
# PATCH-FIX-OPENSUSE relax-argparse.patch
Patch1:         relax-argparse.patch
BuildRequires:  %{python_module linecache2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module traceback2}
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       python-traceback2
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
unittest2 is a backport of the new features added to the unittest testing
framework in Python 2.7. It is tested to run on Python 2.4 - 2.7.

%prep
%setup -q -n unittest2-%{version}
%patch1 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/unit2

%post
%python_install_alternative unit2

%preun
%python_uninstall_alternative unit2

%files %{python_files}
%doc README.txt
%python_alternative %{_bindir}/unit2
%{python_sitelib}/unittest2
%{python_sitelib}/unittest2-%{version}-py*.egg-info

%changelog
