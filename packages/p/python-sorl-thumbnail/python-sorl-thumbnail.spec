#
# spec file for package python-sorl-thumbnail
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-sorl-thumbnail
Version:        12.7.0
Release:        0
Summary:        Thumbnails for Django
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/sorl-thumbnail
Source:         https://files.pythonhosted.org/packages/source/s/sorl-thumbnail/sorl-thumbnail-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  lsof
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2
Recommends:     ImageMagick
Recommends:     python-dbm
Suggests:       GraphicsMagick
Suggests:       python-Wand
Suggests:       python-pgmagick
Suggests:       vips-tools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2}
BuildRequires:  %{python_module boto}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module Wand}
BuildRequires:  %{pythons}
BuildRequires:  GraphicsMagick
BuildRequires:  ImageMagick
BuildRequires:  python3-pgmagick
BuildRequires:  redis
BuildRequires:  vips-tools
# /SECTION
%python_subpackages

%description
Thumbnails for Django.

Features at a glance
---------------------
- Storage support
- Pluggable Engine support (PIL, pgmagick)
- Pluggable Key Value Store support (redis, cached db)
- Pluggable Backend support
- Admin integration with possibility to delete
- Dummy generation
- Flexible, simple syntax, generates no html
- ImageField for model that deletes thumbnails
- CSS style cropping options
- Margin calculation for vertical positioning

%prep
%setup -q -n sorl-thumbnail-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8

PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings.pil
%pytest -rs -k 'not TemplateTestCaseB and not test_image_file_deserialize'
export DJANGO_SETTINGS_MODULE=tests.settings.imagemagick
%pytest -rs -k 'not TemplateTestCaseB and not test_image_file_deserialize'
export DJANGO_SETTINGS_MODULE=tests.settings.dbm
%pytest -rs -k 'not TemplateTestCaseB and not test_image_file_deserialize'
export DJANGO_SETTINGS_MODULE=tests.settings.graphicsmagick
%pytest -rs -k 'not TemplateTestCaseB and not test_image_file_deserialize'
export DJANGO_SETTINGS_MODULE=tests.settings.wand
%pytest -rs -k 'not TemplateTestCaseB and not test_image_file_deserialize'

# pgmagick is not installed in all environments
%{python_expand if [ -d %{$python_sitearch}/pgmagick/ ]; then
  export DJANGO_SETTINGS_MODULE=tests.settings.pgmagick
  $python -m pytest -rs -k 'not (TemplateTestCaseB or test_image_file_deserialize or test_is_valid_image)'
fi
}

%{_sbindir}/redis-server &
export DJANGO_SETTINGS_MODULE=tests.settings.redis
# skipping test_write and test_no_source_get_image skipped as they count open file descriptors and sometimes is off
%pytest -rs -k 'not (TemplateTestCaseB or test_image_file_deserialize or test_no_source_get_image or test_write)'

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
