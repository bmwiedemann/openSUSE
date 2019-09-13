#
# spec file for package python-WebError
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
#


%define modname WebError
Name:           python-WebError
Version:        0.13.1
Release:        0
Summary:        Web Error handling and exception catching
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/weberror
Source:         https://files.pythonhosted.org/packages/source/W/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-Paste
BuildRequires:  python-Pygments
BuildRequires:  python-Tempita
BuildRequires:  python-WebOb
BuildRequires:  python-WebTest
BuildRequires:  python-devel
BuildRequires:  python-nose
BuildRequires:  python-setuptools
BuildRequires:  python-simplejson
BuildRequires:  python-xml
BuildArch:      noarch
Requires:       python-Paste
Requires:       python-Pygments
Requires:       python-Tempita
Requires:       python-WebOb
Requires:       python-simplejson
Requires:       python-xml
Provides:       python-weberror = %{version}
Provides:       python2-WebError = %{version}
Obsoletes:      python-weberror < %{version}

%description
A web error handling and exception catching module for Paste applications.

%prep
%setup -q -n %{modname}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}%{python_sitelib}

%check
python setup.py test

%files
%license LICENSE
%doc CHANGELOG README.rst
%{python_sitelib}/*

%changelog
