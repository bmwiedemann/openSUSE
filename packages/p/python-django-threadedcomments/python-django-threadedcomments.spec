#
# spec file for package python-django-threadedcomments
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
Name:           python-django-threadedcomments
Version:        1.2
Release:        0
Summary:        Threaded commenting system for Django applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/HonzaKral/django-threadedcomments
Source:         https://github.com/HonzaKral/django-threadedcomments/archive/v%{version}.tar.gz#/django-threadedcomments-%{version}.tar.gz
Patch0:         dj-test-settings.patch
Patch1:         test-use-content-type.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django > 1.11
Requires:       python-django-contrib-comments >= 1.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django > 1.11}
BuildRequires:  %{python_module django-contrib-comments >= 1.9.0}
# /SECTION
%python_subpackages

%description
threadedcomments is a Django application which allows for the
creation of a threaded commenting system.

Commenters can reply both to the original item, and reply to other
comments as well.

The application is built on top of django-contrib-comments, which allows
it to be extended by other modules.

%prep
%setup -q -n django-threadedcomments-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
