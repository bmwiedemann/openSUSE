#
# spec file for package python-ncclient
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
%bcond_without test
Name:           python-ncclient
Version:        0.6.4
Release:        0
Summary:        Python library for NETCONF clients
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://ncclient.org
Source:         https://files.pythonhosted.org/packages/source/n/ncclient/ncclient-%{version}.tar.gz
Patch0:         sphinx-use-imgmath-extension.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml >= 3.3.0
Requires:       python-paramiko >= 1.15.0
%ifpython2
Requires:       python-selectors2 >= 2.0.1
%endif
Requires:       python-setuptools > 0.6
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module lxml >= 3.3.0}
BuildRequires:  %{python_module paramiko >= 1.15.0}
BuildRequires:  %{python_module setuptools > 0.6}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
ncclient is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol.

%package -n python-ncclient-doc
Summary:        Python NETCONF protocol library - Documentation
Group:          Documentation/HTML
BuildRequires:  %{python_module Sphinx-latex}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  texlive-dvipng
Provides:       %{python_module python-ncclient-doc = %{version}}

%description -n python-ncclient-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n ncclient-%{version}
%patch0

%build
%python_build
cd docs && make %{?_smp_mflags} html && rm build/html/.buildinfo

%install
%python_install
%fdupes %{buildroot}

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%files -n python-ncclient-doc
%doc README README.rst examples docs/build/html

%changelog
