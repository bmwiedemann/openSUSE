#
# spec file for package python-future
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
Name:           python-future
Version:        0.18.0
Release:        0
Summary:        Single-source support for Python 3 and 2
License:        MIT AND Python-2.0
# See https://github.com/PythonCharmers/python-future/issues/242 for PSF licensing
Url:            https://python-future.org
Source0:        https://files.pythonhosted.org/packages/source/f/future/future-%{version}.tar.gz
Source100:      python-future-rpmlintrc
# PATCH-FIX-UPSTREAM python38-pow.patch gh#PythonCharmers/python-future#474 mcepl@suse.com
Patch0:         python38-pow.patch
# UPSTREAM ISSUE https://github.com/PythonCharmers/python-future/issues/508
Patch1:         future-correct-mimetype.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dbm
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Future is a compatibility layer between Python 2 and Python 3.
It allows you to use a single Python 3.x-compatible codebase to
support both Python 2 and Python 3.

%prep
%setup -q -n future-%{version}
%autopatch -p1
sed -i -e '/^#!\//, 1d' src/future/backports/test/pystone.py

%build
%python_build

%install
%python_install

%python_clone -a %{buildroot}%{_bindir}/futurize
%python_clone -a %{buildroot}%{_bindir}/pasteurize

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%{python_install_alternative futurize pasteurize}

%preun
%python_uninstall_alternative futurize

%check
# test_moves_urllib_request_http or test_urllib_request_http require internet
# test_geturl or test_main fail only on Leap 42.3 and SLE 12 SP4
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m pytest \
  -k 'not (test_moves_urllib_request_http or test_urllib_request_http or test_geturl or test_main)'
}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/futurize
%python_alternative %{_bindir}/pasteurize
%{python_sitelib}/*

%changelog
