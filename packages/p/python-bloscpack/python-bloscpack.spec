#
# spec file for package python-bloscpack
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
%bcond_without python2
Name:           python-bloscpack
Version:        0.16.0
Release:        0
Summary:        Command line interface and serialization format for Blosc
License:        MIT
URL:            https://github.com/blosc/bloscpack
Source:         https://files.pythonhosted.org/packages/source/b/bloscpack/bloscpack-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blosc
Requires:       python-numpy
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     cryptography >= 1.3.4
Recommends:     python-pyOpenSSL >= 0.14
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module blosc}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module coveralls}
BuildRequires:  %{python_module cryptography >= 1.3.4}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pyOpenSSL >= 0.14}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module wheel}
%if %{with python2}
BuildRequires:  python-ipaddress
%endif
# /SECTION
%ifpython2
Requires:       python-ipaddress
%endif
%python_subpackages

%description
Command line interface and serialization format for Blosc, a
multi-threaded, blocking and shuffling compressor. It uses
python-blosc bindings to interface with Blosc. It also comes with native
support for serializing and deserializing Numpy arrays.

%prep
%setup -q -n bloscpack-%{version}
find bloscpack -name '*.py' -exec sed -i '1{\@^#!%{_bindir}/env python@d}' {} +

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/blpk
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -c 'import blosc'
# Tests take too long
# %%python_expand nosetests-%%{$python_bin_suffix} test

%post
%python_install_alternative blpk

%postun
%python_uninstall_alternative blpk

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/blpk
%{python_sitelib}/*

%changelog
