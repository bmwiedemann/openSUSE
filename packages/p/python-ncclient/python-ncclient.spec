#
# spec file for package python-ncclient
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{?sle15allpythons}
Name:           python-ncclient
Version:        0.7.0
Release:        0
Summary:        Python library for NETCONF clients
License:        Apache-2.0
URL:            https://ncclient.readthedocs.io/en/latest/
Source:         https://github.com/ncclient/ncclient/archive/v%{version}.tar.gz#/ncclient-%{version}.tar.gz
# PATCH-FIX-OPENSUSE allow_old_sphinx.patch mcepl@suse.com
# Allow build with old Sphinx (< 2.0) on Leap
Patch0:         allow_old_sphinx.patch
# PATCH-FIX-UPSTREAM intersphinx-mapping.patch gh#ncclient/ncclient#604 mcepl@suse.com
# use conditionally new form of intersphinx_mapping
Patch1:         intersphinx-mapping.patch
BuildRequires:  %{python_module lxml >= 3.3.0}
BuildRequires:  %{python_module paramiko >= 1.15.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml >= 3.3.0
Requires:       python-paramiko >= 1.15.0
BuildArch:      noarch
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
%if 0%{?suse_version} < 1550
%patch -p 1 -P 0
%endif
%patch -p 1 -P 1

find examples/ -name "*.py" -exec sed -i 's|#!/usr/bin/env python$|#!/usr/bin/python|g' {} \;
# drop shebang
find ncclient/operations/third_party/ -name "*.py" -exec sed -i '/^#!\//, 1d' {} \;

%build
%pyproject_wheel
cd docs && make %{?_smp_mflags} html && rm build/html/.buildinfo

%install
%pyproject_install
%fdupes %{buildroot}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/ncclient
%{python_sitelib}/ncclient-%{version}.dist-info

%files -n python-ncclient-doc
%doc README.md README.rst examples docs/build/html

%changelog
