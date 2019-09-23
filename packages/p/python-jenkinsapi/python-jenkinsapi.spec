#
# spec file for package python-jenkinsapi
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
Name:           python-jenkinsapi
Version:        0.3.9
Release:        0
Summary:        A Python API for accessing resources on a Jenkins continuous integration server
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/salimfadhley/jenkinsapi
Source:         https://pypi.io/packages/source/j/jenkinsapi/jenkinsapi-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz >= 2014.4
Requires:       python-requests >= 2.3.0
BuildArch:      noarch
%python_subpackages

%description
Jenkins is a continuous integration system.

Jenkins (and its predecessor Hudson) are projects for automating
common development tasks (e.g. unit testing, production batches), but
they are somewhat Java-centric. The designers have provided a REST
interface. This library wraps up that interface as more conventional
Python objects.

This library can help to:

 * Query the test-results of a completed build
 * Get a objects representing the latest builds of a job
 * Search for artefacts by simple criteria
 * Block until jobs are complete
 * Install artefacts to custom-specified directory structures

and has

 * username/password auth support for jenkins instances with auth turned on
 * Ability to search for builds by subversion revision
 * Ability to add/remove/query Jenkins slaves
 * Ability to add/remove/modify Jenkins views

%prep
%setup -q -n jenkinsapi-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jenkins_invoke
%python_clone -a %{buildroot}%{_bindir}/jenkinsapi_version
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%{python_install_alternative jenkins_invoke jenkinsapi_version}

%postun
%python_uninstall_alternative jenkins_invoke

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license license.txt
%python_alternative %{_bindir}/jenkins_invoke
%python_alternative %{_bindir}/jenkinsapi_version
%{python_sitelib}/*

%changelog
