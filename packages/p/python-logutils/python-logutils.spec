#
# spec file for package python-logutils
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-logutils
Version:        0.3.5
Release:        0
Summary:        Logging utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://logutils.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/l/logutils/logutils-%{version}.tar.gz
Patch0:         sphinx4.patch
# PATCH-FIX-UPSTREAM logutils-pr1-fix-testasserts-py3.12.patch https://bitbucket.org/vinay.sajip/logutils/pull-requests/1
Patch1:         https://bitbucket.org/hugovk/logutils/commits/0a3af211128567c437e68261a02591ffe2682d95/raw#/logutils-pr1-fix-testasserts-py3.12.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  redis
BuildArch:      noarch
%python_subpackages

%description
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and
so they are packaged here. Others are updated versions which have
appeared in recent Python releases, but are usable with older versions
of Python and so are packaged here.

%package -n python-logutils-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module logutils-doc = %{version}}

%description -n python-logutils-doc
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and
so they are packaged here. Others are updated versions which have
appeared in recent Python releases, but are usable with older versions
of Python and so are packaged here.

This package contains the documentation.

%prep
%setup -q -n logutils-%{version}
%autopatch -p1

%build
%pyproject_wheel
pushd doc
make html
rm _build/html/.buildinfo
popd

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH="$PATH:/sbin:/usr/sbin"
%pyunittest discover -v tests

%files %{python_files}
%license LICENSE.txt
%doc NEWS.txt README.rst
%{python_sitelib}/logutils
%{python_sitelib}/logutils-%{version}.dist-info

%files -n python-logutils-doc
%license LICENSE.txt
%doc doc/_build/html

%changelog
