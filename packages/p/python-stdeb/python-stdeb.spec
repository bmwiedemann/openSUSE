#
# spec file for package python-stdeb
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
Name:           python-stdeb
Version:        0.9.0
Release:        0
Summary:        Python to Debian source package conversion utility
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/astraw/stdeb
Source:         https://files.pythonhosted.org/packages/source/s/stdeb/stdeb-%{version}.tar.gz
# Test data
Source1:        tablib-0.13.0.tar.gz
# The tests default to using requests as the test scenario, however that
# has urllib3 & pyOpenSSL as dependencies, which makes the tests break due
# to constant incompatibilities in openssl and vendoring/de-vendoring.
# Instead use tablib.
Patch0:         tests-use-tablib.patch
# stdeb is of limited use on openSUSE as any attempt to install
# dpkg packages needed to create a valid dpkg database will destroy the
# openSUSE python runtime that stdeb was installed into.  Therefore it
# can only be used with a fake database, or without enforced dpkg
# dependency checks.  The next two patches provide the latter approach.
# https://github.com/astraw/stdeb/issues/144
Patch1:         remove-version-checks.patch
Patch2:         ignore-unmet-deps.patch
# The python helpers come from the debian python-defaults and python3-defaults
# packages, e.g. https://salsa.debian.org/cpython-team/python-defaults
# and they need to be ported to a openSUSE package.
Patch3:         remove-python-helper-rules.patch
Patch4:         no-install-layout.patch
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  debhelper
BuildRequires:  dpkg
BuildRequires:  fakeroot
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       debhelper
Requires:       dpkg
Requires:       fakeroot
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The stdeb package produces Debian source packages from Python packages
via a new distutils command, sdist_dsc. Automatic defaults are provided
for the Debian package, but many aspects of the resulting package can be
customized (see the customizing section, below). An additional command,
bdist_deb, creates a Debian binary package, a .deb file. The install_deb
command installs this .deb file. The debianize command builds a
debian/ directory directly alongside your setup.py.

The openSUSE version does not fail for unmet dependencies in the host
dpkg database.

%prep
%setup -q -n stdeb-%{version}
%autopatch -p1

cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pypi-install
%python_clone -a %{buildroot}%{_bindir}/pypi-download
%python_clone -a %{buildroot}%{_bindir}/py2dsc-deb
%python_clone -a %{buildroot}%{_bindir}/py2dsc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# There is also test2and3.sh which could be inlined here
export PATH=/sbin:%{_prefix}/sbin:%{buildroot}/%{_bindir}:$PATH
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
# update-alternatives: use available versioned binaries
sed -i 's:\(_LOC=`which\s\+[-a-zA-Z0-9]\+\):\1-%{python_version}:' test.sh
PYEXE=$python bash -x ./test.sh
}

%post
%python_install_alternative pypi-install
%python_install_alternative pypi-download
%python_install_alternative py2dsc-deb
%python_install_alternative py2dsc

%postun
%python_uninstall_alternative pypi-install
%python_uninstall_alternative pypi-download
%python_uninstall_alternative py2dsc-deb
%python_uninstall_alternative py2dsc

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.txt README.rst
%python_alternative %{_bindir}/py2dsc
%python_alternative %{_bindir}/py2dsc-deb
%python_alternative %{_bindir}/pypi-download
%python_alternative %{_bindir}/pypi-install
%{python_sitelib}/*

%changelog
