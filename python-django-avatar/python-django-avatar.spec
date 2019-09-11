#
# spec file for package python-django-avatar
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


Name:           python-django-avatar
Version:        4.1.0
Release:        0
Summary:        Django-avatar package
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/grantmcconnaughey/django-avatar/
Source:         https://files.pythonhosted.org/packages/source/d/django-avatar/django-avatar-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Pillow >= 2.0}
BuildRequires:  %{python_module django-appconf >= 0.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-Pillow >= 2.0
Requires:       python-django-appconf >= 0.6
BuildArch:      noarch
%python_subpackages

%description
Django-avatar is a reusable application for handling user avatars.  It has the
ability to default to Gravatar_ if no avatar is found for a certain user.
Django-avatar automatically generates thumbnails and stores them to your default
file storage backend for retrieval later.

%prep
%setup -q -n django-avatar-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
python2 %{_bindir}/django-admin.py-2.7 test tests --pythonpath=`pwd`

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
