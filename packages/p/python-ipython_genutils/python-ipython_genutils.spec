#
# spec file for package python-ipython_genutils
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
Name:           python-ipython_genutils
Version:        0.2.0
Release:        0
Summary:        Vestigial utilities from IPython
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://ipython.org
Source:         https://files.pythonhosted.org/packages/source/i/ipython_genutils/ipython_genutils-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-nose
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
This contains some common utilities shared by Jupyter and IPython projects
during The Big Split. As soon as possible, those packages will remove their
dependency on this, and this package will go away.

No projects should depend on this package directly.  It will be pulled in by
whatever packages need it

%prep
%setup -q -n ipython_genutils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.utf8
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%defattr(-,root,root,-)
%doc CONTRIBUTING.md COPYING.md README.md
%{python_sitelib}/*

%changelog
