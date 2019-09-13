#
# spec file for package cookiecutter
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 LISA GmbH, Bingen, Germany.
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


Name:           cookiecutter
Version:        1.6.0
Release:        0
Summary:        A command-line utility that creates projects from project templates
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/audreyr/cookiecutter
Source:         https://files.pythonhosted.org/packages/source/c/cookiecutter/cookiecutter-%{version}.tar.gz
Source1:        ccext.py
# PATCH-FIX-OPENSUSE fix-python-invocation-tests.diff hpj@urpla.net
Patch0:         fix-python-invocation-tests.diff
Patch1:         cookiecutter-click7.patch
BuildRequires:  git
BuildRequires:  python3-Jinja2 >= 2.7
BuildRequires:  python3-Sphinx
BuildRequires:  python3-binaryornot >= 0.2.0
BuildRequires:  python3-click >= 7.0
BuildRequires:  python3-devel
BuildRequires:  python3-future >= 0.15.2
BuildRequires:  python3-jinja2-time >= 0.1.0
BuildRequires:  python3-poyo >= 0.1.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-whichcraft >= 0.4.0
Requires:       git
Requires:       python3-Jinja2 >= 2.7
Requires:       python3-binaryornot >= 0.2.0
Requires:       python3-click >= 7.0
Requires:       python3-future >= 0.15.2
Requires:       python3-jinja2-time >= 0.1.0
Requires:       python3-poyo >= 0.1.0
Requires:       python3-requests >= 2.18.0
Requires:       python3-whichcraft >= 0.4.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION Testing requirements
BuildRequires:  python3-chardet >= 2.0.0
BuildRequires:  python3-freezegun
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-requests >= 2.18.0
# /SECTION

%package doc
Summary:        Documentation files for %{name}
Group:          Documentation/HTML

%description
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

Project templates can be in any programming language or markup format.

%description doc
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

This package contains the documentation for cookiecutter.

%prep
%setup -q -n cookiecutter-%{version}
%patch0 -p1
%patch1 -p1
sed -i "s/cookiecutter =/cookiecutter-%{py3_ver} =/" setup.py
cp %{SOURCE1} docs

%build
python3 setup.py build
pushd docs
make %{?_smp_mflags} html
rm _build/html/.buildinfo
popd

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/cookiecutter
ln -sf %{_sysconfdir}/alternatives/cookiecutter %{buildroot}%{_bindir}/cookiecutter

%check
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test tests

%pre
[ -h %{_bindir}/cookiecutter ] || rm -f %{_bindir}/cookiecutter

%post
update-alternatives --install %{_bindir}/cookiecutter cookiecutter %{_bindir}/cookiecutter-%{py3_ver} 30

%postun
if [ $1 -eq 0 ] ; then
    update-alternatives --remove cookiecutter %{_bindir}/cookiecutter-%{py3_ver}
fi

%files
%doc AUTHORS.rst README.rst
%license LICENSE
%ghost %{_sysconfdir}/alternatives/cookiecutter
%{_bindir}/cookiecutter
%{_bindir}/cookiecutter-%{py3_ver}
%{python3_sitelib}/*

%files doc
%doc docs/_build/html
%license LICENSE

%changelog
