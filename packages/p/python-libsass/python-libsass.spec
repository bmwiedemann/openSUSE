#
# spec file for package python-libsass
#
# Copyright (c) 2023 SUSE LLC
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


%define _name   libsass-python
Name:           python-libsass
Version:        0.22.0
Release:        0
Summary:        Python binding for libsass
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sass/libsass-python
Source:         https://github.com/sass/libsass-python/archive/%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libsass-devel >= 3.6.4
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A straightforward binding of libsass for Python. Compile Sass/SCSS in Python
with no Ruby stack at all!

%prep
%setup -q -n libsass-python-%{version}

%build
sed -i -e '/^#!\//, 1d' *.py
export SYSTEM_SASS=true
%python_build

%install
export SYSTEM_SASS=true
%python_install
%python_clone -a %{buildroot}%{_bindir}/pysassc
%{python_expand \
# We don't want to install tests
rm %{buildroot}%{$python_sitearch}/sasstests.py \
   %{buildroot}%{$python_sitearch}/__pycache__/sasstests.*.pyc
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pytest_arch sasstests.py

%post
%python_install_alternative pysassc

%postun
%python_uninstall_alternative pysassc

%files %{python_files}
%python_alternative %{_bindir}/pysassc
%{python_sitearch}/pysassc.py
%{python_sitearch}/sass.py
%{python_sitearch}/_sass*.so
%{python_sitearch}/sassutils
%pycache_only %{python_sitearch}/__pycache__/*sass*.pyc
%{python_sitearch}/libsass-%{version}*-info

%changelog
