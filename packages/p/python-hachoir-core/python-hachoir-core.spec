#
# spec file for package python-hachoir-core
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           python-hachoir-core
Version:        1.3.3
Release:        0
Summary:        Part of a library to manipulate a binary stream field-by-field
License:        GPL-2.0
Group:          Development/Libraries/Python
Url:            https://bitbucket.org/haypo/hachoir/
Source0:        http://cheeseshop.python.org/packages/source/h/hachoir-core/hachoir-core-1.3.3.tar.gz
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%else
BuildArch:      noarch
%endif

%description
Hachoir is a Python library that allows to view and edit a binary stream field by field. In other words, Hachoir allows you to "browse" any binary stream just like you browse directories and files. A file is split in a tree of fields, where the smallest field is just one bit.

%prep
%setup -q -n hachoir-core-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING doc README
%{python_sitelib}/hachoir_core
%{python_sitelib}/hachoir_core*.egg-info

%changelog
