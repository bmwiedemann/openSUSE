#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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

%define pypi_name cheroot
%bcond_without python2
%bcond_with ringdisabled
Name:           python-%{pypi_name}
Version:        8.6.0
Release:        0
Summary:        Pure-python HTTP server
License:        BSD-3-Clause
URL:            https://github.com/cherrypy/cheroot
Source:         https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE no-pypytools.patch mcepl@suse.com
# We don't have PyPy at all, so no need support for it
Patch0:         no-pypytools.patch
# PATCH-FIX-UPSTREAM no-relative-imports.patch bsc#[0-9]+ mcepl@suse.com
Patch1:         no-relative-imports.patch
BuildRequires:  %{python_module jaraco.functools}
BuildRequires:  %{python_module more-itertools >= 2.6}
BuildRequires:  %{python_module setuptools >= 34.4}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools_scm_git_archive >= 1.0}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
%if %{with python2}
BuildRequires:  python-backports.functools_lru_cache
BuildRequires:  python-selectors2
%endif
# SECTION test requirements
%if ! %{with ringdisabled}
# This is not in Ring1 for Staging. See check section
BuildRequires:  %{python_module jaraco.context}
%endif
BuildRequires:  %{python_module jaraco.text >= 3.1}
BuildRequires:  %{python_module portend}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest-mock >= 1.11.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests-unixsocket}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module urllib3 >= 1.25}
# /SECTION
Requires:       python-jaraco.functools
Requires:       python-more-itertools >= 2.6
Requires:       python-six >= 1.11.0
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
# the package and distribution name is lowercase-cheroot,
# but PyPI claims the name is capital-Cheroot
# *smacks head against desk*
Provides:       python-Cheroot = %{version}
BuildArch:      noarch
%ifpython2
Requires:       python-backports.functools_lru_cache
Requires:       python-selectors2
%endif
%python_subpackages

%description
Cheroot is the pure-Python HTTP server used by CherryPy.

%prep
%autosetup -p1 -n cheroot-%{version} -p1
# do not check coverage
sed -i -e '/--cov/ d' pytest.ini

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/cheroot
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mkdir testclean
pushd testclean
%if %{with ringdisabled}
# skip this test file (1 test only) in Factory staging, because we
# do not want to add python-jaraco.context to Ring1
%python_expand pytest_opts+=" --ignore  %{buildroot}%{$python_sitelib}/cheroot/test/test_wsgi.py"
%endif
# test_tls_client_auth[...-False-localhost-builtin] fails ocassionally on server-side OBS
donttest="(test_tls_client_auth and False-localhost-builtin)"
# looks like there's a bug with pytest.mark.forked
# https://github.com/cherrypy/cheroot/issues/511
donttest+=" or test_high_number_of_file_descriptor"
%pytest --pyargs cheroot $pytest_opts -k "not ($donttest)"
popd

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative cheroot

%post
%python_install_alternative cheroot

%postun
%python_uninstall_alternative cheroot

%files %{python_files}
%license LICENSE.md
%doc README.rst CHANGES.rst
%python_alternative %{_bindir}/cheroot
%{python_sitelib}/cheroot
%{python_sitelib}/cheroot-%{version}*-info

%changelog
