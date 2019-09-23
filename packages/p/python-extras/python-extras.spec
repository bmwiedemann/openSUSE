#
# spec file for package python-extras
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# A build cycle exists between python-extras and python-testtools. Thus, only
# enable testing with a build conditional (off by default):
%bcond_with tests
Name:           python-extras
Version:        1.0.0
Release:        0
Summary:        Extra bits for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/testing-cabal/extras
Source:         https://files.pythonhosted.org/packages/source/e/extras/extras-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Break cycle
#!BuildIgnore:  python-extras
BuildArch:      noarch
# Test requirements:
%if %{with tests}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module testtools}
%endif
%python_subpackages

%description
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.

%prep
%setup -q -n extras-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
%python_exec %{_bindir}/nosetests
%endif

%files %{python_files}
%license LICENSE
%doc NEWS README.rst
%{python_sitelib}/extras
%{python_sitelib}/extras-%{version}-py%{python_version}.egg-info/

%changelog
