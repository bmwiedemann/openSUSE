#
# spec file for package python-ssdeep
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ssdeep
Version:        3.3
Release:        0
License:        LGPL-3.0+
Summary:        Python wrapper for the ssdeep library
Url:            http://github.com/DinoTools/python-ssdeep
Group:          Development/Languages/Python
#Source:         https://files.pythonhosted.org/packages/source/s/ssdeep/ssdeep-%%{version}.tar.gz # no docs here, see https://github.com/DinoTools/python-ssdeep/issues/37
Source:         https://github.com/DinoTools/python-ssdeep/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module cffi >= 0.8.6}
# SECTION tests
BuildRequires:  %{python_module pytest-runner}
# /SECTION
# SECTION docs
BuildRequires:  python-sphinx
BuildRequires:  python-mock
# /SECTION
BuildRequires:  libfuzzy-devel
BuildRequires:  fdupes
Requires:       ssdeep

%python_subpackages

%description
A Python wrapper for ssdeep, which is a library for computing context triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs
have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both
content and length.

%prep
%setup -q -n python-ssdeep-%{version}

%build
%python_build
pushd docs
make html
rm build/html/.buildinfo
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%{python_sitearch}/*
%doc README.rst CHANGELOG.rst docs/build/html/
%license LICENSE

%changelog
