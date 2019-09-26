#
# spec file for package python-Glances
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Glances
Version:        3.1.2
Release:        0
Summary:        A cross-platform curses-based monitoring tool
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/nicolargo/glances
Source:         https://github.com/nicolargo/glances/archive/v%{version}.tar.gz
Patch0:         adjust-data-files.patch
Patch1:         remove-shebang.patch
Patch2:         skip-online-tests.patch
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module netifaces}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module psutil >= 5.3.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-future
Requires:       python-bottle
Requires:       python-curses
Requires:       python-psutil >= 5.6.3
Requires:       python-requests
Provides:       python-glances = %{version}
Obsoletes:      python-glances < %{version}
BuildArch:      noarch
%ifpython2
Requires:       python-future
%endif
%ifpython3
Provides:       glances
%endif
%python_subpackages

%description
Glances is a cross-platform monitoring tool which presents a
large amount of monitoring information through a curses or Web
based interface. The information dynamically adapts depending on the
size of the user interface.

%prep
%setup -q -n glances-%{version}
%autopatch -p1

%build
%python_build

# tests are failing on upstream, they apparently don't mind
%check
export LANG=en_US.UTF-8
%python_exec unitest.py
%python_exec unitest-restful.py
%python_exec unitest-xmlrpc.py

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc NEWS.rst README.rst
%python3_only %{_bindir}/glances
%python3_only %{_mandir}/man1/glances.1.gz
%{python_sitelib}/*

%changelog
