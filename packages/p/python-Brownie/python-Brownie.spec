#
# spec file for package python-Brownie
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-Brownie
Version:        0.5.1
Release:        0
Url:            http://github.com/DasIch/brownie/
Summary:        Common utilities and datastructures for Python applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/B/Brownie/Brownie-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:  python-Attest
BuildRequires:  python-devel
BuildRequires:  python-setuptools
#BuildRequires:  python-functional
#BuildRequires:  python-nose
BuildRequires:  python-Sphinx
%if 0%{?suse_version} > 1320
Provides:       python2-Brownie = %{version}
%endif
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Welcome to Brownie!

- Have you ever started a new project and implemented this little function
  foo or this datastructure bar you already implemented for another project?
- Ever wondered why a specific feature is not in the `standard library`_
  already?
- Wanted to use that new datastructure but you are still stuck with this
  ancient Python version or are just not willing or able to switch to
  Python 3.x, yet?
- And most importantly were too lazy to implement this datastructure which
  would be more appropriate to use?

Brownie wants to solve these problems by providing all these small things
well documented, well tested and most importantly right now when you need
it.

%prep
%setup -q -n Brownie-%{version}

%build
python setup.py build
cd docs && make html && rm -r _build/html/.buildinfo

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

#%%check
#nosetests

%files
%defattr(-,root,root,-)
%doc LICENSE.rst README.rst docs/_build/html
%{python_sitelib}/*

%changelog
