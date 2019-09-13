#
# spec file for package python-salt-testing
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-salt-testing
Version:        2016.9.7
Release:        0
Summary:        Testing tools needed in the several Salt Stack projects
License:        Apache-2.0
Group:          Development/Libraries/Python
Url:            http://saltstack.org/
Source0:        https://pypi.io/packages/source/S/SaltTesting/SaltTesting-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-mock
BuildRequires:  python-requests
BuildRequires:  python-setuptools
BuildRequires:  python-unittest2
Requires:       python-mock
Requires:       python-requests
Requires:       python-six
Requires:       python-unittest2
Recommends:     python-coverage
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Salt-Testing provides the required testing tools needed in the several Salt Stack projects.

%prep
%setup -q -n SaltTesting-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}%{_prefix}

%files
%defattr(-,root,root)
%doc LICENSE AUTHORS.rst
%{_bindir}/github-commit-status
%{_bindir}/salt-jenkins-build
%{python_sitelib}/*

%changelog
