#
# spec file for package python-svneverever
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define mod_name svneverever
Name:           python-svneverever
Version:        1.2.2
Release:        0
Summary:        Tool collecting path entries across SVN history
License:        GPL-3.0
Group:          Development/Tools/Version Control
Url:            http://git.goodpoint.de/?p=svneverever.git
Source:         http://hartwork.org/public/%{mod_name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       subversion
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{!?python_sitelib: %global python_sitelib %(python -c "from %{distutils}.config import get_python_lib; print get_python_lib()")}
%if %{?suse_version}
%py_requires
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif
%endif

%description
Tool collecting path entries across SVN history. It runs through all SVN history
collecting additions of directories. In the end it presents a tree of all
directories ever having existed in the repository.

%prep
%setup -q -n %{mod_name}-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README.txt
%{_bindir}/%{mod_name}
%{python_sitelib}/%{mod_name}-%{version}-*.egg-info
%{python_sitelib}/%{mod_name}/

%changelog
