#
# spec file for package python-django-minio-storage
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_with test
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-django-minio-storage
Version:        0.5.3
Release:        0
Summary:        Django file storage using minio
License:        Apache-2.0 OR MIT
URL:            https://github.com/py-pa/django-minio-storage
Source:         https://files.pythonhosted.org/packages/source/d/django-minio-storage/django-minio-storage-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-minio >= 7
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module minio >= 7}
BuildRequires:  %{python_module pytest-django >= 3.5.1}
BuildRequires:  %{python_module pytest-pythonpath}
BuildRequires:  %{python_module requests}
BuildRequires:  minio
%endif
%python_subpackages

%description
Django file storage using the minio python client.

%prep
%setup -q -n django-minio-storage-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export MINIO_ACCESS_KEY=weak_access_key
export MINIO_SECRET_KEY=weak_secret_key
rm -rf $HOME/minio_export
mkdir $HOME/minio_export
/usr/sbin/minio server $HOME/minio_export &

export MINIO_STORAGE_ENDPOINT=localhost:9000
export MINIO_STORAGE_ACCESS_KEY=$MINIO_ACCESS_KEY
export MINIO_STORAGE_SECRET_KEY=$MINIO_SECRET_KEY
%pytest -rs
%endif

%files %{python_files}
%doc README.md docs/usage.md
%license LICENSE-APACHE LICENSE-MIT
%{python_sitelib}/minio_storage
%{python_sitelib}/django_minio_storage-%{version}.dist-info

%changelog
