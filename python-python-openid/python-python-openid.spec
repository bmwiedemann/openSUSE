#
# spec file for package python-python-openid
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           python-python-openid
Version:        2.2.5
Release:        1
Url:            http://github.com/openid/python-openid
Summary:        OpenID support for servers and consumers
License:        Apache-2.0
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/python-openid/python-openid-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
Provides:       python2-python-openid = %{version}
Provides:       python-openid = %{version}
#TODO: Change '<=' to '<' after version update:
Obsoletes:      python-openid <= %{version}
BuildArch:      noarch

%description
This is a set of Python packages to support use of
the OpenID decentralized identity system in your application.  Want to enable
single sign-on for your web site?  Use the openid.consumer package.  Want to
run your own OpenID server? Check out openid.server.  Includes example code
and support for a variety of storage back-ends.

%prep
%setup -q -n python-openid-%{version}
find . -name "._*" -type f | xargs rm -f # Remove junk files

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README NEWS
%doc examples/
%{python_sitelib}/*

%changelog
