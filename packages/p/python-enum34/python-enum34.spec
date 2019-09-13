#
# spec file for package python-enum34
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


Name:           python-enum34
Version:        1.1.6
Release:        0
Url:            https://pypi.python.org/pypi/enum34
Summary:        Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/e/enum34/enum34-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif
Provides:       python2-enum34 = %{version}

%description
enum34 is the new Python stdlib enum module available in Python 3.4
backported for previous versions of Python from 2.4 to 3.3.

%prep
%setup -q -n enum34-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%if 0%{?suse_version}
%fdupes %{buildroot}
%endif

%files
%defattr(-,root,root,-)
%doc enum/LICENSE enum/README
%{python_sitelib}/enum/
%{python_sitelib}/enum34-%{version}-py*.egg-info

%changelog
