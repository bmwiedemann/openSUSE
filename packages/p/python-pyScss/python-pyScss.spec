#
# spec file for package python-pyScss
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014 LISA GmbH, Bingen, Germany.
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
Name:           python-pyScss
Version:        1.4.0
Release:        0
Summary:        pyScss, a Scss compiler for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Kronuz/pyScss
Source:         https://github.com/Kronuz/pyScss/archive/refs/tags/v%{version}.tar.gz#/pyScss-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-311.patch gh#Kronuz/pyScss#426
Patch0:         python-311.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  pcre-devel
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
pyScss is a compiler for SCSS flavor of the Sass language, a superset of CSS3
that adds programming capabilities and some other syntactic sugar.

95% of Sass 3.2 is supported.  If it's not supported, it's a bug!  Please file
a ticket.

Most of Compass 0.11 is also built in.

Documentation:
http://pyscss.readthedocs.org/en/latest/

The canonical syntax reference is part of the Ruby Sass documentation:
http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html

%prep
%autosetup -p1 -n pyScss-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyscss
%python_clone -a %{buildroot}%{_bindir}/less2scss

%post
%python_install_alternative pyscss
%python_install_alternative less2scss

%postun
%python_uninstall_alternative pyscss
%python_uninstall_alternative less2scss

%check
# test_stdio depends on 'python' binary
%pytest -k 'not test_stdio'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/scss
%{python_sitearch}/pyScss-%{version}*-info
%python_alternative %{_bindir}/pyscss
%python_alternative %{_bindir}/less2scss

%changelog
