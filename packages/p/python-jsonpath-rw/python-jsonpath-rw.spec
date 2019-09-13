#
# spec file for package python-jsonpath-rw
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-jsonpath-rw
Version:        1.4.0
Release:        0
Summary:        An extended implementation of JSONPath for Python
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/kennknowles/python-jsonpath-rw
Source:         https://pypi.python.org/packages/source/j/jsonpath-rw/jsonpath-rw-%{version}.tar.gz
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
Requires:       python-decorator
Requires:       python-ply >= 3.4
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

# detritus in /etc/alternatives from brp-python-bytecompile must be removed
%define __os_install_post %(echo '%{__os_install_post}; \
  rm -f %{buildroot}%{_sysconfdir}/alternatives/jsonpath.pyo; \
  rm -f %{buildroot}%{_sysconfdir}/alternatives/jsonpath.pyc')

%python_subpackages

%description
This library provides a robust and significantly extended implementation
of JSONPath for Python. It is tested with Python 2.6, 2.7, 3.2, 3.3, and PyPy.

This library differs from other JSONPath implementations in that it is a
full *language* implementation, meaning the JSONPath expressions are
first class objects, easy to analyze, transform, parse, print, and
extend. (You can also execute them :-)

%prep
%setup -q -n jsonpath-rw-%{version}
# remove unwanted shebang
sed -i '/^#!/ d' jsonpath_rw/bin/jsonpath.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jsonpath.py

%post
%python_install_alternative jsonpath.py

%postun
%python_uninstall_alternative jsonpath.py

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%python_alternative %{_bindir}/jsonpath.py
%{python_sitelib}/*

%changelog
