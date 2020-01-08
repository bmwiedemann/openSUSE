#
# spec file for package python-thespian
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-thespian
Version:        3.9.11
Release:        0
Summary:        Python Actor concurrency library
License:        MIT
Group:          Development/Languages/Python
URL:            https://thespianpy.com
Source0:        https://files.pythonhosted.org/packages/source/t/thespian/thespian-%{version}.zip
BuildRequires:  %{python_module setproctitle}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-setproctitle
BuildArch:      noarch
%python_subpackages

%description
Thespian is a Python library providing a framework for developing
concurrent, distributed, fault tolerant applications.

Thespian is built on the Actor Model which allows applications to be
written as a group of independently executing but cooperating
"Actors" which communicate via messages.  These Actors run within
the Actor System provided by the Thespian library.

      * Concurrent
      * Distributed
      * Fault Tolerant
      * Scalable
      * Location independent

Actor programming is broadly applicable and it is ideally suited
for Cloud-based applications as well, where compute nodes are
added and removed from the environment dynamically.

   * More Information: http://thespianpy.com
   * Release Notes: http://thespianpy.com/doc/releases.html

%prep
%setup -q -n thespian-%{version}
sed -i -e '1{\@^#!%{_bindir}/.*python@d}' thespian/{director,shell}.py

%build
%python_build

%install
%python_install
%{python_expand mv %{buildroot}%{$python_sitelib}/{contrib,thespian}
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%license LICENSE.txt
%doc README.rst doc/*.org
%{python_sitelib}/thespian*

%changelog
