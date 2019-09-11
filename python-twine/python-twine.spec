#
# spec file for package python-twine
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
Name:           python-twine
Version:        1.13.0
Release:        0
Summary:        Collection of utilities for interacting with PyPI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pypa/twine
Source:         https://files.pythonhosted.org/packages/source/t/twine/twine-%{version}.tar.gz
BuildRequires:  %{python_module pkginfo >= 1.4.2}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readme_renderer >= 24.0}
BuildRequires:  %{python_module requests >= 2.17.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.8.0}
BuildRequires:  %{python_module setuptools >= 0.7.0}
BuildRequires:  %{python_module tqdm >= 4.14}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pkginfo >= 1.4.2
Requires:       python-readme_renderer >= 24.0
Requires:       python-requests >= 2.17.0
Requires:       python-requests-toolbelt >= 0.8.0
Requires:       python-setuptools >= 0.7.0
Requires:       python-tqdm >= 4.14
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-keyring
%ifpython2
# tests/test_package.py will fail without pyblake2
BuildRequires:  python2-pyblake2
Recommends:     python-pyblake2
%endif
%python_subpackages

%description
Twine is a utility for publishing Python packages on PyPI.

Currently it supports registering projects, uploading distributions, and
checking, if descriptions will render correctly.

%prep
%setup -q -n twine-%{version}

sed -i '1s/^#!.*//' twine/__main__.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/twine
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_version}

%post
%python_install_alternative twine

%postun
%python_uninstall_alternative twine

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%dir %{python_sitelib}/twine
%dir %{python_sitelib}/twine-%{version}-py*.egg-info
%{python_sitelib}/twine/*
%{python_sitelib}/twine-%{version}-py*.egg-info/*
%python_alternative %{_bindir}/twine

%changelog
