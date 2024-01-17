#
# spec file for package python-ssdeep
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
Name:           python-ssdeep
Version:        3.4.1
Release:        0
Summary:        Python wrapper for the ssdeep library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/DinoTools/python-ssdeep
#Source:         https://files.pythonhosted.org/packages/source/s/ssdeep/ssdeep-%%{version}.tar.gz # no docs here, see https://github.com/DinoTools/python-ssdeep/issues/37
Source:         https://github.com/DinoTools/python-ssdeep/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/DinoTools/python-ssdeep/commit/6cf96d63e9512fa14b6557d0d8afaa5128e0e853
Patch0:         python-ssdeep-no-six.patch
BuildRequires:  %{python_module cffi >= 0.8.6}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libfuzzy-devel
BuildRequires:  python-rpm-macros
Requires:       python-cffi
Requires:       ssdeep
# SECTION tests
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Python wrapper for ssdeep, which is a library for computing context triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs
have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both
content and length.

%prep
%setup -q -n python-ssdeep-%{version}
%patch0 -p1
# https://github.com/DinoTools/python-ssdeep/issues/57
sed -i 's:"pytest-runner.*"::' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%{python_sitearch}/ssdeep
%{python_sitearch}/ssdeep-*egg-info
%doc README.rst CHANGELOG.rst
%license LICENSE

%changelog
