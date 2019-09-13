#
# spec file for package python-imagestore
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


Name:           python-imagestore
Version:        2.9.1
Release:        0
Summary:        Gallery solution for django projects
License:        GPL-2.0+
Group:          Development/Languages/Python
Url:            https://github.com/hovel/imagestore
Source0:        https://pypi.python.org/packages/source/i/imagestore/imagestore-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
ImageStore
==========

An image gallery, created for easy integration for an exiting django project.

`Documentation available on ReadTheDocs <http://readthedocs.org/projects/imagestore/>`_

Gallery for site
----------------

* Albums
* Mass upload
* Thumbnails in admin intereface
* Ordering
* Tagging support
* Easy PrettyPhoto integration
* Django-cms integration

Gallery for your site users
---------------------------

* You can use imagestore to create gallery for your users.
* Users can:
    * create albums, upload photos to albums
    * make albums non-public
    * set name, descripion and tags for photos
    * edit infomation about photo or upload new veresion

%prep
%setup -q -n imagestore-%{version}
find . -type f -name "*.py" | xargs sed -i "/#!.*/d" # Fix non-executable script warning
chmod -x imagestore/locale/fi/LC_MESSAGES/django.po # remove erroneous executable bit

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%find_lang django %{name}.lang

%files -f %{name}.lang
%defattr(-,root,root,-)
%{python_sitelib}/*
%doc README README.rst

%changelog
