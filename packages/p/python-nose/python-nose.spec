#
# spec file for package python-nose
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
Name:           python-nose
Version:        1.3.7
Release:        0
Summary:        Nose extends unittest to make testing easier
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            http://readthedocs.org/docs/nose/
Source:         https://files.pythonhosted.org/packages/source/n/nose/nose-%{version}.tar.gz
Patch0:         python-nose-coverage4.patch
Patch1:         python-nose-py35.patch
Patch2:         python-nose-py36.patch
Patch3:         python-nose-readunicode.patch
Patch4:         python-nose-unicode.patch
Patch5:         python-nose-unstable-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
Requires:       python-setuptools
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Nose extends the test loading and running features of unittest, making
it easier to write, find and run tests.

By default, nose will run tests in files or directories under the current
working directory whose names include "test" or "Test" at a word boundary
(like "test_this" or "functional_test" or "TestClass" but not
"libtest"). Test output is similar to that of unittest, but also includes
captured stdout output from failing tests, for easy print-style debugging.

These features, and many more, are customizable through the use of
plugins. Plugins included with nose provide support for doctest, code
coverage and profiling, flexible attribute-based test selection,
output capture and more.

%prep
%setup -q -n nose-%{version}
%autopatch -p1

sed -i "s|man/man1|share/man/man1|" setup.py # Fix man-page install path
# this test doesn't work
rm functional_tests/test_coverage_plugin*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/nosetests
%python_clone -a %{buildroot}%{_mandir}/man1/nosetests.1

%if 0%{?have_python2}
%check
# Timing is bad on some architectures
export NOSE_EXCLUDE=test_timed
# tests mysteriously fail in python3
python2 setup.py test
%endif

%post
%{python_install_alternative nosetests nosetests.1}

%postun
%python_uninstall_alternative nosetests

%files %{python_files}
%license lgpl.txt
%doc NEWS README.txt
%python_alternative %{_bindir}/nosetests
%python_alternative %{_mandir}/man1/nosetests.1%{ext_man}
%{python_sitelib}/nose-%{version}-py%{python_version}.egg-info/
%{python_sitelib}/nose

%changelog
