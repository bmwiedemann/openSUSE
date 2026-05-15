#
# spec file for package python-SQLAlchemy-spanner
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-SQLAlchemy-spanner
Version:        1.17.3
Release:        0
Summary:        SQLAlchemy dialect integrated into Cloud Spanner database
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/sqlalchemy-spanner
Source:         https://files.pythonhosted.org/packages/source/s/sqlalchemy-spanner/sqlalchemy_spanner-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module alembic}
BuildRequires:  %{python_module google-cloud-spanner >= 3.55.0}
BuildRequires:  %{python_module opentelemetry-api >= 1.1.0}
BuildRequires:  %{python_module opentelemetry-instrumentation >= 0.20b0}
BuildRequires:  %{python_module opentelemetry-sdk >= 1.1.0}
BuildRequires:  %{python_module sqlalchemy >= 1.1.13}
# /SECTION
BuildRequires:  fdupes
Requires:       python-alembic
Requires:       python-google-cloud-spanner >= 3.55.0
Suggests:       python-opentelemetry-api >= 1.1.0
Suggests:       python-opentelemetry-sdk >= 1.1.0
Suggests:       python-opentelemetry-instrumentation >= 0.20b0
BuildArch:      noarch
Provides:       python-sqlalchemy-spanner
%python_subpackages

%description
Spanner dialect for SQLAlchemy represents an interface API designed to make it
possible to control Cloud Spanner databases with SQLAlchemy API.

%prep
%autosetup -p1 -n sqlalchemy_spanner-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# tests need spanner infra so it's not possible to run at build time
#%%check
#%%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/google/cloud/sqlalchemy_spanner
%{python_sitelib}/sqlalchemy_spanner-%{version}.dist-info

%changelog
