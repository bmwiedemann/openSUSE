#
# spec file for package python-Glances
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
%define         skip_python2 1
Name:           python-Glances
Version:        3.1.4.1
Release:        0
Summary:        A cross-platform curses-based monitoring tool
License:        LGPL-3.0-only
URL:            https://github.com/nicolargo/glances
Source:         https://github.com/nicolargo/glances/archive/v%{version}.tar.gz
Patch0:         adjust-data-files.patch
Patch1:         remove-shebang.patch
Patch2:         skip-online-tests.patch
Patch3:         fix-tests.patch
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module psutil >= 5.6.3}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bottle
Requires:       python-future
Requires:       python-psutil >= 5.6.3
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-curses
Provides:       python-glances = %{version}
Obsoletes:      python-glances < %{version}
Provides:       glances
BuildArch:      noarch
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

%install
%python_install
%python_clone -a %{buildroot}%{_mandir}/man1/glances.1
%python_clone -a %{buildroot}%{_bindir}/glances
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec unitest.py
%python_exec unitest-restful.py
%python_exec unitest-xmlrpc.py

%post
%python_install_alternative glances glances.1

%postun
%python_uninstall_alternative glances

%files %{python_files}
%license COPYING
%doc NEWS.rst README.rst
%python_alternative %{_bindir}/glances
%python_alternative %{_mandir}/man1/glances.1%{?ext_man}
%{python_sitelib}/*

%changelog
