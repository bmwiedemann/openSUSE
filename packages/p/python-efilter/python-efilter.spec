#
# spec file for package python-efilter
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


%define base_name efilter
%define version 1.1.5
%define mangled_version 1!1.5
%define unmangled_version 1-1.5
%define release 1
Name:           python-%{base_name}
Version:        1.1.5
Release:        0
Summary:        EFILTER query language
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
License:        Apache-2.0
URL:            https://github.com/google/dotty/
Source0:        https://pypi.python.org/packages/9f/48/82fd1254d70b5d7831ece84270cb99c178c0254e2568efad72c5ca2a31c7/%{base_name}-%{unmangled_version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-setuptools
Requires:       python-python-dateutil
Requires:       python-six >= 1.4.0
Requires:       python-tz
BuildArch:      noarch

%description
EFILTER is a general-purpose destructuring and search language implemented in Python, and suitable for integration with any Python project that requires a search function for some of its data.

%package -n python-%{name}
Summary:        EFILTER query language

%description -n python-%{name}
EFILTER is a general-purpose destructuring and search language implemented in Python, and suitable for integration with any Python project that requires a search function for some of its data.

%prep
%setup -q -n %{base_name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=%{buildroot}
%fdupes %{buildroot}

%files
%license LICENSE.txt
%doc AUTHORS.txt README.md
%{python_sitelib}/efilter*
%exclude %{python_sitelib}/sample_projects

%changelog
