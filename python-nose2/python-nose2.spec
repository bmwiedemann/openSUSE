#
# spec file for package python-nose2
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
Name:           python-nose2
Version:        0.9.1
Release:        0
Summary:        Second generation of the "nose" Python testing framework
License:        BSD-2-Clause AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nose-devs/nose2
Source:         https://files.pythonhosted.org/packages/source/n/nose2/nose2-%{version}.tar.gz
Patch0:         remove_unittest2.patch
Patch1:         fix-mock-dep.patch
BuildRequires:  %{python_module cov-core >= 1.12}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-cov-core >= 1.12
BuildArch:      noarch
%python_subpackages

%description
nose2 is a new version of the nose unit testing framework,
supporting Python 2.6+ and 3.x, but not 2.4.
nose2 does not need a custom importer anymore and instead imports
modules with __import__. nose2 does not support all of the
test project layouts that nose did, and also does not
support package-level fixtures. Almost all configuration for nose2
is to be done through config files, not command-line options.

%prep
%setup -q -n nose2-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/nose2

%check
export LC_CTYPE=C.UTF8
%python_exec setup.py test

%post
%python_install_alternative nose2

%postun
%python_uninstall_alternative nose2

%files %{python_files}
%license license.txt
%doc AUTHORS README.rst
%python_alternative %{_bindir}/nose2
%{python_sitelib}/*

%changelog
