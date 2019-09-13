#
# spec file for package python-django-minio-storage
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/

%bcond_with test
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-minio-storage
Version:        0.2.2
Release:        0
License:        MIT or Apache-2.0
Summary:        Django file storage using minio
Url:            https://github.com/py-pa/django-minio-storage
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/django-minio-storage/django-minio-storage-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
%if %{with test}
BuildRequires:  %{python_module Django >= 1.8}
BuildRequires:  %{python_module minio >= 4.0.3}
BuildRequires:  %{python_module pytest-django >= 3.1.2}
BuildRequires:  %{python_module pytest-pythonpath}
BuildRequires:  %{python_module requests}
BuildRequires:  minio
%endif
BuildRequires:  fdupes
Requires:       python-Django >= 1.8
Requires:       python-minio >= 4.0.3
BuildArch:      noarch

%python_subpackages

%description
Django file storage using the minio python client.

%prep
%setup -q -n django-minio-storage-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export MINIO_ACCESS_KEY=weak_access_key
export MINIO_SECRET_KEY=weak_secret_key
rm -rf $HOME/minio_export
mkdir $HOME/minio_export
minio server $HOME/minio_export &

export MINIO_STORAGE_ENDPOINT=localhost:9000
export MINIO_STORAGE_ACCESS_KEY=$MINIO_ACCESS_KEY
export MINIO_STORAGE_SECRET_KEY=$MINIO_SECRET_KEY
%python_exec -m pytest
%endif

%files %{python_files}
%doc README.md docs/usage.md
%license LICENSE-APACHE LICENSE-MIT
%{python_sitelib}/*

%changelog
