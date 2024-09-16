#
# spec file
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
# Tests known to fail on 32 bit due to fp precision
ExcludeArch:    %{ix86}
%else
%bcond_with test
%define psuffix %{nil}
%endif

%define pname lscsoft-glue
# Support dropped for python2 by upstream
%define skip_python2 1

%define modname glue
Name:           lscsoft-glue%{psuffix}
Version:        4.0.0
Release:        0
Summary:        Grid LSC User Environment
License:        GPL-2.0-only
URL:            http://software.ligo.org/lscsoft
Source:         https://files.pythonhosted.org/packages/source/l/lscsoft-glue/%{pname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ligo-segments
Requires:       python-numpy
Requires:       python-pyOpenSSL
Requires:       python-six
Provides:       lscsoft-glue-data = %{version}
Obsoletes:      lscsoft-glue-data < %{version}
Provides:       python-glue = %{version}-%{release}
Obsoletes:      python-glue < %{version}-%{release}
BuildArch:      noarch
%define oldpython python
Provides:       %{oldpython}-glue = %{version}-%{release}
Obsoletes:      %{oldpython}-glue < %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module lscsoft-glue = %{version}}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Glue is a collection of utilities for running data analysis pipelines
for online and offline analysis as well as accessing various grid
utilities.  It also provides the infrastructure for the segment
database.

%package -n %{pname}-data
Summary:        Collection of data files for use by %{name}

%description -n %{pname}-data
Glue is a collection of utilities for running data analysis pipelines
for online and offline analysis as well as accessing various grid
utilities.  It also provides the infrastructure for the segment
database.

This package provides a common set of data files for %{name}.

%prep
%autosetup -p1 -n %{pname}-%{version}
# Taken from bundled specfile template
%if 0%{?suse_version} < 1650
cat > setup.cfg <<EOF
[metadata]
name = %{pname}
version = %{version}
description = %{summary}
license = %{license}
license_files = LICENSE
url = %{url}
[options]
packages = find:
python_requires = >=3.6
install_requires =
	ligo-segments
	pyOpenSSL
	six
EOF
%endif

%build
%if ! %{with test}
%pyproject_wheel
%endif

%install
%if ! %{with test}
%pyproject_install

# SECTION Remove non-library config/php files
rm -fr %{buildroot}%{_prefix}%{_sysconfdir}
rm -fr %{buildroot}%{_prefix}%{_localstatedir}
# /SECTION

%python_expand %fdupes -s %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# test_ldbd.py requires network; disable
%pytest -k 'not test_ldbd'
%endif

%if ! %{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/glue/
%{python_sitelib}/lscsoft_glue-%{version}*-info
%endif

%changelog
