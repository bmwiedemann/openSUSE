#
# spec file for package python-pecan
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pecan
Version:        1.4.2
Release:        0
Summary:        A WSGI object-dispatching web framework
License:        BSD-3-Clause
URL:            https://github.com/pecan/pecan
Source:         https://files.pythonhosted.org/packages/source/p/pecan/pecan-%{version}.tar.gz
Patch0:         pecan-no-kajiki.patch
BuildRequires:  %{python_module Genshi >= 0.7}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Mako >= 0.4.0}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module WebOb >= 1.8}
BuildRequires:  %{python_module WebTest >= 1.3.1}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module logutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  uwsgi
# we need sqlite module
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-Mako >= 0.4.0
Requires:       python-WebOb >= 1.8
# Still needed by pecan.testing
Requires:       python-WebTest >= 1.3.1
Requires:       python-logutils >= 0.3
Requires:       python-setuptools
Requires:       python-six
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%if 0%{?suse_version}
Suggests:       python-Genshi
Suggests:       python-Jinja2
Suggests:       python-gunicorn
%endif
%python_subpackages

%description
A WSGI object-dispatching web framework.

%prep
%setup -q -n pecan-%{version}
%patch0 -p1
sed -ie "/^uwsgi$/d" test-requirements.txt
sed -ie "/^pep8$/d" test-requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pecan
%python_clone -a %{buildroot}%{_bindir}/gunicorn_pecan

%check
%pyunittest discover -v

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pecan
%python_libalternatives_reset_alternative gunicorn_pecan

%post
%python_install_alternative pecan
%python_install_alternative gunicorn_pecan

%postun
%python_uninstall_alternative pecan
%python_uninstall_alternative gunicorn_pecan

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/pecan
%python_alternative %{_bindir}/gunicorn_pecan
%{python_sitelib}/*

%changelog
