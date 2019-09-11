#
# spec file for package python-poppler-qt5
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 LISA GmbH, Bingen, Germany.
# Copyright (c) 2012 Johannes Engel <jcnengel@gmail.com>
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
Name:           python-poppler-qt5
Version:        0.25.1
Release:        0
Summary:        Python binding to poppler-qt5
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/zehome/python-poppler-qt5
Source0:        https://github.com/zehome/python-poppler-qt5/archive/v%{version}.tar.gz
BuildRequires:  %{python_module sip-devel}
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-qt5-devel
%requires_eq    python-qt5
Requires:       python-sip(api) = %{python_sip_api_ver}
Obsoletes:      python-poppler-qt4
%python_subpackages

%description
A Python binding for libpoppler-qt5 that aims for completeness
and for being actively maintained.

%prep
%setup -q

%build
export PATH=%{_libdir}/qt5/bin:$PATH
%python_build

%install
export PATH=%{_libdir}/qt5/bin:$PATH
%python_install

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst TODO
%{python3_sitearch}/popplerqt5*.so
%{python3_sitearch}/python_poppler_qt5*.egg-info

%changelog
