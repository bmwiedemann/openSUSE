#
# spec file for package 
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           python-requestbuilder
Version:		0.1.0
Release:		0
License:		ISC
Summary:		Command line-driven HTTP request builder		
Url:			https://github.com/boto/requestbuilder
Group:			Development/Languages/Python
Source:			requestbuilder-%{version}.tar.gz
BuildRequires:	python	
BuildRequires:	python-devel
BuildRequires:	python-distribute
Requires:		python
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Command line-driven HTTP request builder

%prep
%setup -q -n requestbuilder-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{python_sitelib}/*

%changelog

