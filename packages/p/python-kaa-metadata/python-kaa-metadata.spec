#
# spec file for package python-kaa-metadata
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


%define _name kaa-metadata
%if 0%{?suse_version} <= 1110
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(True))")}
%endif
Name:           python-kaa-metadata
Version:        0.7.7
Release:        0
Summary:        The Kaa Media Repository Metadata Library
License:        GPL-2.0+
Group:          Development/Languages/Python
Url:            https://github.com/freevo/kaa-metadata
Source:         https://github.com/freevo/%{_name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  libdvdread-devel
BuildRequires:  python-devel
BuildRequires:  python-kaa-base
Requires:       python-kaa-base
Obsoletes:      python-mmpython < %{version}
Provides:       python-mmpython = %{version}
%if 0%{?suse_version} <= 1110
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
%endif

%description
The Kaa Media Repository is a set of python modules related to media.
This module extracts metadata from media files.

%prep
%setup -q -n %{_name}-%{version}

%build
export CFLAGS="%{optflags}"
python2 setup.py build

%install
python2 setup.py install \
  --prefix=%{_prefix} --root=%{buildroot}

%fdupes %{buildroot}%{python_sitearch}/

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/mminfo
%{python_sitearch}/kaa/metadata/
%{python_sitearch}/kaa_metadata-*

%changelog
